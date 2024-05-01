import pygame , sys , random
#========Setting==========
SCREEN_WIDTH = 720          #window's width
SCREEN_HEIGHT = 640         #window's height
DEFAULT_ARMY_SIZE = 15   #Each object's number
FPS = 120                    #Fuck PinkMustastche Sluts
CHẾ_ĐỘ_ẢO_LÒI = False       #No fill blank
choices = (-5,-4,-3,-2,1,1,2,3,4,5,)  #Set init speed possibilities
#========Setting==========
#Press R to restart simulation
class soldier():
    colliding = False
    def __init__(self,id,width_spawn,height_spawn,current_speed_x,current_speed_y):
        self.box = ROCK_IMAGE.get_rect()
        self.box.center = (width_spawn,height_spawn)
        self.current_speed_x = current_speed_x
        self.current_speed_y = current_speed_y

    def move(self):
        self.box.x += self.current_speed_x
        self.box.y += self.current_speed_y
        if self.box.top <= 0 or self.box.bottom >= SCREEN_HEIGHT:
            self.current_speed_y *= -1
        if self.box.left <= 0 or self.box.right >= SCREEN_WIDTH:
            self.current_speed_x *= -1

    def rect(self):
        return self.box
            
rocks = []
papers = []
scissors = []


pygame.init()
FONT = pygame.font.SysFont('Arial', 25)
clock = pygame.time.Clock()
won = False
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Rock-Paper-Scissors battle!')
ROCK_IMAGE = pygame.image.load('rock.png').convert_alpha()
PAPER_IMAGE = pygame.image.load('paper.png').convert_alpha()
SCISSORS_IMAGE = pygame.image.load('scissors.png').convert_alpha()

winner = pygame.Rect(SCREEN_WIDTH/2-50,SCREEN_HEIGHT/4-50,SCREEN_WIDTH/2+100,SCREEN_HEIGHT/4+50)

current_index_rock_to_paper = []
current_index_paper_to_scissors = []
current_index_scissors_to_rock = []
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                rocks = []
                papers = []
                scissors = []
                for i in range(DEFAULT_ARMY_SIZE):
                    width_spawn = random.randint(20,SCREEN_WIDTH/4)
                    height_spawn= random.randint(20,SCREEN_HEIGHT/2)
                    current_speed_x = random.choice(choices)
                    current_speed_y = random.choice(choices)
                    rocks.append(soldier('Rock',width_spawn,height_spawn,current_speed_x,current_speed_y))
                for i in range(DEFAULT_ARMY_SIZE):
                    width_spawn = random.randint(SCREEN_WIDTH/2+SCREEN_WIDTH/4,SCREEN_WIDTH-20)
                    height_spawn= random.randint(20,SCREEN_HEIGHT/2)
                    current_speed_x = random.choice(choices)
                    current_speed_y = random.choice(choices)
                    papers.append(soldier('Paper',width_spawn,height_spawn,current_speed_x,current_speed_y))
                for i in range(DEFAULT_ARMY_SIZE):
                    width_spawn = random.randint(SCREEN_WIDTH/2-SCREEN_WIDTH/4,SCREEN_WIDTH/2+SCREEN_WIDTH/4)
                    height_spawn= random.randint(SCREEN_HEIGHT/4+SCREEN_HEIGHT/2,SCREEN_HEIGHT-20)
                    current_speed_x = random.choice(choices)
                    current_speed_y = random.choice(choices)
                    scissors.append(soldier('Scissors',width_spawn,height_spawn,current_speed_x,current_speed_y))     
    if not CHẾ_ĐỘ_ẢO_LÒI:
        screen.fill((0,0,0))

    for j, i in enumerate(rocks):
        i.move()
        screen.blit(ROCK_IMAGE, i.box)
        collide_with_paper = i.box.collidelistall(papers)
        if collide_with_paper:
            current_index_rock_to_paper.append(j)
    if len(current_index_rock_to_paper) != 0:
        for i in current_index_rock_to_paper:
            try:
                papers.append(rocks[i])
                rocks.pop(i)
            except:
                pass
    current_index_rock_to_paper = []

    for j,i in enumerate(papers):
        i.move()
        screen.blit(PAPER_IMAGE, i.box)
        collide_with_scissors = i.box.collidelistall(scissors)
        if collide_with_scissors:
            current_index_paper_to_scissors.append(j)
    if len(current_index_paper_to_scissors) != 0:
        for i in current_index_paper_to_scissors:
            try:
                scissors.append(papers[i])
                papers.pop(i)
            except:
                pass 
    current_index_paper_to_scissors = []      

    for j, i in enumerate(scissors):
        i.move()
        screen.blit(SCISSORS_IMAGE, i.box)
        collide_with_rocks = i.box.collidelistall(rocks)
        if collide_with_rocks:
            current_index_scissors_to_rock.append(j)
    if len(current_index_scissors_to_rock) != 0:
        for i in current_index_scissors_to_rock:
            try:
                rocks.append(scissors[i])
                scissors.pop(i)
            except:
                pass 
    current_index_scissors_to_rock = []
    
    if len(scissors) == 0 and len(papers) == 0:
        screen.blit(FONT.render('ROCKS WIN', True, (255,0,0)), (200, 100))
    if len(rocks) == 0 and len(papers) == 0:
        screen.blit(FONT.render('SCISSORS WIN', True, (255,0,0)), (200, 100))
    if len(scissors) == 0 and len(rocks) ==0:
        screen.blit(FONT.render('PAPERS WIN', True, (255,0,0)), (200, 100))

    pygame.display.flip()
    clock.tick(FPS)
