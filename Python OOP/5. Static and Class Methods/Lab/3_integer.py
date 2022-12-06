from math import floor

class Integer:
    def __init__(self, value: int):
        self.value = value

    
    @classmethod
    def from_float(cls, float_value):
        if not isinstance(float_value, float):
            return "value is not a float"
        
        return cls(floor(float_value))


    @classmethod
    def from_roman(cls, num):
        result = Integer.convert_to_decimal(num)
        return cls(result)


    @classmethod
    def from_string(cls, value):
        if not isinstance(value, str):
            return "wrong type"

        try:
            number = int(value)
            return cls(number)
        except:
            return "wrong type"


    @staticmethod
    def convert_to_decimal(num):
        roman_numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 }
        result = 0
        for i, c in enumerate(num):
            if (i + 1) == len(num) or roman_numerals[c] >= roman_numerals[num[i + 1]]:
                result += roman_numerals[c]
            else:
                result -= roman_numerals[c]
        return result


# Test Code
first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("LXVIDC")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))

