import pygame, sys
import time
import pathlib
path = pathlib.Path(__file__).parent.resolve()

pygame.init()

# Settings
WHITE = (255, 255, 255)
screen = pygame.display.set_mode((1000,720))
screen.fill(WHITE)
pygame.display.set_caption("Serik's paninis")

# pygame.mixer.music.load("assets\\mp3\\.mp3")
# pygame.mixer.music.play(-1)

#Main menu: background, buttons
play_button = pygame.image.load("assets\\buttons\\play_button.png")
# sound_button = pygame.image.load("assets\\buttons\\sound_button.png")
quit_button = pygame.image.load("assets\\buttons\\quit_button.png")
bg = pygame.image.load("assets\\menu.png")
wp = pygame.image.load("assets\\wp.png")
cm = pygame.image.load("assets\\cm.png")
# end = pygame.image.load("assets\\thanks.png")
play_rect = play_button.get_rect()
# sound_rect = sound_button.get_rect()
quit_rect = quit_button.get_rect()
play_rect.center = (500, 440)
# sound_rect.center = (1000 // 2, 720 // 3)
quit_rect.center = (500, 590)

# beginning = [
#     pygame.image.load("assets\\beginning\\image1.jpg"),
#     pygame.image.load("assets\\beginning\\image2.jpg"),
#     pygame.image.load("assets\\beginning\\image3.jpg")
# ]

# Text for each beginning image
# texts = [
#     "Text corresponding to the first image.",
#     "Text corresponding to the second image.",
#     "Text corresponding to the third image."
# ]

# Font settings
font = pygame.font.Font(None, 36)

# Current frame index
current_frame = 0
screen.blit(bg, (0,0))
screen.blit(play_button, play_rect)
screen.blit(quit_button, quit_rect)
pygame.display.flip()

current_screen = 'main'

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.MOUSEBUTTONDOWN and quit_rect.collidepoint(event.pos)):
            pygame.quit()
            sys.exit()

        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if current_screen == 'main' and play_rect.collidepoint(event.pos):
                screen.blit(wp, (0, 0))
                pygame.display.flip()
                current_screen = 'wp'
                continue  

            if current_screen == 'wp':
                x, y = pygame.mouse.get_pos()
                if 21 < x < 230 and 230 < y < 450:
                    screen.blit(cm, (0, 0))
                    pygame.display.flip()
                    current_screen = 'cm'

    screen.fill((0, 0, 0))
    # screen.blit(beginning[current_frame], (0, 0))
    # text_surface = font.render(texts[current_frame], True, (255, 255, 255))
    # screen.blit(text_surface, (50,720 - 50))


pygame.quit()
sys.exit()