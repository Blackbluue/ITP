#!/usr/bin/env python3


def main():
    # Problem 1
    character_1 = 'i'
    string_1 = "I want a puppy"
    string_2 = "Supercalifragilisticexpialidocious"
    string_3 = "This dinner is not that bad!"
    string_4 = "xxh4ckermanoo"
    name_1 = "John Wick"
    print("The first character in string '{:s}' is '{:s}''".
          format(string_1, first_letter(string_1)))
    # Problem 2
    print("The last 3 characters in string '{:s}' are '{:s}''".
          format(string_1, last_three(string_1)))
    # Problem 3
    print("The number of '{:s}' characters in the string '{:s}' is {:d}".
          format(character_1, string_2, char_count(character_1, string_2)))
    # Problem 4
    print("The string '{:s}' with all vowels removed is '{:s}''".
          format(string_1, remove_vowels(string_2)))
    # Problem 5
    print(hello_goodbye(name_1, 1))
    # Problem 6
    print("The sPoOkY form of the string '{:s}' is '{:s}'".
          format(string_2, spooky(string_2)))
    # Problem 7
    print("The initials of '{:s}' are '{:s}'".format(name_1, initials(name_1)))
    # Problem 8
    print("The mixed up strings of '{:s}' and '{:s}' is '{:s}'".
          format(string_1, string_2, mixup(string_1, string_2, 4)))
    # Problem 9
    print("String '{:s}' translates to '{:s}'".
          format(string_3, not_bad(string_3)))
    # Problem 10
    print("133+ sp33k for '{:s}' is '{:s}'".
          format(string_3, h4ck3r_sp33k(string_3)))
    # Problem 11
    print("It is {:s} that the string '{:s}' has same number of x's and o's".
          format(str(same_x_and_o(string_4)), string_4))


# Problem 1
def first_letter(string):
    return string[0]


# Problem 2
def last_three(string):
    return string[-3:]


# Problem 3
def char_count(char, string):
    return string.lower().count(char.lower())


# Problem 4
def remove_vowels(string):
    vowles = "aeiou"
    result = ""
    for c in string:
        if c.lower() not in vowles:
            result += c
    return result


# Problem 5
def hello_goodbye(name, code):
    if code == 1:
        return "Hello, {:s}".format(name)
    elif code == 2:
        return "Goodbye, {:s}".format(name)
    else:
        return "Invalid code"


# Problem 6
def spooky(string):
    result = ""
    for index in range(len(string)):
        if index % 2 == 0:
            result += string[index].lower()
        else:
            result += string[index].upper()
    return result


# Problem 7
def initials(name):
    result = ""
    for word in name.split():
        result += word[0]
    return result


# Problem 8
def mixup(string_1, string_2, count=1):
    return (string_2[0:count] + string_1[count:]
            + " " + string_1[0:count] + string_2[count:])


# Problem 9
def not_bad(string):
    start = string.find("not")
    end = string.find("bad", start) + 3
    return string[:start] + "good" + string[end:]


# Problem 10
def h4ck3r_sp33k(string):
    translator = {
        'a': '4',
        'e': '3',
        'l': '1',
        't': '+'
    }
    result = ""
    for letter in string:
        result += translator.get(letter.lower(), letter)
    return result


# Problem 11
def same_x_and_o(string):
    return string.lower().count('x') == string.lower().count('o')


if __name__ == "__main__":
    main()
