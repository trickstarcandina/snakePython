#đối với ma trận trống thì dùng như sau

def list_empty_spaces(world, space):
    result = []
    for i in range(len(world)):
        for j in range(len(world[i])):
            if world[i][j] == space:
                result.append([i, j])
    return result

BORDER = '⬜️'
SPACE = '  '
h, w = 20, 30

world = [[SPACE] * w for _ in range(h)]

for i in range(h):
    world[i][0] = BORDER
    world[i][-1] = BORDER
for j in range(w):
    world[0][j] = BORDER
    world[-1][j] = BORDER

#ma trận 1
    world = [['⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️'],
             ['⬜️', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '⬜️'],
             ['⬜️', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '⬜️', '⬜️', '  ', '  ', '  ', '  ', '⬜️'],
             ['⬜️', '  ', '  ', '⬜️', '  ', '⬜️', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '⬜️', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '⬜️', '  ', '  ', '  ', '  ', '⬜️'],
             ['⬜️', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '⬜️', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '⬜️', '⬜️', '  ', '  ', '  ', '  ', '⬜️'],
             ['⬜️', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '⬜️', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '⬜️', '⬜️', '  ', '  ', '  ', '  ', '⬜️'],
             ['⬜️', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '⬜️', '⬜️', '  ', '  ', '  ', '  ', '⬜️', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '⬜️'],
             ['⬜️', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '⬜️', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '⬜️'],
             ['⬜️', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '⬜️'],
             ['⬜️', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '⬜️'],
             ['⬜️', '  ', '⬜️', '⬜️', '⬜️', '⬜️', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '⬜️', '⬜️', '  ', '⬜️'],
             ['⬜️', '  ', '⬜️', '  ', '  ', '⬜️', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '⬜️', '⬜️', '  ', '⬜️'],
             ['⬜️', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '⬜️'],
             ['⬜️', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '⬜️'],
             ['⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️']]
