import statistics
import random
#2.1
#Create a list of your favorite fruits.
ls=['strawberry','passion fruit','grape']
print(ls)
# Append a new fruit to the list
ls.append('apple')
print(ls)
#Remove the second fruit from the list.
del ls[1]
print(ls)
#Check if "banana" is in the list
if 'banana' in ls:
    print('banana is in the list')
else:
    print('banana is not on the list')
# Loop through the list and print each fruit
for x in ls:
    print(x)
# Create a list of numbers and find the average
ls2=[5,4,6,8,7,5,2,4,9,65,27]

s=0
for x in ls2:
    s+=x
print(f'The average is {s/(len(ls2))} ')
#Remove all duplicates from a list
ls3=list(set(ls2))
print(ls2)
print(ls3)
#Create a list of names and sort them alphabetically.
ls4=['juan','camilo','sebastian','laura','ana']
ls4.sort()
print(ls4)
# Find the second-largest number in a list.
ls2.sort()
print(ls2[-2])
#Create a list of words and capitalize the first letter of each.
for x in range(len(ls4)):
    ls4[x]=ls4[x].capitalize()
print(ls4)
#Create a list of numbers and find the median.
print(statistics.median(ls2))
#Shuflle the elements of a list randomly.
random.shuffle(ls2)
print(ls2)
# Create a list of strings and sort them based on their lengths.
def mylen(x):
    return len(x)
ls4.sort(key=mylen)
print(ls4)
#2.2
#Create a dictionary with items representing cities and their populations.
dic={'Bogota':7.181,'Cali':2.228,'Medellin':2.569} #in millions
print(dic)
# Add a new city and its population to the dictionary.
dic['Barranquilla']=1.206
print(dic)
#Remove a city from the dictionary.
del dic['Cali']
print(dic)
#Access the population of a specific city.
print(dic['Medellin'])
#Loop through the dictionary and print each city and population.
for x in dic:
    print(x,dic[x])
# Create a dictionary of usernames and passwords, and implement a login system.
uss_pas={'fifu12':'ls23','kimoni':'domic24','JEGS':'aSami45'}
us=input('usernames: ')
pas=input('passwords: ')
if us in uss_pas:
    if pas == uss_pas[us]:
        print('you have login')
else:
    print('username or password wrong')
#Implement a simple language translation system using dictionaries
#ing_esp_colors={'red':'rojo','pink':'rosa','orange':'naranja','yellow':'amarillo','green':'verde','blue':'azul','brown':'marrón'}
#leng=input('select and optinon \n 1.Spanish -> English\n 2.English -> Spanish \n')
#word=input('what word do you what to transalate: ')
#if leng==1:


