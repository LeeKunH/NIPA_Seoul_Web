import pygame
import os

# 게임 초기화 진행
# 게임 스크린 제목
# 게임 초기 설정값
pygame.init()

# 게임 화면을 위한 변수 정의
SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
icon = pygame.image.load(os.path.join("self_ChromeDinoGame\\Assets\\Dino","DinoStart.png"))
pygame.display.set_caption('크롬 공룡 게임-미니프로젝트@@@')
pygame.display.set_icon(icon)


# 게임 캐릭터 객체_동작 변수 정의
RUNNING = [pygame.image.load(os.path.join("self_ChromeDinoGame\\Assets\\Dino","DinoRun1.png")), pygame.image.load(os.path.join("self_ChromeDinoGame\\Assets\\Dino","DinoRun2.png")) ]

JUMPING = pygame.image.load(os.path.join("self_ChromeDinoGame\\Assets\\Dino","DinoJump.png"))

DUCKING = [pygame.image.load(os.path.join("self_ChromeDinoGame\\Assets\\Dino","DinoDuck1.png")), pygame.image.load(os.path.join("self_ChromeDinoGame\\Assets\\Dino","DinoDuck2.png")) ]

START = pygame.image.load(os.path.join("self_ChromeDinoGame\\Assets\\Dino","DinoStart.png"))

DEAD = pygame.image.load(os.path.join("self_ChromeDinoGame\\Assets\\Dino","DinoDead.png"))

GAMEOVER = pygame.image.load(os.path.join("self_ChromeDinoGame\\Assets\\Other","GameOver.png"))



# 게임 속 장애물 객체 변수 정의
SMALL_CACTUS = [pygame.image.load(os.path.join("self_ChromeDinoGame\\Assets\\Cactus","SmallCactus1.png")),
                pygame.image.load(os.path.join("self_ChromeDinoGame\\Assets\\Cactus","SmallCactus2.png")),
                pygame.image.load(os.path.join("self_ChromeDinoGame\\Assets\\Cactus","SmallCactus3.png"))]

LARGE_CACTUS = [pygame.image.load(os.path.join("self_ChromeDinoGame\\Assets\\Cactus","LargeCactus1.png")),
                pygame.image.load(os.path.join("self_ChromeDinoGame\\Assets\\Cactus","LargeCactus2.png")),
                pygame.image.load(os.path.join("self_ChromeDinoGame\\Assets\\Cactus","LargeCactus3.png"))]

BIRD = [pygame.image.load(os.path.join("self_ChromeDinoGame\\Assets\\Bird","Bird1.png")),
        pygame.image.load(os.path.join("self_ChromeDinoGame\\Assets\\Bird","Bird2.png"))]

# 배경 요소_변수 정의
CL = pygame.image.load(os.path.join("self_ChromeDinoGame\\Assets\\Other", "Cloud.png"))
BG = pygame.image.load(os.path.join("self_ChromeDinoGame\\Assets\\Other", "Track.png"))