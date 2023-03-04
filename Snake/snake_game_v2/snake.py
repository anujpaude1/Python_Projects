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
score=0


active=pygame.K_UP

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
        active=pygame.K_UP

    elif keys[pygame.K_DOWN]:
        tempx=snake.bodyx[0]
        tempy=snake.bodyy[0]
        snake.bodyy[0]+=5
        snake.move(tempx,tempy)
        active=pygame.K_DOWN

    elif keys[pygame.K_LEFT]:
        tempx=snake.bodyx[0]
        tempy=snake.bodyy[0]
        snake.bodyx[0]-=5
        snake.move(tempx,tempy)
        active=pygame.K_LEFT

    elif keys[pygame.K_RIGHT]:
        tempx=snake.bodyx[0]
        tempy=snake.bodyy[0]
        snake.bodyx[0]+=5
        snake.move(tempx,tempy)
        active=pygame.K_RIGHT

    else:
        if active==pygame.K_UP:
            tempx=snake.bodyx[0]
            tempy=snake.bodyy[0]
            snake.bodyy[0]-=5
            snake.move(tempx,tempy)

        elif active==pygame.K_DOWN:
            tempx=snake.bodyx[0]
            tempy=snake.bodyy[0]
            snake.bodyy[0]+=5
            snake.move(tempx,tempy)


        elif active==pygame.K_LEFT:
            tempx=snake.bodyx[0]
            tempy=snake.bodyy[0]
            snake.bodyx[0]-=5
            snake.move(tempx,tempy)


        elif active==pygame.K_RIGHT:
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
        score=score+1
    else:
        food_spawn=False

    
    if body[0].x<=0:
        pygame.quit()
        sys.exit(print("Your score is ",score))
    
    if body[0].x>=screen_width:
        pygame.quit()
        sys.exit(print("Your score is ",score))

    if body[0].y>=screen_height:
        pygame.quit()
        sys.exit(print("Your score is ",score))

    if body[0].y<=0:
        pygame.quit()
        sys.exit(print("Your score is ",score))

    

    




    pygame.display.update()
    
    pygame.display.flip()
    pygame.time.Clock().tick(60)

    
    
            



        

    

    
    







