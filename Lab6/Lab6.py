# Задание 1
def task1(name_input, name_output):
    with open(name_input, "r") as file:
        num = list(map(int, file.read().split()))
    product = 1
    for n in num:
        product *= n
    with open(name_output, "w") as file:
        file.write(str(product))


task1("input.txt", "output.txt")


# Задание 2
def task2(name_input, name_output):
    with open(name_input, "r") as file:
        num = [int(line.strip()) for line in file]
    sorted_numbers = sorted(num)
    with open(name_output, "w") as file:
        for n in sorted_numbers:
            file.write(f"{n}\n")


task2("input2.txt", "output2.txt")


# Задание 3
def task3():
    with open("children.txt", "r", encoding="utf-8") as file:
        children = [line.strip().split() for line in file]
    children = [[last_name, first_name, int(age)] for last_name, first_name, age in children]
    oldest_child = max(children, key=lambda x: x[2])
    youngest_child = min(children, key=lambda x: x[2])
    with open("oldest.txt", "w", encoding="utf-8") as file:
        file.write(f"{oldest_child[0]} {oldest_child[1]} {oldest_child[2]}\n")
    with open("youngest.txt", "w", encoding="utf-8") as file:
        file.write(f"{youngest_child[0]} {youngest_child[1]} {youngest_child[2]}\n")


task3()
