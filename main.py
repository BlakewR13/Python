print("Howdy world")








def multipicaton():

    x = input("Give me a number to multiply:")
    y = input("What do you want to multiply by?")

    z = int(x) * int(y)

    print("The result is " + str(z))




def division(): 
    
    x = input("Give me a dividant:")
    y = input("What do you want to divide by?")

    z = float(x) / int(y)

    print("The result is " + str(z))


def wide_boy_str():
    user_str = input("Give me a string to w i d e n ")

    for char in user_str:
        print(char, end=" ")



def wide_boy_str_2():
    user_str = input("Give me a string to w i d e n ")

    i = 0

    wide_str = ""

    for char in user_str:

        if i < len(user_str) - 1:
            wide_str + wide_str + char + " "
        else:
            wide_str + wide_str + char 

        i += 1

    print(wide_str)



def for_loop_example():
    x = int(input("How many times should I run?"))

    for i in range(x):
        print("This loop is running for the "+ str(i+1) +" time.")



def odd_or_even():
    x = int(input("Which number do you want me to check?"))

    if x % 2 == 0:
        print("The number " + str(x)+" is even")
    else:
        print("The number " + str(x)+" is an odd duck")



def ascii_sum():
    user_str = input("Give me a string you would like the ascii values of its chars: \n ")

    str_size = len(user_str)

    i = 0

    sum = 0

    while(i < str_size):

        sum = sum + ord(user_str[i])
        i = i + 1

    print("The sum  of all these ASCII values is ", sum)





def string_flipper():
    user_str = input("Give me a string you would like flipped or reversed \n ")

    for char in reversed(user_str):
        print(char, end="")



user_input = int(input("Which function would you like to run?"))

if user_input == 0:
    multipicaton()
elif user_input ==1:
    division()
elif user_input == 2:
    wide_boy_str()
elif user_input == 3:
    wide_boy_str_2()
elif user_input == 4:
    for_loop_example()
elif user_input == 5:
    else_or_even()
elif user_input == 6:
    ascii_sum()
elif user_input == 7:
    string_flipper()