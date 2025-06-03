from tkinter.font import Font
import pygame

from Code.Const import C_ORANGE, C_WHITE, MENU_OPTION, WIN_WIDTH

class Menu:
    
    def __init__(self,window):
        self.window = window
        self.surf = pygame.image.load('./Asset/MenuBg.png')
        self.rect = self.surf.get_rect(left=0,top=0)
        
    def run(self,):
        
        pygame.mixer_music.load('./Asset/Menu.mp3')
        pygame.mixer_music.play(-1)

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Mountain", C_ORANGE, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "Shooter", C_ORANGE, ((WIN_WIDTH / 2), 120))
            
            for i in range(len(MENU_OPTION)):
                    self.menu_text(20, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))
            
            
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: pygame.Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: pygame.Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
    