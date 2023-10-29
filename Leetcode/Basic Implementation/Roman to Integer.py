# https://leetcode.com/problems/roman-to-integer/description/?envType=study-plan-v2&envId=programming-skills
def romanToInt(self, roman_str: str) -> int:
        roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }
    
        length = len(roman_str)
        num, total = 0, 0
    
        i = 0
        while i < length:
            if i == (length - 1):
                num = roman[roman_str[i]]
                i += 1
            elif roman[roman_str[i]] < roman[roman_str[i + 1]]:
                num = roman[roman_str[i + 1]] - roman[roman_str[i]]
                i = i + 2
            else:
                num = roman[roman_str[i]]
                i += 1
            total += num

        return total
