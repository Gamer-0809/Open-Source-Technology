a= float(input("enter the rate of product :"))
s= float(input("enter the amount of selling price :"))
x=s-a
y=a-s
if x>y:
    print ("the profit is "+ str(x)+" ")

elif x<y:
    abs(y)
    print ("the loss is "+ str(y)+" ")

else:
    print ("no loss no profit") 
