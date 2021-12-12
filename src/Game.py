import pygame
import ButtonClass

LIGHT_GRAY = (200,200,200)
DARK_GREY = (150,150,150)

def main():
    pygame.init()
    surface = pygame.display.set_mode((700,600))
    backGround = pygame.image.load(r'Background(700x600).png')
    keyboard = pygame.image.load(r'350x165keyboard.png')

    C = ButtonClass.Button(15,(200,380), LIGHT_GRAY)
    Cs = ButtonClass.Button(9,(220,330), LIGHT_GRAY)
    D = ButtonClass.Button(15,(250,380), LIGHT_GRAY)
    Ds = ButtonClass.Button(9,(280,330), LIGHT_GRAY)
    E = ButtonClass.Button(15,(300,380), LIGHT_GRAY)
    F = ButtonClass.Button(15,(350,380), LIGHT_GRAY)
    Fs = ButtonClass.Button(9,(368,330), LIGHT_GRAY)
    G = ButtonClass.Button(15,(400,380), LIGHT_GRAY)
    Gs = ButtonClass.Button(9,(425,330), LIGHT_GRAY)
    A = ButtonClass.Button(15,(450,380), LIGHT_GRAY)
    As = ButtonClass.Button(9,(483,330), LIGHT_GRAY)
    B = ButtonClass.Button(15,(500,380), LIGHT_GRAY)

    surface.blit(backGround, (0, 0))
    surface.blit(keyboard, (175,235))

    C.render(surface)
    Cs.render(surface)
    D.render(surface)
    Ds.render(surface)
    E.render(surface)
    F.render(surface)
    Fs.render(surface)
    G.render(surface)
    Gs.render(surface)
    A.render(surface)
    As.render(surface)
    B.render(surface)


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            pygame.display.update()



if __name__ == '__main__':
    main()
