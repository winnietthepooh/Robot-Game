game = []
mapSize = (6, 4)
field = None


# used to detect if something is in said position
def object_scan(x_position, y_position):
    global game
    global mapSize
    result = False
    for unit in game:
        if (
                unit.xPosition == x_position and unit.yPosition == y_position) or y_position <= 0 or x_position <= 0 \
                or y_position > mapSize[1] or x_position > mapSize[0]:
            result = True
            break
    return result


# how to train your robot
class Bot:
    def __init__(self, h, d, x, y, name):
        self.health = h
        self.damage = d
        self.xPosition = x
        self.yPosition = y
        self.name = name

    def movement(self, direction):
        global field
        if direction == 'w':
            if object_scan(self.xPosition, self.yPosition - 1):
                print('Ran into something')
            else:
                self.yPosition -= 1
        elif direction == 's':
            if object_scan(self.xPosition, self.yPosition + 1):
                print('Ran into something')
            else:
                self.yPosition += 1
        elif direction == 'a':
            if object_scan(self.xPosition - 1, self.yPosition):
                print('Ran into something')
            else:
                self.xPosition -= 1
        elif direction == 'd':
            if object_scan(self.xPosition + 1, self.yPosition):
                print('Ran into something')
            else:
                self.xPosition += 1
        else:
            print('Recived a non direction')


# finds robot in game
def find_bot(target):
    global game
    for unit in game:
        if unit.name == target:
            return unit


def new_turn():
    global game
    print('Your turn to move')
    signal = input()
    find_bot('player').movement(signal)


# creates robots for play
game.append(Bot(10, 2, 2, 2, 'player'))
game.append(Bot(4, 3, 5, 3, 'enemy'))

if __name__ == "__main__":
    while True:
        new_turn()
