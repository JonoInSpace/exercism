# Globals for the directions
# Change the values as you see fit
EAST = (1,0)
NORTH = (0,1)
WEST = (-1,0)
SOUTH = (0,-1)

ROTATION = [NORTH, EAST, SOUTH, WEST]

class Robot:
    def __init__(self, direction=NORTH, x=0, y=0):
        self.coordinates = (x, y)
        self.direction = direction
        
    def move(self, command_string):
        for command in command_string:
            if command == 'R':
                self.direction = ROTATION[ (ROTATION.index(self.direction) + 1 )% 4]
            elif command == 'L':
                self.direction = ROTATION[ (ROTATION.index(self.direction) - 1 )% 4]
            elif command  == 'A':
                self.coordinates = (self.coordinates[0] + self.direction[0], self.coordinates[1] + self.direction[1])
        
        
