no1=float(input("frist number"))
operator=input(" operator ")
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

elif operator == "+":
    print(no1 + no2)
elif operator == "-":
    print(no1 - no2)