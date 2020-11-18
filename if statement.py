name=input(" Please Enter your name:")
age=int(input(" How Old you are {} ?".format(name )))
print(age)

if age >= 18:
    print ("You are eligibale for voting")
    print("Please put an X in the box")

else:
    print("Please come in next {} years back".format(18-age))
    print(" Sorry you are not eligible for voting this time")


if age < 18:

    print("Please come in next {} years back".format(18-age))
    print(" Sorry you are not eligible for voting this time")

else:
    print ("You are eligibale for voting")
    print("Please put an X in the box")






