print("---------Head First Python Chapter 1 START !---------")

# List
print("--------List----------")
animals = ["Dog", "Cat", "Tiger", "Bear"]
print(animals)
print(animals[1])

#Functions
print("--------len( )----------")
print(len(animals))

print("--------append----------")
animals.append("Eagle")
print(animals)

print("---------pop---------")
animals.pop()
print(animals)

print("---------extend---------")
animals.extend(["Eagle", "Snake"])
print(animals)

print("---------remove---------")
animals.remove("Tiger")
print(animals)

print("---------insert---------")
animals.insert(0, "Tiger")
print(animals)

# Lists can contain data of mixed type
print("---------Lists can contain data of mixed type---------")
animals.insert(1, 1988)
animals.insert(3, 2004)
animals.insert(5, 1995)
animals.insert(7, 2001)
animals.insert(9, 2007)
print(animals)

# Loop_For each
print("---------Loop_For each---------")
for animal in animals :
	print(animal)

# Loop_while
print("---------Loop_while---------")
count=0
while count < len(animals) :
	print(animals[count])
	count+=1

# Lists within Lists
print("---------Lists within Lists---------")
movies = [
	"The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
		["Graham Chapman",
			["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]
print(movies[4][1][3])

# if
print("---------if_1---------")
if animals[0] == "Dog" : 
	print("True")
else :
	print(animals[0])

print("---------if_2---------")
if isinstance(animals, list) : 
	print("True")
else :
	print("False")

# Function
print("---------Functions---------")
def function01() :
	print("Hello! Python's Function !")

function01()

def function02(number) :
	print("Hello! Python's Function ! %d" %number)

function02(1234)

def function03(num1, num2) :
	sum = num1 + num2
	return sum

print(function03(10, 20))


print("---------Head First Python Chapter 1 END !---------")