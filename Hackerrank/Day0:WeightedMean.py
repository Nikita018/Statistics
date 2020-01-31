###########################################################################################################################
Objective
In the previous challenge, we calculated a mean. In this challenge, we practice calculating a weighted mean. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given an array, , of  integers and an array, , representing the respective weights of 's elements, calculate and print the weighted mean of 's elements. Your answer should be rounded to a scale of  decimal place (i.e.,  format).

Input Format

The first line contains an integer, , denoting the number of elements in arrays  and .
The second line contains  space-separated integers describing the respective elements of array .
The third line contains  space-separated integers describing the respective elements of array .

Constraints

, where  is the  element of array .
, where  is the  element of array .
Output Format

Print the weighted mean on a new line. Your answer should be rounded to a scale of  decimal place (i.e.,  format).
##############################################################################################################################


Solution :

size = int(input())
numbers = list(map(int, input().split()))
weights = list(map(int, input().split()))
sum_num = 0

n = len(numbers)
for i in range(0,n):
    sum_num = (numbers[i]*weights[i]) + sum_num
print(round(sum_num/sum(weights),1))
