
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    elem_1 = elem_2 = 1
    summ = 0
    for i in range(3,n + 1):
        summ = elem_1 + elem_2
        elem_1 , elem_2 = elem_2 , summ
    return summ
        
for n in range(1,11):
    print(f"{n} --> {fib(n)}")
        