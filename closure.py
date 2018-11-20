def outer():
    cnt = 0

    def inner():
        nonlocal cnt
        cnt += 1
        print(cnt)
    return inner


a = outer()
a()
a()
a()
a()
