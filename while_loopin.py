#!/usr/bin/env python3


def main():
    # Problem 1
    num = 200
    count = 0
    while num >= 1:
        num /= 2
        count += 1
    print("Can be divided %d times" % count)
    # Problem 2
    num_1 = 10
    num_2 = 1
    counter = max(num_1, num_2)
    end = min(num_1, num_2)
    print(counter)
    while counter != end:
        counter -= 1
        print(counter)
    print("Blast Off!")


if __name__ == "__main__":
    main()
