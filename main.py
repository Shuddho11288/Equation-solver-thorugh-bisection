import time, decimal

# Main Function
def mybisec(f,a:float,b:float,N:int,err=1E-10):
    left = decimal.Decimal(a)
    right = decimal.Decimal(b)
    if f(left)*f(right)>0:
        raise RuntimeError(f"No approximate answer can be found from range {a} to {b}")
    for i in range(N):
        mid:float = (left + right) / 2
        res_mid = f(mid)
        if res_mid == 0 or abs(res_mid) < err:
            return mid
        elif res_mid < 0:
            left = mid
        else:
            right = mid
    return mid


# Testing Time
st = time.time()
func = lambda x: x**3 - 2*x + 1
result = mybisec(func,-9999999,9999999,10000000)
print("RESULT : {}".format(result))
print("ERROR : {}".format(func(result)))
et = time.time()
print('Total time needed:',et-st)

