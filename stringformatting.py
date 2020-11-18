for i in range(1, 13):
    print("No.{0:2} Squared is {1:3} and Cuqbed is {2:3} and 4th is {3:3}".format(i, i ** 2, i ** 3, i ** 4))

print()
for i in range(1, 13):
    print("No.{0:<2} Squared is {1:<3} and Cuqbed is {2:<3} and 4th is {3:<3}".format(i, i ** 2, i ** 3, i ** 4))
print()

print("Pi is approximately {0:12}".format(22 / 7))
print("Pi is approximately {0:<12f}".format(22 / 7))
print("Pi is approximately {0:12.50f}".format(22 / 7))
print("Pi is approximately {0:<60.75}".format(22 / 7))
print("Pi is approximately {0:<50.12}".format(22 / 7))


print()
age = 27
name = "varsha"
age_in_words="2 Years"
print(name + f" is {age} Years old") ## F- string for concatenation
print(f"pi is approximately {22 / 7 : 12.50f}")

print()
pi=22/7
print(f"pi is approximately {pi:12.50f}")# we can use the f string instaed of replacement operator


days = "Mon, Tue, Wed, Thu, Fri, Sat, Sun"
print(days[::5])
