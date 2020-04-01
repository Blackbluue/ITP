#!/usr/bin/env python3


def main():
    # Problem 1
    num_1 = 5
    num_2 = num_1 + 5
    total = 0
    for n in range(num_1, num_2 + 1):
        total += n
    print("sum == %d" % total)
    # Problem 2
    vowels = "aeiou"
    crazy_string = "Pneumonoultramicroscopicsilicovolcanoconiosis"
    result = ""
    for letter in crazy_string:
        if letter in vowels:
            result += letter
    print(result)


if __name__ == "__main__":
    main()
