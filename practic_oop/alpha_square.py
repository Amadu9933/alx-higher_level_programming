#Printing a square of the same alphabet

size = 5

for i in range(size):
    for j in range(size):
        print(chr(65 + i), end=" ")
    print()

