from testHelper import *
import unittest
from skeleton import *
import random

class TestHasRepeat(unittest.TestCase):
    def test_Basecases(self):
        self.assertTrue(has_repeat1("ababa", 3))
        self.assertFalse(has_repeat1("ababa", 4))
        self.assertTrue(has_repeat1("aba", 1))

        self.assertTrue(has_repeat2("ababa", 3))
        self.assertFalse(has_repeat2("ababa", 4))
        self.assertTrue(has_repeat2("aba", 1))

    def testRandom(self):
        string = chooseRandomSubstring()
        k = random.randrange(1, len(string))

        self.assertEqual(has_repeat1(string, k), has_repeat2(string, k))

    def test100(self):
        result = True

        for i in range(100):
            string = chooseRandomSubstring()
            if (len(string) == 1):
                k = 1
            else:
                k = random.randrange(1, len(string))


            result = (has_repeat1(string, k) == has_repeat2(string, k))

        self.assertTrue(result)

class TestDiv(unittest.TestCase):
    def testBaseCases(self):
        self.assertEqual(div("1010", "10"), "101")
        self.assertEqual(div("1010", "11"), "11")
        self.assertEqual(div("10001", "1"), "10001")
        self.assertEqual(div("11001", "100"), "110")

    def testRandom(self):
        self.assertTrue(compareRandomDiv())
        self.assertTrue(compareRandomDivSmaller())

    def test100(self):
        result = True
        for i in range(100):
            result = compareRandomDiv() and compareRandomDivSmaller()

        self.assertTrue(result)

class TestLeq(unittest.TestCase):
    def testBaseCases(self):
        self.assertTrue(leq("11", "100"))
        self.assertFalse(leq("100", "11"))
        self.assertTrue(leq("1010", "1010"))
        self.assertFalse(leq("1010", "0"))
        self.assertTrue(leq("1010","1011"))

    def testRandom(self):
        self.assertTrue(compareRandomLeq())

    def test100(self):
        result = True
        for i in range(100):
            result = compareRandomLeq()

        self.assertTrue(result)


class TestDec(unittest.TestCase):
    def testBaseCases(self):
        self.assertEqual(dec("1"), "0")
        self.assertEqual(dec("10"), "1")
        self.assertEqual(dec("110"), "101")
        self.assertEqual(dec("1000"), "111")

    def testRandom(self):
        self.assertTrue(compareRandomDec())

    def test100(self):
        result = True
        for i in range(100):
            result = compareRandomDec()

        self.assertTrue(result)

class TestSub(unittest.TestCase):
    def testBaseCases(self):
        self.assertEqual(sub("0", "0"), "0")
        self.assertEqual(sub("1000", "0"), "1000")
        self.assertEqual(sub("1000", "1"), "111")
        self.assertEqual(sub("101", "100"), "1")

    def testRandom(self):
        self.assertTrue(compareRandomSub())

    def test100(self):
        result = True
        for i in range(100):
            result = compareRandomSub()

        self.assertTrue(result)


class TestInc(unittest.TestCase):
    def testBaseCases(self):
        self.assertEqual(inc("0"), "1")
        self.assertEqual(inc("1"), "10")
        self.assertEqual(inc("101"), "110")
        self.assertEqual(inc("111"), "1000")
        self.assertNotEqual(inc("111"), "1001")

    def testRandom(self):
        self.assertTrue(compareRandomInc())

    def test100(self):
        result = True
        for i in range(100):
            result = compareRandomInc()

        self.assertTrue(result)

class TestLegalPar(unittest.TestCase):
    def testBaseCases(self):
        self.assertTrue(legal_par("<<>>"))
        self.assertFalse(legal_par("<{>}"))
        self.assertTrue(legal_par("<<{}<>()[<>]>>"))
        self.assertFalse(legal_par("{{{]}}"))

    def testComplicated(self):
        str = '{' * 100 + "<" * 50 + 20 * "[[[]]]" + 10 * "()" + 50 * ">" + 100 * "}"

        self.assertTrue(legal_par(str))
        self.assertFalse(legal_par(str+"("))

    def testMoreOpenersThanClosers(self):
        str = '{' * 100 + "<" * 50 + 20 * "[[[]]]" + 10 * "()" + 50 * ">" + 100 * "}" + "{"

        self.assertFalse(legal_par(str + "("))

    def testMoreClosersThanOpeners(self):
        str = '{' * 100 + "<" * 50 + 20 * "[[[]]]" + 10 * "()" + 50 * ">" + 100 * "}" + "}"

        self.assertFalse(legal_par(str + "("))

class TestSumDivisors(unittest.TestCase):
    def testBaseCases(self):
        self.assertEqual(sum_divisors(1), 0)
        self.assertEqual(sum_divisors(2), 1)
        self.assertEqual(sum_divisors(4), 3)
        self.assertEqual(sum_divisors(220), 284)

    def testRandom(self):
        self.assertEqual(True, compareRandomSumDivisors())

    def testPrime(self):
        self.assertEqual(sum_divisors(5), 1)
        self.assertEqual(sum_divisors(31), 1)

    def test100(self):
        for i in range(100):
            result = compareRandomSumDivisors()
            if result == False:
                break

        self.assertEqual(result, True)