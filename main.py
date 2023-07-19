import pygame


pygame.init()
width = 600
height = 600
color_white = (255, 255, 255)
color_red = (255, 0, 0)
color_black = (0, 0, 0)
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
speed = 5
x_position= 100
y_position= 100
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT]:
        x_position = (x_position + speed)
    elif key[pygame.K_LEFT]:
        x_position = (x_position - speed)
    screen.fill(color_black)
    # pygame.draw.rect(screen, color_white, (100, 100, 12, 12))
    pygame.draw.circle(screen, color_red, (x_position, y_position), 12)
    pygame.display.update()
    clock.tick(60)




# if __name__ == '__main__':
#     print_hi('PyCharm')

