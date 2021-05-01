#!/usr/bin/env python
# coding: utf-8

# In[142]:


import random
import numpy as np

def getTickets():
    
  #will contain the values of tickets
  ticket = np.zeros((3, 9), dtype=int)

  #Total numbers from 1 to 90
  numbers = [num for num in range(1, 91)]
    
  #Indices of the ticket
  indices = [(i, j) for i in range(3) for j in range(9)]

  random_indices = []

  #Randomly select 5 positions in each row
  first_row = random.sample(indices[:9], 5)
  second_row = random.sample(indices[9:18], 5)
  third_row = random.sample(indices[-9:], 5)

  for i in first_row:
    random_indices.append(i)

  for i in second_row:
    random_indices.append(i)

  for i in third_row:
    random_indices.append(i)

  #Populate the ticket with non-zero numbers
  for num in random_indices:
    if num[1] == 0:
      number=-1
      while(number==-1):
          number = random.choice(numbers[0:9])
      ticket[num] = number
      numbers[numbers.index(number)] = -1
    elif num[1] == 1:
      number=-1
      while(number==-1):
          number = random.choice(numbers[9:19])
      ticket[num] = number
      numbers[numbers.index(number)] = -1
    elif num[1] == 2:
      number=-1
      while(number==-1):
          number = random.choice(numbers[19:29])
      ticket[num] = number
      numbers[numbers.index(number)] = -1
    elif num[1] == 3:
      number=-1
      while(number==-1):
          number = random.choice(numbers[29:39])
      ticket[num] = number
      numbers[numbers.index(number)] = -1
    elif num[1] == 4:
      number=-1
      while(number==-1):
          number = random.choice(numbers[39:49])
      ticket[num] = number
      numbers[numbers.index(number)] = -1
    elif num[1] == 5:
      number=-1
      while(number==-1):
          number = random.choice(numbers[49:59])
      ticket[num] = number
      numbers[numbers.index(number)] = -1
    elif num[1] == 6:
      number=-1
      while(number==-1):
          number = random.choice(numbers[59:69])
      ticket[num] = number
      numbers[numbers.index(number)] = -1
    elif num[1] == 7:
      number=-1
      while(number==-1):
          number = random.choice(numbers[69:79])
      ticket[num] = number
      numbers[numbers.index(number)] = -1
    elif num[1] == 8:
      number=-1
      while(number==-1):
          number = random.choice(numbers[79:90])
      ticket[num] = number
      numbers[numbers.index(number)] = -1

  #Sort the columns now
  for col in range(9):
        # if column contains 3 numbers
        if(ticket[0][col] != 0 and ticket[1][col] != 0 and ticket[2][col] != 0):
            for row in range(2):
                if ticket[row][col] > ticket[row+1][col]:
                    temp = ticket[row][col]
                    ticket[row][col] = ticket[row+1][col]
                    ticket[row+1][col] = temp

        # if column contains 2 numbers
        elif(ticket[0][col] != 0 and ticket[1][col] != 0 and ticket[2][col] == 0):
            if ticket[0][col] > ticket[1][col]:
                temp = ticket[0][col]
                ticket[0][col] = ticket[1][col]
                ticket[1][col] = temp
        elif(ticket[0][col] != 0 and ticket[2][col] != 0 and ticket[1][col] == 0):
            if ticket[0][col] > ticket[2][col]:
                temp = ticket[0][col]
                ticket[0][col] = ticket[2][col]
                ticket[2][col] = temp
        elif(ticket[0][col] == 0 and ticket[1][col] != 0 and ticket[2][col] != 0):
            if ticket[1][col] > ticket[2][col]:
                temp = ticket[1][col]
                ticket[1][col] = ticket[2][col]
                ticket[2][col] = temp
        
        #if column contains no numbers then simply try new combination
        elif(ticket[0][col] == 0 and ticket[1][col] == 0 and ticket[2][col] == 0):
            return getTickets()

  return ticket


ticket = getTickets()
for row in range(3):
    for col in range(9):
        print("{:02d}".format(ticket[row][col]).rjust(3), end="")
    print()


# In[ ]:




