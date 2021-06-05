from blessed import Terminal
import random
import copy
from collections import deque
import pyglet

term = Terminal()
UP = term.KEY_UP
RIGHT = term.KEY_RIGHT
LEFT = term.KEY_LEFT
DOWN = term.KEY_DOWN
DIRECTIONS = [LEFT, UP, RIGHT, DOWN]
MOVEMENT_MAP = {LEFT: [0, -1], UP: [-1, 0], RIGHT: [0, 1], DOWN: [1, 0]}
WASD_MAP = {'w': UP, 'a': LEFT, 's': DOWN, 'd': RIGHT,
            'W': UP, 'A': LEFT, 'S': DOWN, 'D': RIGHT}

dead = False


def sendGIF(ag_file):
    animation = pyglet.resource.animation(ag_file)
    sprite = pyglet.sprite.Sprite(animation)
    # tạo window và set gif
    winda = pyglet.window.Window(width=sprite.width, height=sprite.height)

    @winda.event
    def on_draw():
        winda.clear()
        sprite.draw()

    pyglet.app.run()


# start
BORDER = '⬜️'
BODY = '💳'
HEAD = '👽'
SPACE = '  '
DUCK = '🦆'

# init snake
snake = deque([[2, 6], [2, 5], [2, 4]])
# init food
food = [5, 1]
h, w = 20, 30  # height, width
score = 0
# init speed
speed = 1
# max speed
MAX_SPEED = 3

# tần số chuyển động của rắn
# Rắn chỉ di chuyển N1 trong N2 số lượt.
N1 = 1
N2 = 2

# Sau growUp turn rắn sẽ lớn lên
growUp = 8
# end config

messages = ['cố lên bạn có thể làm được!', "đừng để bị ăn thịt!", 'nhanh, nhanh lên nào!', "bạn có thể đánh bại nó!", "vượt qua con rắn!"]
message = None


with term.cbreak(), term.hidden_cursor():
    # clear screen
    print(term.home + term.clear)

    # Init ma trận
    world = [['⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️'],
         ['⬜️', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '⬜️'],
         ['⬜️', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '⬜️'],
         ['⬜️', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '⬜️'],
         ['⬜️', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '⬜️'],
         ['⬜️', '  ', '⬜️', '  ', '  ', '  ', '  ', '  ', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '  ', '⬜️', '  ', '  ', '  ', '⬜️', '  ', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '  ', '  ', '  ', '  ', '⬜️'],
         ['⬜️', '  ', '⬜️', '  ', '  ', '  ', '  ', '  ', '⬜️', '  ', '  ', '  ', '⬜️', '  ', '⬜️', '  ', '  ', '  ', '⬜️', '  ', '⬜️', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '⬜️'],
         ['⬜️', '  ', '⬜️', '  ', '  ', '  ', '  ', '  ', '⬜️', '  ', '  ', '  ', '⬜️', '  ', '  ', '⬜️', '  ', '⬜️', '  ', '  ', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '  ', '  ', '  ', '  ', '⬜️'],
         ['⬜️', '  ', '⬜️', '  ', '  ', '  ', '  ', '  ', '⬜️', '  ', '  ', '  ', '⬜️', '  ', '  ', '⬜️', '  ', '⬜️', '  ', '  ', '⬜️', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '⬜️'],
         ['⬜️', '  ', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '  ', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '  ', '  ', '  ', '⬜️', '  ', '  ', '  ', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '  ', '  ', '  ', '  ', '⬜️'],
         ['⬜️', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '⬜️'],
         ['⬜️', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '⬜️'],
         ['⬜️', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '⬜️'],
         ['⬜️', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '⬜️'],
         ['⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️']]
    for s in snake:
        world[s[0]][s[1]] = BODY
    head = snake[2]
    world[head[0]][head[1]] = HEAD
    world[food[0]][food[1]] = DUCK

    #print matrix
    for row in world:
        print(' '.join(row))
    print('sử dụng các phím ←, ↑, →, ↓ hoặc phím WASD để duy chuyển!')
    print("bạn đang là đồ ăn 😱 hãy tìm cách lừa rắn để chiến thắng\n")

    val = ''
    moving = False
    turn = 0

    while True:
        val = term.inkey(timeout=1/speed)
        if val.code in DIRECTIONS or val in WASD_MAP.keys():
            moving = True
        if not moving:
            continue

        # rắn quyết định nơi di chuyển bằng cách tính toán vị trí đầu rắn so với vịt 
        head = snake[0]
        y_diff = food[0] - head[0]
        x_diff = food[1] - head[1]

        preferred_move = None
        preferred_moves = []
        #ưu tiên đi lên / xuống trước
        if abs(y_diff) > abs(x_diff):
            if y_diff <= 0:
                preferred_move = UP
            else:
                preferred_move = DOWN
            #add vào mảng thứ tự
            preferred_moves = [preferred_move] + list(preferred_moves)
            #sau khi đi lên hoặc xuống sẽ rẽ trái(phải) tùy vào độ ưu tiên 
            if x_diff >= 0:
                preferred_moves = list(preferred_moves) + [RIGHT, LEFT]
            else:
                preferred_moves = list(preferred_moves) + [LEFT, RIGHT]
            #vị trí ưu tiên cuối 
            if UP in preferred_moves:
                preferred_moves = list(preferred_moves) + [DOWN]
            else:
                preferred_moves = list(preferred_moves) + [UP]
        #ưu tiên rẽ trái hoặc phải
        else:
            if x_diff >= 0:
                preferred_move = RIGHT
            else:
                preferred_move = LEFT
            preferred_moves = [preferred_move] + list(preferred_moves)
            #tương tự trên sẽ lên(xuống)
            if y_diff <= 0:
                preferred_moves = list(preferred_moves) + [UP, DOWN]
            else:
                preferred_moves = list(preferred_moves) + [DOWN, UP]
            #ưu tiên cuối 
            if RIGHT in preferred_moves:
                preferred_moves = list(preferred_moves) + [LEFT]
            else:
                preferred_moves = list(preferred_moves) + [RIGHT]

        # kiểm tra xem nước đi ưu tiên có hợp lệ không
        # nếu không, hãy kiểm tra xem tất cả các nước đi khác có hợp lệ không

        next_move = None
        for move in preferred_moves:
            movement = MOVEMENT_MAP[move]
            head_copy = copy.copy(head)
            head_copy[0] += movement[0]
            head_copy[1] += movement[1]
            heading = world[head_copy[0]][head_copy[1]]
            if heading == BORDER:
                continue
            elif heading == BODY:
                # Sau growUp turn thì rắn sẽ lớn lên
                # đầu chỉ có thể di chuyển đến vị trí của đuôi if turn % growUp != 0
                if head_copy == snake[-1] and turn % growUp != 0:
                    next_move = head_copy
                    break
                else:
                    continue
            else:
                next_move = head_copy
                break

        if next_move is None:
            break

        turn += 1
        # rắn chỉ di chuyển N - 1 trong số N lượt.
        # trước khi rắn di chuyển, clear toàn bộ vị trí của thức ăn
        world[food[0]][food[1]] = SPACE
        if turn % N2 < N1:
            snake.appendleft(next_move)
            # sau growUp turn rắn sẽ dài, to và nhanh hơn :))
            world[head[0]][head[1]] = BODY
            if turn % growUp != 0:
                speed = min(speed * 1.05, MAX_SPEED)
                tail = snake.pop()
                world[tail[0]][tail[1]] = SPACE
            world[next_move[0]][next_move[1]] = HEAD

        # sau đó thức ăn di chuyển thì
        food_copy = copy.copy(food)
        # encode chuyển động food_copy
        if val.code in DIRECTIONS or val in WASD_MAP.keys():
            direction = None
            if val in WASD_MAP.keys():
                direction = WASD_MAP[val]
            else:
                direction = val.code
            movement = MOVEMENT_MAP[direction]
            food_copy[0] += movement[0]
            food_copy[1] += movement[1]

        # Check nơi food hướng đến
        food_heading = world[food_copy[0]][food_copy[1]]
        # bạn sẽ chết nếu bị đầu rắn ăn, thân rắn ko ăn đc bạn
        if food_heading == HEAD:
            dead = True
        # Chỉ di chuyển thức ăn nếu bạn đang cố gắng di chuyển đến một chỗ trống.
        if food_heading == SPACE:
            food = food_copy
        # Nếu bằng cách nào đó vị trí hiện tại của con vịt trùng với cơ thể con rắn, thì con vịt đã chết.
        if world[food[0]][food[1]] == BODY or world[food[0]][food[1]] == HEAD:
            dead = True
        if not dead:
            world[food[0]][food[1]] = DUCK

        print(term.move_yx(0, 0))
        for row in world:
            print(' '.join(row))
        score = len(snake) - 3
        print(f'Lượt: {turn} - Điểm: {score} - Độ dài: {len(snake)}' + term.clear_eol)
        if dead:
            break
        if turn % 50 == 0:
            message = random.choice(messages)
        if message:
            print(message + term.clear_eos)
        print(term.clear_eos, end='')

if dead:
    print('Bạn đã bị ăn thịt' + term.clear_eos)
    ag_file = "gif/lose.gif"
    sendGIF(ag_file)
else:
    ag_file = "gif/win.gif"
    sendGIF(ag_file)
    print('WOW bạn đã thắng' + term.clear_eos)
