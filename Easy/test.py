import random

numberOfFruits = 5


def genFruits():
    positions = ()
    for _ in range(numberOfFruits):
        xPos = random.randint(1, 20)
        yPos = random.randint(1, 20)
        while (xPos, yPos) in positions:
            xPos = random.randint(1, 20)
            yPos = random.randint(1, 20)
        positions += ((xPos, yPos),)
    return positions


print(genFruits())
