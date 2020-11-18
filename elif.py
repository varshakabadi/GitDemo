name=input(" Enter Your name:")
age=int(input( "How old your {} ? :".format(name)))
print(age)

if age < 18:
    print("Please come in next {} years back".format(18-age))
    print(" Sorry you are not eligible for voting this time")

elif age >= 100:
    print("sorry {} are not live".format(name))

else:
    print ("You are eligibale for voting")
    print("Please put an X in the box")
