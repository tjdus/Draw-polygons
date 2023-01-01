import pygame
import numpy as np

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (255, 200, 180)

def RandomColor():
    r= np.random.randint(256)%256
    g= np.random.randint(256)%256
    b= np.random.randint(256)%256
    return (r,g,b)


class Polygon():
    def __init__(self, n, position):
        self.n= n
        self.deg = 180 * (n-2)
        self.position = pygame.Vector2(position)
        self.rotation = 0
        self.rotate_speed = np.random.choice([-3,-2,-1,1,2,3])
        self.radius = np.random.randint(10,100)
        self.color= RandomColor()
        vertices = []
        for i in range(n):
            degree = i * 360.0 / n
            radian = degree * np.pi / 180
            c = np.cos(radian)
            s = np.sin(radian)
            x = self.radius * c
            y = self.radius * s
            vertices.append([x,y]) 
        self.vertices = np.array(vertices)
        self.base = self.vertices
        
    def update(self):
        self.rotation += self.rotate_speed
        self.rotate()
        self.translate()
        
    def rotate(self):
        radian = np.deg2rad(self.rotation)
        c = np.cos(radian)
        s = np.sin(radian)
        Rr = np.array([[c, -s], [s, c]])
        new_vertices = Rr @ self.base.T
        self.vertices =  new_vertices.T 
            
    def translate(self):
        self.vertices +=self.position
        
    def drawLines(self):
        for i in range(self.n):
            pygame.draw.line(screen, self.color, self.vertices[i%self.n], \
                            self.vertices[(i+1)%self.n], 4)
    
    def fill(self):   
        pygame.draw.polygon(screen, self.color, self.vertices)
        
    def drawStar(self):
        for i in range(self.n):
            pygame.draw.line(screen, self.color, self.vertices[i%self.n], \
                            self.vertices[(i+2)%self.n], 4)



pygame.init()
pygame.display.set_caption("Drawing Polygons")

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

clock = pygame.time.Clock()

square = Polygon(4, (50,100))
triangle = Polygon(3, (200,200))
pentagon = Polygon(5, (200,300))
hexagon = Polygon(6, (400, 200))

polygons=[]
polygons.append(square)
polygons.append(triangle)
polygons.append(hexagon)

for i in range(10):
    n= np.random.randint(3, 13)
    x = np.random.randint(WINDOW_WIDTH)
    y = np.random.randint(WINDOW_HEIGHT)
    polygons.append(Polygon(n, (x,y)))

stars= []
for i in range(10):
    n= np.random.randint(5, 13)
    x = np.random.randint(WINDOW_WIDTH)
    y = np.random.randint(WINDOW_HEIGHT)
    stars.append(Polygon(n, (x,y)))
    


done=False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            


    screen.fill(WHITE)       

    for i in polygons:
        i.update()
        i.drawLines()
        i.fill()
    
    for i in stars:
        i.update()
        i.drawStar()
    
    pentagon.update()
    pentagon.drawStar()
    
    pygame.display.flip()
    clock.tick(60)


pygame.quit()



