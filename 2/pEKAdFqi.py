import random
import time
import hw2_207704842 as hw


def test_with_time(cases, func):
    for args, expected_result in cases:
        func_pretty_name = f"{func.__name__}({', '.join(str(i) for i in args)})"

        start = time.perf_counter()
        result = func(*args)
        if result != expected_result:
            print(f"{func_pretty_name}: expected {expected_result}, got {result}")
        end = time.perf_counter()

        elapsed_time = end - start
        if elapsed_time >= 1:
            print(f"{func_pretty_name}: took {elapsed_time} seconds")


def test_legal_par():
    TESTS = [
        (("[[{}<>[]]]", ), True),
        (("{}{}", ), True),
        (("[()][<>][[()]]", ), True),
        (("[(])", ), False),
        (("](())", ), False),
         (("<<<{>>}>", ), False)
    ]

    test_with_time(TESTS, hw.legal_par)


def test_spiral_num():
    TESTS = [
        ((1, ), 1),
        ((3, ), 25),
        ((100001, ), 666691667100001)
    ]

    test_with_time(TESTS, hw.spiral_sum)


def test_binary():
    TESTS_SUB = [
        (("0", "0"), "0"), (("1", "0"), "1"), (("10", "1"), "1"), (("11", "10"), "1"), (("1" + "0" * 19, "1" * 19), "1")
    ]
    TESTS_INC = [(("0",), "1")]
    TESTS_DEC = [(("1",), "0")]
    TESTS_LEQ = [(("1", "0"), False), (("1", "1"), True)]
    TESTS_DIV = [(("10101", "11"), "111"), (("0", "11"), "0")]

    TESTS = [(TESTS_INC, hw.inc), (TESTS_DEC, hw.dec), (TESTS_SUB, hw.sub),
             (TESTS_LEQ, hw.leq), (TESTS_DIV, hw.div)]

    for i in range(100):
        # bin1 >= bin2
        bin1 = random.randint(0, 100000)
        bin2 = random.randint(0, bin1)
        bin1_str = bin(bin1)[2:]
        bin2_str = bin(bin2)[2:]
        TESTS_SUB.append((
            (bin1_str, bin2_str), bin(bin1 - bin2)[2:]
        ))

        TESTS_INC.append(((bin2_str,), bin(bin2 + 1)[2:]))
        TESTS_DEC.append(((bin1_str,), bin(bin1 - 1)[2:]))

        if bin1 == bin2:
            TESTS_LEQ.append(((bin1_str, bin2_str), True))
        else:
            TESTS_LEQ.append(((bin1_str, bin2_str), False))
            TESTS_LEQ.append(((bin2_str, bin1_str), True))

        if bin2 != 0:
            TESTS_DIV.append(((bin1_str, bin2_str), bin(bin1 // bin2)[2:]))

    for cases, func in TESTS:
        test_with_time(cases, func)


def test_has_repeat():
    TESTS = [
        (("a", 1), False),
        (("ababa", 3), True),
        (("abab", 3), False),
        (("abab", 2), True),
        (("abcdeabcde", 5), True),
        (("abcdeabcde", 4), True),
        (("abcdeabcde", 6), False),
        (("abcdeabcde", 1), True),
        (("bcece", 2), True),
    ]

    test_with_time(TESTS, hw.has_repeat1)
    test_with_time(TESTS, hw.has_repeat2)


def test_reading():
    TESTS = [
        ((1, ), "1"),
        ((2, ), "11"),
        ((3, ), "21"),
        ((4, ), "1211"),
        ((5, ), "111221"),
        ((6, ), "312211"),
        ((7, ), "13112221"),
        ((8, ), "1113213211"),
        ((9, ), "31131211131221"),
    ]

    test_with_time(TESTS, hw.reading)


def test_max_div_seq():
    TESTS = [
        ((23300247524689, 2), 4),
        ((1357, 2), 0),
        ((1630860, 3), 3),
        ((1630860, 8), 2),
    ]

    test_with_time(TESTS, hw.max_div_seq)


def run_all_tests():
    test_legal_par()
    test_spiral_num()
    test_binary()
    test_has_repeat()
    test_reading()
    test_max_div_seq()
    hw.test()


if __name__ == "__main__":
    run_all_tests()