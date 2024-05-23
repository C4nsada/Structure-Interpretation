def decrease(x):
    if x <= 0:
        return 0
    elif x % 2 != 0:
        return x - 2
    else:
        return x - 3

def fractionSum(x, y):
    ans = 1/x - 1/y
    print(f"x = {x} ; y = {y} ; [1/x - 1/y] = {ans}")
    print()
    return ans
    

def row(func, decr, x, y):
    if x + y <= 4:
        return func(x, y)
    elif x + y <= 0:
        return 0
    else:
        return func(x, y) + row(func, decr, decr(decr(x)), decr(x))

def outerFunction(x, y):
    return row(fractionSum, decrease, x, y)

print()

x = 13
y = x + 2
print(outerFunction(x, y))
