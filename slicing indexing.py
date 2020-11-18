Name=" Varsha Yashawant Kabadi"

print(Name[:])       #print name string
print(Name[0:6])     # slicing start with position 0 upto 6 but not incuding 6 position # Varsha only 5 words
print(Name[6:])      #indexing start with position 6 and on words

print(Name[9:-2])   #indexing start with position  -2 up position no 14 from +ve indexing #
print(Name[-10:-1])  # indexing start with position -3 up position -10

parrot="Norwegian Blue"
print(parrot[-3:-2])
print(parrot[-13:-10])
print(parrot[0:9:2])
print(parrot[0:14:3])  #Nwi u
print(parrot[4::3])    #start with 4th position and step size btw them is 3 up end of the string

Number="1,563,897,654,321,987,456,123,159,357"
print(Number[1::4])  # here start with position 1 upto end of the string and step size is 4

Number="1,563;897:654'321+987/456-123'159,357"
print(Number[1::4]) # start with 1 upto end of the string and step size is 4
print(Number[1:6])  # start with 1 upto 6 position but not included 6 position