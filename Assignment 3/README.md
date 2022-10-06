This is my set of answers to the assignment


Variables operations exercises:

1. We need to add the string form of subnr to sub. You can't add int to a string and that's why int form subnr doesn't work
2. (sub_code, subnr_str)\n(sub_code, subnr_str*3) 
   ((sub_code + subnr_str)*3) 
   (sub_code*3+subnr_str*3)

list operations exercises:

1. (numlist\*2)
2. (numarr\*2) when you multiple a list you double, you repeat all the numbers in the list. When you multiple an array you multiple all the items in the array
3. ([x*2 for x in strlist])
   (strlist*2)
   [item for sublist in [[x]*2 for x in (strlist)] for item in sublist]
   [[x]\*2 for x in (strlist)]

Zipping Exercises:

facelist = ["face1.png", "face2.png", "face3.png", "face4.png", "face5.png"]*10
houselist = ["house1.png"]*10 + ["house2.png"]*10 + ["house3.png"]*10 + ["house4.png"]*10 + ["house5.png"]*10
cuelist = ["cue1", "cue2"]\*25

counterbalanced = (list(zip(facelist, houselist, cuelist)) + list(zip(houselist, facelist, cuelist)))
np.random.shuffle(counterbalanced)

Indexing Exercises:

1. colors = ["red", "orange", "yellow", "green", "blue", "purple"]
2. print(colors[-2])
3. print(colors[-2][2], colors[-2][3])
4. colors.pop(5)
   colors.append("indigo")
   colors.append("violet")

Slicing Exercises:

1. list100 = list(range(100))
2. print(list100[:10])
3. print(list100[::-2])
4. print(list100[:95:-1])
5. print(list100[40:44] == list(range(39, 43)))
