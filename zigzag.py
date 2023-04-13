def convert(s, n):
    result = ""
    step = ((n-1) * 2)
    for row in range(n):
        start = row
        end = len(s)
        take = list(range(start, end, step))
        if row != 0 and row != n-1:
            start = (n-row) * 2 -1
            take += list(range(start, end, step))
            take.sort()

        for i, c in enumerate(s):
            if i in take:
                result += c

    return result

print(convert("paypalishiring", 3))
