print('A')
print('I')
print('S')
print('H')
print('A')
A = 'A'
I = 'I'
S = 'S'
H = 'H'
A = 'A'
aX= 'A'
print(A)
print(I)
print(S)
print(H)
print(aX)
# Yes, variables show up on the variable editor 
print(A,aX)
# No, there is no problem with two variable having the same character
aX = 'z'
print(A)
print(I)
print(S)
print(H)
print(aX)
# No, changing aX did not change the value of the other variables 
aX=A
print(aX,A)
A='z'
print(aX,A)
# Yes, changing the variab;e assignment changed the 'A' to 'z'. Therefore python variable assignment can change based on how it's defined 
