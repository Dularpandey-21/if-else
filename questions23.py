marks=int(input("enter your marks"))
text="your grade is"
if marks==25:
    print(text,"F")
elif 25>marks and marks<=45:
    print(text,"E")
elif 45>marks and marks<=50:    
    print(text,"D")
elif 50>marks and marks<=60:
    print(text,"C") 
elif 60>marks and marks<=80:
    print(text,"B")
else: 
    print(text,"A")                      