import time

print("hello! this is a calculator written in python")
time.sleep(1)

print(
"""
What do you want to calculate?
1. +
2. -
3. *
4. /
"""
)

calculateanswer = input(">")

if calculateanswer == "1":
    print(
"""alright!

please input your first number(s)"""
    )
    firsinputadding = int(input())

    print("please add you second input")
    time.sleep(1)
    secondinputadding = int(input())

    answeradding = int(firsinputadding) + int(secondinputadding)
    print(answeradding)

if calculateanswer == "3":
    print(
"""multiplication! alright!

please input your first number(s)"""
    )
    firsinputmultiplication = int(input())

    print("please add you second input")
    time.sleep(1)
    secondinputmultiplication = int(input())

    answermultiplication = int(firsinputmultiplication) * int(secondinputmultiplication)
    print(answermultiplication)


if calculateanswer == "2":
    print(
"""minus! okay

please input your first number(s)"""
    )
    firsinputminus = int(input())

    print("please add you second input")
    time.sleep(1)
    secondinputminus = int(input())

    answerminus = int(firsinputminus) - int(secondinputminus)
    print(answerminus)


if calculateanswer == "4":
    print(
"""uuuh idk.. doing that alright!

please input your first number(s)"""
    )
    firsinputidk = int(input())

    print("please add you second input")
    time.sleep(1)
    secondinputidk = int(input())

    answeridk = int(firsinputidk) / int(secondinputidk)
    print(answeridk)
