import re
from unidecode import unidecode


def palindrome(test):
    sanitized = re.sub(r'[^a-zA-Z0-9]+', "", unidecode(test.lower()))
    return sanitized == sanitized[::-1]


def main():
    while (True):
        test = input("Enter string to test for palindrome or 'exit': ")
        if test == 'exit':
            exit(0)
        print("Palindrome test: {}".format(palindrome(test)))


if __name__ == "__main__":
    main()
