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
    #pygame.draw.polygon(screen,"black",[(200,175),(150,150),(150,100),(200,75),(250,100),(250,150)])
    draw_tile(200,175,"Mountains")
    draw_tile(300,175,"Hills")
    draw_tile(400,175,"Forest")
    draw_tile(150,250,"Fields")
    draw_tile(250,250,"Pasture")
    draw_tile(350,250,"Desert")
    draw_tile(450,250,"Mountains")
    draw_tile(100,325,"Hills")
    draw_tile(200,325,"Forest")
    draw_tile(300,325,"Fields")
    draw_tile(400,325,"Pasture")
    draw_tile(500,325,"Desert")
    draw_tile(150,400,"Fields")
    draw_tile(250,400,"Pasture")
    draw_tile(350,400,"Desert")
    draw_tile(450,400,"Mountains")
    draw_tile(200,475,"Mountains")
    draw_tile(300,475,"Hills")
    draw_tile(400,475,"Forest")
    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()

