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
}

grid = [[0]*5 for _ in range(5)]

def findAnimal(animal):
    animalNames = [key for key in patterns]
    animalPatterns = [patterns[animalName] for animalName in animalNames]
    while animal not in animalNames:
        longestAnimalName = max(animalNames, key=len)
        animalNames = map(lambda animalName: animalName[:len(longestAnimalName)-1], animalNames)
    return animalPatterns[animalNames.index(animal)]

animals = map(findAnimal, ['T-Rex', 'Tric'])
for animal in animals:
    for y in range(5 - len(animal) + 1):
        for x in range(5 - len(animal[0]) + 1):
            for iy in range(len(animal)):
                for ix in range(len(animal[0])):
                    grid[y+iy][x+ix] += 1
for row in grid: print row
