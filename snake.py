class Point:
    row = 0
    col = 0

    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __copy__(self):
        return Point(row=self.row, col=self.col)


import pygame

# init env
pygame.init()
W = 800
H = 600

COL = 40
ROW = 30

snake = [Po]
size = (W, H)
window = pygame.display.set_mode(size)

pygame.display.set_caption('Eating Snake Game_GG')  # Window's name

# Define Coordinate
head = Point(row=int(ROW / 2), col=int(COL / 2))  # Snake head in the middle of window
food = Point(row=2, col=3)

bg_color = (255, 255, 255)  # white
head_color = (0, 128, 128)
food_color = (255, 255, 0)

direct = 'left'


# Draw with coordinates
def _rect(point, color):
    """draw snake in the window"""
    cell_width = W / COL
    cell_height = H / ROW

    left = point.col * cell_width
    top = point.row * cell_height

    pygame.draw.rect(
        window,
        color,
        (left, top, cell_width, cell_height))
    pass

# ending game
quit = True

# timing control
clock = pygame.time.Clock()
while quit:
    # Handling Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # quit game
            quit = False
        elif event.type == pygame.KEYDOWN:
            if event.key == 1073741906 or event.key == 119:
                direct = 'up'
            elif event.key == 1073741905 or event.key == 115:
                direct = 'down'
            elif event.key == 1073741904 or event.key == 97:
                direct = 'left'
            elif event.key == 1073741903 or event.key == 100:
                direct = 'right'

    # Snake Body : 1. insert a rect at snake head
    snake.insert(0, head.__copy__())
    # 2. Delete the last rect
    snake.pop()


    # Snake Move
    if direct == 'left':
        head.col -= 1
    elif direct == 'right':
        head.col += 1
    elif direct == 'up':
        head.row -= 1
    elif direct == 'down':
        head.row += 1

    # Background
    pygame.draw.rect(
        window,
        bg_color,
        (0, 0, W, H))  # Whole window white (position, color, size)

    # Snake head
    _rect(head, head_color)

    # Food
    _rect(food, food_color)

    pygame.display.flip()

    # setting frame
    clock.tick(30)  # sleep (60/1000)
