import random
answer = "y"

answer = input("Do you want  to roll dice?(y/n)")

no_ = random.randint(1,6)
while answer == "n":
    break
while answer == "y":
    no_ = random.randint(1,6)
    if no_ == 1:
        print('1')
    elif no_ == 2:
        print('2')
    elif no_ == 3:
        print('3')
    elif no_ == 4:
        print('4')
    elif no_ == 5:
        print('5')
    elif no_ == 6:
        print('6')
    answer = input("Do you want  to roll dice?(y/n)")
