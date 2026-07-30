'''
input : [12,45,63,20,96,25,10]
output: [12,20,96,10]



1)create an empty list 
2)traverse array and check element is even or odd
3)if element is even add it to res
4)display res

Brute-force approach: O(n) time complexity and O(n) space complexity

arr = list(map(int, input().split()))
res = []
for num in arr:
    if num % 2 == 0:
        res.append(num)

print(res)

two_pointer_optimization approach: O(n) time complexity and O(1) space complexity

arr = list(map(int, input().split()))
i = 0
for j in range(len(arr)):
    if arr[j] % 2 == 0:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
print(arr[:i])

s = list("python")

left = 0
right = len(s) - 1

while left < right:
    s[left], s[right] = s[right], s[left]
    left += 1
    right -= 1

print("".join(s))
'''

s = "python"
res = ""

for i in range(len(s)): 
    if s[i] not in res: 
        res += s[i]
