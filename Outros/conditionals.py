#Some conditionals involving numbers and strings
#Created by Tiago Luiz in 06/13/2014

varA = "Tiago Luiz"
varB = 18

if(type(varA)==str or type(varB)==str):  #Each variable has been checked to see if they were string, using the type() function. "str" is equal to string, just a reminder.
    print("string involved")
elif(varA>varB):
    print("bigger")
elif(varA==varB):
    print("equal")
else:
   print("smaller")
