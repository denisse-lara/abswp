#! python3
# strongPassword.py - Validates password strength
# Usage: strongPassword.py <password>

import sys, re

def validatePassword(password):
    if len(password) < 8:
        return "Error: Password must of eight characters long"

    lowerUpper = re.compile(r'[a-z]+[A-Z]+')
    if not lowerUpper.match(password):
        return "Error: Password must have lowercase and uppercase characters"

    oneDigit = re.compile(r'.{0,}\d.{0,}')
    if not oneDigit.match(password):
        return "Error: Password must have at least one digit"

    return "Valid password"

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: dateDetectionlpy <date>")
        sys.exit()

    password = sys.argv[1]

    print(validatePassword(password))
