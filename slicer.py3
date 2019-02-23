# f = open("a_example.in", "r")
# f = open("b_small.in", "r")
# f = open("c_medium.in", "r")
f = open("d_big.in", "r")
isFirst = True
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
                pizza[-1].append(True)
                tCount += 1
            elif(s == 'M'):
                pizza[-1].append(False)
                mCount += 1

print("Tomato count: ", tCount)
print("Mushroom count: ", mCount)
# print(pizza)