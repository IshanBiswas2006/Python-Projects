print("Enter 5 Elements for Set A: ")
setOne = []
for i in range(5):
    setOne.append(input())
setOne = set(setOne)

print("Enter 5 Elements for Set B: ")
setTwo = []
for i in range(5):
    setTwo.append(input())
setTwo = set(setTwo)

print("\nUnion of Two Sets A and B are:")
print(setOne | setTwo)