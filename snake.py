import pygame
import random


class Point:
    row = 0
    col = 0

    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __copy__(self):
        return Point(row=self.row, col=self.col)


# init env
pygame.init()
W = 800
H = 600

COL = 40
ROW = 30

size = (W, H)
window = pygame.display.set_mode(size)

pygame.display.set_caption('Eating Snake Game_GG')  # Window's name

# Define Coordinate
head = Point(row=int(ROW / 2), col=int(COL / 2))  # Snake head in the middle of window

snake = [Point(row=head.row, col=head.col + 1),
         Point(row=head.row, col=head.col + 2),
         Point(row=head.row, col=head.col + 3),
         Point(row=head.row, col=head.col + 4)]

bg_color = (255, 255, 255)  # white
head_color = (0, 128, 128)
food_color = (255, 255, 0)
snake_color = (128, 128, 128)  # gray
direct = 'left'


# Generate food
def gen_food():
    while 1:
        pos = Point(row=random.randint(0, ROW - 1), col=random.randint(0, COL - 1))
        is_coll = False
        if head.row == pos.row and head.col == pos.col:
            is_coll = True
        for _rectSnake in snake:
            if _rectSnake.row == pos.row and _rectSnake.col == pos.col:
                is_coll = True
                break
        if not is_coll:
            break

    return pos


food = gen_food()


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
quit = False

# timing control
clock = pygame.time.Clock()
while not quit:
    # Handling Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # quit game
            quit = True
        elif event.type == pygame.KEYDOWN:
            if event.key == 1073741906 or event.key == 119:
                if direct == 'left' or direct == 'right':
                    direct = 'up'
            elif event.key == 1073741905 or event.key == 115:
                if direct == 'left' or direct == 'right':
                    direct = 'down'
            elif event.key == 1073741904 or event.key == 97:
                if direct == 'up' or direct == 'down':
                    direct = 'left'
            elif event.key == 1073741903 or event.key == 100:
                if direct == 'up' or direct == 'down':
                    direct = 'right'

    # Snake Eating
    eat = (head.row == food.row and head.col == food.col)

    # Refresh food
    if eat:
        food = Point(row=random.randint(0, ROW - 1), col=random.randint(0, COL - 1))

    # Snake Move : 1. insert a rect at snake head
    snake.insert(0, head.__copy__())  # insert new head in the first place of snake by copy the old head
    # 2. Delete the last rect

    if not eat:
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

    # Verify 1. Meeting wall
    dead = False
    for rectSnake in snake:
        if rectSnake.row == head.row and rectSnake.col == head.col:
            dead = True
            break

    # Verify 1. Meeting wall
    if head.row < 0 or head.row >= ROW or head.col < 0 or head.col >= COL:
        dead = True

    if dead:
        print("GAME OVER")
        quit = True

    # Background
    pygame.draw.rect(
        window,
        bg_color,
        (0, 0, W, H))  # Whole window white (position, color, size)

    # Draw Snake body
    for rectSnake in snake:
        _rect(rectSnake, snake_color)

    # Snake head
    _rect(head, head_color)

    # Food
    _rect(food, food_color)

    pygame.display.flip()

    # setting frame
    clock.tick(10)  # sleep (60/1000)
pass
