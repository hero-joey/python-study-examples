if __name__ == '__main__':
    list1 = [1, 2, 3]
    print(type(list1))
    print(list("123"))
    a = []
    print(len(a))

    b = [1, 2.2, "hello", [1, 2]]
    print(type(b[1]))
    print(type(b[2]))
    print(type(b[3]))

    a = [1, 2, 3]
    print(len(a))
    a.append(4)
    print(len(a))
    a.insert(0, -2)
    print(a)
    print(len(a))
    b = list(range(1, 100))
    # print(b)
    print(b[10])
