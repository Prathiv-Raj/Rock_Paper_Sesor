import random

print(" 1.rock \n 2.paper \n 3.sesor")

user_input=int(input("enter your choice:"))
print()

system_input=random.randint(1,3)

print("system_choice:",system_input)
print()

if user_input==1 and system_input==1:
    print("player choice : rock")
    print("system choice : rock")
    print("match is draw")
elif user_input==1 and system_input==2:
    print("player choice : rock")
    print("system choice : paper")
    print("system is won the match")
elif user_input==1 and system_input==3:
    print("player choice : rock")
    print("system choice : sesor")
    print("user is won the match")
elif user_input==2 and system_input==1:
    print("player choice : paper")
    print("system choice : rock")
    print("user won the match")
elif user_input==2 and system_input==2:
    print("player choice : paper")
    print("system choice : paper")
    print("match is draw")
elif user_input==2 and system_input==3:
    print("player choice : paper")
    print("system choice : sesor")
    print("system won the match")
elif user_input==3 and system_input==1:
    print("player choice : sesor")
    print("system choice : rock")
    print("system won the match")
elif user_input==3 and system_input==2:
    print("player choice : sesor")
    print("system choice : paper")
    print("user is won the match")
elif user_input==3 and system_input==3:
    print("player choice : sesor")
    print("system choice : sesor")
    print("draw the match")