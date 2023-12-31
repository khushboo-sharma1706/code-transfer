while True:
    try:
        n1 = int(input(f"Number 1 : "))
    except ValueError:
        print("Invalid Input..")

    else:
        print("Good Job!!")
        break

while True:
    try:
        n2 = int(input(f"Number 2 : "))
        if n2 == 0:
            print("Number 2 can't be 0")
            continue
    except ValueError as e:
        print(f"Invalid Input.. {e}")
    else:
        print("Good Job!!")
        break

try:
    print(f"Div : {n1/n2}")
except Exception as e:
    print(f"Error... {e}")

