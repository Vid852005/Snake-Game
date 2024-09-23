import pygame
import sys
import random
from pygame.math import Vector2

# Constants
CELL_SIZE = 40
CELL_NUMBER = 20
SCREEN_UPDATE=pygame.USEREVENT

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((CELL_NUMBER * CELL_SIZE, CELL_NUMBER * CELL_SIZE))
clock = pygame.time.Clock()

class Snake:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction=Vector2(1,0)
        self.new_block=False

    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x * CELL_SIZE)
            y_pos = int(block.y * CELL_SIZE)
            block_rect = pygame.Rect(x_pos, y_pos, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, (183, 111, 122), block_rect)
    
    def move_snake(self):
        if self.new_block==True:

            body_copy=self.body[:]
            body_copy.insert(0,body_copy[0]+self.direction)
            self.body=body_copy[:]
            self.new_block=False
        else:
            body_copy=self.body[:-1]
            body_copy.insert(0,body_copy[0]+self.direction)
            self.body=body_copy[:]


    
    def add_block(self):
        self.new_block =True





class Fruit:
    def __init__(self):
        self.randomize()
    
    def randomize(self):
         self.x = random.randint(0, CELL_NUMBER - 1)
         self.y = random.randint(0, CELL_NUMBER - 1)
         self.pos = Vector2(self.x, self.y)
        
    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * CELL_SIZE), int(self.pos.y * CELL_SIZE), CELL_SIZE, CELL_SIZE)
        screen.blit(apple,fruit_rect)
        #pygame.draw.rect(screen, (126, 166, 114), fruit_rect)

class MAIN:
    def __init__(self):
        self.snake=Snake()
        self.fruit=Fruit()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()

    def check_collision(self):
        if self.fruit.pos==self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
    
    def check_fail(self):
        if not 0 <=self.snake.body[0].x<=CELL_NUMBER or not 0 <=self.snake.body[0].y<=CELL_NUMBER:
            self.game_over()
        for block in self.snake.body[1:]:
            if block==self.snake.body[0]:
                self.game_over()
    
    def game_over(self):
        pygame.quit()
        sys.exit()

apple=pygame.image.load("tictactoe/apple_processed.png").convert_alpha()    
apple = pygame.transform.scale(apple, (CELL_SIZE , CELL_SIZE ))         

def main():
    running = True
    pygame.time.set_timer(SCREEN_UPDATE,150)
    main_game=MAIN()
    


    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type== SCREEN_UPDATE:
                main_game.update()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    if main_game.snake.direction.y!=1:
                        main_game.snake.direction=Vector2(0,-1)
                if event.key==pygame.K_DOWN:
                    if main_game.snake.direction.y!=-1:
                        main_game.snake.direction=Vector2(0,1)
                if event.key==pygame.K_LEFT:
                    if main_game.snake.direction.x!=1:
                        main_game.snake.direction=Vector2(-1,0)
                if event.key==pygame.K_RIGHT:
                    if main_game.snake.direction.x!=-1:
                        main_game.snake.direction=Vector2(1,0)
        
        screen.fill((175, 215, 70))
        main_game.draw_elements()
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()
