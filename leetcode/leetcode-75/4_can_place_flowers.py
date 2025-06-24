"""
605. Can Place Flowers
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false"""

from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i, spot in enumerate(flowerbed):
            if i==0 and spot==0:
                count+=1
                prev_spot = 1
            elif i!=0 and (prev_spot != 1 and spot==0):
                count+=1
                prev_spot = 1
            else:
                prev_spot = spot
        return count>=n

print(Solution.canPlaceFlowers(Solution, flowerbed=[1,0,0,0,0,1], n=2)) 
100001
101010