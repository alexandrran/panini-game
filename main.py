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

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.MOUSEBUTTONDOWN and play_rect.collidepoint(event.pos)):
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and play_rect.collidepoint(event.pos):
            # pygame.mixer.music.fadeout(500)
            time.sleep(0.5)

    screen.fill((0, 0, 0))
    # screen.blit(beginning[current_frame], (0, 0))
    # text_surface = font.render(texts[current_frame], True, (255, 255, 255))
    # screen.blit(text_surface, (50,720 - 50))


pygame.quit()
sys.exit()