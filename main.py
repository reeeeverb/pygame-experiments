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
    print(len(array_board(x,y)))
def array_board(x,y):
    out = []
    out+=(array_tile(x-50,y-75,3))
    out+=(array_tile(x-100,y,4))
    out+=(array_tile(x-150,y+75,5))
    out+=(array_tile(x-150,y+125,5,True))
    out+=(array_tile(x-100,y+200,4,True))
    out+=(array_tile(x-50,y+275,3,True))
    return out
def array_tile(x,y,r,inverted=False):
    #150,100
    result = []
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
        pygame.draw.circle(screen,"red",(c[0],c[1]),5)
    return result


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            print(pos)
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("aqua")
    draw_board(200,175,[])
    #pygame.draw.polygon(screen,"black",[(200,175),(150,150),(150,100),(200,75),(250,100),(250,150)])
    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()

