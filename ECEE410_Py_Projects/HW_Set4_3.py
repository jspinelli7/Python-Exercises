# Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter).
# For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20.

limit = int(input("Enter the upper limit for the function: "))

def multiple(limit):
    sum = 0
    for x in range(0, limit+1):
        if x % 3 == 0 or x % 5 == 0:
            sum += x
    print(f"The sum of multiples of 3 and 5 within your range is {sum}.")


multiple(limit)