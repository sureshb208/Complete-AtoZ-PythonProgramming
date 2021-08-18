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