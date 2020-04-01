#!/usr/bin/env python3


def main():
    num_1 = 5
    num_2 = 16
    num_3 = 9
    # Problem 1
    print("sum_of_two_nums(%d, %d): %d"
          % (num_1, num_2, sum_of_two_nums(num_1, num_2)))
    # Problem 2
    print("greater_than_ten(%d): %s" % (num_2, greater_than_ten(num_2)))
    # Problem 3
    print("odd_or_even(%d): " % num_1, end="")
    odd_or_even(num_1)
    # Problem 4
    print("how_many_legs(%d, %d, %d): %d"
          % (num_1, num_2, num_3, how_many_legs(num_1, num_2, num_3)))
    # Problem 5
    print("multiple_of_3(%d): %s" % (num_3, multiple_of_3(num_3)))
    # Problem 6
    print("area_of_triangle(%d, %d): %d"
          % (num_1, num_2, area_of_triangle(num_1, num_2)))


# Problem 1
def sum_of_two_nums(n1, n2):
    return n1 + n2


# Problem 2
def greater_than_ten(num):
    return num > 10


# Problem 3
def odd_or_even(num):
    if num % 2 == 0:
        print("even")
    else:
        print("odd")


# Problem 4
def how_many_legs(num_cows, num_chickens, num_spiders):
    return (num_cows * 4) + (num_chickens * 2) + (num_spiders * 8)


# Problem 5
def multiple_of_3(num):
    return num % 3 == 0


# Problem 6
def area_of_triangle(base, height):
    return (base * height) / 2


if __name__ == "__main__":
    main()
