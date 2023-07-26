# Numeric

print("----------------INTEGERS--------------------")
# Integers
A = 12
A = 123
print(A)

print("---------------------FLOAT-------------------")
# Float
B = 2.55567883738
print(B)

print("----------------STRINGS----------------------")
# Strings, ptyhon don't have any keyword character or char

name = 'Nitish'
print(name)
print(name[1])
print(name[2])

print("----------------TUPLES----------------------------------")
# tuples are list which can contain objects of different data types and are Immutable, it has fixed size we cannot assign value in it

address = (7, 'red cross road', 'adampur', 'bhagalpur', 'bihar', 812001)
print(address)
print(address[0])
print(address[4])
print(address[5])
# print(address[11]) -- this will give index out of range error


print("-----------------LIST---------------------------")
#List , it allows , different data types, allows duplicates

#Empty List
D = []
G = [7, 'red cross road', 'adampur', 'bhagalpur', 'bihar', 812001]

print(G)
print(G[1])
print(G[4])
print(G[5])
print(len(G))  # length of list
print(G[-1])  # last item of list
print(G[-2])  #2nd last Item
print(G[-4:-1])  #Range of Items
print(G[4:1])

#check If item present in the list

if 'adampur' in G:
    print("adampur present in the list")

#update list Item
G[-1] = 700156
print(G)

#append items in the list
G.append("India")
print(G)

#update more than one items
G[1:3] = ['Power Tower', 'New Town', 'Kolkata']
print(G)

#Insert item without replacing any item
G.insert(1, 'Nitish')
print(G)

# Note: The length of the list will change when the number of items inserted does not match the number of items replaced.

'''D[0] = 'nitish'
D[1] = '25j'
D[2] = 'Hello'
print(D)'''

# Join two lists
l1 = ["apple", "mango", "papaya"]
l2 = ["mango", "pineapple", "papaya"]
l1.extend(l2)  # it will join two list in this case add two papaya which is common in both list
print(l1)
# extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.)
t1 = ("kiwi", "apple")
l1.extend(t1)

#Remove from list
l2.remove("papaya")
print(l2)
print(len(l2))
# Remove by Index
l3 = ['a', 'b', 'c', 'd']
l3.pop(2)
print(l3)
# if we don't specify index number it will remove last item using pop() method
l3.pop()
print(l3)

# del command also remove the specified list
l4 = ['w', 'x', 'y', 'z']
del l4[2]
print(l4)

del l4   # this deletes the entire list
#print(l4)
# Note it deletes complete data type, if we print the the list , it will say not defined and give error exit code 1

l5 = ['m', 'n', 'o', 'p']
print(l5)
l5.clear()
print(l5)









