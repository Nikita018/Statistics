########################################################################################################################
Objective
In this challenge, we practice calculating quartiles. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given an array, , of  integers, calculate the respective first quartile (), second quartile (), and third quartile (). It is guaranteed that , , and  are integers.

Input Format

The first line contains an integer, , denoting the number of elements in the array.
The second line contains  space-separated integers describing the array's elements.

Constraints

, where  is the  element of the array.
Output Format

Print  lines of output in the following order:

The first line should be the value of .
The second line should be the value of .
The third line should be the value of .
###########################################################################################################################


from statistics import median
n = int(input())
num = sorted(list(map(int, input().split())))
print(int(median(num[:n//2])))
print(int(median(num)))
print(int(median(num[(n+1)//2:])))
