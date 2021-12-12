import pygame

class Button:
    def __init__(self, pos, colour, sound):
        self.pos = pos
        self.colour = colour
        self.sound_file = sound

    def render(self, window):
        #window.blit(self.button, (self.pos[0], self.pos[1]))
        pygame.draw.rect(window, self.colour, (self.pos[0], self.pos[1], 15, 15))

    def clicked(self, events):
        mousePos = pygame.mouse.get_pos()#  get the mouse position
        for event in events:
            if self.pos(topleft=self.pos).collidepoint(mousePos[0], mousePos[1]):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print("was clicked")
                    return True
            return False