import pygame
import ButtonClass

LIGHT_GRAY = (200,200,200)
DARK_GREY = (150,150,150)


def main():
    pygame.init()
    pygame.mixer.init()


    surface = pygame.display.set_mode((700,600))
    backGround = pygame.image.load(r'Background(700x600).png')
    keyboard = pygame.image.load(r'350x165keyboard.png')
    logo = pygame.image.load(r'memorykeys.png')

    C = ButtonClass.Button((200,380), LIGHT_GRAY, pygame.mixer.Sound("notes/c4.mp3"))
    Cs = ButtonClass.Button((220,330), LIGHT_GRAY, pygame.mixer.Sound("notes/c-4.mp3"))
    D = ButtonClass.Button((250,380), LIGHT_GRAY, pygame.mixer.Sound("notes/d4.mp3"))
    Ds = ButtonClass.Button((280,330), LIGHT_GRAY, pygame.mixer.Sound("notes/d-4.mp3"))
    E = ButtonClass.Button((300,380), LIGHT_GRAY, pygame.mixer.Sound("notes/e4.mp3"))
    F = ButtonClass.Button((350,380), LIGHT_GRAY, pygame.mixer.Sound("notes/f4.mp3"))
    Fs = ButtonClass.Button((368,330), LIGHT_GRAY, pygame.mixer.Sound("notes/f-4.mp3"))
    G = ButtonClass.Button((400,380), LIGHT_GRAY, pygame.mixer.Sound("notes/g4.mp3"))
    Gs = ButtonClass.Button((425,330), LIGHT_GRAY, pygame.mixer.Sound("notes/g-4.mp3"))
    A = ButtonClass.Button((450,380), LIGHT_GRAY, pygame.mixer.Sound("notes/a4.mp3"))
    As = ButtonClass.Button((483,330), LIGHT_GRAY, pygame.mixer.Sound("notes/a-4.mp3"))
    B = ButtonClass.Button((500,380), LIGHT_GRAY, pygame.mixer.Sound("notes/b4.mp3"))

    surface.blit(backGround, (0, 0))
    surface.blit(keyboard, (183,235))
    surface.blit(logo, (0,0))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if C.pos[0] <= event.pos[0] <= C.pos[0]+15 and C.pos[1] <= event.pos[1] <= C.pos[1]+15:
                        C.sound_file.play()

                    elif Cs.pos[0] <= event.pos[0] <= Cs.pos[0]+15 and Cs.pos[1] <= event.pos[1] <= Cs.pos[1]+15:
                        Cs.sound_file.play()

                    elif D.pos[0] <= event.pos[0] <= D.pos[0]+15 and D.pos[1] <= event.pos[1] <= D.pos[1]+15:
                        D.sound_file.play()

                    elif Ds.pos[0] <= event.pos[0] <= Ds.pos[0]+15 and Ds.pos[1] <= event.pos[1] <= Ds.pos[1]+15:
                        Ds.sound_file.play()

                    elif E.pos[0] <= event.pos[0] <= E.pos[0]+15 and E.pos[1] <= event.pos[1] <= E.pos[1]+15:
                        E.sound_file.play()

                    elif F.pos[0] <= event.pos[0] <= F.pos[0]+15 and F.pos[1] <= event.pos[1] <= F.pos[1]+15:
                        F.sound_file.play()

                    elif Fs.pos[0] <= event.pos[0] <= Fs.pos[0]+15 and Fs.pos[1] <= event.pos[1] <= Fs.pos[1]+15:
                        Fs.sound_file.play()

                    elif G.pos[0] <= event.pos[0] <= G.pos[0]+15 and G.pos[1] <= event.pos[1] <= G.pos[1]+15:
                        G.sound_file.play()

                    elif Gs.pos[0] <= event.pos[0] <= Gs.pos[0]+15 and Gs.pos[1] <= event.pos[1] <= Gs.pos[1]+15:
                        Gs.sound_file.play()

                    elif A.pos[0] <= event.pos[0] <= A.pos[0]+15 and A.pos[1] <= event.pos[1] <= A.pos[1]+15:
                        A.sound_file.play()

                    elif As.pos[0] <= event.pos[0] <= As.pos[0]+15 and As.pos[1] <= event.pos[1] <= As.pos[1]+15:
                        As.sound_file.play()

                    elif B.pos[0] <= event.pos[0] <= B.pos[0]+15 and B.pos[1] <= event.pos[1] <= B.pos[1]+15:
                        B.sound_file.play()


            #elif event.type==pygame.MOUSEBUTTONDOWN:
                #if C.button.collidepoint(event.pos):
                    #C.sound_file.play()


        pygame.display.update()

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



if __name__ == '__main__':
    main()