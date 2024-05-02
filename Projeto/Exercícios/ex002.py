value_one = input("Write a value: ")
value_two = input("Write a value: ")

if value_one >= value_two:
    print(f"{value_one} is bigger or equal than {value_two}")
elif value_two >= value_one:
    print(f"{value_two} is bigger or equal than {value_one}")
else:
    print("Values invalids...")
    