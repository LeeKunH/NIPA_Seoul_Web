import pygame
import os
import random
from constants import * # 전역상수 코드 따로 정의 후 불러와 사용.

class Dinosaur() :
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5 # 공룡 점프 시 높이

    def __init__(self) -> None:
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING
        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False
        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

    def update(self, userInput) :
        if self.dino_duck :
            self.duck()
        if self.dino_run :
            self.run()
        if self.dino_jump :
            self.jump()

        if self.step_index >= 10 :
            self.step_index = 0

        if userInput[pygame.K_UP] and not self.dino_jump :
            self.dino_duck = False
            self.dino_jump = True
            self.dino_run = False
        elif userInput[pygame.K_DOWN] and not self.dino_jump :
            self.dino_duck = True
            self.dino_jump = False
            self.dino_run = False
        elif not (self.dino_jump or userInput[pygame.K_DOWN]) :
            self.dino_duck = False
            self.dino_jump = False
            self.dino_run = True

    def duck(self) :
        self.image = self.duck_img[self.step_index//5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK # run 달라 좌표점
        self.step_index += 1

    def run(self) :
        self.image = self.run_img[self.step_index//5]
        self.step_index += 1 # 1씩 증가 -> 10이 되는순간 값 초기화
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1 # 1씩 증가 -> 10이 되는순간 값 초기화

    def jump(self) :
        self.image = self.jump_img

        if self.dino_jump :
            self.dino_rect.y = self.dino_rect.y - self.jump_vel * 4
            self.jump_vel = self.jump_vel - 0.8

        if self.jump_vel < -self.JUMP_VEL :
            self.dino_jump = False # 점프가 끝난 상황
            self.jump_vel = self.JUMP_VEL # 다시 처음값으로 초기화 // 왜? 점프는 언제든 다시 가능

    def draw(self, SCREEN) :
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

class Cloud() :
    def __init__(self) -> None:
        self.x = SCREEN_WIDTH + random.randint(300, 500)
        self.y = random.randint(50, 100)
        self.image = CL
        self.width = self.image.get_width()

    def update(self) :
        self.x -= game_speed

        if (self.x < - self.width ) :
            self.x = SCREEN_WIDTH + random.randint(1300, 2000)
            self.y = random.randint(50, 100)

    def draw(self, SCREEN ) :
        SCREEN.blit(self.image, (self.x, self.y))

class Obstacle :
    def __init__(self, image, type) -> None:
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self) :
        self.rect.x -= game_speed

        if self.rect.x < - self.rect.width :
            obstacles.pop()

    def draw(self, SCREEN) :
        SCREEN.blit(self.image[self.type], self.rect)

class SmallCactus(Obstacle) :
    def __init__(self, image) -> None:
        self.type = random.randint(0,2)
        super().__init__(image, self.type)
        self.rect.y = 325

class LargeCactus(Obstacle) :
    def __init__(self, image ) -> None:
        self.type = random.randint(0,2)
        super().__init__(image, self.type)
        self.rect.y = 300

class Bird(Obstacle) :
    def __init__(self, image) -> None:
        self.type = 0
        self.index = 0
        super().__init__(image, self.type)
        self.rect.y = 250

    def draw(self, SCREEN):
        if self.index >= 9 : # 0 1 2 3 ~ 7 8 9되는 순간 초기화
            self.index = 0

        SCREEN.blit(self.image[self.index//5], self.rect)
        self.index += 1

def main() :
    global game_speed
    global x_pos_bg, y_pos_bg
    global points
    global obstacles

    run = True
    clock = pygame.time.Clock()
    cloud = Cloud()
    player = Dinosaur()
    game_speed = 14
    x_pos_bg = 0
    y_pos_bg = 380
    points = 0
    font = pygame.font.Font('freesansbold.ttf', 20)
    # font = pygame.font.Font(None, 20)
    obstacles = []
    death_count = 0

    def score() :
        global points, game_speed
        points += 1

        if points % 100 == 0 :
            game_speed += 1

        text = font.render(f"points : {str(points)}", True, (0,0,0))
        textRect = text.get_rect()
        textRect.center = (1000,40)
        SCREEN.blit(text, textRect)

    def background() :
        global x_pos_bg, y_pos_bg

        image_width = BG.get_width() # 대략 2404
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))

        if x_pos_bg <= - image_width :
            SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed

    while run :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                run = False

        SCREEN.fill((255, 255, 255))
        userInput = pygame.key.get_pressed()
        player.draw(SCREEN)
        player.update(userInput)

        if len(obstacles) == 0 :
            if random.randint(0, 2) == 0 :
                obstacles.append(SmallCactus(SMALL_CACTUS))
            elif random.randint(0, 2) == 1 :
                obstacles.append(LargeCactus(LARGE_CACTUS))
            elif random.randint(0, 2) == 2 :
                obstacles.append(Bird(BIRD))

        for obstacle in obstacles : # 리스트 요소 반복
            obstacle.draw(SCREEN) # 화면에 장애물 출력
            obstacle.update() # 부모 클래스 업데이트 메서드 호출 - 객체 이동하는 모습을 위해

            if player.dino_rect.colliderect(obstacle.rect) :
                pygame.time.delay(2000)
                death_count += 1
                menu(death_count)

        background()
        cloud.draw(SCREEN)
        cloud.update()
        score()
        clock.tick(30)
        pygame.display.update()

def menu(death_count) :
    global points

    run = True
    while run :
        SCREEN.fill((255,255,255))
        font = pygame.font.Font('freesansbold.ttf', 30)

        if death_count == 0 :
            text = font.render("Press any Key to Start!", True, (0,0,0))
            SCREEN.blit(START, (SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2 - 140)) # 코드 추가
        elif death_count > 0 :
            text = font.render("Press any Key to Start!", True, (0,0,0))
            score = font.render("Your Score :  " + str(points), True, (0,0,0)) # 죽었을 때 점수를 출력
            scoreRect = score.get_rect() # 위치 파악을 위한 사각형 값 할당
            scoreRect.center = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 50) # 점수판 위치 설정
            SCREEN.blit(score, scoreRect)
            SCREEN.blit(DEAD, (SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2 - 140)) # 코드추가
            SCREEN.blit(GAMEOVER, (SCREEN_WIDTH // 2 - 160 , SCREEN_HEIGHT // 2 - 200)) # 코드추가

        textRect = text.get_rect() # 메뉴에 출력될 텍스트 위치 설정을 위함
        textRect.center = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2)# get_rect() 메서드 호출 후 반환값이 클래스 인스턴스고 그 안에 center 변수가 정의되어 있음
        SCREEN.blit(text, textRect)
        SCREEN.blit(RUNNING[0], (SCREEN_WIDTH//2 - 20 , SCREEN_HEIGHT//2 - 140)) # 화면에 위치 지정 후 객체_요소 출력
        pygame.display.update()

        for event in pygame.event.get() :
            if event.type == pygame.QUIT : # 의미 : 사용자가 게임 스크린 x 버튼을 누른다면....
                run = False
            if event.type == pygame.KEYDOWN : # 사용자가 아무런 키를 누르면 main 함수가 다시 실행되도록 작성
                main() # main 함수가 호출되면 > 게임 실행


if __name__ == "__main__":
    menu(death_count=0)