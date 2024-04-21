import pygame, sys
import time
import pathlib
import random
from pygame.locals import *
path = pathlib.Path(__file__).parent.resolve()

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000,720))
pygame.display.set_caption("Serik's panini")

WHITE = (255, 255, 255)
money_font_size = 28
working_day_lenght = 300
client_patience_max = 10
order_time = 5
working_day_start = 8 * 60
working_day_end = 18 * 60
hot_hours = [(10, 14), (17, 18)]
order_money = 40
hearts = 3

# pygame.mixer.music.load("assets\\mp3\\.mp3")
# pygame.mixer.music.play(-1)

play_button = pygame.image.load("assets/buttons/play_button.png")
quit_button = pygame.image.load("assets/buttons/quit_button.png")
bg = pygame.image.load("assets/menu.png")
wp = pygame.image.load("assets/workplace.png")

c1_images = [pygame.image.load(f"assets/customers/c1.{i}.png") for i in range(1,5)]
c2_images = [pygame.image.load(f"assets/customers/c2.{i}.png") for i in range(1,5)]
c3_images = [pygame.image.load(f"assets/customers/c3.{i}.png") for i in range(1,5)]
c4_images = [pygame.image.load(f"assets/customers/c4.{i}.png") for i in range(1,5)]


o1 = pygame.image.load("assets/stuff/paninicoffee.png")
o2 = pygame.image.load("assets/stuff/coffeedouble.png")
o3 = pygame.image.load("assets/stuff/paninidouble.png")
o4 = pygame.image.load("assets/stuff/panini.png")
o5 = pygame.image.load("assets/stuff/coffee.png")

grill_opened = pygame.image.load("assets/stuff/grill_opened.png")
grill_opened = pygame.transform.scale(grill_opened, (200, 150))
grill_cooking = pygame.image.load("assets/stuff/grill_cooking.png")
grill_cooking = pygame.transform.scale(grill_cooking, (200, 150))

cm = pygame.image.load("assets/stuff/cm.png")
cm = pygame.transform.scale(cm, (240, 250))

patience_images = [pygame.image.load(f"assets/patience/{i}.png") for i in range(1, client_patience_max + 1)]

grill_cooking_rect = grill_cooking.get_rect()
grill_opened_rect = grill_opened.get_rect()
cm_rect = cm.get_rect()

play_rect = play_button.get_rect()
quit_rect = quit_button.get_rect()

grill_cooking_rect.center = (820, 450)
grill_opened_rect.center = (820, 450)
cm_rect.center = (150, 450)
play_rect.center = (500, 440)
quit_rect.center = (500, 590)

font = pygame.font.Font(None, 36)
money_font = pygame.font.Font(None, money_font_size)

current_frame = 0
screen.blit(bg, (0,0))
screen.blit(play_button, play_rect)
screen.blit(quit_button, quit_rect)
pygame.display.flip()
character_index = 0
current_screen = 'main'

def characters_appearing():

    character_index = random.randint(1, 4)

money = 0
HEARTS = hearts
current_minute = working_day_start
is_working_day = True

hot_hours_in_minutes = [(start * 60, end * 60) for start, end in hot_hours]



class Clients(pygame.sprite.Sprite): 
    def __init__(self, images, happy_image, sad_image, pos_x, pos_y, character_index):
        super().__init__()
        self.images = images
        self.happy_image = pygame.image.load(f'c{character_index}.[2].png')
        self.sad_image = sad_image
        self.image_index = 0
        self.image = images[self.image_index]
        self.rect = self.image.get_rect(topbottom=(pos_x, pos_y))
        self.patience = client_patience_max
        self.patience_timer = pygame.time.get_ticks()
        self.is_happy = False
        self.is_sad = False
        self.has_ordered = False

    def update(self):
        self.image_index = (self.image_index + 1) % len(self.images)
        self.image = self.images[self.image_index]
        if self.leaving:
            self.move_out_of_screen()
        elif self.order_complete:
            self.image = self.happy_images[self.image_index % len(self.happy_images)]
        else:
            if self.patience <= 0:
                self.image = self.angry_images[self.image_index % len(self.angry_images)]
                self.leaving = True

    def decrease_patience(self):
        if not self.order_complete and not self.leaving:
            self.patience -= 1

    def move_out_of_screen(self):
        self.rect.x -= 5  

    def serve_order(self):
        self.order_complete = True

# class Order:

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.MOUSEBUTTONDOWN and quit_rect.collidepoint(event.pos)):
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if current_screen == 'main' and play_rect.collidepoint(event.pos):
                screen.blit(wp, (0, 0))
                pygame.display.flip()
                money = 0
                hearts = HEARTS
                # customers.clear()
                # orders.clear()
                current_minute = working_day_start
                current_screen = 'workplace'
                screen.blit(cm, cm_rect)
                screen.blit(grill_opened, grill_opened_rect)
                money_surface = money_font.render(f"Money: ${money}", True, (0, 0, 0))
                screen.blit(money_surface, (850, 10))
             
    # if current_minute >= working_day_end:
    #     check_end_of_day()
    # else:
    #     if current_minute % 60 == 0:  # Every minute, potentially generate a customer
    #         if any(start <= current_minute <= end for start, end in HOT_HOURS_IN_MINUTES):
    #             generate_customer()  # More likely to generate during hot hours
    #         handle_orders()
    #     current_minute += 1
                

    pygame.display.flip()
    pygame.time.Clock().tick(60)
   
pygame.quit()
sys.exit()