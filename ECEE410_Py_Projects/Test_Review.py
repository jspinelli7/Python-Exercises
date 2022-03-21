




"""
for x in range(-50, 51):
    for y in range(-50, 51):
        if 2*x+3*y == 4 and x-y == 7:
            print(x,y)
"""
"""
class IOString():
    def __init__(self):
        self.str1 = ""

    def get_String(self):
        self.str1 = input("Input the string \n")

    def print_String(self):
        print("Your string all in upper case: ")
        print(self.str1.upper())


str3 = IOString()
str3.get_String()
str3.print_String()
"""

"""
user1 = input("Enter Plater 1 name: ")
user2 = input("Enter Player 2 name: ")
u1 = input(f"{user1}, do you choose rock, paper or scissors?")
u2 = input(f"{user2}, do you choose rock, paper or scissors?")

def compare(u1, u2):
    if u1 == u2:
        return("It's a tie!")
    elif u1 == 'rock':
        if u2 == 'scissors':
            return("Rock wins!")
        else:
            return("Paper wins!")
    elif u1 == 'scissors':
        if u2 == 'paper':
            return('Scissors wins!')
        else:
            return('Rock wins!')
    elif u1 == 'paper':
        if u2 == 'rock':
            return("Paper wins!")
        else:
            return("Scissors win!")
    else:
        return("Invalud input! Enter the correct selections.")

print(compare(u1, u2))
"""

"""
start = int(input("Enter the starting number: "))
end = int(input("Enter a number: "))

for val in range(start, end+1):
    if val > 1:

        for n in range(2, val):
            if val % n == 0:
                break
            else:
                print(val)
"""

list_1 = [1, 5, 12, 75, 203, 20, 2]

even_count, odd_count = 0,0

for num in list_1:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even numbers in the list:")

