no1=float(input("frist number"))
operator=input("enter an operator (*,/)")
no2=float(input("second number"))
if operator=="*":
    result=no1 * no2 
    print(result)
elif operator=="/":
    if no2!=0:
        result =no1 /no2
        print("result:", result)
    else:
        print("error")
