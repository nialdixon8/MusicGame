import pygame

class Button:
    def __init__(self, size, pos, colour, sound_file):
        self.pos = pos
        self.size = size
        self.colour = colour
        self.sound = pygame.mixer.Sound(sound_file)
        self.rect = pygame.Rect(pos, self.size)

    def render(self, window):
        #window.blit(self.button, (self.pos[0], self.pos[1]))
        pygame.draw.circle(window, self.colour, (self.pos[0], self.pos[1]), self.size)

    def clicked(self, events):
        mousePos = pygame.mouse.get_pos()#  get the mouse position
        for event in events:
            if self.button.get_rect(topleft=self.pos).collidepoint(mousePos[0], mousePos[1]):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return True
        return False