#!/bin/python3

import math
import os
import random
import re
import sys


def maxSubarray(arr):
    s = 0
    h = -100000
    for i in arr:
        if i > 0:
            s += i
        else:
            if h < i:
                h = i

    if s == 0:
        s = h

    curr = 0
    mmax = 0
    for i in range(0, len(arr)):
        if curr > curr + arr[i]:
            curr = arr[i]
        mmax = max(mmax, curr)

    return [mmax, s]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()