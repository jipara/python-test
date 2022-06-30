def add(*args):
    print(args[2])
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(2, 3, 6))
