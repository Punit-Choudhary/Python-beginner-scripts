import pygame
import random

width,height = 1200,600
size = 50
bombs = ((width//size)*(height//size))//7
win = pygame.display.set_mode((width,height+40))
pygame.display.set_caption("Minesweeper")
pygame.init()
font = pygame.font.Font(pygame.font.get_default_font(), int(size/1.5))
time_font = pygame.font.Font(pygame.font.get_default_font(), 36)

class Cell():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.n = 0
        self.revealed = False
        self.flag = False

    def setup(self,grid):
        if self.n == -1:
            return
        for i in range(-1,2):
            for j in range(-1,2):
                if (i,j) != (0,0) and x+i >= 0 and x+i < width//size and y+j >= 0 and y+j < height//size:
                    try:
                        if grid[self.x+i][self.y+j].n == -1:
                            self.n += 1
                    except:
                        pass

    def draw(self,win):
        if self.revealed:
            if self.n == -1:
                if self.flag:
                    pygame.draw.rect(win,(255,255,150),(self.x*size,self.y*size,size,size))
                    pygame.draw.line(win,(0,0,0), (self.x*size+size/5,self.y*size+size/5),(self.x*size+size/5,self.y*size+size/5*4),3)
                    pygame.draw.rect(win,(255,0,0),(self.x*size+size/5+2,self.y*size+size/5,size/2,size/3))
                else:
                    pygame.draw.rect(win,(255,0,0),(self.x*size,self.y*size,size,size))
                    pygame.draw.circle(win,(50,50,50),(self.x*size+size/2,self.y*size+size/2),size/4)
                    pygame.draw.circle(win,(0,0,0),(self.x*size+size/3,self.y*size+size/3),size/8)
            elif self.n > 0:
                pygame.draw.rect(win,(150,255,150),(self.x*size,self.y*size,size,size))
                if self.flag:
                    pygame.draw.line(win,(0,0,0),(self.x*size+size/5,self.y*size+size/5),(self.x*size+size/5*4,self.y*size+size/5*4),5)
                    pygame.draw.line(win,(0,0,0),(self.x*size+size/5,self.y*size+size/5*4),(self.x*size+size/5*4,self.y*size+size/5),5)
                else:
                    num = font.render(str(self.n), True, (70, 70, 70))
                    win.blit(num, (self.x*size+size/3,self.y*size+size/4))
            else:
                pygame.draw.rect(win,(0,150,0),(self.x*size,self.y*size,size,size))
        elif self.flag:
            pygame.draw.rect(win,(255,255,150),(self.x*size,self.y*size,size,size))
            pygame.draw.line(win,(0,0,0), (self.x*size+size/5,self.y*size+size/5),(self.x*size+size/5,self.y*size+size/5*4),3)
            pygame.draw.rect(win,(255,0,0),(self.x*size+size/5+2,self.y*size+size/5,size/2,size/3))
        else:
            pygame.draw.rect(win,(255,255,255),(self.x*size,self.y*size,size,size))
        
        pygame.draw.rect(win,(0,0,0),(self.x*size,self.y*size,size,size),2)

    def reveal(self,grid):
        self.revealed = True
        if self.n == -1:
            return False
        
        if self.n == 0:
            for i in range(-1,2):
                for j in range(-1,2):
                    if (i,j) != (0,0) and self.x+i >= 0 and self.x+i < width//size and self.y+j >= 0 and self.y+j < height//size:
                        try:
                            if grid[self.x+i][self.y+j].n != -1 and not grid[self.x+i][self.y+j].revealed and not grid[self.x+i][self.y+j].flag:
                                grid[self.x+i][self.y+j].reveal(grid)
                        except:
                            pass
        return True

grid = []
for x in range(width//size):
    grid.append([])
    for y in range(height//size):
        grid[x].append(Cell(x,y))

count = 0
while count < bombs:
    x = random.randint(0,width//size-1)
    y = random.randint(0,height//size-1)
    if grid[x][y].n == 0:
        count += 1
        grid[x][y].n = -1

for x in range(width//size):
    for y in range(height//size):
        grid[x][y].setup(grid)

timemins = 0
timesecs = 0
timecount = 0
clock = pygame.time.Clock()
count = 0
dead = False
run = True
finished = False
while run:
    if not finished and not dead:
        timecount += 1
    if timecount == 30:
        timecount = 0
        timesecs += 1
        if timesecs == 60:
            timesecs = 0
            timemins += 1

    clock.tick(30)


    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x = event.pos[0]//size
            y = event.pos[1]//size
            if y < len(grid[x]):
                if not grid[x][y].revealed:
                    if event.button == 1:
                        if grid[x][y].flag:
                            grid[x][y].flag = False
                            count -= 1
                        else:
                            count += 1
                            if not grid[x][y].reveal(grid):
                                dead = True
                                for x in range(width//size):
                                    for y in range(height//size):
                                        grid[x][y].reveal(grid)
                        
                    elif event.button == 3:
                        if grid[x][y].flag:
                            grid[x][y].flag =  False
                            count -= 1
                        else:
                            grid[x][y].flag = True
                            count += 1

        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                grid = []
                for x in range(width//size):
                    grid.append([])
                    for y in range(height//size):
                        grid[x].append(Cell(x,y))

                b = 0
                while b < bombs:
                    x = random.randint(0,width//size-1)
                    y = random.randint(0,height//size-1)
                    if grid[x][y].n == 0:
                        b += 1
                        grid[x][y].n = -1

                for x in range(width//size):
                    for y in range(height//size):
                        grid[x][y].setup(grid)

                dead = False

                
                finished = False
                timesecs = 0
                timecount = 0
                timemins = 0
    
    if count == (width//size)*(height//size):
        finished = True
        for x in range(width//size):
            for y in range(height//size):
                grid[x][y].reveal(grid)
        
    win.fill((255,255,255))

    for x in range(width//size):
        for y in range(height//size):
            grid[x][y].draw(win)

    if timesecs == 0:
        textsecs = "00"
    elif timesecs < 10:
        textsecs = "0" + str(timesecs)
    else:
        textsecs = str(timesecs)
    
    if timemins == 0:
        textmins = "00"
    elif timemins < 10:
        textmins = "0" + str(timemins)
    else:
        textmins = str(timemins)

    time = time_font.render(textmins + ":" + textsecs,True,(0,0,0))
    win.blit(time,(2,height+2))

    pygame.display.update()

pygame.quit()
exit()