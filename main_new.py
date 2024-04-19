import pygame, sys
import time
import pathlib

path = pathlib.Path(__file__).parent.resolve()

pygame.init()

# Settings
WHITE = (255, 255, 255)
screen = pygame.display.set_mode((1000, 720))
screen.fill(WHITE)
pygame.display.set_caption("Serik's paninis")

# pygame.mixer.music.load("assets\\mp3\\.mp3")
# pygame.mixer.music.play(-1)

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


def main_menu():
    bg = pygame.image.load("assets\\menu.png")
    play_button = pygame.image.load("assets\\buttons\\play button(new).png")
    sound_button = pygame.image.load("assets\\buttons\\sound button(new).png")
    quit_button = pygame.image.load("assets\\buttons\\quit button(new).png")
    play_rect = play_button.get_rect(center=(500, 430))
    quit_rect = quit_button.get_rect(center=(500, 560))


    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(bg, (0, 0))
        screen.blit(play_button, play_rect)
        screen.blit(quit_button, quit_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                    event.type == pygame.MOUSEBUTTONDOWN and quit_rect.collidepoint(event.pos)):
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and play_rect.collidepoint(event.pos):
                game_window()

        pygame.display.flip()
    pass


def setting_menu():
    pass


def game_window():
    wp = pygame.image.load("assets\\wp.png")
    cm = pygame.image.load("assets\\cm.png")
    grill_opened = pygame.image.load("assets\\Grill opened.png")
    grill_animation = [
        pygame.image.load("assets\\Grill opened.png"),
        pygame.image.load("assets\\Grill cooking.png"),
    ]
    grill_rect = grill_opened.get_rect(center=(850, 350))
    animation = 0
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(wp, (0, 0))
        screen.blit(grill_animation[animation], grill_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and grill_rect.collidepoint(event.pos):
                if animation == 0:
                    animation += 1
                else:
                    animation = 0


        pygame.display.flip()
    pass


if __name__ == '__main__':
    main_menu()
