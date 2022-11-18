#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input())
    x_arr = []
    y_arr = []
    for n_itr in range(n):
        xy = input().split()

        x = int(xy[0])

        y = int(xy[1])
        
        x_arr.append(x)
        y_arr.append(y)
        
    if len(set(x_arr))==1 or len(set(y_arr))==1:
        print('YES')
    else:
        print('NO')
