import time


def start_of_program():
    print("hello! this is a calculator written in python")
    time.sleep(1)

    print("""
        What do you want to calculate?
        1. +
        2. -
        3. *
        4. /
        5. BMI
        """)

    return input(">")


calculateanswer = start_of_program()


def calculation_finished():
    time.sleep(1)
    print("""You have finished calculating, would you like to calculate something again?
    1. yes
    2. no (end the program)
    3. use the answer from your last calculation in the next.
    """)
    end_of_program = input(">")

    if end_of_program == "1":
        start_of_program()
    elif end_of_program == "2":
        print("you exited program")
        exit()


if calculateanswer == "1":
    print("please input your first number(s)")
    first_input_adding = input(">")
    print("please input your second number(s)")
    second_input_adding = input(">")
    print(int(first_input_adding) + int(second_input_adding))
    calculation_finished()
elif calculateanswer == "2":
    print("please input your first number(s)")
    first_input_minus = input(">")
    print("please input your second number(s)")
    second_input_minus = input(">")
    print(int(first_input_minus) - int(second_input_minus))
    calculation_finished()
elif calculateanswer == "3":
    print("please input your first number(s)")
    first_input_multiply = input(">")
    print("please input your second number(s)")
    second_input_multiply = input(">")
    print(int(first_input_multiply) * int(second_input_multiply))
    calculation_finished()
elif calculateanswer == "4":
    print("please input your first number(s)")
    first_input_divide = input(">")
    print("please input your second number(s)")
    second_input_divide = input(">")
    print(int(first_input_divide) / int(second_input_divide))
    calculation_finished()
elif calculateanswer == "5":
    print("please input your weight")
    weight = float(input(">"))
    print("please input your length. Like 1.70 meters, not 170 meters, not 1,70, but 1.70")
    length = float(input(">"))
    lenth_x_length = length * length
    output_bmi = weight / lenth_x_length
    print(output_bmi)
    calculation_finished()
else:
    print("invalid syntax! please try again!")
    start_of_program()
