#!/usr/bin/env python3
from itertools import starmap


def main():
    num = 13
    list_1 = [1, 15, 33, 13, 2]
    list_2 = [3, 15, 4, 7, 11, 9, 44]
    list_3 = ['ooga', 'booga', 'dog']
    list_4 = [1, -50, 4, -120, 460, -612, 90]
    students = [
        ['Maria', 91.5],
        ['George', 47.3],
        ['Anquan', 94.0],
        ['Lucia', 89.2]
    ]
    # Problem 1
    print("Largest number in {} is {}".format(list_1, largest_num(list_1)))
    # Problem 2
    print("It is {} that {} is in {}".
          format(includes(list_1, num), num, list_1))
    # Problem 3
    print("Average of the numbers in {} is {}".format(list_1, average(list_1)))
    # Problem 4
    print("Median of the numbers {} is {}".format(list_2, median(list_2)))
    # Problem 5
    print("Words with the letter 'a' in the list {} are {}".
          format(list_3, only_a(list_3)))
    # Problem 6
    print("Odd couple in list {} are {}".format(list_2, odd_couple(list_2)))
    # Problem 7
    print("The student with the highest average is {}".
          format(overachiever(students)))
    # Problem 8
    print("The total absolute value of the numbers {} is {}".
          format(list_4, absolute_total(list_4)))
    # Problem 9
    print("The sum of the cubes of {} is {}".
          format(list_4, sum_of_cubes(list_4)))
    # Problem 10
    print("{} summed and multiplied by index is {}".
          format(list_4, multiply_by_index(list_4)))


# Problem 1
def largest_num(nums):
    answer = nums[0]
    for n in nums[1:]:
        if n > answer:
            answer = n
    return answer


# Problem 2
def includes(nums, num):
    for n in nums:
        if n == num:
            return True
    return False


# Problem 3
def average(nums):
    return float(sum(nums)) / len(nums)


# Problem 4
def median(nums):
    nums = sorted(nums)
    if len(nums) % 2 == 0:  # even length of list
        return average((nums[len(nums)//2 - 1], nums[len(nums)//2]))
    else:  # odd length of list
        return float(nums[len(nums)//2])


# Problem 5
def only_a(words):
    result = []
    for word in words:
        if 'a' in word.lower():
            result.append(word)
    return result


# Problem 6
def odd_couple(nums):
    result = []
    for num in nums:
        if len(result) == 2:
            break
        elif num % 2 != 0:
            result.append(num)
    return result


# Problem 7
def overachiever(students):
    highest = students[0]
    for student in students[1:]:
        if student[1] > highest[1]:
            highest = student
    return highest


# Problem 8
def absolute_total(nums):
    return sum(map(abs, nums))


# Problem 9
def sum_of_cubes(nums):
    return sum(map(lambda n: n ** 3, nums))


# Problem 10
def multiply_by_index(nums):
    return sum(starmap((lambda index, num: num * index), enumerate(nums)))


if __name__ == "__main__":
    main()
