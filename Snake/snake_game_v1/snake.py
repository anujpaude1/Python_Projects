import pygame
import random
import sys
from csnake import Snake


pygame.display.init()
screen_width=960
screen_height=540
screen=pygame.display.set_mode([screen_width,screen_height])
pygame.display.set_caption("Snake")
food_spawn=True
snake=Snake(screen_width,screen_height)



while True:
    body=[]
    screen.fill((255, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit("Game Is QUIT")
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        tempx=snake.bodyx[0]
        tempy=snake.bodyy[0]
        snake.bodyy[0]-=5
        snake.move(tempx,tempy)

    if keys[pygame.K_DOWN]:
        tempx=snake.bodyx[0]
        tempy=snake.bodyy[0]
        snake.bodyy[0]+=5
        snake.move(tempx,tempy)

    if keys[pygame.K_LEFT]:
        tempx=snake.bodyx[0]
        tempy=snake.bodyy[0]
        snake.bodyx[0]-=5
        snake.move(tempx,tempy)

    if keys[pygame.K_RIGHT]:
        tempx=snake.bodyx[0]
        tempy=snake.bodyy[0]
        snake.bodyx[0]+=5
        snake.move(tempx,tempy)
    
 
    


    for i in range(len(snake.bodyx)):
        body_rect = pygame.Rect(snake.bodyx[i],snake.bodyy[i],20,20)
        body.append(body_rect)

    for i in range(len(body)):
        pygame.draw.rect(screen, (255, 255, 255), body[i])

    if food_spawn==True:
        food_location=snake.food()
        
    food=pygame.Rect(food_location[0],food_location[1],20,20)
    pygame.draw.ellipse(screen,(0,0,0),food)
    
    if food.colliderect(body[0]):
        food_spawn=True
        snake.add()
    else:
        food_spawn=False
    print(body)
    print(snake.bodyx,snake.bodyy)
    pygame.display.update()
    
    pygame.display.flip()
    pygame.time.Clock().tick(60)

    
    
            



        

    

    
    







