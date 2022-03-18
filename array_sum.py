'''Input: 1 4 2 5
Output: 2
Explanation: If 2 is the partition, 
      subarrays are : {1, 4} and {5}

Input: 2 3 4 1 4 5
Output: 1
Explanation: If 1 is the partition, 
Subarrays are : {2, 3, 4} and {4, 5}'''

s = [2, 3, 4, 1, 4, 5]
s = [1, 4, 2, 5]

def array_sum(s):

    for i in range(1, len(s)):
        rhs = s[:i]
        lhs = s[i+1:]
        if sum(rhs) == sum(lhs):
            return (rhs, lhs)

    return 0

out = array_sum(s)
print(out)



