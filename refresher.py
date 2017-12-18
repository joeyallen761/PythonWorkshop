#refresher.py

print "integer division", 3/2
print "float division", 3/2.0

myInt = 4
myFloat = 4.0
myString = "four"
print myInt*2, myFloat*2, myString*2

length = 3
width = 4
height = 10

print length, width, height

square_area = length * width
print square_area

volume = length * width * height
print "volume", volume

isBig = volume > 100
print "isBig",isBig

if isBig:
    print "This cube is huge!"
else:
    print "This is a tiny cube."

colors = ["red","yellow","blue"]
colors.append("violet")
print colors[0], colors[2]

for color in colors:
    print "my favorite color might be",color


def getHypotenuse(a,b):
    csquared = a**2 + b**2
    c = csquared**(1.0/2.0)
    return c

hypotenuse = getHypotenuse(length, width)
print length, width, hypotenuse
