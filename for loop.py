# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

age = [17, 44, 54, 60]

for a in age:
    if a < 18:
        print("Children")
    elif a < 45:
        print("Adult")
    elif a < 55:
        print("Citizen")
    else:
        print("Senior citizen")
        
#%%        
        
        
mark = [35, 45, 75, 90]

for m in mark:
    if m <= 35:
        print("Fail")
    elif m <= 45:
        print("Pass")
    elif m <= 75:
        print("Good")
    else:
        print("Excellent")
        
#%%        
    
 ticket = [35, 45, 75, 90]

 for p in ticket:
     if p <= 35:
         print("Go chennai")
     elif p <= 45:
         print("Madhavaram")
     elif p <= 75:
         print("Poondi")
     else:
         print("Go home")
         
#%%

name = "Artificial intelligence"
print(name)
for letter in name:
    print(letter)         



name=input("Your Name-")
age=int(input("Your Age-"))
profession=input("Your Profession-")
print("Your Name", name)
print("Your Age" , age)
print("Your Profession" , profession)
    
#%%

tup1=int(1, 'Welcome'))
tup2=int(2, 'Hope'))
tup3= tup1, +tup2
print(tup3)




import keyword
print(keyword.kwlist)