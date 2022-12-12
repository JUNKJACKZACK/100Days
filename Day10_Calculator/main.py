print("Welcome to the calculator machine!")
total = 0


def start_calc():
    global first_num, second_num, operation
    first_num = int(input("What is the first number you would like?"))
    operation = input("Pick an operator\n+\n-\n*\n/\n")
    second_num = int(input("What is the second number you would like?"))
    operator(operation)


def operator(chosen_operator):
    global first_num, second_num
    if chosen_operator == "+":
        total = first_num + second_num
        print(f"{first_num} + {second_num} = {total}")
    if chosen_operator == "-":
        total = first_num - second_num
        print(f"{first_num} - {second_num} = {total}")
    if chosen_operator == "*":
        total = first_num * second_num
        print(f"{first_num} * {second_num} = {total}")
    if chosen_operator == "/":
        total = first_num / second_num
        print(f"{first_num} / {second_num} = {total}")

def continued():
    global first_num, second_num, operation, total
    operation = input("Pick an operator\n+\n-\n*\n/\n")
    second_num = int(input("What is the second number you would like?"))
    if operation == "+":
        new_total = total + second_num
        print(f"{total} + {second_num} = {new_total}")
    if operation == "-":
        new_total = first_num - second_num
        print(f"{total} - {second_num} = {new_total}")
    if operation == "*":
        new_total = first_num * second_num
        print(f"{total} * {second_num} = {new_total}")
    if operation == "/":
        new_total = first_num / second_num
        print(f"{total} / {second_num} = {new_total}")

    total = new_total


start_calc()

redo = input(f"Type 'y' if you would like to continue calculoting with {total}, or \n type 'n' to start a new calculator")
if redo == "y":
    continued()
if redo == "n":
    start_calc()