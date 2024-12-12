from collections import deque

#List
squares = [1,25, 4, 9, 16, 25]

print(squares) # print values of squares
print(len(squares)) # Length of squares
print(squares[0])  # indexing returns the item
print(squares[-3:])  # slicing returns a new list

#Adding new items to list
print(squares + [36, 49, 64, 81, 100]) # print values of squares

# replacing value of third index, starting with 0 index.
squares[3]=10 
print(squares)

# appending value to list.
squares.append(99) 
print(squares)

#Add item at specific index. Rest of the items will be moved to next indexes.
squares.insert(0,-1)
print(squares)

#removes item from the list, default removes last item.
squares.pop(0)
print(squares)

#Return the number of times 25 appears in the list.
print(squares.count(25))

#Sort a list.
squares.sort(reverse=True)
print(squares)

squares.reverse()

print(squares)

#find at what index 16 is available.
print(squares.index(16))



#Using Lists as Queue
print('**********************************************************************')
queue = deque (['April','May','June'])
print(queue)
queue.append('January')
print(queue)
queue.append('Feburary')
print(queue)
queue.popleft()
print(queue)
queue.popleft()
print(queue)