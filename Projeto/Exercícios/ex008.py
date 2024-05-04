# Calculator with While

while True:
    num_1_ = input("Digit the value one: ")
    num_2_ = input("Digit the value two: ")
    if num_1_.isdigit() and num_2_.isdigit():
        num_1 = float(num_1_)
        num_2 = float(num_2_)
        division_ = input(f"[1]: num_1/num_2 or [2]: num_2/num_1? ")
        if (int(division_) == 1):
            if (num_2 != 0):
                print(f"{num_1}+{num_2}: {(num_1+num_2)}\n{num_1}-{num_2}: {(num_1-num_2)}\n{num_1}*{num_2}: {(num_1*num_2)}\n{num_1}/{num_2}: {(num_1/num_2)}")
        elif (int(division_) == 2):
            if (num_1 != 0):
                print(f"{num_1}+{num_2}: {(num_1+num_2)}\n{num_1}-{num_2}: {(num_1-num_2)}\n{num_1}*{num_2}: {(num_1*num_2)}\n{num_2}/{num_1}: {(num_2/num_1)}")

        choose_ = input("Deseja sair? [s]air [n]ão:").lower().endswith('s')
        if choose_:
            break