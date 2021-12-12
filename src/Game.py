import pygame

def main():
    pygame.init()
    surface = pygame.display.set_mode((700,600))
    backGround = pygame.image.load(r'Background(700x600).png')
    keyboard = pygame.image.load(r'keyboard\350x165keyboard.png')
    surface.blit(backGround, (0, 0))
    surface.blit(keyboard, (175,235))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            pygame.display.update()

    

if __name__ == '__main__':
    main()
