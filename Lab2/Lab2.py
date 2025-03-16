def pascal_triangle(n):
    t = [[1]]
    for i in range(1, n):
        prev_row = t[-1]
        new_row = [1]
        for j in range(1, len(prev_row)):
            new_row.append(prev_row[j - 1] + prev_row[j])
        new_row.append(1)
        t.append(new_row)

    for row in t:
        print(" ".join(map(str, row)))


def sierpinski_triangle(i):
    t = ["*"]
    for _ in range(i):
        space = " " * len(t)
        new_t = [space + row + space for row in t]
        new_t += [row + " " + row for row in t]
        t = new_t

    for row in t:
        print(row)


n = int(input())
pascal_triangle(n)
i = 5
sierpinski_triangle(i)
