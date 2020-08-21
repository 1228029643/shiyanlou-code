for i in range(1,101):
    a = i % 7
    b = i % 10
    c = i // 7
    if a != 0 and b != 7 and c != 10:
        print(i)
    else:
        pass
