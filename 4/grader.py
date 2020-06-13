import sys
import os
import traceback
import time
import os.path
import operator
import random
import types

import multiprocessing
from contextlib import contextmanager
from threading import Thread
import functools
import signal
import inspect
import ast
import itertools
from io import StringIO

from importlib.machinery import SourceFileLoader
import types
from types import CodeType, FunctionType
import xml.etree.ElementTree as ET
import csv

import argparse
from bdb import Bdb

CSV_NAME = "grades.csv"
TIME_LIMIT = 2  # time limit for single function run in sec
MULTITHREAD = False
DEBUG = False
ONLY_TEST = False
ONLY_OPTIONAL = False
BREAK_ON_FAILURE = True
STD_OUTPUT_ALLOWED = False # Does not work with MULTITHREAD

class TimeoutException(Exception):
    pass


@contextmanager
def time_limit(seconds):
    # used to timeout on unix systems- see the optional in 'examine_for_errors'
    def signal_handler(_, __):
        raise TimeoutException("Timed out!")

    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)


def timeout(time_out):
    def deco(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            res = [TimeoutException("TimeOut!")]

            def new_func():
                try:
                    res[0] = func(*args, **kwargs)
                except Exception as e:
                    res[0] = e
            t = Thread(target=new_func)
            t.daemon = True
            try:
                t.start()
                t.join(time_out)
            except Exception as je:
                print('error starting thread')
                raise je
            ret = res[0]
            if isinstance(ret, BaseException):
                raise ret
            return ret
        return wrapper
    return deco

def load_module(module_path):
    loader = SourceFileLoader("student_code", module_path) 
    hw_module = types.ModuleType(loader.name)
    loader.exec_module(hw_module)
    set_tests(hw_module)
    return hw_module

@timeout(0.1)
def load_module_first_time(module_path):
    return load_module(module_path)

@timeout(5)
def load_module_again(module_path):
    return load_module(module_path)

def examine_for_errors(module_path, test_schema, output_dict):
    print("Examining", module_path, flush=True)
    total_grade = 0
    total_errors = []
    total_manual_checks = []
    student_id = get_id_from_path(module_path)

    root = ET.parse(test_schema).getroot()
    
    try:
        if not STD_OUTPUT_ALLOWED:
            sys.stdout = mystdout = StringIO()

        try:
            hw_module = load_module_first_time(module_path)
        except Exception as e:
            total_errors += [f"YYYE: {str(e)}"]

            if not STD_OUTPUT_ALLOWED:
                print("", end="", flush=True)
                sys.stdout = sys.__stdout__

            if student_id not in output_dict:
                output_dict[student_id] = [0, "", ""]

            output_dict[student_id] = list(map(operator.add, output_dict[student_id], [total_grade, ', '.join(total_errors), ""]))
            return

        for function_obj in root:
            func_sign = function_obj.get("sign")
            try:
                curr_function = getattr(hw_module, function_obj.tag)
            except AttributeError as e:
                total_errors += [f"T_{func_sign}E:'{repr(e)}'"]
                continue

            for test in function_obj.iterfind("test"):
                sign = test.get("sign")
                grade = int(test.get("grade"))
                inputs = test.iterfind("input")
                outputs = {output.get("id"): output for output in test.findall("output")}

                success = True

                if not ONLY_OPTIONAL:
                    for input_element in inputs:
                        hw_module = load_module_again(module_path)
                        curr_function = getattr(hw_module, function_obj.tag)

                        input_id = input_element.get("id")
                        output_element = outputs[input_id]

                        input_values = eval("[" + input_element.text + "]")

                        # Actual Testing
                        @timeout(TIME_LIMIT)
                        def test_now(*input_values):
                            return curr_function(*input_values)

                        try:
                            function_output = test_now(*input_values)
                        except Exception as e:
                            total_errors += [f"T_{sign}_{input_id}E:'{repr(e)}'"]
                            success = False
                            if BREAK_ON_FAILURE:
                                break
                            else:
                                continue

                        output_values = eval("[" + output_element.text + "]")
                        is_multi = output_element.get("is_multi").lower() == "true" if output_element.get("is_multi") else False
                        if is_multi:
                            output_values = output_values[0]

                        correct_output = False
                        for output_value in output_values:
                            if function_output == output_value:
                                correct_output = True
                                break
                        if not correct_output:
                            total_errors += [f"T_{sign}_{input_id}"]
                            success = False
                            if BREAK_ON_FAILURE:
                                break
                            else:
                                continue

                if success:
                    total_grade += grade

        if not STD_OUTPUT_ALLOWED:
            print("", end="", flush=True)
            if mystdout.getvalue():
                pass
                total_errors += [f"P"]
                #total_grade -= 10
            
            sys.stdout = sys.__stdout__

        if student_id not in output_dict:
            output_dict[student_id] = [0, "", ""]

        output_dict[student_id] = list(map(operator.add, output_dict[student_id], 
                                    [total_grade, ', '.join(total_errors), ', '.join(total_manual_checks)]))
    finally:
        if not STD_OUTPUT_ALLOWED:
            print("", end="", flush=True)
            sys.stdout = sys.__stdout__
        print("Examined", module_path, flush=True)


def get_exercise_list(path):
    def filter_func(file_name):
        return file_name.endswith(".py") and file_name.find("matrix.py") == -1 and file_name.find("linked_list.py") == -1
    exercise_list = os.listdir(path)
    exercise_list = list(map(lambda file_name: os.path.join(path, file_name), filter(filter_func, exercise_list)))
    return sorted(exercise_list)


def grade_submissions(exercise_list, test_schema):
    if MULTITHREAD:
        manager = multiprocessing.Manager()
        graded_submissions_dict = manager.dict()

        cpu_count = multiprocessing.cpu_count()
        cpu_count = cpu_count if cpu_count > 1 else 1
        print('CPU cores to use:', cpu_count)
        pool = multiprocessing.Pool(processes=cpu_count)

        pool.starmap(
            examine_for_errors,
            ((exercise_path, test_schema, graded_submissions_dict) for exercise_path in exercise_list)
        )
        pool.starmap(find_conventions_errors, ((exercise_path, graded_submissions_dict) for exercise_path in exercise_list))

        return dict(graded_submissions_dict)
    else:
        graded_submissions_dict = {}
        for exercise_path in exercise_list:
            examine_for_errors(exercise_path, test_schema, graded_submissions_dict)
        return graded_submissions_dict


def find_conventions_errors(exercise_path, graded_submissions_dict):
    # for future implementation
    return


def write_results_to_csv(csv_path, graded_submissions, mode='w'):
    with open(csv_path, mode, newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["id", "grade", "errors", "manual_checks"], delimiter=",")
        for student_id, values in sorted(graded_submissions.items()):
            grade = values[0]
            errors = values[1]
            manual_checks = values[2]
            writer.writerow({"id": student_id, "grade": grade, "errors": errors, "manual_checks": manual_checks})


def get_id_from_path(path):
    name = os.path.basename(path)
    return os.path.basename(path)[name.index('_') + 1 : name.index('.')]


# Logic to verify recursion and memoization
class CallsValidator(Bdb):
    def do_clear(self, arg):
        # required for Bdb, do not remove
        pass

    @staticmethod
    def used_functions(func_ast):
        call_names = [c.func.id for c in ast.walk(func_ast)
                    if hasattr(c, 'func') and hasattr(c.func, 'id') and isinstance(c, ast.Call)]
        return call_names

    @staticmethod
    def convert_module_ast_to_function_def_ast(module_ast, func_name):
        return next((node for node in ast.walk(module_ast) 
                          if type(node).__name__=='FunctionDef' and node.name == func_name), None)

    def __init__(self, *args, entry_func, module, stopping_conditions, memoization_mapping):
        Bdb.__init__(self, *args)
        pass

    def user_call(self, frame, argument_list):
        pass

    def user_return(self, frame, return_value):
        pass

# my tests:-----------------------------------------


def set_tests(hw_module):
    def verify_usage(func, usage_func_name):
        func_ast = CallsValidator.convert_module_ast_to_function_def_ast(ast.parse(inspect.getsource(func)), func.__name__)
        call_names = CallsValidator.used_functions(func_ast)
        return usage_func_name in call_names

    def _raise(ex):
        raise ex

    def verify_usage_by_deletion(func, usage_func_name, *args):
        setattr(hw_module, usage_func_name, lambda: raise_(Exception()))
        try:
            func(*args)
        except:
            return True
        return False

    def is_string_in_source(func, search_str):
        source_code = inspect.getsource(func)
        return search_str in source_code
    
    d = {
        'verify_usage': verify_usage,
        'verify_usage_by_deletion': verify_usage_by_deletion,
        'is_string_in_source': is_string_in_source
    }
    """
    How to add function to the student module:

    %
    def add_me():
        print('yes!')

    d = {'add_me': add_me}
    %

    call using: hw_module.add_me()
    """

    def sort_of_sorts(L):
        return sorted([sorted(x) for x in L])

    def subset_sum_search_all_sorted(L, s):
        return sort_of_sorts(hw_module.subset_sum_search_all(L, s))

    new_d = {
        'sort_of_sorts': sort_of_sorts,
        'subset_sum_search_all_sorted': subset_sum_search_all_sorted
    }

    d.update(new_d)
    for k in d:
        setattr(hw_module, k, d[k])


def main():
    parse = argparse.ArgumentParser()
    parse.add_argument("python_path", type=str, help="python file location (or folder for multiple files)")
    parse.add_argument("scheme_path", type=str, help="scheme file location")
    parse.add_argument("--output", default=None, type=str, help="output file location")
    parse.add_argument("--batch", action='store_true', default=False, help="")
    args = parse.parse_args()

    file_location = args.python_path
    scheme_path = args.scheme_path
    output_path = args.output if args.output is not None else os.path.join(file_location, CSV_NAME)
    
    if os.path.isfile(file_location):
        d = {}
        examine_for_errors(file_location, scheme_path, d)
        if args.batch:
            write_results_to_csv(output_path, d, mode='a')
        else:
            out = d[list(d.keys())[0]]
            print("grade: ", out[0])
            print("errors: ", out[1])
            print("manual checks: ", out[2])

    elif os.path.isdir(file_location):
        # expected python names are: "hw#_123456789.py"

        submissions = get_exercise_list(file_location)
        graded_submissions_dict = grade_submissions(submissions, scheme_path)
        write_results_to_csv(output_path, graded_submissions_dict)

    else:
        print("Wrong input type")


if __name__ == '__main__':
    main()
    k=input("press close to exit") 
