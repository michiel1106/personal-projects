import time

variable1 = float(46)
variable2 = float(2.89)

print(variable1 / variable2)



print("hello! this is a calculator written in python")
time.sleep(1)

print(
    """
    What do you want to calculate?
    1. +
    2. -
    3. *
    4. /
    5. BMI
    """
)

calculateanswer = input(">")

if calculateanswer == "1":
    print("please input your first number(s)")
    first_input_adding = input(">")
    print("please input your second number(s)")
    second_input_adding = input(">")
    print(int(first_input_adding) + int(second_input_adding))
elif calculateanswer == "2":
    print("please input your first number(s)")
    first_input_minus = input(">")
    print("please input your second number(s)")
    second_input_minus = input(">")
    print(int(first_input_minus) - int(second_input_minus))
elif calculateanswer == "3":
    print("please input your first number(s)")
    first_input_multiply = input(">")
    print("please input your second number(s)")
    second_input_multiply = input(">")
    print(int(first_input_multiply) * int(second_input_multiply))
elif calculateanswer == "4":
    print("please input your first number(s)")
    first_input_divide = input(">")
    print("please input your second number(s)")
    second_input_divide = input(">")
    print(int(first_input_divide) / int(second_input_divide))
elif calculateanswer == "5":
    print("please input your weight")
    weight = float(input(">"))
    print("please input your length. Like 1.70 meters, not 170 meters, not 1,70, but 1.70")
    length = float(input(">"))
    lenth_x_length = length * length
    output_bmi = weight / lenth_x_length
    print(output_bmi)



