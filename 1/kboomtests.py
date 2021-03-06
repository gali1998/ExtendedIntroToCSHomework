import unittest
from skeleton import *

class TestHW1(unittest.TestCase):
    def test_random_q5(self):
        result = k_boom(100, 200, 6)
        expected = "100 101 boom! 103 104 105 boom! 107 boom! 109 110 111 112 113 boom! 115 boom! 117 118 119 boom! 121 122 123 124 125 bada-boom! 127 128 129 130 131 boom! 133 134 135 boom! 137 boom! 139 140 141 142 143 boom! 145 boom! 147 148 149 boom! 151 152 153 154 155 bada-boom! 157 158 159 boom! boom! bada-boom! boom! boom! boom! boom-boom! boom! bada-boom! boom! 170 171 172 173 boom! 175 boom! 177 178 179 boom! 181 182 183 184 185 bada-boom! 187 188 189 190 191 boom! 193 194 195 boom! 197 boom! 199 200"

        self.assertEqual(result, expected)