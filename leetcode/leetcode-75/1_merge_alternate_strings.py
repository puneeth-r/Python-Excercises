"""You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
Return the merged string
Example 1:
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r"""


class Solution:
    # Time Complexity: O(n+m), where n is the length of word1 and m is the length of word2.
    # Space Complexity: O(n+m), where n is the length of word1 and m because we are storing the merged string in a list.
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        i = 0
        len_word_1 = len(word1)
        len_word_2 = len(word2)
        while i <= len_word_1 - 1 or i <= len_word_2 - 1:
            if i < len_word_1:
                result.append(word1[i])
            if i < len_word_2:
                result.append(word2[i])
            i += 1
        return "".join(result)

print(Solution.mergeAlternately(Solution, "abc", "pqr"))