import random

import wrap


def carta():
    global pacman, grass,grass1, sum

    cordinaty = []
    pix_y=0
    col=0
    line=0
    carta="""_______x____________
____________________
___________x________
____________________
______x_____________
____________________
________x___________
____________________
_x___x______________
__x_________________
__0_________________
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
____________________"""
    for i in carta:

        if i=="x":
            pix_x=col*50
            cordinaty.append([pix_x,pix_y])

        if i == "0":
            pix_x = col * 50
            pacman_x=pix_x
            pacman_y=pix_y

        col = col + 1

        if i == "\n":
            line = line + 1
            col=0
            pix_y = line * 50
    print(pix_y)


    width=random.randint(10,250)
    grass = wrap.sprite.add("texstures", 250, 500, "forest")
    wrap.sprite.set_size(grass,width , 500)
    wrap.sprite.move_bottom_to(grass, pix_y)
    decorations.append(grass)
    sum=width

    while sum<750:
        width1 = random.randint(10, 250)
        grass1 = wrap.sprite.add("texstures", 250, 500, "forest")
        decorations.append(grass1)
        wrap.sprite.set_size(grass1,width1, 500)
        right = wrap.sprite.get_right(grass)
        wrap.sprite.move_bottom_to(grass1, pix_y)
        wrap.sprite.move_left_to(grass1, right)
        grass=grass1
        sum=sum+width1




    pacman = wrap.sprite.add("pacman", pacman_x, pacman_y, "player2")
    wrap.sprite.move_left_to(pacman, pacman_x)


    print(cordinaty)

    for i in cordinaty:
        platform = wrap.sprite.add("mario-items", i[0], i[1], "moving_platform2")
        wrap.sprite.set_width(platform,50)
        wrap.sprite.move_left_to(platform,i[0])
        cacoyto_list.append(platform)

def check_platform(platform,keys):
    global speed
    top_platform = wrap.sprite.get_top(platform)
    bottom = wrap.sprite.get_bottom(pacman)
    bottom_platform=wrap.sprite.get_bottom(platform)
    if speed>0 and wrap.sprite.is_collide_sprite(pacman,platform):
        wrap.sprite.move_bottom_to(pacman, top_platform)
        speed = -7
        if wrap.K_SPACE in keys:
            speed = -20
    elif speed<0 and wrap.sprite.is_collide_sprite(pacman,platform):
        wrap.sprite.move_top_to(pacman, bottom_platform+2)



def move_camera(number_y,number_x):
    global grass, grass1
    wrap.sprite.move(pacman,number_x,number_y)
    for i in cacoyto_list:
        wrap.sprite.move(i, number_x, number_y)
    for i in decorations:
        wrap.sprite.move(i, number_x, number_y)

    left=wrap.sprite.get_left(decorations[0])
    right1 = wrap.sprite.get_right(decorations[-1])
    if right1 < 500:
        wrap.sprite.move_left_to(decorations[0], right1)
        decorations.append(decorations[0])
        del decorations[0]
    elif left>0:
        wrap.sprite.move_right_to(decorations[-1], left)
        decorations.insert(0,decorations[-1])
        del decorations[-1]
def move_pacman():
    y=wrap.sprite.get_y(pacman)
    x=wrap.sprite.get_x(pacman)
    colpix_x=250-x
    colpix_y=300-y
    move_camera(colpix_y,colpix_x)

wrap.add_sprite_dir("mysprite")
wrap.world.create_world(500,600)

decorations = []
cacoyto_list=[]
pacman=None
grass=None
grass1=None
sum=0
carta()



speed=0







@wrap.on_key_always(wrap.K_LEFT,wrap.K_RIGHT)
def move(keys):
    global speed

    if wrap.K_LEFT in keys:
        wrap.sprite.move(pacman,-5,0)
        for i in cacoyto_list:
            if wrap.sprite.is_collide_sprite(pacman,i):
                right_platform = wrap.sprite.get_right(i)
                wrap.sprite.move_left_to(pacman,right_platform)
    elif wrap.K_RIGHT in keys:
        wrap.sprite.move(pacman, 5, 0)
        for i in cacoyto_list:
            if wrap.sprite.is_collide_sprite(pacman, i):
                left_platform = wrap.sprite.get_left(i)
                wrap.sprite.move_right_to(pacman, left_platform)

@wrap.always()
def padenye(pos_x,pos_y,keys):
    global speed
    wrap.world.set_title(pos_y)


    wrap.sprite.move(pacman, 0, speed)
    for i in cacoyto_list:
        check_platform(i, keys)
    speed = speed + 2

    if speed>=20:
        speed=20
    move_pacman()



import wrap_py
wrap_py.app.start()