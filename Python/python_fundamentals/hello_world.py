import math

print ("hello world!!")

x = 42
print ("my name is:", x)

x = "John"
print ("my name is:" + x)
print ("my name is:", x)

first_name = "Zen"
last_name = "Coder"
my_num = 42
print ("My name is {} {} {}".format(first_name, last_name, my_num))

x = "Hello World"
print (x.upper())

print ("abcdabcva".count("ab"))

print ("zzassaWWW".endswith("WW"))

print ("aaaabaaaa".find("b"))

print ("aaxx11223".isalnum())
print ("aaxxc  11``223".isalnum())  
#  similar methods: .isalpha(), .isdigit(), .islower(), .isupper()

print ( "--".join(['physics', 'chemistry', "1997", "2000"]))

print ("sss aaa 111".split())

my_list = ['4', ['list', 'in', 'a', 'list'], 987]
empty_list = []
print (my_list*3)


print (my_list+my_list)
print (my_list[1][1])

x = [1,2,3,4,5]
x.append(99)
print (x)

x = [99,4,2,5,-3]
print (x[:])
print (x[1:])
print (x[:4])
print (x[2:4])

print (len(x))

for i in enumerate(x):
    print (i)


print(list(map(lambda x: x**2, [1,2,3,4])))

print(min(1,2,3,4))

print(sorted([4,3,2,1,2,3,4]))


#print([1,2,3,4].extend([10,11,12]))


aList = [123, 'xyz', 'zara', 'abc', 123]
bList = [2009, 'manni']
aList.extend(bList)
print ("Extended List: ", aList)

x=[1,2,3,4,5]
print(x.pop(1))
print(x)

x=["aa","bb","cc","dd"]
print(x.index("cc"))


age = 17
if age >= 18:
  print ('Legal age')
elif age == 17 and (not age>20) or (not age<10):
  print ('You are seventeen.')
else:
  print ('You are so young!')


for i in range(0,5):
    print("looping - ", i)

aList = [1,10,30,40]
for i in aList:
    print(i)


i = 0
while i<=5:
    print ("while loop: ",i)
    i+=1

i = 0
while i<1000:
    i+=1
    if i ==3:
        continue
    elif i ==8:
        break
    print ("zzzzzzop: ",i)
    
for val in "xxxds":
    pass


x = 3
y = x
while y > 0:
  print (y)
  y = y - 1
else:
  print ("Final else statement")

x=[]
if not x:
    print("dd")




def say_hi(name):
  print ("Hi, " + name)
  return "wow"


say_hi("booboo")
x=say_hi("booboo")
print(x)


tuple_letters = ("a", "b", "c", "d")
print(tuple_letters)

tuple_data = ('physics', 'chemistry', 1997, 2000)
print(tuple_data[1])


tuple_num = (1, 2, 3, 4, 5 )
tuple_num += (777,)
tuple_num = tuple_num[:3] + ("fff",) +tuple_num[4:]
print(tuple_num)


def get_circle_area(r):
    c = 2 * math.pi * r
    a = math.pi * r * r
    return (c, a)

print(get_circle_area(3))


weekend = {"Sun": "Sunday", "Sat": "Saturday"} #literal notation
print (weekend["Sun"])


capitals = {} #create an empty dictionary then add values
capitals["svk"] = "Bratislava"
capitals["deu"] = "Berlin"
capitals["dnk"] = "Copenhagen"
print (capitals["svk"])


for data in capitals:
     print (data)   #prints keys!

for key in capitals.keys():
     print( key)    #prints keys!

for val in capitals.values():
     print (val)    #prints values!

for key,data in capitals.items():
     print( key, " = ", data)     #prints keys and values!


# cmp(weekend, capitals)


context = {
  'questions': [
   { 'id': 1, 'content': 'Why is there a light in the fridge and not in the freezer?'},
   { 'id': 2, 'content': 'Why don\'t sheep shrink when it rains?'},
   { 'id': 3, 'content': 'Why are they called apartments when they are all stuck together?'},
   { 'id': 4, 'content': 'Why do cars drive on the parkway and park on the driveway?'}
  ]

    'questions2': [
   { 'id': 1, 'content': 'Why is there a light in the fridge and not in the freezer?'},
   { 'id': 2, 'content': 'Why don\'t sheep shrink when it rains?'},
   { 'id': 3, 'content': 'Why are they called apartments when they are all stuck together?'},
   { 'id': 4, 'content': 'Why do cars drive on the parkway and park on the driveway?'}
  ]
 }



for  data in context.values():
    for value in data:
        print ("Question #", value["id"], ": ", value["content"])
        print ("----")


data ={"house":"Haus","cat":"Katze","red":"rot"}
print(data.items())