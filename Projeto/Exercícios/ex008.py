# Calculator with While

while True:
    num_1_ = input("Digit the value one: ")
    num_2_ = input("Digit the value two: ")
    operation_ = input("Choose the operation ( + , - , * , / ): ")
    if num_1_.isdigit() and num_2_.isdigit():
        num_1 = float(num_1_)
        num_2 = float(num_2_)
        if operation_ == "+":
            sum = num_1 + num_2
            print(f"{num_1} {operation_} {num_2}: {sum}")
        elif operation_ == "-":
            sub = num_1 - num_2
            print(f"{num_1} {operation_} {num_2}: {sub}")
        elif operation_ == "*":
            product = num_1 * num_2
            print(f"{num_1} {operation_} {num_2}: {product}")
        elif operation_ == "/":
            if num_2 != 0:
                div = num_1 / num_2
                print(f"{num_1} {operation_} {num_2}: {div}")
            else:
                raise ZeroDivisionError(f"{num_1} {operation_} {num_2}: Divisão inválida!")  
        choose_ = input("Deseja parar? [s]im [n]ão: ").lower()
        if choose_ == "s":
            break 