def cachedFibonacci(int, dict):
    if int in dict:
        return dict[int]
    elif int == 1 or int == 0:
        return int
    else:
        dict[int] = cachedFibonacci(int-1,dict) + cachedFibonacci(int-2,dict)
        return cachedFibonacci(int-1,dict) + cachedFibonacci(int-2,dict)

FIBONACCI = 998

cachedFibonacci(FIBONACCI,dict={})
