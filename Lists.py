squares = [1, 4, 9, 16, 25]

print(squares) # print values of squares
print(len(squares)) # Length of squares
print(squares[0])  # indexing returns the item
print(squares[-3:])  # slicing returns a new list

#Adding new items to list
print(squares + [36, 49, 64, 81, 100]) # print values of squares

squares[3]=10 # replacing value of third index, starting with 0 index.
print(squares)

squares.append(99) # appending value to list.
print(squares)
