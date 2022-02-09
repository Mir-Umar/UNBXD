# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 14:19:12 2022

@author: Mir Umar
"""

def LongestSubstr(s):
        def chk(start, end):
            chars = [0] * 128
            for i in range(start, end + 1):
                c = s[i]
                chars[ord(c)] += 1
                if chars[ord(c)] > 1:
                    return False
            return True
 
        n = len(s)
 
        res = 0
        for i in range(n):
            for j in range(i, n):
                if chk(i, j):
                    res = max(res, j - i + 1)
        return res
    
#Time Complexity: O(N^3), where N is the length of the string.
#Space Complexity: O(min(N, M)), as HashSet is used. N is the length of the string and M is the size of the substrings.