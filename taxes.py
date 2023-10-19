Gender=str(input("enter your gender"))
Age=int(input("enter your age"))
if Gender=="female" and Age>=18 and Age<=35 :
    print("pay tax")
elif Gender=="Male" and Age>=20 :
    print("pay tax")
else:
    print("don't pay any taxes")