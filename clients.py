import pygame
import sys
import random
import time

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 720
WHITE = (255, 255, 255)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Serik's Paninis")
FPS = 60  

FONT = pygame.font.Font(None, 36)

bg = pygame.image.load("assets/wp3.png")

client_images = {
    'c1': [pygame.image.load(f"assets/customers/c1.{i}.png") for i in range(1, 5)],
    'c2': [pygame.image.load(f"assets/customers/c2.{i}.png") for i in range(1, 5)],
    'c3': [pygame.image.load(f"assets/customers/c3.{i}.png") for i in range(1, 5)],
    'c4': [pygame.image.load(f"assets/customers/c4.{i}.png") for i in range(1, 5)]
}

patience_bars = [pygame.image.load(f"assets/patience/{i}.png") for i in range(1, 11)]

clients = []
last_spawn_time = 0
spawn_delay = random.randint(4000, 8000)  

clock = pygame.time.Clock()
start_time = time.time() * 1000  

def find_first_available_position():
    if not clients:
        return 50  

    
    sorted_clients = sorted(clients, key=lambda x: x['stop_x'])
    last_position = 50  

    
    for client in sorted_clients:
        if client['stop_x'] - (last_position + 50) >= 150:  
            return last_position + 150  
        last_position = client['stop_x'] + 50  

    
    if SCREEN_WIDTH - (last_position + 50) >= 50:
        return last_position + 50 + 30  

    return None 

def spawn_client():
    
    active_clients = [client for client in clients if client['state'] != 'leaving']
    if len(active_clients) < 4:  
        stop_x = find_first_available_position()
        if stop_x is not None:
            client_type = random.choice(list(client_images.keys()))
            images = client_images[client_type]
            image_height = images[0].get_height()
            image_width = images[0].get_width()

            new_x_position = stop_x

            new_client = {
                'images': images,
                'current_image_index': 0,  
                'last_image_switch': pygame.time.get_ticks(),
                'x': SCREEN_WIDTH,  
                'stop_x': new_x_position,
                'y': 450 - image_height,  
                'type': client_type,
                'patience': 10,  
                'last_update_time': pygame.time.get_ticks(),
                'state': 'walking'
            }
            clients.append(new_client)
            return True
    return False

    if len(clients) < 4:  
        stop_x = find_first_available_position()
        client_type = random.choice(list(client_images.keys()))
        images = client_images[client_type]
        image_height = images[0].get_height()
        image_width = images[0].get_width()

        if clients:
            last_client = clients[-1]
            new_x_position = last_client['stop_x'] + last_client['images'][0].get_width() + 30
        else:
            new_x_position = 50  

        new_client = {
            'images': images,
            'current_image_index': 0,  
            'last_image_switch': pygame.time.get_ticks(),
            'x': SCREEN_WIDTH,  
            'stop_x': new_x_position,
            'y': 450 - image_height,  
            'type': client_type,
            'patience': 10,  
            'last_update_time': pygame.time.get_ticks(),
            'state': 'walking'  
        }
        clients.append(new_client)
        return True  
    return False  


to_remove = []
def update_clients():
    current_ticks = pygame.time.get_ticks()
    for i in range(len(clients) - 1, -1, -1):  
        client = clients[i]
        if client['state'] == 'walking':
            if current_ticks - client['last_image_switch'] >= 500:  
                client['current_image_index'] = (client['current_image_index'] + 1) % 2  
                client['last_image_switch'] = current_ticks
            if client['x'] > client['stop_x']:  
                client['x'] -= 2  
            else:
                client['state'] = 'waiting'  
        if client['state'] == 'waiting':
            if current_ticks - client['last_update_time'] >= 1000: 
                client['patience'] -= 1
                client['last_update_time'] = current_ticks
                if client['patience'] > 0:
                    client['patience_image'] = patience_bars[client['patience'] - 1]
                else:
                    client['state'] = 'leaving'
        elif client['state'] == 'leaving':
            client['x'] += 4  
            if client['x'] + client['images'][0].get_width() < 0:  
                clients.pop(i)

    
    for client in to_remove:
        clients.remove(client)

def draw_clients():
    for client in clients:
        image = client['images'][client['current_image_index']]
        screen.blit(image, (client['x'], client['y']))
        if client['state'] == 'waiting':
           
            bar_x = client['x'] + client['images'][0].get_width() + 5
            bar_y = client['y'] + client['images'][0].get_height() // 2 - patience_bars[0].get_height() // 2
            screen.blit(client['patience_image'], (bar_x, bar_y))

def display_time(current_time):
    game_minutes = (current_time - start_time) / 10000  
    game_hour = 8 + int(game_minutes // 60) % 10
    game_minute = int(game_minutes % 60)
    time_text = f"{game_hour:02}:{game_minute:02}"
    time_surf = FONT.render(time_text, True, (0, 0, 0))
    screen.blit(time_surf, (50, 50))


running = True
while running:
    current_time = time.time() * 1000  
    game_minutes = (current_time - start_time) / 10000  
    game_hour = 8 + int(game_minutes // 60) % 10  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pass  

    
    active_clients = [client for client in clients if client['state'] != 'leaving']
    if game_hour in range(8, 18) and (current_time - last_spawn_time > spawn_delay) and len(active_clients) < 4:
        if spawn_client():
            last_spawn_time = current_time
            spawn_delay = random.randint(2000, 4000) 

    update_clients()
    screen.fill(WHITE)
    screen.blit(bg, (0, 0))
    draw_clients()
    display_time(current_time)
    pygame.display.flip()
    clock.tick(FPS)


pygame.quit()
sys.exit()