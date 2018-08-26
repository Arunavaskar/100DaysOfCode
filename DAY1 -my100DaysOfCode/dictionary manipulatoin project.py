#this is a dictionary with keys containing values... different types of values
#like 'k2' key contains a list of strings, integers, floats and numbers as value
#'k5'contains a dictionary as its value which has its own key named 'key' that has a list as its value containing strings, integers, float and number
d={'k1':12.08,'k2':['fuck','me','please',2,10.02,'22'],'k3':12,'k4':'122','k5':{'key':['value',100,100.00,'100']}}
#now from the dictionary d, we called key 'k5' first
#then we called 'key' key from the dictionary which actually the value of the key 'k5'
#then we called the value of the key 'key' 'value', a string which is at index no. 0
value=d['k5']['key'][0]
#then through the very same process we called the number '100'
the100=d['k5']['key'][3]
#now we assigned the result of the addition of this two values to the vriable value100
value100=value+the100
#again... its the same process
int100=d['k5']['key'][1]
#same process repeated again here
float100=d['k5']['key'][2]
#this time those two values are multiplied and the result is assigned to the variable intfloat
intfloat=int100*float100
#now finally using f-string method for print formatting we passed those pre-assignedd variables "value100" and "intfloat" to those curly brackets respectively
print(f"The string is {value100} and the float is {intfloat}.")
#mode='w' we wrote created a new txt file 
with open('testshittwo.txt',mode='w') as test:
    test.write('this is a text test file created in python.. directly!')
#mode='a' we append a new string at the end of the last string and by using '\n' we set that new string to a new line!
with open('testshittwo.txt',mode='a') as test:
    test.write('\nthis is the second line!')
#with mode='r' we read the file that we just created 
with open('testshittwo.txt',mode='r') as test:
    print(test.read())

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

#this is a random list of numbers 
list_1=[1,5,65,98,26,44,21,35,798]
#for num(every item in the list) in list_1(the list we created up there!)
for num in list_1:
#if num(every item in the list) % 2(any number, suppose 17 gets divided by 2 and the answer is 8 so the remainder will be 1. but if the number is suppose 20 then the result will be 10 but remainder will be 0 )
	if num % 2!=0:
#this will print all the uneven numbers with that messege included 
		print(f"This is an Un-even number!: {num}")
#else-if num%2==0 means this equation is looking for a 0 remainder which means even numbers!
	elif num % 2==0:
#this will now print the even numbers with the messege included!
		print(f"This is an even number!: {num}")
#and to end this flow comes else where if and elif conditions turns out to be false, print the following messege.
	else:
		print("fuck my asshole, is there even any numbers to choose from!")

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

list_sum=0
for num in list_1:
    list_sum+=num#list_sum = List_sum + num
print(list_sum)

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

#this works for strings as well!
for letter in "This is a string!.":
    print(letter)

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

#it works quite as same as lists, with tupples too!
tupples = (1,5,65,98,26,44,21,35,798)
for tup in tupples:
	print(tup)

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

#TUPPLE UN-PACKING!!!
#here we added tuples in a list as list items!
list_2 = [(1,2,3),(4,5,6),(7,8,9)]
for tup in list_2:
#it prints every tup(every tup goes for every items from the list which is actualy those tupples!) in list_2
	print(tup)

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

#HERE "NONE" IS WROKING AS A PLACEHOLDER TO KEEP WITH OTHER TUPPLES STRUCTURE SO THAT WHEN WE CALL IT BY FOR LOOPS, WE DONT GET ANY ERROR MESSEGES!!
list_2 = [(1,2,3),(4,5,None),(7,8,9)]
#Here we do the unpacking of those item/tupples in the list by making an exact copy of those tupples using variables "(my, ass, hole)"
for (my, ass, hole) in list_2:
	print(hole)

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

d = {'k1':1,'k2':2,'k3':3}#its a dictionary
for item in d:
    print(f"this returns only the keys by default!: {item}")

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

#We're going to introduce three new Dictionary methods: .keys(), .values() and .items() to pullout individuals as we want!!
#Since the .items() method supports iteration, we can perform dictionary unpacking to separate keys and values just as we did in the previous examples.
print(f"Create a dictionary view object: {d.items()}")
#Create a dictionary view object: dict_items([('k1', 1), ('k2', 2), ('k3', 3)])
#dictionary unpacking 
for k, v in d.items():
	print(f"here is the key: {k} \nhere is the the value: {v}")

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

#If you want to obtain a true list of keys, values, or key/value tuples, you can cast the view as a list:
print(f"this is a list of only keys! using .keys() function: {list(d.keys())}")
print(f"this is a list of only values! using .values() function: {d.values()}")
print(f"this is a sorted list of only values! using .values() function: {sorted(d.values())}")
print(f"this turns the dictionary into iterable list to be available for unpacking! using .items() function: {d.items()}")
for k,v in sorted(d.items()):
    print("the key" , k)
    print("the value " , v)

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

#this is an example of implementation of while loop where we also use break statement and continue statement!
a= 0

while a < 10:
	print("a is less than 5 which is actually right now",a)
	print("adding 2 to a")
	a+=1
	if a==6:
		print("a is now ",a,"and the loop ends here! LOL!")
		break
	else:
		print("continue...")
	continue

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

#here we will be using pass statement wich actually does nothing thats why its like a placeholder for different actions!
#this while loop will neither give any error messege for not having any proper action against a condition nor will actually do anything, like giving any kind of output!

a= 0

while a < 10:
	pass #print("a is less than 5 which is actually right now",a)
	pass #print("adding 2 to a")
	a+=1
	if a==6:
		pass #print("a is now ",a,"and the loop ends here! LOL!")
		break
	else:
		pass #print("continue...")
	continue
print("this while loop will neither give any error messege for not having any proper action against a condition \nnor will actually do anything, like giving any kind of output!")

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

#here we will be going through a new genarator called enumerate!

#sometimes when we want to all the laters of some kind of a string we also want to get the index number of that or say from a list we printed something and how many times that got printed is also a thing we may want to know
#for that this a very common technique
i = 0 #here we assign i to 0 so that when we print it in the loop with laters of the string word we get also end where the words's laters end printing for being over vslued through 1 addition 

for l in 'word':#here we call each laters of the string word by l 

	print (i,l)#here we print that previous i with the value of 0 and l with value of each laters of the string word!

#python has its own dedicated genarator for this operation called enumerate

for i in enumerate("word"):
	print("here we see enumerate automatically genarates tupples of index numbers with that respective string or the given object",i)

#now as if we wanted the index numbers and the items individually so that to be used in defferent sec we can do this by tupple unpacking method as enumerate creates tupples of index numbers and the item itself
for i,l in enumerate("word"):
	print(f"here is the index number {i} \nand here is the later {l}")
#so what we now know is 
#1: enumarate is genarator that genarates a tupple out of a given set may be that can be a list even with there respective index numbers
#2: we can then use that index numbers by using tupple unpacking! simple!

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

#zip operator example!
#zip() operator basically combines to lists in to one where each list's  items will erspectivley get combined into a tupple making a new combined list containing tupples!
#example!
list1=[1,2,3]
list2=["a","b","c"]
for     one,two                                               in            zip(list1           ,list2):
	#(one,two)representing the tupples in zip(list1,list2)                   #(1,2,3)            #("a","b","c")
																			  #one                  #two
	print(one)
	print(two)

#more example of it's usage 
for one,two in zip(list1,list2):
	print(f"this index number {one} \nthis is the later {two}")
#awesome!!!!

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

#We've already seen the in keyword durng the for loop, but we can also use it to quickly check if an object is in a list
#in keywords loooks for if the given number, int, float or str is in a certain list, string or even in a tupple

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

#now we wiil work on min(), max() suffle(), importing random library and taking user input to get up with a list
from random import randint #randint function genarates random numbers each time it is called
random=randint(0,100)
random2=randint(25,66)
user_number=int(input("enter a number of your choice "))
user_number2=int(input("enter another number of your choice "))
mylist_=[random,random2,user_number,user_number2]
print(mylist_)

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||


#Use for, .split(), and if to create a Statement that will print out words that start with 's':
#st = 'Print only the words that start with s in this sentence'
st = 'Print only the words that start with s in this sentence'
for word in st.split():
	if word[0]=='s':
		print(word)

l=list(range(9,16,2))
for n in l:
	print(n)

#Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3
l=[x for x in range(1,51) if x%3==0]

#
