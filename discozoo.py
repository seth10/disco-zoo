patterns = {
# Farm
    'Sheep': [[1,1,1,1]],
    'Pig': [[2,2],
            [2,2]],
    'Rabbit': [[3],
               [3],
               [3],
               [3]],
    'Horse': [[4],
              [4],
              [4]],
    'Cow': [[5,5,5]],
    'Unicorn': [[6,0,0],
                [0,6,6]],
# Outback
    'Kangaroo': [[1,0,0,0],
                 [0,1,0,0],
                 [0,0,1,0],
                 [0,0,0,1]],
    'Platypus': [[2,2,0],
                 [0,2,2]],
    'Crocodile': [[3,3,3,3]],
    'Koala': [[4,4],
              [0,4]],
    'Cockatoo': [[5,0],
                 [0,5],
                 [0,5]],
    'Tiddalik': [[0,6,0],
                 [6,0,6]],
# Savanna
    'Zebra': [[0,1,0],
              [1,0,1],
              [0,1,0]],
    'Hippo': [[2,0,2],
              [0,0,0],
              [2,0,2]],
    'Giraffe': [[3],
                [3],
                [3],
                [3]],
    'Lion': [[4,4,4]],
    'Elephant': [[5,5],
                 [5,0]],
    'Gryphon': [[6,0,6],
                [0,6,0]],
# Northern
    'Bear': [[1,1],
             [0,1],
             [0,1]],
    'Skunk': [[0,2,2],
              [2,2,0]],
    'Beaver': [[0,0,3],
               [3,3,0],
               [0,0,3]],
    'Moose': [[4,0,4],
              [0,4,0]],
    'Fox': [[5,5,0],
            [0,0,5]],
    'Sasquatch': [[6],
                  [6]],
# Polar
    'Penguin': [[0,1,0],
                [0,1,0],
                [1,0,1]],
    'Seal': [[2,0,0,0],
             [0,2,0,2],
             [0,0,2,0]],
    'Muskox': [[3,3,0],
               [3,0,3]],
    'Polar Bear': [[4,0,4],
                   [0,0,4]],
    'Walrus': [[5,0,0],
               [0,5,5]],
    'Yeti': [[6],
             [0],
             [6]],
# Jungle
    'Monkey': [[1,0,1,0],
               [0,1,0,1]],
    'Toucan': [[0,2],
               [2,0],
               [0,2],
               [0,2]],
    'Gorilla': [[3,0,3],
                [3,0,3]],
    'Panda': [[0,0,4],
              [4,0,0],
              [0,0,4]],
    'Tiger': [[5,0,5,5]],
    'Phoenix': [[6,0,0],
                [0,0,0],
                [0,0,6]],
# Jurassic
    'Diplodocus': [[1,0,0],
                   [0,1,1],
                   [0,1,0]],
    'Stegosaurus': [[0,2,2,0],
                    [2,0,0,2]],
    'Raptor': [[3,3,0],
               [0,3,0],
               [0,0,3]],
    'T-Rex': [[4,0],
              [0,0],
              [4,4]],
    'Triceratops': [[5,0,0],
                    [0,0,5],
                    [5,0,0]],
    'Dragon': [[6,0,0],
               [0,0,6]]
# Ice Age
# City
# Mountain
# Moon
# Mars
}

def findAnimal(animal):
    animalNames = [key for key in patterns]
    animalPatterns = [patterns[animalName] for animalName in animalNames]
    while animal.title() not in animalNames:
        longestAnimalName = max(animalNames, key=len)
        animalNames = map(lambda animalName: animalName[:len(longestAnimalName)-1], animalNames)
    return animalPatterns[animalNames.index(animal.title())]

def findPatterns(animals):
    grid = [[0]*5 for _ in range(5)]
    for animal in animals:
        for y in range(5 - len(animal) + 1):
            for x in range(5 - len(animal[0]) + 1):
                for iy in range(len(animal)):
                    for ix in range(len(animal[0])):
                        if animal[iy][ix]:
                            grid[y+iy][x+ix] += 1
    return grid

# check that there aren't any -1 in this possible pattern location,
# and that there aren't any matching numbers outside of this location
def checkPossiblePatternPosition(ay, ax, animal, grid, numberToFind):
    animalOnGrid = [[False]*5 for _ in range(5)]
    for iy in range(len(animal)):
        for ix in range(len(animal[0])):
            if animal[iy][ix]:
                animalOnGrid[ay+iy][ax+ix] = True
    for y in range(5):
        for x in range(5):
            if animalOnGrid[y][x]:
                if grid[y][x] == -1: return False # one of the cells in this possible pattern position is known to be empty
                if grid[y][x] > 0 and grid[y][x] != numberToFind: return False # a cell of another animal is contained here
            else:
                if grid[y][x] == numberToFind: return False # a cell of the animal has been found outside of this position
    return True

def addAnimalToGrid(y, x, animal, chancesGrid):
    for iy in range(len(animal)):
        for ix in range(len(animal[0])):
            if animal[iy][ix]:
                chancesGrid[y+iy][x+ix] += 1
    return chancesGrid


grid = [[0]*5 for _ in range(5)]
chancesGrid = [[0]*5 for _ in range(5)]
animals = map(findAnimal, ['tidd', 'pLAT'])
grid[2][2] = -1
grid[3][2] = 2
grid[3][1] = -1
grid[1][2] = 6

for animal in animals:
    numberToFind = filter(lambda n: n!=0, animal[0])[0]
    for y in range(5 - len(animal) + 1):
        for x in range(5 - len(animal[0]) + 1):
            if checkPossiblePatternPosition(y, x, animal, grid, numberToFind):
                chancesGrid = addAnimalToGrid(y, x, animal, chancesGrid)
 
for y in range(5):
    for x in range(5):
        if grid[y][x] > 0:
            chancesGrid[y][x] = float('inf')

for row in chancesGrid: print ('{:^3} '*5).format(*row)
