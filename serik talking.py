import pygame
import sys


pygame.init()


screen = pygame.display.set_mode((1000, 720))


bg = pygame.image.load('assets/kbtu front.png')
closed_mouth = pygame.image.load('assets/serik 1.png')
open_mouth = pygame.image.load('assets/serik 2.png')
ram = pygame.image.load('assets/text frame.png')

font = pygame.font.Font(None, 16)
text = font.render('Im Serik, I have always been a wizard with a coffee machine and a panini grill. When I stumbled upon a job ad for someone to master the art of', True, (0,0,0))
text_lower1 = font.render('heating paninis and brewing coffee at the KBTU cafeteria, I couldnt resist. After a chat with the manager—who seemed quite impressed', True,(0,0,0))
text_lower2 = font.render('with my panini flipping flair—I landed the job. Now, I serve up steaming hot paninis and cups of coffee with a side of charm, proving every day', True, (0,0,0))
text_lower3 = font.render('that even reheating deserves a round of applause!',True, (0,0,0))

pygame.display.set_caption("Talking Animation")


clock = pygame.time.Clock()
fps = 60  

current_image = closed_mouth
toggle_time = 700 
last_switch = pygame.time.get_ticks()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    now = pygame.time.get_ticks()
    
    if now - last_switch > toggle_time:
        last_switch = now
        current_image = open_mouth if current_image == closed_mouth else closed_mouth

    screen.fill((255, 255, 255))  
    
    screen.blit(bg, (0, 0)) 
    screen.blit(current_image, (800, 200))  
    screen.blit(ram, (0, 0))
    screen.blit(text,(115,605))
    screen.blit(text_lower1,(115,620))
    screen.blit(text_lower2,(115,635))
    screen.blit(text_lower3,(115,650))
    pygame.display.flip()  
    
    
    clock.tick(fps)

pygame.quit()
sys.exit()
