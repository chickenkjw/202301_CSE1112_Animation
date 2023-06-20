from cs1graphics import *
import math
import time


def marisa():
    layers = Layer()

    body_layer = Layer()
    head_layer = Layer()
    arm_layer = Layer()

    head = Polygon(Point(578, 225), Point(572, 230), Point(576, 236), Point(581, 231), Point(585, 237), Point(581, 242),
                   Point(585, 245), Point(599, 239), Point(606, 258), Point(631, 260), Point(643, 273), Point(661, 282),
                   Point(650, 273), Point(668, 281), Point(670, 273), Point(679, 283), Point(679, 276), Point(685, 281),
                   Point(688, 273), Point(697, 283), Point(696, 269), Point(683, 257), Point(692, 255), Point(668, 246),
                   Point(645, 231), Point(621, 219), Point(598, 218))
    head.setFillColor('white')
    head.setBorderColor('white')
    chin = Polygon(Point(585, 243), Point(593, 252), Point(600, 249), Point(613, 248), Point(611, 237), Point(595, 236))
    chin.setFillColor('white')
    chin.setBorderColor('white')
    chin.setBorderWidth(4)
    hat = Polygon(Point(537, 197), Point(561, 204), Point(547, 188), Point(546, 181), Point(550, 177), Point(554, 184),
                  Point(571, 185), Point(567, 196), Point(569, 202), Point(583, 200), Point(592, 188), Point(604, 181),
                  Point(627, 180), Point(637, 183), Point(673, 207), Point(662, 208), Point(651, 203), Point(642, 199),
                  Point(635, 204), Point(636, 220), Point(665, 231), Point(674, 238), Point(668, 246), Point(635, 243),
                  Point(584, 231), Point(554, 219), Point(537, 209))
    hat.setFillColor('white')
    hat.setBorderColor('white')

    chin_layer = Layer()
    chin_layer.add(chin)
    hat_layer = Layer()
    hat_layer.add(hat)

    head_layer.add(head)
    head_layer.add(chin_layer)
    head_layer.add(hat_layer)

    upper_body = Polygon(Point(600, 241), Point(606, 257), Point(602, 269), Point(595, 277), Point(597, 290),
                         Point(599, 297), Point(588, 315), Point(581, 326), Point(574, 339), Point(564, 352),
                         Point(561, 359), Point(574, 360), Point(588, 357), Point(583, 351), Point(589, 332),
                         Point(598, 322), Point(606, 303), Point(611, 306), Point(618, 318), Point(620, 328),
                         Point(654, 323), Point(650, 313), Point(677, 327), Point(685, 327), Point(725, 356),
                         Point(735, 349), Point(699, 324), Point(736, 330), Point(737, 321), Point(683, 315),
                         Point(678, 283), Point(667, 286), Point(660, 296), Point(653, 305), Point(643, 278),
                         Point(636, 265), Point(626, 258), Point(621, 242))
    upper_body.setFillColor('white')
    upper_body.setBorderColor('white')
    upper_body.setBorderWidth(2)
    lower_body = Polygon(Point(617, 312), Point(622, 323), Point(615, 333), Point(574, 358), Point(572, 365),
                         Point(582, 374), Point(580, 380), Point(585, 388), Point(597, 389), Point(640, 381),
                         Point(646, 383), Point(646, 409), Point(650, 418), Point(655, 417), Point(661, 403),
                         Point(667, 413), Point(675, 412), Point(680, 405), Point(675, 387), Point(677, 375),
                         Point(722, 372), Point(735, 361), Point(706, 344), Point(655, 321), Point(649, 306))
    lower_body.setFillColor('black')
    brush = Polygon(Point(393, 340), Point(674, 360), Point(746, 336), Point(791, 330), Point(826, 332),
                    Point(824, 340), Point(836, 339), Point(831, 343), Point(833, 350), Point(839, 350),
                    Point(839, 358), Point(852, 354), Point(847, 360), Point(865, 365), Point(855, 367),
                    Point(859, 372), Point(854, 375), Point(861, 379), Point(852, 381), Point(859, 394),
                    Point(842, 391), Point(855, 400), Point(849, 403), Point(837, 396), Point(836, 401),
                    Point(822, 408), Point(828, 414), Point(802, 406), Point(816, 422), Point(789, 404),
                    Point(732, 395), Point(712, 388), Point(698, 379), Point(470, 362), Point(500, 370),
                    Point(500, 375), Point(521, 386), Point(516, 391), Point(450, 362), Point(440, 373),
                    Point(431, 369), Point(429, 360), Point(402, 354))
    brush.setFillColor('black')

    body_layer.add(upper_body)
    body_layer.add(lower_body)
    body_layer.add(brush)

    arm = Polygon(Point(601, 302), Point(595, 306), Point(588, 303), Point(579, 272), Point(572, 271), Point(583, 263),
                  Point(584, 267), Point(588, 269), Point(595, 287))
    arm.setFillColor('black')

    arm_layer.add(arm)
    arm_layer.adjustReference(602, 302)

    for layer in [body_layer, head_layer, arm_layer]:
        layers.add(layer)

    return layers


def marisa_2():
    layer = Layer()

    body = Polygon(Point(763, 231), Point(749, 238), Point(740, 246), Point(743, 254), Point(747, 278), Point(740, 294),
                   Point(739, 299), Point(743, 302), Point(745, 322), Point(747, 325), Point(754, 329), Point(760, 343),
                   Point(755, 352), Point(753, 366), Point(742, 373), Point(732, 378), Point(726, 387), Point(721, 400),
                   Point(761, 423), Point(760, 441), Point(760, 449), Point(769, 459), Point(776, 457), Point(786, 420),
                   Point(797, 418), Point(799, 424), Point(807, 425), Point(815, 459), Point(824, 464), Point(834, 462),
                   Point(839, 452), Point(837, 438), Point(840, 332), Point(848, 322), Point(854, 299), Point(830, 304),
                   Point(814, 311), Point(804, 317), Point(806, 308), Point(805, 284), Point(802, 258), Point(788, 235))
    body.setFillColor('white')
    body.setBorderColor('white')

    hair = Polygon(Point(809, 243), Point(831, 263), Point(822, 264), Point(840, 275), Point(823, 273), Point(827, 285),
                   Point(818, 283), Point(819, 291), Point(810, 289), Point(795, 283), Point(773, 264), Point(768, 237))
    hair.setFillColor('white')
    hair.setBorderColor('white')

    hair_layer = Layer()
    hair_layer.add(hair)

    hat = Polygon(Point(775, 178), Point(782, 183), Point(788, 181), Point(799, 190), Point(799, 203), Point(792, 204),
                  Point(801, 225), Point(845, 236), Point(847, 241), Point(839, 250), Point(833, 251), Point(823, 252),
                  Point(771, 247), Point(740, 242), Point(729, 245), Point(711, 250), Point(706, 242), Point(713, 236),
                  Point(730, 229), Point(718, 221), Point(718, 216), Point(732, 223), Point(736, 218), Point(746, 215),
                  Point(752, 200), Point(763, 188))
    hat.setFillColor('white')
    hat.setBorderColor('white')

    brush = Polygon(Point(704, 396), Point(705, 409), Point(713, 409), Point(710, 419), Point(716, 424),
                    Point(717, 422), Point(717, 412), Point(757, 426), Point(776, 416), Point(792, 412),
                    Point(843, 437), Point(857, 447), Point(861, 445), Point(870, 447), Point(870, 462),
                    Point(874, 453), Point(882, 467), Point(878, 441), Point(889, 447), Point(902, 461),
                    Point(893, 443), Point(912, 451), Point(897, 433), Point(941, 438), Point(911, 427),
                    Point(915, 421), Point(934, 429), Point(948, 427), Point(920, 416), Point(929, 414),
                    Point(918, 400), Point(932, 398), Point(919, 386), Point(919, 379), Point(943, 385),
                    Point(923, 370), Point(935, 365), Point(911, 357), Point(920, 352), Point(896, 343),
                    Point(907, 334), Point(846, 332), Point(807, 359), Point(784, 377), Point(755, 400),
                    Point(727, 395))
    brush.setFillColor('white')
    brush.setBorderColor('white')

    for polygon in [body, hair_layer, hat, brush]:
        layer.add(polygon)

    return layer


def apple():
    layer = Layer()
    apple_ = Polygon(Point(416, 271), Point(425, 275), Point(450, 271), Point(454, 279), Point(453, 291),
                     Point(453, 305), Point(460, 325), Point(464, 335), Point(478, 350), Point(497, 362),
                     Point(515, 373), Point(537, 379), Point(564, 377), Point(594, 369), Point(619, 359),
                     Point(645, 342), Point(662, 322), Point(677, 303), Point(681, 288), Point(683, 275),
                     Point(682, 262), Point(677, 245), Point(671, 234), Point(672, 218), Point(672, 208),
                     Point(667, 199), Point(655, 183), Point(634, 166), Point(605, 150), Point(582, 142),
                     Point(558, 138), Point(534, 138), Point(508, 142), Point(485, 155), Point(470, 173),
                     Point(461, 193), Point(457, 212), Point(454, 228), Point(450, 243), Point(449, 259),
                     Point(433, 261), Point(419, 261))
    apple_.setFillColor('black')

    layer.add(apple_)
    layer.adjustReference(566, 260)

    return layer


def pick_apple(apple_, obj, seconds, one_frame):
    for s in range(seconds * 2):
        horizontal_move = 6
        move_power = 0
        if s < seconds:
            move_power = math.sin(math.pi * (s / seconds)) * 40
        elif seconds <= s:
            move_power = math.sin(math.pi * s / seconds) * 14

        apple_.move(horizontal_move, move_power)
        apple_.rotate(math.pi * 6.2)
        apple_.scale(1.008)

        time.sleep(one_frame)

    arm_layer = obj.getContents()[2]
    arm_layer.move(0, 70)
    arm_layer.rotate(math.pi * 180)

    # 이리저리 사과 헤멤
    for s in range(seconds):
        h_axis = math.sin(2 * math.pi * (s / seconds)) * 4 - 2
        v_axis = math.sin(2 * math.pi * (s / seconds)) * 7 + 3

        if s >= seconds // 2 + 3:
            obj.move(-338, 0)

        apple_.move(h_axis, v_axis)
        apple_.rotate(math.pi * 7)

        time.sleep(one_frame)


def flying(apple_, obj, seconds, one_frame):
    apple_pol = apple_.getContents()[0]
    apple_pol.setFillColor('white')
    apple_pol.setBorderColor('white')

    body_layer = obj.getContents()[0]
    head_layer = obj.getContents()[1]
    arm_layer = obj.getContents()[2]

    hat_layer = head_layer.getContents()[2]

    arm_pol = arm_layer.getContents()[0]
    arm_pol.setFillColor('white')
    arm_pol.setBorderColor('white')

    brush_pol = body_layer.getContents()[2]
    brush_pol.setFillColor('white')
    brush_pol.setBorderColor('white')

    lower_body_pol = body_layer.getContents()[1]
    lower_body_pol.setFillColor('white')
    lower_body_pol.setBorderColor('white')

    for s in range(seconds // 2):
        time.sleep(one_frame)

    apple_.adjustReference(0, -1300)
    obj.adjustReference(-2300, 0)

    hat_layer.rotate(math.pi * -0.2)
    hat_layer.move(10, 10)

    for s in range(seconds):
        h_axis = math.sin(math.pi * 2 * (s / seconds)) * -170
        apple_h_axis = h_axis
        v_axis = math.sin(math.pi * 0.5 * (s / seconds)) * 80

        if seconds // 2 - 2 <= s < seconds // 2 + seconds // 4 - 2:
            h_axis = 0
            obj.scale(0.98)
            apple_.scale(0.98)
        elif seconds // 2 + seconds // 4 - 2 <= s:
            h_axis = math.sin(math.pi * 2 * (s / seconds)) * -210
            obj.scale(0.98)
            apple_.scale(0.98)

        obj.move(h_axis + 4, v_axis - 4)

        arm_layer.adjustReference(-0.5, -1)
        arm_layer.move(0.9, -2.1)
        arm_layer.rotate(math.pi * 1.8)

        apple_.adjustReference(-15, 92)
        apple_.move(apple_h_axis * 0.9 + 2.1, -4)
        apple_.rotate(math.pi * 0.5)

        time.sleep(one_frame)


def eat_apple(obj, seconds, one_frame, is_scaling, sky):
    scaling_adjust = 1 if is_scaling else 0.6

    marisa_obj = obj.getContents()[0]
    apple_ = obj.getContents()[1]

    head_layer = marisa_obj.getContents()[1]
    arm_layer = marisa_obj.getContents()[2]

    chin_layer = head_layer.getContents()[1]

    obj.adjustReference(640, 300)

    if is_scaling:
        chin_layer.adjustReference(755, 141)
    head_layer.adjustReference(900, 336)

    apple_move_power = 26
    arm_move_power = 0.4
    arm_rotate_power = 5

    shake_index = 0

    if is_scaling:
        arm_layer.adjustReference(100, 30)

    # 사과 가져다 대기
    for s in range(seconds - 3):
        move_power = math.sin(math.pi * 0.5 * (s / seconds)) * arm_move_power
        arm_layer.move(move_power, -move_power)
        arm_layer.rotate(abs(move_power) * arm_rotate_power * math.pi / seconds * 3)

        apple_.move(move_power * apple_move_power, -move_power * apple_move_power)

        shake_power = math.sin(math.pi * (shake_index / seconds)) * 4 * scaling_adjust
        shake_index += 1

        obj.move(shake_power, -shake_power)

        if s > seconds // 2:
            head_layer.rotate(math.pi / (seconds * 6) * -1)
            chin_layer.rotate(math.pi / seconds * -1.4 * scaling_adjust)

        if not is_scaling:
            sky.move(2, 0)

        time.sleep(one_frame)

    # 머금기?
    for s in range(6):
        if is_scaling:
            obj.scale(1.005)

        move_power = math.sin(math.pi * 2 * (shake_index / seconds)) * 1.8
        shake_index += 1

        obj.move(-move_power, move_power)

        if not is_scaling:
            sky.move(2, 0)

        time.sleep(one_frame)

    # 팔 내리기
    for s in range(seconds - 3):

        if s < seconds // 2:
            head_layer.rotate(math.pi / (seconds * 6))
            chin_layer.rotate(math.pi / seconds * 1.4 * scaling_adjust)

            if not is_scaling:
                chin_layer.move(0, 6 / seconds)

        shake_power = math.sin(math.pi * 2 * (shake_index / seconds)) * 4 * scaling_adjust
        shake_index += 1

        obj.move(shake_power, shake_power)

        move_power = math.sin((math.pi * 0.5 * (s / seconds)) * -1) * arm_move_power

        arm_layer.move(move_power, -move_power)
        arm_layer.rotate(abs(move_power) * arm_rotate_power * math.pi / seconds * -3)
        apple_.move(move_power * apple_move_power, -move_power * apple_move_power)

        if is_scaling:
            obj.scale(0.98)

        if not is_scaling:
            sky.move(2, 0)

        time.sleep(one_frame)

    # scaling
    for s in range(seconds):
        shake_power = math.sin(math.pi * 2 * (s / seconds)) * -4 * scaling_adjust
        shake_index += 1

        obj.move(shake_power, -shake_power + 2)

        if is_scaling:
            move_power = math.sin(math.pi * 2 * (shake_index / seconds)) * 2
            scale_power = math.sin(math.pi * (s / seconds) / 2) * 0.05 + 0.95

            obj.scale(scale_power * 0.97)
            obj.move(move_power - 2, move_power)

        if not is_scaling:
            sky.move(2, 0)

            if s > seconds // 2:
                break

        time.sleep(one_frame)


def rotate_body(obj1, obj2, castle, night_sky, seconds, one_frame):
    castle.adjustReference(284, 649)
    obj1.adjustReference(-1100, -530)
    obj2.adjustReference(650, 400)

    for s in range(seconds // 2):
        obj1.stretch(0.82, 0.97)
        obj1.move(-2, 0)
        obj2.stretch(1.05, 1)
        obj2.move(8, 0)

        night_sky.move(7, 0)

        castle.move(32, 0)

        time.sleep(one_frame)


def flying2(obj, night_sky, castle, seconds, one_frame):
    for s in range(seconds * 2):
        move_power = math.sin(math.pi * 0.5 * (s / seconds) * 2) * 2.9

        obj.move(-move_power * 0.5, move_power)

        castle.scale(1.006)
        castle.move(1, 0)

        time.sleep(one_frame)

    print(night_sky.getReferencePoint())
    print(obj.getReferencePoint())

    # 확대
    # for s in range(seconds):
    #
    #
    #     time.sleep(one_frame)
