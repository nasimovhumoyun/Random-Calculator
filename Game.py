from operations import operator
import random
mark = 0
game = True
while game:
    operators = random.choice(operator)
    if operators == "+":
        value1 = random.randint(0, 101)
        value2 = random.randint(0, 101)
        answer = value1+value2
    elif operators == "*":
        value1 = random.randint(0, 11)
        value2 = random.randint(0, 101)
        answer = value1*value2
    elif operators ==":":
        value1 = random.randint(0, 101)
        value2 = random.randint(0, 101)
        if value1%value2 == 0:
            answer = value1%value2
        else:
            continue
    else:
        value1 = random.randint(0, 101)
        value2 = random.randint(0, 101)
        answer = value1-value2
    print(f"{value1} {operators} {value2}")
    user_answer = int(input(">>>>"))
    if user_answer == answer:
        print("Correct")
        mark += 1
        game = True
    else:
        print("Your last answer is INCORRECT")
        print(f"Correct answer is {answer}")
        print(f"Your mark is {mark}")
        game = False