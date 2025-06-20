"""1071. Greatest Common Divisor of Strings
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).
Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Example 1:
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:
Input: str1 = "ABABAB", str2 = "ABAB"
Output: AB"""

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if a common base string exists
        if str1 + str2 != str2 + str1:
            return ""
        
        # Manual implementation of gcd
        def gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a
        
        gcd_len = gcd(len(str1), len(str2))
        return str1[:gcd_len]