My answers to the Assignment



Conditional exercises
You want to tell your experiment to record participant responses. 
If the response is "1" or "2", print OK. If the response is "NaN" (empty), print a "subject did not respond" message. If the response is anything else, print "subject pressed the wrong key".
```Python
x = input("Enter Number: ")
if(x == 1 or x == 2):
    print("OK")
elif(x==""):
    print("subject did not respond")
else:
    print("subject pressed the wrong key")

```
Create a nested "if" statement in the above exercise. If the response is "1", print "Correct!". If the response is "2", print "Incorrect!"
```Python
x = input("Enter Number: ")

if(x == "1" or x == "2"):
    
    if(x=="1"):
        print("correct")
    elif(x=="2"):
        print("incorrect")


```
Test out your script with various responses. Does it do what you expect it to?
```Python

Testing done

```

For loop exercises
Remember the exercise where you printed each letter of your name? Create a for loop that prints each letter without writing out all of the print statements manually.
```Python
name = "Aisha"

for x in name:
    print(x)

```
Add an index counter and modify your loop to print the index number after each letter
```Python

name = "Aisha"

for x in name:
    print(x , name.index(x))

```
Create a list of names "Amy","Rory", and "River". Create a nested for loop to loop through each letter of each name.
```Python
names = ["Amy","Rory", "River"]
for name in names:
    for x in name:
        print(x)

```
Add an index counter that gives the index of each letter for each name. The counter should start over at 0 for each name in the list.
```Python
names = ["Amy","Rory", "River"]
for name in names:
    for x in name:
        print(x, name.index(x))

```


While loop exercises
Create a while loop of 20 iterations that prints "image1.png" for the first 10 iterations, and "image2.png" for the next 10 iterations.
```Python
x = 0
while(x<20):
    if(x<10):
        print("image1.png")
    else:
        print("image2.png")
    x+=1


```
Create a while loop that shows an image until the participant makes a response of 1 or 2. Run it a few times to make sure it works the way you expect.
```Python

while(True):
    print("Image1.png")
    x = input("enter number: ")
    if(x == "1" or x=="2"):
        break

```
Create a failsafe that terminates the previous while loop after 5 iterations if one of the valid responses (1,2) have not been made in that time.
```Python
its = 0
while(True):
    print("Image1.png")
    x = input("enter number: ")
    its += 1
    if(x == "1" or x=="2" or its == 5):
        print("Breaking loop")
        break


```
