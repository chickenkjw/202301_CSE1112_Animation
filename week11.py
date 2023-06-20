from cs1graphics import *
from animation import reimu, marisa, castle
import time
import math

frame = 24
one_frame = 1 / frame

canvas = Canvas()


def show_animation():
    canvas.setTitle("Bad Apple!!")
    canvas.setWidth(1280)
    canvas.setHeight(720)
    canvas.setBackgroundColor('white')

    animate_cut_1()
    animate_cut_2()
    animate_cut_3()
    animate_cut_4()


def test():
    rect1 = Rectangle(30, 60, Point(600, 400))
    rect2 = Rectangle(30, 60, Point(600, 460))

    rect2_layer = Layer()
    rect2_layer.add(rect2)

    rect_layer = Layer()
    rect_layer.add(rect1)
    rect_layer.add(rect2_layer)

    canvas.add(rect_layer)

    rect_layer.adjustReference(600, 400)
    rect2_layer.adjustReference(rect_layer.getReferencePoint().getX(), rect_layer.getReferencePoint().getY())
    print(rect_layer.getReferencePoint())
    print(rect2_layer.getReferencePoint())
    for i in range(frame):
        rect_layer.rotate(1)
        rect2_layer.rotate(1)
        time.sleep(one_frame)


def remove_object(obj):
    canvas.remove(obj)


def draw_object(obj):
    canvas.add(obj)


def animate_cut_1():
    reimu_obj = reimu.reimu()
    reimu_obj.adjustReference(632, 300)
    draw_object(reimu_obj)
    reimu_obj.scale(16)  # 16
    # 1초
    for _ in range(frame):
        reimu_obj.scale(0.98)  # 0.98
        time.sleep(one_frame)

    reimu.shake_2sec(reimu_obj, frame, one_frame, 7, True, False)  # 숫자는 흔들리는 가중치
    reimu.shake_2sec(reimu_obj, frame, one_frame, 8, False, False)
    reimu.shake_2sec(reimu_obj, frame, one_frame, 7, False, True)

    reimu_obj_2 = reimu.reimu_2()
    reimu_obj_2.adjustReference(632, 300)
    reimu_obj_2.stretch(0.5, 1)

    arm_layer = reimu_obj_2.getContents()[1]
    arm_layer.adjustReference(732, 551)
    arm_layer.rotate(math.pi / 5)

    draw_object(reimu_obj_2)

    reimu.rotate_body(reimu_obj, reimu_obj_2, frame, one_frame)
    remove_object(reimu_obj)


def animate_cut_2():
    reimu_obj = canvas.getContents()[0]

    straight_arm = Polygon(Point(994, 435), Point(935, 421), Point(873, 406), Point(853, 352), Point(806, 383),
                           Point(739, 383), Point(683, 379), Point(592, 321), Point(506, 279), Point(464, 240),
                           Point(437, 227), Point(395, 248), Point(402, 207), Point(364, 222), Point(296, 182),
                           Point(277, 165), Point(255, 215), Point(286, 259), Point(360, 285), Point(393, 280),
                           Point(404, 280), Point(435, 276), Point(448, 320), Point(443, 370), Point(414, 443),
                           Point(358, 572), Point(347, 619), Point(354, 633), Point(406, 655), Point(475, 669),
                           Point(523, 670), Point(559, 693), Point(635, 701), Point(735, 704), Point(770, 680),
                           Point(778, 604), Point(761, 558), Point(747, 508), Point(737, 478), Point(742, 459),
                           Point(790, 457), Point(803, 491), Point(833, 471), Point(881, 486), Point(903, 489),
                           Point(929, 445))
    straight_arm_layer = Layer()
    straight_arm.setFillColor('black')
    straight_arm_layer.add(straight_arm)
    straight_arm_layer.adjustReference(783, 462)

    straight_arm_layer.move(0, 600)
    straight_arm_layer.rotate(math.pi / 2 * -1)

    draw_object(straight_arm_layer)

    reimu.throw_apple(reimu_obj, straight_arm_layer, frame, one_frame)

    contents = canvas.getContents()

    for content in contents:
        canvas.remove(content)


def animate_cut_3():
    apple = marisa.apple()
    marisa_obj = marisa.marisa()

    apple.scale(0.7)
    apple.move(-170, -350)

    marisa_obj.adjustReference(880, 300)
    marisa_obj.move(5000, -900)
    marisa_obj.scale(8)

    night_sky = Layer()
    stars = [Circle(1, Point(306, 166)), Circle(1, Point(335, 370)), Circle(1, Point(574, 207)),
             Circle(1, Point(349, 380)), Circle(1, Point(292, 249)), Circle(1, Point(178, 484)),
             Circle(1, Point(203, 448)), Circle(1, Point(207, 551)), Circle(1, Point(236, 627)),
             Circle(1, Point(753, 230)), Circle(1, Point(722, 361)), Circle(1, Point(897, 254)),
             Circle(1, Point(884, 460)), Circle(1, Point(1059, 330)), Circle(1, Point(659, 505)),
             Circle(1, Point(572, 412)), Circle(1, Point(466, 346)), Circle(1, Point(275, 306)),
             Circle(1, Point(132, 334)), Circle(1, Point(135, 440)), Circle(1, Point(314, 450)),
             Circle(1, Point(826, 624)), Circle(1, Point(859, 682)), Circle(1, Point(1035, 674)),
             Circle(1, Point(1087, 553)), Circle(1, Point(1100, 466)), Circle(1, Point(1040, 403)),
             Circle(1, Point(928, 352)), Circle(1, Point(937, 249)), Circle(1, Point(1165, 434)),
             Circle(1, Point(1209, 364)), Circle(1, Point(1221, 242)), Circle(1, Point(417, 503)),
             Circle(1, Point(307, 495)), Circle(1, Point(299, 585)), Circle(1, Point(374, 661)),
             Circle(1, Point(470, 681)), Circle(1, Point(548, 564)), Circle(1, Point(539, 485)),
             Circle(1, Point(458, 545)), Circle(1, Point(380, 80)), Circle(1, Point(468, 32)),
             Circle(1, Point(638, 50)), Circle(1, Point(691, 140)), Circle(1, Point(871, 130)),
             Circle(1, Point(875, 65)), Circle(1, Point(1130, 210)), Circle(1, Point(1187, 46)),
             Circle(1, Point(1077, 64)), Circle(1, Point(204, 110)), Circle(1, Point(180, 198)),
             Circle(1, Point(154, 61)), Circle(1, Point(441, 190)), Circle(1, Point(760, 484)),
             Circle(1, Point(142, 632)), Circle(1, Point(681, 665)), Circle(1, Point(1218, 651)),
             Circle(1, Point(612, 308))]

    stars_2 = [Circle(1, Point(205, -110)), Circle(1, Point(198, -24)), Circle(1, Point(207, 78)),
               Circle(1, Point(371, 85)), Circle(1, Point(405, 168)), Circle(1, Point(453, 111)),
               Circle(1, Point(470, 34)), Circle(1, Point(435, -105)), Circle(1, Point(364, -208)),
               Circle(1, Point(460, -127)), Circle(1, Point(477, -128)), Circle(1, Point(612, -85)),
               Circle(1, Point(687, -60)), Circle(1, Point(805, -183)), Circle(1, Point(993, -111)),
               Circle(1, Point(996, -97)), Circle(1, Point(1084, -73)), Circle(1, Point(991, -28)),
               Circle(1, Point(1094, 94)), Circle(1, Point(1001, 208))]

    for point in stars:
        point.setFillColor('white')
        night_sky.add(point)

    for point in stars_2:
        point.setFillColor('white')
        night_sky.add(point)

    night_sky.move(-600, 0)
    canvas.add(marisa_obj)
    canvas.add(apple)

    marisa.pick_apple(apple, marisa_obj, frame, one_frame)

    canvas.setBackgroundColor('black')

    marisa.flying(apple, marisa_obj, frame, one_frame)

    entire_layer = Layer()
    entire_layer.add(marisa_obj)
    entire_layer.add(apple)

    draw_object(entire_layer)

    remove_object(marisa_obj)
    remove_object(apple)

    marisa.eat_apple(entire_layer, frame, one_frame, True, night_sky)
    night_sky.setDepth(60)
    night_sky.scale(2)
    draw_object(night_sky)

    marisa.eat_apple(entire_layer, frame, one_frame, False, night_sky)
    marisa.eat_apple(entire_layer, frame, one_frame, False, night_sky)

    marisa_obj2 = marisa.marisa_2()
    marisa_obj2.stretch(0.7, 1)
    marisa_obj2.move(280, 20)

    castle_layer = castle.castle()
    castle_layer.move(-530, 0)

    draw_object(marisa_obj2)
    draw_object(castle_layer)

    marisa.rotate_body(entire_layer, marisa_obj2, castle_layer, night_sky, frame, one_frame)

    remove_object(entire_layer)


def animate_cut_4():
    contents = canvas.getContents()

    night_sky = contents[0]
    marisa_obj = contents[1]
    castle_obj = contents[2]

    marisa.flying2(marisa_obj, night_sky, castle_obj, frame, one_frame)


show_animation()
