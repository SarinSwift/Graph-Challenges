

# 1.
# Slow time complexity
def fibo(num):
    if num == 0:
        return 0
    if num == 1:
        return 1

    return fibo(num-1) + fibo(num-2)


# 2.
# O(n) runtime because we're usign memoization

memo = {0: 0, 1:1}      # Global variable
def fib_memo(num, memo):
    if num not in memo:
        memo[num] = fib_memo(num - 1, memo) + fib_memo(num - 2, memo)

    return memo[num]



# 3.
# Using memoization with a callback(closure)!!

def memoize(func):
    memo = {}           # don't need to initialy put in 0 or 1 because we catch these cases in the fib() function

    def helper(num):    # adding to our dictionary of computed values
        if num not in memo:
            memo[num] = func(num)
        return memo[num]

    return helper

def fib(num):           # the function where we get the actual value of our fibonacci
    if num == 0:
        return 0
    if num == 1:
        return 1
    return fib(num-1) + fib(num-2)

fib = memoize(fib)      # create a variable to call from the memoize function
print(fib(100))         # it calculates the value of fibonacci sequence of the parameter value (uses memoization to
                        # make computation of the fibonacci sequences)


# print(fib_memo(100, memo))
