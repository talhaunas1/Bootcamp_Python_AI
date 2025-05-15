# Step 1: Variables & Data Types
print("step1")

name = "talha"
age = 24
height = 5.9
is_employed = False

print(type(name))
print(type(age))
print(type(height))
print(type(is_employed))



# Step 2: Conditional Statements
print("step2")

print("Grade system Evalation")

score = int(input("enter your score"))

if score >=85 :
    print("A")

elif score >=80:
    print("b")

elif score>=70:
    print("C")

elif score>=60:
    print("D")

elif score >=50:
    print("E")

elif score <=49: 
    print("F") 

else: ("EFFORT MORE")


# Step 3: Loops & Pattern Printing
print("step3")

n=5 
# range (start,end)
for i in range(1,n+1): 
    print('*' * i)


# Step 4: Lists & Comprehensions
print("step4")
squares = [ 1,2,3,4,5,6,7,8,9,10]
print(squares[5])

squares= [] 
for i in range(1 , 5): 
    squares.append(i*1)

print(squares)
print(squares[1])

# Step 5: Tuples, Sets, and Dictionaries
print("step5")

fruits = ("apple", "orange", "mango")
print(fruits)

my_set = set()
my_set.add("banana")
my_set.add("apple")
my_set.add("apple")
print("myset", my_set)

my_dict= { 'name' : 'talha', 'age' : 25 , 'employed': False}

print("my_dict" )



# Step 6: Challenge - Word Frequency Counter
print("step6")


text = "Python is simple yet powerful. Python is easy to learn."

words= text.split()

word_frequency = {}

for word in words : 
    if word in word_frequency:
        word_frequency[word] = word_frequency[word]+1
    else:
        word_frequency[word] = 1

print(word_frequency)


