#2DArrayDS
#Author: Mihai Munteanu
#Date 21 Feb 2017
n = 6
arr = []
for arr_i in xrange(n):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)
max_sum = -10000
for i in range(n-2):
    for j in range(n-2):
        this_sum = arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
        if this_sum > max_sum:
            max_sum = this_sum
print max_sum

