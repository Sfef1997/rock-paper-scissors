import random

user = input("What is your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
pc = random.choice(["r", "p", "s"])

print(f"You played: {user}")
print(f"PC played: {pc}")

if user == pc:
    print('It\'s a tie!')
elif (user == "r" and pc == "s") or (user == "p" and pc == "r") or (user == "s" and pc == "p"):
    print('You won!')
else:
    print('PC won!')
