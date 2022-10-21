a=str(input("Name : "))
print("(Project Officer, Exec Engineer, Exec Asst)")
b=str(input("job :"))
c=float(input("How much Salary do you expect :"))

if b=="Project Officer":
    print("Employe name:",a,"\n your salary will be :2500000 with 7% bonus i.e :1,75,000")

elif b=="Exec Engineer":
    print("Employe name:",a,"\n your salary will be :1000000 with 5%bonus i.e :50,000")
elif b=="Exec Asst":
    print("Employe name:",a,"\n your salary will be :800000 with 3%bonus i.e :24,000")
    
else:
    print ("no job available \n Mr/Ms:",a)
