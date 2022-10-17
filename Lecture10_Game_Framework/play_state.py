from pico2d import *
import game_framework
import item_state
import add_delete_state
import random
import logo_state
import title_state


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(0, 600), 90
        self.frame = 0
        self.dir = 1
        self.image = load_image('animation_sheet.png')
        self.item = 'BigBall'
        self.ball_image = load_image('ball21x21.png')
        self.big_ball_image = load_image('ball41x41.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir * 2
        if self.x > 800:
            self.x = 800
            self.dir = -1
        elif self.x < 0:
            self.x = 0
            self.dir = 1

    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        elif self.dir == -1:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        if self.item == 'BigBall':
            self.big_ball_image.draw(self.x + 10, self.y + 50)
        elif self.item == 'Ball':
            self.ball_image.draw(self.x + 10, self.y + 50)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.key == SDLK_i:
                game_framework.push_state(item_state)
            elif event.key == SDLK_b:
                game_framework.push_state(add_delete_state)


# boy_count = 2
# boys = ['boy2', 'boy3', 'boy4']
# boys = [Boy() for i in range(boy_count)]
boy = None
grass = None
# running = None

# 초기화
def enter():
    global boy, grass, running, boy_count
    boy = Boy()
    grass = Grass()
    # running = True


# 종료
def exit():
    global boy, grass
    del boy
    del grass


def update():
    # global boys, boy_count
    # for boy in boys:
    #     boy.update()
    # boys = [Boy() in range(boy_count+1)]
    boy.update()



def draw():
    clear_canvas()
    draw_world()
    update_canvas()


def draw_world():
    # global boys, boy_count
    grass.draw()
    # for boy in boys:
    #     boy.draw()
    boy.draw()


def pause():
    pass


def resume():
    pass


open_canvas()

enter()

# game main loop code


# finalization code
close_canvas()
