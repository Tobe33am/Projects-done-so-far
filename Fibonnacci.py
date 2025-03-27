#A Febornoulli program
def fibonacci(n):
    #defining n where i describe different outputs for different data type inputs
    if n <= 0:
        raise ValueError("Input must be a positive integer.")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    print("Welcome to the Fibonacci Sequence program!")
    
    while True:
        try:
            n = int(input("How many Fibonacci terms do you want to generate? "))
            if n <= 0:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    print(f"The first {n} terms of the Fibonacci sequence are:")
    for i in range(1, n + 1):
        print(fibonacci(i), end=' ')
    print()  # For a new line after printing the sequence

if __name__ == "__main__":
    main()