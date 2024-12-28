import random

import wrap
wrap.add_sprite_dir("mysprite")
wrap.world.create_world(500,600)
grass=wrap.sprite.add("texstures",250,600,"grass")
pacman=wrap.sprite.add("pacman",150,50,"player2")



platform_grass=wrap.sprite.add("mario-items",250,557,"moving_platform2",False)
wrap.sprite.set_width(platform_grass,500)

wrap.sprite.set_size(grass,500,500)
cacoyto_list=[]
decorations=[grass]
cordinaty=[[220,300],[150,360],[290,230],[220,100],[280,0]]
speed=0


col=0
carta="""
____________________
__________xx________
_______*____________
______xx____________
"""
for i in carta:
    col=col+1
    if i=="x":
        pix=col*50
        cordinaty.append([pix,pix])


for i in cordinaty:
    platform = wrap.sprite.add("mario-items", i[0], i[1], "moving_platform2")
    cacoyto_list.append(platform)
@wrap.always()
def padenye(pos_x,pos_y,keys):
    global speed
    wrap.world.set_title(pos_y)


    wrap.sprite.move(pacman, 0, speed)
    speed = speed + 2

    if speed>=20:
        speed=20

    for i in cacoyto_list:
        check_platform(i,keys)
    move_pacman()
def check_platform(platform,keys):
    global speed
    top_platform = wrap.sprite.get_top(platform)
    bottom = wrap.sprite.get_bottom(pacman)
    if bottom>top_platform and wrap.sprite.is_collide_sprite(pacman,platform):
        wrap.sprite.move_bottom_to(pacman, top_platform)
        speed = -7
        if wrap.K_SPACE in keys:
            speed = -20
@wrap.on_key_always(wrap.K_LEFT,wrap.K_RIGHT)
def move(keys):
    global speed
    if wrap.K_LEFT in keys:
        wrap.sprite.move(pacman,-5,0)
    elif wrap.K_RIGHT in keys:
        wrap.sprite.move(pacman, 5, 0)


def move_camera(number_y,number_x):
    wrap.sprite.move(pacman,number_x,number_y)
    for i in cacoyto_list:
        wrap.sprite.move(i, number_x, number_y)
    for i in decorations:
        wrap.sprite.move(i, number_x, number_y)


def move_pacman():
    y=wrap.sprite.get_y(pacman)
    x=wrap.sprite.get_x(pacman)
    colpix_x=250-x
    colpix_y=300-y
    move_camera(colpix_y,colpix_x)
