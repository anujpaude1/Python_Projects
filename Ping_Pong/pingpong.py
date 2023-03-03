import pygame
import sys
keys={}
pygame.display.init()
screen_width=1920/2
screen_height=1080/2
player_speed=5
ball_speed_x=7
ball_speed_y=7

screen=pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Ping Pong")
ball=pygame.Rect(screen_width/2-15,screen_height/2-15,30,30)
player=pygame.Rect(screen_width-15,screen_height/2,15,120)
opponent=pygame.Rect(0,screen_height/2,15,120)
screen.fill((0,0,255))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit("Game is Quit")

    screen.fill((0,0,255))
    pygame.draw.ellipse(screen, (0,0,0), ball)
    pygame.draw.rect(screen, (0,0,0), player)
    pygame.draw.rect(screen, (0,0,0), opponent)

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        player.y -= player_speed
    elif keys[pygame.K_DOWN]:
        player.y += player_speed

    if keys[pygame.K_w]:
        opponent.y -= player_speed
    elif keys[pygame.K_s]:
        opponent.y += player_speed


    if ball.x<=0:
        sys.exit("Player 2 wins")
    if ball.x>=(screen_width-30):
        sys.exit("Player 1 wins")
    if ball.y<=0 or ball.y>=(screen_height-30):
        ball_speed_y=ball_speed_y*-1

    if player.y<=0:
        player.y=0
    if player.y>=(screen_height-120):
        player.y=screen_height-120

    if opponent.y<=0:
        opponent.y=0
    if opponent.y>=(screen_height-120):
        opponent.y=screen_height-120

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x=ball_speed_x*-1
    pygame.display.flip()
    pygame.time.Clock().tick(60)

