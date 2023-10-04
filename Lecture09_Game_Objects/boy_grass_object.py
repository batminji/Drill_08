from pico2d import *


# Game object class here

class Grass:
    def __init__(self):  # 생성자 함수
        self.image = load_image('grass.png')  # shift + enter : 바로 개행
        # self : 생성괸 객체를 가리키는 더미 변수

    def draw(self):  # 항상 첫번째 파라미터로 self를 넣어야 한다.
        self.image.draw(400, 30)

    def upodate(self):
        pass



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

    running = True
    grass = Grass()


def update_world():
    pass


def render_world():
    clear_canvas()
    grass.draw()
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
