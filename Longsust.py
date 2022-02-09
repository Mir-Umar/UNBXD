# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 14:27:02 2022

@author: Mir Umar
"""

def lonsunstr(s):
       
        slow=fast=0
        window =set()
        max_length = 0
        while fast < len(s):
            if s[fast] not in window:
                window.add(s[fast])
                fast+=1
            else:
                window.remove(s[slow])
                slow+=1
            max_length = max(max_length, fast - slow)
        return max_length