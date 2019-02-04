# fibonacci series
def fib(n):
    cnt = 0
    n1 = 0
    n2 = 1

    if (n < 0):
        print("enter positvie values")
    elif(n ==1):
        print("Fibonacci series:")
        print(n1)
    else:
        while(cnt <= n):
            print(n1,end=',')
            nxt = n1 + n2
            n1 = n2
            n2 = nxt
            cnt += 1


fib(10)
