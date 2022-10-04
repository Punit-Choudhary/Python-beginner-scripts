import pygame
import ice

pygame.init()


infoObject = pygame.display.Info()
screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))

screen_x, screen_y = screen.get_size()

pygame.display.set_caption('Ice3D Use WASD to turn cube')

screen.fill("white")


cube = ice.Cube((screen_x/2,screen_y/2),50)


def main():
  clock = pygame.time.Clock()
  
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        return
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a]:
      cube.rotate(0,-3,0)
    if keys[pygame.K_d]:
      cube.rotate(0,3,0)
    if keys[pygame.K_w]:
      cube.rotate(3,0,0)
    if keys[pygame.K_s]:
      cube.rotate(-3,0,0)
    '''if keys[pygame.K_LEFT]: # movement is kinda lame rn lmao
      cube.move(-3,0)
    if keys[pygame.K_RIGHT]:
      cube.move(3,0)
    if keys[pygame.K_UP]:
      cube.move(0,-3)
    if keys[pygame.K_DOWN]:
      cube.move(0,3)'''
    
    screen.fill("white")
    
    cube.render(screen)
    
    clock.tick(30)
    pygame.display.update()


main()
