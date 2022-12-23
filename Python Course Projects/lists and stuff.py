names = ['john','david','jesus','noah','mary']
names[0] = 'Juan'
print (names[0])

#find largest number in a list

list_num = [12,34,26,87,46,56,28,85,63,58]
champ = 0
for value in list_num:
    if value > champ:
        champ = value
print (champ)

#Matrixes are lists where every item is another list

matrix = [
[1,2,3],
[4,5,6],
[7,8,9],
]
print(matrix)

#to access a certain value of a list withn a list (matrix) yousimply call it using more []

#i.e. to print the number 5
print(matrix[1][1]) #the first [1] represents the index of the list we access and the second represents 
#the index of the item in the list, in this case, 5,

matrix = [
[1,2,3],
[4,5,6],
[7,8,9],
]
matrix[2][0] = 'this is code' # matrixes can only be made up of numbers, but using the indexes 
# you can change what individual numbers output, in this matrix i  got the 2nd index list's 0th index value and made it say 
# something this could be useful for sorting or keping track of invetory i think

print(matrix[2][0])
