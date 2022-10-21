o=(input("enter the operation you want to execute (c=circle, r=rectangle, s=square) :"))
if o=="c":
    r=float(input("enter the value of radius : "))
    pi=3.14
    ac=2*pi*r
    print("The area of circle is:",ac,"sq.cm")
elif o=="r":
    l=float(input("enter the value of length : "))
    b=float(input("enter the value of width : "))
    ar=l*b
    print("the area of rectangle is: ",ar,"sq.cm")
elif o=="s":
    s=float(input("enter the value of side : "))
    aos=s*s
    print("the area of square is :",aos,"sq.cm")
else:
    print ("invalid value")
