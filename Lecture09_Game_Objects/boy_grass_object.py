from pico2d import *
import random


# Game object class here

class Grass:
    def __init__(self):  # 생성자 함수
        self.image = load_image('grass.png')  # shift + enter : 바로 개행
        # self : 생성괸 객체를 가리키는 더미 변수

    def draw(self):  # 항상 첫번째 파라미터로 self를 넣어야 한다.
        self.image.draw(400, 30)

    def update(self):

        pass


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(0, 750), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


class SmallBall:
    def __init__(self):
        self.x, self.y = random.randint(0, 800), 599
        self.speed = (random.randint(1,10))
        self.image = load_image('ball21x21.png')

    def update(self):
        self.y -= self.speed

    def draw(self):
        self.image.draw(0, 0, 21, 21, self.x, self.y)


class BigBall:
    def __init__(self):
        self.x, self.y = random.randint(0, 800), 599
        self.speed = (random.randint(1,10))
        self.image = load_image('ball41x41.png')

    def update(self):
        self.y -= self.speed

    def draw(self):
        self.image.draw(0, 0, 41, 41, self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def reset_world():
    global running
    global grass
    global team
    global world

    running = True
    world = []

    team = [Boy() for i in range(10)]
    world += team
    grass = Grass()
    world.append(grass)


def update_world():
    for o in world:
        o.update()


def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()


open_canvas()

# initialization code
reset_world()

# game main loop code
while running:
    handle_events()
    update_world()  # game logic
    render_world()  # draw game world
    delay(0.05)

# finalization code
close_canvas()
