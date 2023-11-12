# Start the Gaem
# Ask the USer to make Move (r,p,s)
# PC would Chose Move Randomly
# PC === Player =>Tie
#( PC == P and Pc == Rock) or (User == r and pc == Scissors) or  (User == S and pc == P) => USer Won
# any other Case 
#  PC Won / you Lose 

import random

user = input ("what is your Chose ? 'r' for rock , 'p' for Paper , 's' For Scissors \n")
pc = random.choice(["r","p","s"]) 

# Function to PRint Result When User Win
def result ():
   res = print('you won' , "you played : " + user , "and Pc played : " + pc  )
   return res

if(user == pc):
    print('tie')
elif(user == "r" and pc == "s" or user == "p"  and pc == "r"  or user == "s" and pc == "p"):
    result()
else:
    print("PC won" ,  "you played : " + user , "and Pc played : " + pc )


