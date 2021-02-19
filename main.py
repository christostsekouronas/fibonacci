import fibonacci_sequence

nterms = int(input("How many terms?: "))

if nterms < 0:
    print("Please provide only POSITIVE numbers")
else:
    fnumber = fibonacci_sequence.fibonacci(nterms)
    print("Fibonacci sequence: {}".format(fnumber))