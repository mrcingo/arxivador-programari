sort = [-40, 21, 54, 4000000, 2, 40, 10000]
old = []
for j in range(len(sort)):
    for i in range(len(sort)):
        try:
            if sort[i + 1] > sort[i]:
                previous = sort[i]
                sort[i] = sort[i + 1]
                sort[i + 1] = previous
        except IndexError:
            pass
print(sort)