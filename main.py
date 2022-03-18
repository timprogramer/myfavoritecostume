"""
На стрелки вправо-влево марио ходит по низу экрана.
При смене направления меняет костюм на подходящий.
"""
import wrap,time
wrap.world.create_world(600,500,200,500)
wrap.world.set_back_color(154, 255, 255)
mario=wrap.sprite.add("mario-1-big",300,250,"stand")

@wrap.on_key_always(wrap.K_RIGHT)
def right():
    #if wrap.sprite.get_angle(mario)==180:
    #wrap.sprite.set_angle(mario,0)
   # wrap.sprite.set_reverse_y(mario,False)
    if wrap.sprite.get_reverse_y(mario)==True:
        wrap.sprite.set_reverse_y(mario,False)
    wrap.sprite.set_reverse_x(mario,False)
    wrap.sprite.move(mario,10,0)
    wrap.sprite.set_costume(mario,"walk1")

@wrap.on_key_always(wrap.K_LEFT)
def left():
    if wrap.sprite.get_reverse_y(mario)==True:
        wrap.sprite.set_reverse_y(mario,False)
    wrap.sprite.set_reverse_x(mario,True)
    wrap.sprite.move(mario, -10, 0)
    wrap.sprite.set_costume(mario, "walk1")

@wrap.on_key_always(wrap.K_UP)
def up():
    wrap.sprite.set_costume(mario,"swim3")
    wrap.sprite.set_reverse_y(mario,False)
    wrap.sprite.move(mario, 0, -10)

@wrap.on_key_always(wrap.K_DOWN)
def down():
    wrap.sprite.set_reverse_y(mario,True)
    wrap.sprite.move(mario, 0, 10)














































