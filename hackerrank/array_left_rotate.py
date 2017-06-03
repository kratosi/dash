"""
Print a single line of  space-separated integers denoting the final state of the array after performing  left rotations.

Sample Input

5 4
1 2 3 4 5
Sample Output

5 1 2 3 4
Explanation

When we perform  left rotations, the array undergoes the following sequence of changes:

Thus, we print the array's final state as a single line of space-separated values, which is 5 1 2 3 4.
"""

i = map(int, raw_input().split())
n, d = i[0], i[1]

arr = map(int, raw_input().split())

# (i - d) % n = pos
# i  = ((n * n) + pos) + d

for i in range(0, n):
    pos = (n*n + d + i) % n
    print arr[pos],
