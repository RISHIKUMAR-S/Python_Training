import math

x = 1.0 #Assignment
y = int(x) #type casting
print(type(y)) #to know and print what type of variable is y

#string

a = "Kello" #single line string
b = """ this is a muti line strings 
here the line breaks are inserted at the same position as in the code """
c = "world"
print(a) #to display the value of a
a=a.upper() #to convert all the character to uppercase
print(a)
a=a.lower() #to convert all the character to lowercase
print(a)
a.replace("k","h") # to replace k with h
print(a)
b=b.strip() #to remove whitespace from both the ends
lis=b.split(" ") #to create a list of elements seperated by the value specified

print("{0} {1}".format(a,c)) #this is formatting the string

# slicing

print(a[ -2: ]) #to dispaly the last 2 character of the string(array)
print(b[ 0:4 ]) #to dispaly the first 4 characters of the string(array) and it starts from first index and excludes the second index
print(a[ 2: ]) #to dispaly the characters of the string(array) from first index to the last
print(a[ :3 ]) #to dispaly the characters of the string(array) from 0 index excluding the second index

# Arithmetic operator

d = 2
e = 5
print(e % d) # modulus
print(4 // d) # floor division
print(e ** d) # exponent
print(e + d) # add
print(e - d) # exponent
print(e / d) # division
print(e * d) # multiplication

e += 2 # it equals to e=e+2

# comparison operator

print(e == 7) # checks if they are equal
""" != -> not equal
    >  -> greater than
    <  -> less than
    >= -> greater than or equal to
    <= -> less than or equal to"""#multi line comment statement

#logical operator

print(2<5 and 5<10) #check if both the logic are true or false
print(2<5 or 5<10) #check if any one of the logic is true or false
print(not(2<5)) #reverse the result

#identity operator-is and membership operator-in

x = 2
y = x
z = 2
f = "multi"
print(x is y) #check if they are the same object return true but incase of x & z it is false
print(f in "multiline") #check if the value of f is present in b or not

#bitwise operators - work with thir binary value of the integer
print(2 & 3) #set a bit 1 if both bits are 1
print(2 | 3) #set a bit 1 if either one bit is 1 or both bits are 1
print(2 ^ 3) #set a bit 1 if only one bit  1
print(~2) #one's complement
print(2 << 3) #left shift
print(2 >> 3) #right shift

#list

array = ["apple","banana","grapes"] #initializing the array
array2 = ["lemon",1]
array.append("orange") # adding the element
print(array)
print(len(array)) # to find the length of the array
array.insert(1,"watermelon") # adding the value to the specified index
print(array)
array.extend(array2) # adds the element in array2 in array
print(array)
array.remove("watermelon") # remove the specified element
print(array)
array.pop() # removes the last element
print(array)
array.reverse() # inverts the array
print(array)
array.sort(key=str.lower) # sorts the array while keepimg the condition
print(array)
array.sort() # sorts the array
print(array)
array.sort(reverse=True) # sorts array in reverse order
print(array)
array2.clear() # makes the array empty
print(array2)
del array2 # delets the array

# tuples -> can be accessed like list

tup = ("apple", "orange")
tup +=("grapes",) # to add an element to the tuple
print(tup)
# to delete the tuple use -> del tup
tup = tup*2 #to add multiple amount of same data
a, *b = tup # to store data in different variable and 'b' stores rest of the elements in the form of list
print(a , b)
print(tup.count("orange")) # to count how many elements are there
print(tup.index("orange")) # to find the index of specified element

#set -> its unordered

arr={"egg","chicken"}
arr2={"egg", 1, 2, 3, 4}
arr.add("mutton") # to add an item in set
print(arr)
arr.update(["fish","crab"]) # to extend a set with another list\tuple\dictionary
print(arr)
arr.remove("egg") # to remove a particular element
print(arr)
arr.discard("egg") # to remove a particular element and it won't give an error messge if an item doesn't exist
print(arr)
x=arr.union(arr2) # to create a new set with combination of both
print(x)
print(arr.issubset(x)) # to check whether arr is a subset or not
print(x.issuperset(arr)) # to check whether x is a superset or not
print(arr.isdisjoint(x)) # to check whether no common element is present or not
x.intersection_update(arr) #to update x set with only common values and to create a new set use x.intersection(arr)
print(x)
x.symmetric_difference_update(arr) #to update x set with unique values and to create a new set use x.symmetric_difference(arr)
print(x)

#dictionary

thdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thdict['year']) # to get the values of year
print(thdict.get('model')) # to get the values of model
print(thdict.keys()) # to get the keys of dictitionary
print(thdict.values()) # to get the values of dictitionary
print(thdict.items()) # to get the key and value pairs of dictitionary
thdict["branch"] = "bengaluru" # to update the dictionary with a new element
print(thdict)
thdict.pop("model") #remove the particular element
print(thdict)
thdict.update({"model":"GT"}) # to update the dictionary with a new element
print(thdict)
thdict.popitem() # to remove the last item in the dictionary
print(thdict)
# to delete an item use -> del thdict['year'] ,to delete the a dictionary use -> del thdict
thdict2 = thdict.copy() # to copy a dictionary , dict(thdict)
print(thdict2)
x = thdict.setdefault("brand","kia") # if the key is present it returns its original value or else it return the current value and updates the dictionary
print(x)
print(thdict)
thdict3 = dict.fromkeys([1,2,3,4,5],0) # it creats a dictionary like {1:0,2:0,3:0,4:0,5:0}
print(thdict3)

#for loop

for i in array:   
    print(i)       # to display all the elements in the list using for loop
for i in range(1,10):
    if(i % 3 == 0): print(i) # to display the elements divisible by 3 from 1 to 9
for i,j in thdict.items():   
    print(i,j)       # to display all the key and pair in the dictionary

#while loop

i=0
while i<len(array):
    print(array[i])
    i += 1   # to display all the elements in the list using while loop
#if a function body is empty use -> pass , to avoid raising errors

# Escape statements
"""break -> jumps out of the loop
   continue -> skips the rest and jumps to the next iteration"""

#function

def factorial(number):
    if number > 1:
        return number * factorial(number-1)  
    return 1

result = int(input("Enter the number to find the factorial : "))
print(factorial(result))  #to find the factorial of the number using recursion

def show_native(city = "Madurai"):
    print("I am from " + city)

show_native("Coimbatore")
show_native() #to set default value in case if the arguement is not passed

def show_dict(**name):
  print("country name is " + name["country"])

show_dict(country = "India", capital = "New Delhi") #If the number of arguments is unknown, add a double ** before the parameter name to receieve value as dictionary

def show_list(*name):
  print("country name is " + name[1])

show_list("India","America") #If the number of arguments is unknown, add a single * before the parameter name to receieve value as list

#lambda

area = lambda r : math.pi * (r ** 2)
print(area(int(input("Enter the radius of the circle : "))))