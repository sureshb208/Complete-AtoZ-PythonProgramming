# you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr = list(set(arr))
    ar = len(arr)
    print(ar)
    res = sorted(arr)
    print(res)
    print(res[ar-2])

import numpy as np
arr = np.array([1,2,3,4,5,8,5,4,3,2,1,0, -1, 0])

def sor_arr(n):
    n = sorted(set(n))
    return n
print(sor_arr(arr))


#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.(LeetCode)
def twoSum(nums, target):
        values = {}
        for i, num in enumerate(nums):
            remaining = target - num
            #print(remaining)
            #print(values)
            if remaining in values:
                #print(values[remaining])
                return [i, values[remaining]]
            else:
                values[num] = i
        return "NO values"

nums =[2,7,11,15,4]
target = 13

twoSum(nums, target)


#Remove Duplicates from Sorted Array(LeetCode)
def remove_duplicate(nums):
    n = len(set(nums))
    return n , sorted(set(nums))

nums = [0,0,1,1,1,2,2,3,3,4]

n, nums = remove_duplicate(nums)
print(n)
print("num = {}".format(nums))


#Given number is Prime number or not
num = int(input("Enter the number : "))

for i in range(2, num):
    if num % i == 0:
        print("Not a prime")
        break
else :
    print("prime")


#Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
# You are given n scores. Store them in a list and find the score of the runner-up.
def runner_up(n):
    n = sorted(set(n))
    print(n)
    return n[-2]

n =[2,3,6,6,5,7,9,10]
print(runner_up(n))


#  Reverse Integer
# TypeError: 'int' object is not subscriptable. Try using str
def reverse(x):
    if x>0:
        x = str(x)
        x = x.rstrip('0')
        return (x[::-1])
    else:
        a = -1*x
        a = str(a)
        a = a.rstrip('0')
        a = a[::-1]
        return int(a)*-1

print(reverse(-120))


# Merge Two Sorted Lists
l1 = [1,2,4]
l2 = [1,3,4]

def sor_list(l1, l2):
    l1 = sorted(l1)
    l2 = sorted(l2)
    l = sorted(l1+l2)
    return l

print(sor_list(l1, l2))

#Remove Nth Node From End of List
head = [1,2,3,4,5]

def rem_node(l, n):
    l = list(l)
    l.pop(n) 
    return l

print(rem_node(head, 2))
head = [1]
print(rem_node(head ,0))

