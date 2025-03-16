# Задание 1
def count_unique_numbers(numbers):
    unique_numbers = set(numbers)
    return len(unique_numbers)


input1 = [1, 2, 3, 2, 1]
print(count_unique_numbers(input1))
input2 = [1, 2, 3, 4, 5, 6, 7]
print(count_unique_numbers(input2))
input3 = [1, 1, 1, 1, 1]
print(count_unique_numbers(input3))
input4 = [1, 2, 3, 1, 1]
print(count_unique_numbers(input4))
# inputn = map(int, input().split(', '))
# print(count_unique_numbers(inputn))


# Задание 2
def is_subset(set1, set2):
    return set1 - set2 == set() and set1 != set2


print(is_subset({1, 2, 3}, {1, 4, 5}))
print(is_subset({1, 2, 3, 4, 5, 6, 7}, {10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0}))
print(is_subset({1, 10, 223, 413, 2}, {1, 10, 223, 413, 2}))


# Задание 3
n = int(input())
cities = set()
for _ in range(n):
    city = input().strip()
    cities.add(city)

new_city = input().strip()

if new_city in cities:
    print("REPEAT")
else:
    print("OK")
