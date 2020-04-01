#!/usr/bin/env python3


def main():
    # Problem 1 + 5
    grovery_list = {"Pie":  5.63,
                    "Paper towels": 13.40,
                    "Milk": 3.99,
                    "Frozen Tater Tots": 4.57,
                    "Cake": 2.47}
    print(", ".join(grovery_list.keys()))
    # Problem 2
    total = sum(grovery_list.values())
    print("Total grocery list cost: %g" % total)
    # problem 4
    favorite_snack = "Lemon Icebox Pie"
    print(favorite_snack * 100)
    print("test")
    # Problem 4
    print(" ".join([favorite_snack] * 100))


if __name__ == "__main__":
    main()
