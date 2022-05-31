import random
import string

alphabets = list(string.ascii_letters)
digits = list(string.digits)
special_characters = list("!@#$%^&*()~-")
#custom pw length
def custom():
    abc1 = []
    digi1 = []
    specichar1 = []
    customlength1 = int(input("please enter custom password length:\n"))
    for i in range(customlength1):
        abc1.append(random.choice(alphabets))
        digi1.append(random.choice(digits))
        specichar1.append(random.choice(special_characters))
    generatedpw1 = ''.join(
        random.sample(''.join(random.sample(abc1 + digi1 + specichar1, customlength1)), customlength1))
    print("length: "+ str(len(generatedpw1)))
    print(generatedpw1)
#defined password length
def static():
    lengthstatic = int('17')
    abc = []
    digi = []
    specichar = []
    for i in range(lengthstatic):
        abc.append(random.choice(alphabets))
        digi.append(random.choice(digits))
        specichar.append(random.choice(special_characters))
    generatedpw = ''.join(
        random.sample(''.join(random.sample(abc + digi + specichar, lengthstatic)), lengthstatic))
    for i in range(len(generatedpw)):
        random.sample(generatedpw,lengthstatic)

    print("length: "+ str(len(generatedpw)))
    print(generatedpw)

#ask for user input
choice = str(input("custom length, input y, generic length, input n:\n"))
if choice == "y":
    custom()
elif choice == "n":
    static()
else:
    print("Please enter a NUMBER.\n")

