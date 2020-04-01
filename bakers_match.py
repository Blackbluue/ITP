#!/usr/bin/env python3


def main():
    # Problem 1
    num_people = int(input("How many people will attend: "))
    if num_people >= 10:
        cookies_per_person = 2  # Problem 2
    else:
        cookies_per_person = 3  # Problem 3
    # Problem 4
    print("Prepared to bake %d cookies!" % (cookies_per_person * num_people))


if __name__ == "__main__":
    main()
