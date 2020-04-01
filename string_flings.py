#!/usr/bin/env python3


def main():
    # Problem 1
    season = "spring"
    # Problem 2
    sf = season + " fling"
    print(sf)
    # Problem 3
    print(season)  # season has not changed
    # Problem 4
    temp = season
    season = "summer"
    print(temp)
    # Problem 5
    print(temp + " " + season)


if __name__ == "__main__":
    main()
