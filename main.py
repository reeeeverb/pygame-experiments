import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

def draw_tile(x,y,terrain):
    terrain_to_color = {"Mountains":"gray","Hills":"red","Forest":"darkgreen","Fields":"yellow","Pasture":"yellowgreen","Desert":"navajowhite"}
    color = terrain_to_color[terrain]
    pygame.draw.polygon(screen,color,[(x,y),(x-50,y-25),(x-50,y-75),(x,y-100),(x+50,y-75),(x+50,y-25)])
    pygame.draw.polygon(screen,"black",[(x,y),(x-50,y-25),(x-50,y-75),(x,y-100),(x+50,y-75),(x+50,y-25)],4)

def draw_board(x,y,terrains):
    terrains = ["Forest"]*19
    draw_tile(x,y,terrains[0])
    draw_tile(x+100,y,terrains[1])
    draw_tile(x+200,y,terrains[2])
    draw_tile(x-50,y+75,terrains[3])
    draw_tile(x+50,y+75,terrains[4])
    draw_tile(x+150,y+75,terrains[5])
    draw_tile(x+250,y+75,terrains[6])
    draw_tile(x-100,y+150,terrains[7])
    draw_tile(x,y+150,terrains[8])
    draw_tile(x+100,y+150,terrains[9])
    draw_tile(x+200,y+150,terrains[10])
    draw_tile(x+300,y+150,terrains[11])
    draw_tile(x-50,y+225,terrains[12])
    draw_tile(x+50,y+225,terrains[13])
    draw_tile(x+150,y+225,terrains[14])
    draw_tile(x+250,y+225,terrains[15])
    draw_tile(x,y+300,terrains[16])
    draw_tile(x+100,y+300,terrains[17])
    draw_tile(x+200,y+300,terrains[18])
    return board_corners(x,y), board_edges(x,y)
def board_corners(x,y):
    out = []
    out+=(tile_corners(x-50,y-75,3))
    out+=(tile_corners(x-100,y,4))
    out+=(tile_corners(x-150,y+75,5))
    out+=(tile_corners(x-150,y+125,5,True))
    out+=(tile_corners(x-100,y+200,4,True))
    out+=(tile_corners(x-50,y+275,3,True))
    return out
def board_edges(x,y):
    out = []
    out+=(tile_edges(x-50,y-75,3))
    out+=(tile_edges(x-50,y-75,3,vertical=True))
    out+=(tile_edges(x-100,y,4))
    out+=(tile_edges(x-100,y,4,vertical=True))
    out+=(tile_edges(x-150,y+75,5))
    out+=(tile_edges(x-150,y+75,5,vertical=True))
    out+=(tile_edges(x-150,y+125,5,inverted = True))
    out+=(tile_edges(x-100,y+150,4,vertical = True))
    out+=(tile_edges(x-100,y+200,4,inverted = True))
    out+=(tile_edges(x-50,y+225,3,vertical = True))
    out+=(tile_edges(x-50,y+275,3,inverted = True))
    return out
def tile_edges(x,y,r,inverted = False, vertical=False):
    result = []
    sprites = []
    for i in range(r):
        if inverted:
            result.append(((x,y),(x+50,y+25)))
            result.append(((x+50,y+25),(x+100,y)))
        elif vertical:
            result.append(((x,y),(x,y+50)))
        else:  
            result.append(((x,y),(x+50,y-25)))
            result.append(((x+50,y-25),(x+100,y)))
        x +=100 
    if vertical:
        result.append(((x,y),(x,y+50)))
    for fir in result:
        s = pygame.draw.line(screen,"red",fir[0],fir[1],5)
        sprites.append(s)
    return sprites

def tile_corners(x,y,r,inverted=False):
    #150,100
    result = []
    sprites = []
    result.append((x,y))
    for i in range(r):
        if inverted:
            result.append((x+50,y+25))
            result.append((x+100,y))
        else:  
            result.append((x+50,y-25))
            result.append((x+100,y))
        x +=100 
    for c in result:
        s = pygame.draw.circle(screen,"red",(c[0],c[1]),5)
        sprites.append(s)
    return sprites


corners = []
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            print(pos)
            clicked = [s for s in corners if s.collidepoint(pos)]
            print(corners.index(clicked[0]) if len(clicked) == 1 else "Invalid Location")
        if event.type == pygame.QUIT:
            running = False
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("aqua")
    corners = draw_board(200,175,[])
    #pygame.draw.polygon(screen,"black",[(200,175),(150,150),(150,100),(200,75),(250,100),(250,150)])
    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()

