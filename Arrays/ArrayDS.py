#Array-DS
#Author: Mihai Munteanu
#Date: 21 Feb 2017

n = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))
arr_reversed = []
for i in range(n):
    arr_reversed.append(str(arr[n-1-i]))
print " ".join(arr_reversed)
