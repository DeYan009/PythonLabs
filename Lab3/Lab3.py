# Задание 1
def compress_string(s):
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(s[i - 1] + (str(count) if count > 1 else ""))
            count = 1
    result.append(s[-1] + (str(count) if count > 1 else ""))
    return "".join(result)


s = input()
print(compress_string(s))


# Задание 1.1
def decompress_string(s):
    result = []
    i = 0
    while i < len(s):
        char = s[i]
        i += 1
        count = 0
        while i < len(s) and s[i].isdigit():
            count = count * 10 + int(s[i])
            i += 1
        result.append(char * (count if count > 0 else 1))
    return "".join(result)


s = input()
print(decompress_string(s))


# Задание 2
def top_three_characters(s):
    s = s.replace(" ", "")
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    sorted_chars = sorted(char_count.items(), key=lambda x: x[1], reverse=True)
    for char, count in sorted_chars[:3]:
        print(f"Символ: '{char}', Количество: {count}")


user_input = input()
top_three_characters(user_input)


# Задание 3
def number_to_text(n):
    ones = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
    teens = ["", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать",
             "восемнадцать", "девятнадцать"]
    tens = ["", "десять", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят",
            "девяносто"]
    hundreds = ["", "сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]

    if n == 1000:
        return "тысяча"

    result = []
    if n >= 100:
        result.append(hundreds[n // 100])
        n %= 100
    if 10 < n < 20:
        result.append(teens[n % 10])
    else:
        if n >= 10:
            result.append(tens[n // 10])
        if n % 10 > 0:
            result.append(ones[n % 10])
    return " ".join(result)


n = int(input())
if 1 <= n <= 1000:
    print(number_to_text(n))
else:
    print("error")
