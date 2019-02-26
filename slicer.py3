# f = open("a_example.in", "r")
# f = open("b_small.in", "r")
# f = open("c_medium.in", "r")
f = open("a_example.in", "r")
isFirst = True

#order of number to meaning
#Rows, Columns, Minimum number of each ingredient cells in a slice, Maximum total number of cells of a slice

rows, cols, minIngredients, maxIngredients = None, None, None, None
tCount, mCount = 0, 0
pizza = []
for x in f:
    if (isFirst):
        # Open the file and want to take the first 4 numbers into memory
        rows, cols, minIngredients, maxIngredients = x.split()
        rows = int(rows)
        cols = int(cols)
        minIngredients = int(minIngredients)
        maxIngredients = int(maxIngredients)
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
sliceWeb = []
def getSlices():
    isTomato = tCount < mCount
    initSlices(isTomato)
    expandWeb(isTomato)
    combineNodes(1, 1, 1, 2)
    print(sliceWeb)
    if(isTomato):
        pass
    else:
        pass

# Initializes a slice at every instance of the smallest ingredient
def initSlices(isTomato):
    for i in range(len(pizza)):
        for j in range(len(pizza[0])):
            if(pizza[i][j][0] == isTomato):
                pizza[i][j][1] = True
                sliceWeb.append([[i, j]])

# Combines two web nodes into one web
def combineNodes(i, j, i2, j2):
    location, location2 = -1, -1
    for x in sliceWeb:
        # Initialize the location of the webs containing i, j, and i2, j2
        if [i, j] in x:
            location = sliceWeb.index(x)
        if [i2, j2] in x:
            location2 = sliceWeb.index(x)
    if(location == -1):
        if(location2 == -1):
            # Need to create a new web with the two ingredients
            sliceWeb.append([[i, j], [i2, j2]])
        else:
            # Add first node to second web
            sliceWeb[location2].append([i, j])
    else:
        if (location2 == -1):
            # Add second node to first web
            sliceWeb[location].append([i2, j2])
        else:
            # Combine the first and second web
            if (len(sliceWeb[location]) + len(sliceWeb[location2]) > maxIngredients):
                # Can't combine because resulting slice would be too large, return false
                return False
            else:
                # Add the first web into the second, and remove the second web
                newWeb = sliceWeb[location] + sliceWeb[location2]
                sliceWeb[location] = newWeb
                sliceWeb.remove(sliceWeb[location2])
    return True

# Expands the slice web to include min amount of ingredients
def expandWeb(isTomato):
    pass

# Returns true if the ingredient at location (i, j) is already part of a slice
def isAlreadySlice(i, j):
    return pizza[i][j][1]

getSlices()


def rectangleSlicer():
    #test out the rectangle algorithm

    #keep track of the maximum row the pizza slicer is at
    maxRow=0 
    #keep track of the current pizza slices row and column to add to the list when it passes all the tests
    currentSliceRow=pizza[0][0]
    currentSliceColumn=pizza[0][0]

#counts how many ingredients of each are in a slice

    
    

    

    
    

    









