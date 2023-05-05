import os
import logging

logging.basicConfig()
logger = logging.getLogger("RomanToInteger")
logger.setLevel(logging.DEBUG)

class RomanToInteger:
    @staticmethod
    def roman_to_int(s: str) -> int:
        # define a map of roman numerals and their integar values
        roman_numerals_map = {"I": 1,
                        "V": 5,
                        "X": 10,
                        "L": 50,
                        "C": 100,
                        "D": 500,
                        "M": 1000}
        # initialize result int_value
        int_value = 0
        len_of_s = len(s)
        # iterate of the input string 's'
        for i, x in enumerate(s.upper()):
            # the first condition below is a check to identify the last element of the string
            # the second condition checks if the current literal is less than the one following it
            if (len_of_s - 1 != i) and roman_numerals_map.get(s[i]) < roman_numerals_map.get(s[i+1]):
                int_value -= roman_numerals_map.get(x)
            else:
                int_value += roman_numerals_map.get(x)
        logger.info(f"The integer value of Roman numeral:{s} is: {int_value}")
        return int_value


if __name__ == "__main__":
    RomanToInteger().roman_to_int(s=os.getenv("input_str"))
