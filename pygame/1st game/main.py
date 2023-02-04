import pygame
import os
pygame.font.init()
pygame.mixer.init()
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("SPACE ZEN SHOOTER")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

BORDER = pygame.Rect(WIDTH//2 , 0, 10, HEIGHT)

BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('pygames', '1st game', 'Assets','Gun+Silencer.mp3' ))
BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('pygames', '1st game', 'Assets', 'Grenade+1.mp3'))

HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 40)

FPS = 60
Vel = 5
BULLET_Vel = 7
max_bullets = 5
SPACESHIP_WIDTH , SPACESHIP_HEIGHT = 55 ,40

y_hit = pygame.USEREVENT + 1
r_hit = pygame.USEREVENT + 2

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('pygames', '1st game', 'Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH , SPACESHIP_HEIGHT )), 90)

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('pygames', '1st game', 'Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH , SPACESHIP_HEIGHT )), 270)

SPACE = pygame.transform.scale(pygame.image.load(os.path.join('pygames', '1st game','Assets', 'space.png')), (WIDTH,HEIGHT))

def draw_window(red , yellow, r_bullets, y_bullets, r_health, y_health):
    WIN.blit(SPACE,(0, 0))
    pygame.draw.rect(WIN, BLACK, BORDER)
    
    r_health_text = HEALTH_FONT.render("Health: " + str(r_health), 1, WHITE)
    y_health_text = HEALTH_FONT.render("Health: " + str(y_health), 1, WHITE)
    WIN.blit(r_health_text, (WIDTH - r_health_text.get_width() - 10, 10))
    WIN.blit(y_health_text, (10, 10))

    WIN.blit(YELLOW_SPACESHIP, (yellow.x , yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x , red.y))



    for bullet in r_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    for bullet in y_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)

    pygame.display.update()

def yellow_handle_movement(keys_pressed, yellow):
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_a] and yellow.x - Vel > 0: #left
            yellow.x -= Vel
    if keys_pressed[pygame.K_d] and yellow.x + Vel + yellow.width < BORDER.x + BORDER.width: #right
            yellow.x += Vel
    if keys_pressed[pygame.K_w] and yellow.y - Vel > 0: #up
            yellow.y -= Vel
    if keys_pressed[pygame.K_s] and yellow.y + Vel + yellow.height < HEIGHT - 15: #down
            yellow.y += Vel

def red_handle_movement(keys_pressedd, red):
    keys_pressedd = pygame.key.get_pressed()
    if keys_pressedd[pygame.K_UP] and red.y - Vel > 0: #up
        red.y -= Vel
    if keys_pressedd[pygame.K_DOWN] and red.y + Vel + red.height < HEIGHT - 15: #down
        red.y += Vel
    if keys_pressedd[pygame.K_LEFT] and red.x - Vel > BORDER.x + BORDER.width: #left
        red.x -= Vel
    if keys_pressedd[pygame.K_RIGHT] and red.x + Vel + red.width < WIDTH: #right
        red.x += Vel

def handle_bullets(y_bullets, r_bullets, yellow, red):
    for bullet in y_bullets:
        bullet.x += BULLET_Vel
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(r_hit))
            y_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            y_bullets.remove(bullet)

    for bullet in r_bullets:
        bullet.x -= BULLET_Vel
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(y_hit))
            r_bullets.remove(bullet)
        elif bullet.x < 0:
            r_bullets.remove(bullet)

def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width() /2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

def main():
    red = pygame.Rect(700, 200, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(200, 200, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    y_bullets = []
    r_bullets = []

    r_health = 10
    y_health = 10

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and len(y_bullets) < max_bullets:
                        bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)
                        y_bullets.append(bullet)
                        BULLET_FIRE_SOUND.play()

                if event.key == pygame.K_RCTRL and len(r_bullets) < max_bullets:
                        bullet = pygame.Rect(red.x, red.y + red.height//2 - 2, 10, 5)
                        r_bullets.append(bullet)
                        BULLET_FIRE_SOUND.play()

            if event.type == r_hit:
                r_health -= 1
                BULLET_HIT_SOUND.play()

            if event.type == y_hit:
                y_health -= 1
                BULLET_HIT_SOUND.play()

        winner_text = ""
        if r_health <= 0:
            winner_text = "Yellow wins!!!!"

        if y_health <= 0:
            winner_text = "Red wins!!!!"

        if winner_text != "":
            draw_winner(winner_text)
            break

        print(r_bullets, y_bullets)
        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)

        keys_pressed = pygame.key.get_pressed()
        red_handle_movement(keys_pressed, red)
        ##red.x += 1    some auto stuff
        ##yellow.x -= 1

        handle_bullets(y_bullets, r_bullets, yellow, red)
        draw_window(red ,yellow, r_bullets, y_bullets, r_health, y_health)


    main()

if __name__== "__main__":
    main()