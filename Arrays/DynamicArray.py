#DynamicArray
#Author: Mihai Munteanu
#Date: 21 Feb 2017
import sys

first_line = map(long, raw_input().strip().split(' '))
N = first_line[0]
Q = first_line[1]
seqList = [[] for i in range(N)]
lastAns = 0
for line in sys.stdin:
    data_input = map(long, line.strip().split(' '))
    if data_input[0] == 1:
        i = (data_input[1]^lastAns) % N
        seqList[i].append(data_input[2])
    elif data_input[0] == 2:
        i = (data_input[1]^lastAns) % N
        lastAns = seqList[i][data_input[2] % len(seqList[i])]
        print lastAns
    else:
        print "Data doesn't satisfy hypothesis!"

#Note that it's not really a big deal to implement a dynamic array in Python because lists are already dynamic


