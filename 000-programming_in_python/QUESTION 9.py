# def for converting integer to roman numerals

def int_to_roman(n):

    # list of numbers and roman value that would be used as reference to convert entered number to roman numerals
    numbers = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]


# the list roman symbols in reference from the list of integer

    roman = ["I", "IV", "V", "IX", "X", "XL""L",
             "XC", "C", "CD", "D", "CN", "N"]

# here i=12 means the total count of element per each list in index count
    # i=12 for total number of index in each list above
    i = 12

    roman_numerals = ""

# this is loop that checks if entered arguement is satisfied in iteration or not

    while n != 0:
        if numbers[i] <= n:
            roman_numerals += roman[i]
            n = n-numbers[i]
        else:
            i = i-1

# here the return point for execution of function if all condition in a loop is satisfied
    return roman_numerals


# user input button
user = int(input("enter number:"))


# calling statement for_int_to_roman() with an arguement from user input button
if __name__ == "__main__":
    print(int_to_roman(user))
