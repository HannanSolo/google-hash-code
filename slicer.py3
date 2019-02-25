# f = open("a_example.in", "r")
# f = open("b_small.in", "r")
# f = open("c_medium.in", "r")
f = open("a_example.in", "r")
isFirst = True

#order of number to meaning
#Rows, Columns, Minimum number of each ingredient cells in a slice, Maximum total number of cells of a slice

rows, cols, minIngredients, maxSlices = None, None, None, None
tCount, mCount = 0, 0
pizza = []
for x in f:
    if (isFirst):
        # Open the file and want to take the first 4 numbers into memory
        rows, cols, minIngredients, maxSlices = x.split()
        isFirst = False
    else:
        pizza.append([])
        for s in x:
            if(s == 'T'):
                pizza[-1].append([True, False])
                tCount += 1
            elif(s == 'M'):
                pizza[-1].append([False, False])
                mCount += 1

print("Tomato count: ", tCount)
print("Mushroom count: ", mCount)
# print(pizza)

pizzaSlices = []
def getSlices():
    isTomato = tCount < mCount
    initSlices(isTomato)
    expandSlices(isTomato)
    if(isTomato):
        pass
    else:
        pass
    print(pizzaSlices)

# Initializes a slice at every instance of the smallest ingredient
def initSlices(isTomato):
    for i in range(len(pizza)):
        for j in range(len(pizza[0])):
            if(pizza[i][j][0] == isTomato):
                pizza[i][j][1] = True
                pizzaSlices.append([i, j, i, j])

# Expands the 
def expandSlices(isTomato):
    pass

getSlices()


def rectangleSlicer():
    #test out the rectangle algorithm

    #keep track of the maximum row the pizza slicer is at
    maxRow=0 
    #keep track of the current pizza slices row and column to add to the list when it passes all the tests
    currentSliceRow=pizza[0][0]
    currentSliceColumn=pizza[0][0]

#counts how many ingredients of each are in a slice

    
    

    

    
    

    









