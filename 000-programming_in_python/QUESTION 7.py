# to write a program to declare if entered number is prime or not

def is_prime(number):

    if number == 0 and number == 1:

        return False

    elif number > 1:

        for i in range(2, number):

            if (number % i == 0):

                return False

        else:

            return True

    else:

        return False


# calling statement for is_prime() with an arguement of 5
if __name__ == "__main__":
    print(is_prime(2))


# to declare def character frequency():

def character_frequency(string):

    dict = {}

    for i in string:

        if i in dict:

            dict[i] += 1

    return dict


user = input("enter string:")

# calling of def character frequency() with arguement
if __name__ == "__main__":

    print(character_frequency(user))
