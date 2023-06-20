from cs1graphics import *
import time
import math


def reimu():
    layer = Layer()
    body_layer = Layer()
    head_layer = Layer()
    hair_layer = Layer()
    left_arm_layer = Layer()
    right_arm_layer = Layer()

    body = Polygon(Point(477, 731), Point(768, 731), Point(746, 700), Point(728, 655), Point(712, 614),
                   Point(700, 570), Point(694, 537), Point(693, 505), Point(693, 485), Point(691, 459),
                   Point(692, 434), Point(705, 367), Point(720, 309), Point(686, 290), Point(645, 285),
                   Point(608, 285), Point(569, 288), Point(536, 305), Point(540, 355), Point(554, 401),
                   Point(561, 420), Point(563, 440), Point(552, 495), Point(547, 528), Point(532, 580),
                   Point(513, 638), Point(492, 686))
    body.setFillColor('black')

    head = Polygon(Point(611, 290), Point(655, 289), Point(654, 264), Point(679, 252), Point(694, 229),
                   Point(697, 204), Point(699, 177), Point(694, 151), Point(687, 134), Point(663, 127),
                   Point(635, 127), Point(613, 130), Point(592, 150), Point(586, 176), Point(586, 205),
                   Point(589, 236), Point(600, 256), Point(615, 261))
    head.setFillColor('black')
    ribbon = Polygon(Point(539, 39), Point(544, 36), Point(554, 36), Point(568, 36), Point(577, 39), Point(588, 40),
                     Point(600, 45), Point(607, 49), Point(616, 53), Point(623, 60), Point(626, 69), Point(634, 61),
                     Point(643, 61), Point(653, 63), Point(664, 65), Point(669, 69), Point(675, 76), Point(682, 70),
                     Point(691, 69), Point(701, 67), Point(711, 67), Point(720, 67), Point(731, 67), Point(746, 68),
                     Point(756, 73), Point(766, 78), Point(776, 83), Point(783, 90), Point(781, 100), Point(780, 108),
                     Point(776, 116), Point(770, 126), Point(763, 135), Point(757, 145), Point(753, 154),
                     Point(746, 162),
                     Point(733, 166), Point(724, 158), Point(715, 138), Point(701, 123), Point(686, 116),
                     Point(681, 126),
                     Point(673, 135), Point(651, 133), Point(635, 129), Point(626, 119), Point(622, 103),
                     Point(614, 103),
                     Point(599, 110), Point(590, 118), Point(580, 123), Point(545, 133), Point(533, 135),
                     Point(527, 130),
                     Point(527, 118), Point(522, 112), Point(522, 102), Point(522, 93), Point(522, 84), Point(523, 76),
                     Point(523, 67), Point(525, 64), Point(523, 54))
    ribbon.setFillColor('black')

    left_ribbon_1 = Polygon(Point(619, 113), Point(642, 119), Point(634, 148), Point(626, 186), Point(620, 232),
                            Point(590, 228),
                            Point(601, 179), Point(606, 140))
    left_ribbon_1.setFillColor('black')
    right_ribbon_1 = Polygon(Point(650, 143), Point(679, 132), Point(688, 160), Point(693, 196), Point(697, 247),
                             Point(668, 255),
                             Point(661, 213), Point(660, 167))
    right_ribbon_1.setFillColor('black')

    left_ribbon_2 = Polygon(Point(625, 222), Point(593, 212), Point(582, 266), Point(583, 308), Point(581, 366),
                            Point(615, 368),
                            Point(614, 323), Point(619, 266))
    left_ribbon_2.setFillColor('black')
    right_ribbon_2 = Polygon(Point(671, 244), Point(696, 240), Point(704, 289), Point(706, 324), Point(706, 365),
                             Point(670, 367),
                             Point(676, 333), Point(681, 275))
    right_ribbon_2.setFillColor('black')

    left_ribbon_3 = Polygon(Point(582, 359), Point(615, 357), Point(616, 413), Point(618, 446), Point(619, 475),
                            Point(603, 464),
                            Point(590, 483), Point(588, 446), Point(586, 398))
    left_ribbon_3.setFillColor('black')
    right_ribbon_3 = Polygon(Point(704, 363), Point(722, 404), Point(740, 447), Point(749, 466), Point(726, 460),
                             Point(725, 484),
                             Point(715, 449), Point(710, 420), Point(687, 384))
    right_ribbon_3.setFillColor('black')

    left_ribbon_bottom_layer = Layer()
    left_ribbon_bottom_layer.add(left_ribbon_3)
    right_ribbon_bottom_layer = Layer()
    right_ribbon_bottom_layer.add(right_ribbon_3)

    left_ribbon_middle_layer = Layer()
    left_ribbon_middle_layer.add(left_ribbon_2)
    left_ribbon_middle_layer.add(left_ribbon_bottom_layer)
    right_ribbon_middle_layer = Layer()
    right_ribbon_middle_layer.add(right_ribbon_2)
    right_ribbon_middle_layer.add(right_ribbon_bottom_layer)

    left_ribbon_top_layer = Layer()
    left_ribbon_top_layer.add(left_ribbon_1)
    left_ribbon_top_layer.add(left_ribbon_middle_layer)
    right_ribbon_top_layer = Layer()
    right_ribbon_top_layer.add(right_ribbon_1)
    right_ribbon_top_layer.add(right_ribbon_middle_layer)

    ribbon_string_layer = Layer()
    ribbon_string_layer.add(left_ribbon_top_layer)
    ribbon_string_layer.add(right_ribbon_top_layer)

    hair = Polygon(Point(625, 98), Point(600, 109), Point(576, 126), Point(566, 152), Point(559, 177),
                   Point(560, 192), Point(630, 190), Point(692, 190), Point(722, 189), Point(724, 208),
                   Point(729, 198), Point(731, 177), Point(731, 163), Point(722, 142), Point(707, 124),
                   Point(690, 111), Point(661, 101))
    hair.setFillColor('black')

    left_side_hair_1 = Polygon(Point(560, 164), Point(579, 162), Point(581, 192), Point(583, 221),
                               Point(564, 229), Point(560, 202), Point(558, 172))
    left_side_hair_1.setFillColor('black')
    right_side_hair_1 = Polygon(Point(693, 177), Point(717, 177), Point(716, 207), Point(716, 233),
                                Point(694, 236), Point(693, 204))
    right_side_hair_1.setFillColor('black')

    left_side_hair_2 = Polygon(Point(549, 210), Point(577, 212), Point(576, 217), Point(571, 217),
                               Point(568, 249), Point(571, 249), Point(571, 255), Point(545, 256),
                               Point(545, 250), Point(551, 250), Point(553, 218), Point(547, 216))
    left_side_hair_2.setFillColor('black')
    right_side_hair_2 = Polygon(Point(688, 230), Point(722, 226), Point(722, 231), Point(715, 231),
                                Point(717, 273), Point(724, 277), Point(685, 281), Point(690, 276),
                                Point(692, 235), Point(686, 235))
    right_side_hair_2.setFillColor('black')

    left_side_hair_3 = Polygon(Point(549, 247), Point(568, 245), Point(563, 271), Point(551, 291), Point(551, 271))
    left_side_hair_3.setFillColor('black')
    right_side_hair_3 = Polygon(Point(693, 272), Point(715, 270), Point(715, 294), Point(706, 310), Point(697, 287))
    right_side_hair_3.setFillColor('black')

    left_side_hair_bottom_layer = Layer()
    left_side_hair_bottom_layer.add(left_side_hair_3)
    right_side_hair_bottom_layer = Layer()
    right_side_hair_bottom_layer.add(right_side_hair_3)

    left_side_hair_middle_layer = Layer()
    left_side_hair_middle_layer.add(left_side_hair_2)
    left_side_hair_middle_layer.add(left_side_hair_bottom_layer)
    right_side_hair_middle_layer = Layer()
    right_side_hair_middle_layer.add(right_side_hair_2)
    right_side_hair_middle_layer.add(right_side_hair_bottom_layer)

    left_side_hair_top_layer = Layer()
    left_side_hair_top_layer.add(left_side_hair_1)
    left_side_hair_top_layer.add(left_side_hair_middle_layer)
    right_side_hair_top_layer = Layer()
    right_side_hair_top_layer.add(right_side_hair_1)
    right_side_hair_top_layer.add(right_side_hair_middle_layer)

    side_hair_layer = Layer()
    side_hair_layer.add(left_side_hair_top_layer)
    side_hair_layer.add(right_side_hair_top_layer)

    left_back_hair_1 = Polygon(Point(566, 161), Point(555, 198), Point(547, 239), Point(542, 260), Point(561, 225),
                               Point(557, 247), Point(570, 234), Point(571, 252), Point(585, 240), Point(593, 214),
                               Point(597, 186), Point(597, 159), Point(584, 152))
    left_back_hair_1.setFillColor('black')
    right_back_hair_1 = Polygon(Point(718, 193), Point(714, 223), Point(717, 245), Point(702, 218), Point(702, 246),
                                Point(695, 219), Point(685, 252), Point(684, 217), Point(666, 249), Point(671, 209),
                                Point(678, 170), Point(714, 176))
    right_back_hair_1.setFillColor('black')

    left_back_hair_2 = Polygon(Point(559, 214), Point(577, 211), Point(579, 246), Point(577, 268), Point(571, 238),
                               Point(568, 270), Point(564, 247), Point(557, 275), Point(549, 291), Point(552, 252),
                               Point(557, 223))
    left_back_hair_2.setFillColor('black')
    right_back_hair_2 = Polygon(Point(710, 220), Point(714, 244), Point(717, 271), Point(708, 259), Point(703, 274),
                                Point(699, 242), Point(693, 276), Point(688, 261), Point(680, 278), Point(669, 258),
                                Point(669, 228), Point(691, 214))
    right_back_hair_2.setFillColor('black')

    left_back_hair_3 = Polygon(Point(557, 256), Point(561, 290), Point(572, 327), Point(586, 295), Point(586, 313),
                               Point(590, 335), Point(595, 315), Point(596, 293), Point(605, 335), Point(612, 314),
                               Point(621, 335), Point(625, 315), Point(629, 292), Point(630, 259), Point(631, 225),
                               Point(602, 208))
    left_back_hair_3.setFillColor('black')
    right_back_hair_3 = Polygon(Point(715, 259), Point(714, 288), Point(707, 308), Point(706, 285), Point(697, 312),
                                Point(696, 280), Point(684, 314), Point(685, 276), Point(667, 314), Point(664, 277),
                                Point(651, 316), Point(647, 293), Point(644, 270), Point(651, 247), Point(676, 231),
                                Point(705, 239))
    right_back_hair_3.setFillColor('black')

    left_back_hair_bottom_layer = Layer()
    left_back_hair_bottom_layer.add(left_back_hair_3)
    right_back_hair_bottom_layer = Layer()
    right_back_hair_bottom_layer.add(right_back_hair_3)

    left_back_hair_middle_layer = Layer()
    left_back_hair_middle_layer.add(left_back_hair_2)
    left_back_hair_middle_layer.add(left_back_hair_bottom_layer)
    right_back_hair_middle_layer = Layer()
    right_back_hair_middle_layer.add(right_back_hair_2)
    right_back_hair_middle_layer.add(right_back_hair_bottom_layer)

    left_back_hair_top_layer = Layer()
    left_back_hair_top_layer.add(left_back_hair_1)
    left_back_hair_top_layer.add(left_back_hair_middle_layer)
    right_back_hair_top_layer = Layer()
    right_back_hair_top_layer.add(right_back_hair_1)
    right_back_hair_top_layer.add(right_back_hair_middle_layer)

    back_hair_layer = Layer()
    back_hair_layer.add(left_back_hair_top_layer)
    back_hair_layer.add(right_back_hair_top_layer)

    left_arm = Polygon(Point(555, 305), Point(538, 344), Point(521, 399), Point(504, 456), Point(477, 521),
                       Point(461, 561),
                       Point(455, 592), Point(436, 608), Point(435, 628), Point(450, 645), Point(468, 646),
                       Point(476, 629),
                       Point(477, 611), Point(483, 586), Point(500, 546), Point(514, 509), Point(521, 472),
                       Point(540, 436),
                       Point(547, 411), Point(572, 377), Point(575, 339), Point(568, 311))
    left_arm.setFillColor('black')
    right_arm = Polygon(Point(687, 304), Point(716, 328), Point(738, 360), Point(754, 396), Point(767, 438),
                        Point(777, 488),
                        Point(785, 527), Point(790, 550), Point(783, 565), Point(797, 584), Point(805, 599),
                        Point(801, 619),
                        Point(792, 632), Point(775, 633), Point(760, 629), Point(743, 611), Point(744, 590),
                        Point(751, 577),
                        Point(741, 544), Point(726, 506), Point(713, 470), Point(701, 433), Point(684, 399),
                        Point(646, 378),
                        Point(645, 331))
    right_arm.setFillColor('black')

    left_arm_sleeves_1 = Polygon(Point(516, 286), Point(502, 292), Point(497, 308), Point(490, 342), Point(485, 367),
                                 Point(461, 359), Point(469, 389), Point(459, 422), Point(446, 455), Point(435, 483),
                                 Point(421, 516), Point(407, 543), Point(402, 572), Point(402, 592), Point(397, 616),
                                 Point(401, 635), Point(426, 643), Point(451, 633), Point(473, 610), Point(489, 598),
                                 Point(497, 572), Point(504, 539), Point(508, 505), Point(508, 477), Point(512, 429),
                                 Point(512, 405), Point(528, 381), Point(546, 349), Point(546, 311))
    left_arm_sleeves_1.setFillColor('black')
    left_arm_layer.move(30, 25)
    right_arm_sleeves_1 = Polygon(Point(694, 299), Point(711, 303), Point(722, 322), Point(732, 342), Point(737, 358),
                                  Point(742, 379),
                                  Point(764, 370), Point(754, 403), Point(763, 426), Point(771, 452), Point(778, 477),
                                  Point(784, 504),
                                  Point(790, 527), Point(796, 544), Point(794, 557), Point(784, 569), Point(780, 598),
                                  Point(778, 618),
                                  Point(778, 650), Point(779, 672), Point(779, 696), Point(769, 713), Point(751, 709),
                                  Point(724, 693),
                                  Point(709, 678), Point(690, 643), Point(692, 609), Point(691, 573), Point(690, 546),
                                  Point(698, 522),
                                  Point(701, 491), Point(701, 457), Point(699, 435), Point(684, 411), Point(651, 383),
                                  Point(620, 340),
                                  Point(640, 307), Point(657, 297))
    right_arm_sleeves_1.setFillColor('black')

    left_arm_sleeves_2 = Polygon(Point(450, 532), Point(437, 556), Point(440, 594), Point(435, 629), Point(426, 685),
                                 Point(443, 716),
                                 Point(452, 730), Point(473, 727), Point(483, 701), Point(507, 663), Point(520, 616),
                                 Point(535, 575),
                                 Point(541, 547), Point(524, 517), Point(499, 496), Point(473, 502))
    left_arm_sleeves_2.setFillColor('black')
    left_arm_sleeves_2.move(-30, 0)
    right_arm_sleeves_2 = Polygon(Point(703, 462), Point(744, 475), Point(781, 505), Point(799, 541), Point(788, 569),
                                  Point(787, 602),
                                  Point(780, 633), Point(779, 667), Point(776, 702), Point(762, 715), Point(741, 704),
                                  Point(714, 683),
                                  Point(701, 635), Point(699, 588), Point(695, 535), Point(700, 485))
    right_arm_sleeves_2.setFillColor('black')

    left_arm_sleeves_bottom_layer = Layer()
    left_arm_sleeves_bottom_layer.add(left_arm_sleeves_2)
    right_arm_sleeves_bottom_layer = Layer()
    right_arm_sleeves_bottom_layer.add(right_arm_sleeves_2)

    left_arm_sleeves_layer = Layer()
    left_arm_sleeves_layer.add(left_arm_sleeves_1)
    left_arm_sleeves_layer.add(left_arm_sleeves_bottom_layer)
    right_arm_sleeves_layer = Layer()
    right_arm_sleeves_layer.add(right_arm_sleeves_2)
    right_arm_sleeves_layer.add(right_arm_sleeves_bottom_layer)

    # 레이어 추가
    body_layer.add(body)

    head_layer.add(head)
    head_layer.add(ribbon)
    head_layer.add(ribbon_string_layer)

    hair_layer.add(hair)
    hair_layer.add(side_hair_layer)
    hair_layer.add(back_hair_layer)

    left_arm_layer.add(left_arm)
    left_arm_layer.add(left_arm_sleeves_layer)
    right_arm_layer.add(right_arm)
    right_arm_layer.add(right_arm_sleeves_layer)

    # 레이어들을 전체 레이어에 add
    for layers in [body_layer, head_layer, hair_layer, left_arm_layer, right_arm_layer]:
        layer.add(layers)

    return layer


def shake_2sec(obj, second, one_frame, amplitude, is_scaling, is_transition):
    layers = obj.getContents()

    head_layer = layers[1]
    hair_layer = layers[2]
    l_arm_layer = layers[3]
    r_arm_layer = layers[4]

    hair_layers = hair_layer.getContents()
    left_side = hair_layers[1].getContents()[0]
    right_side = hair_layers[1].getContents()[1]
    left_back = hair_layers[2].getContents()[0]
    right_back = hair_layers[2].getContents()[1]
    left_side_2 = left_side.getContents()[1]
    left_side_3 = left_side_2.getContents()[1]
    right_side_2 = right_side.getContents()[1]
    right_side_3 = right_side_2.getContents()[1]
    left_back_2 = left_back.getContents()[1]
    left_back_3 = left_back_2.getContents()[1]
    right_back_2 = right_back.getContents()[1]
    right_back_3 = right_back_2.getContents()[1]

    string_layers = head_layer.getContents()[2]
    left_string_1 = string_layers.getContents()[0]
    left_string_2 = left_string_1.getContents()[1]
    left_string_3 = left_string_2.getContents()[1]
    right_string_1 = string_layers.getContents()[1]
    right_string_2 = right_string_1.getContents()[1]
    right_string_3 = right_string_2.getContents()[1]

    l_sleeves_layer = l_arm_layer.getContents()[1].getContents()[1]
    r_sleeves_layer = r_arm_layer.getContents()[1].getContents()[1]

    if is_scaling:
        fix_lx, fix_ly = layers[1].getContents()[0].getPoint(12).get()
        fix_rx, fix_ry = layers[1].getContents()[0].getPoint(6).get()

        left_back.adjustReference(fix_lx, fix_ly)
        left_back_2.adjustReference(left_back.getReferencePoint().getX(), left_back.getReferencePoint().getY())
        left_back_3.adjustReference(left_back_2.getReferencePoint().getX(), left_back_2.getReferencePoint().getY())
        left_side.adjustReference(fix_lx, fix_ly)
        left_side_2.adjustReference(left_side.getReferencePoint().getX(), left_side.getReferencePoint().getY())
        left_side_3.adjustReference(left_side_2.getReferencePoint().getX(), left_side_2.getReferencePoint().getY())
        right_back.adjustReference(fix_rx, fix_ry)
        right_back_2.adjustReference(right_back.getReferencePoint().getX(), right_back.getReferencePoint().getY())
        right_back_3.adjustReference(right_back_2.getReferencePoint().getX(), right_back_2.getReferencePoint().getY())
        right_side.adjustReference(fix_rx, fix_ry)
        right_side_2.adjustReference(right_side.getReferencePoint().getX(), right_side.getReferencePoint().getY())
        right_side_3.adjustReference(right_side_2.getReferencePoint().getX(), right_side_2.getReferencePoint().getY())

        left_string_1.adjustReference(fix_lx, fix_ly)
        left_string_2.adjustReference(left_string_1.getReferencePoint().getX(),
                                      left_string_1.getReferencePoint().getY())
        left_string_3.adjustReference(left_string_2.getReferencePoint().getX(),
                                      left_string_2.getReferencePoint().getY())
        right_string_1.adjustReference(fix_lx, fix_ly)
        right_string_2.adjustReference(right_string_1.getReferencePoint().getX(),
                                       right_string_1.getReferencePoint().getY())
        right_string_3.adjustReference(right_string_2.getReferencePoint().getX(),
                                       right_string_2.getReferencePoint().getY())

        l_sleeves_layer.adjustReference(487, 509)
        r_sleeves_layer.adjustReference(767, 506)

    # 이동
    for s in range(second * 2):
        move_power = math.sin(2 * math.pi * (s / second)) * -amplitude * 0.95
        angle = math.sin(2 * math.pi * (s / second) + math.pi / 2) * -amplitude * 0.07

        if 0 <= s < 6 and 12 <= s < 24:
            angle = -angle

        if s == 6 or s == 18:
            angle *= 2

        if is_transition and s > second * 2 - 10:
            obj.move(10 - move_power, 0)
        else:
            obj.move(move_power, 0)

        left_back.rotate(angle * 0.9)
        left_back_2.rotate(angle)
        left_back_3.rotate(angle)
        left_side.rotate(angle)
        left_side_2.rotate(angle)
        left_side_3.rotate(angle)

        angle *= 1.4
        right_back.rotate(angle * 0.9)
        right_back_2.rotate(angle)
        right_back_3.rotate(angle)
        right_side.rotate(angle)
        right_side_2.rotate(angle)
        right_side_3.rotate(angle)

        angle *= 0.8
        left_string_1.rotate(angle * 1.2)
        left_string_2.rotate(-angle * 1.1)
        left_string_3.rotate(angle)
        right_string_1.rotate(angle * 1.1)
        right_string_2.rotate(-angle * 1.2)
        right_string_3.rotate(angle)

        l_sleeves_layer.rotate(angle * 2)
        r_sleeves_layer.rotate(angle * 2)

        if is_scaling:
            obj.scale(0.954)

        time.sleep(one_frame)


def reimu_2():
    layer = Layer()

    head_layer = Layer()
    body_layer = Layer()
    arm_layer = Layer()

    body = Polygon(Point(676, 719), Point(924, 720), Point(914, 691), Point(917, 667), Point(956, 656), Point(946, 651),
                   Point(966, 636), Point(944, 635), Point(898, 656), Point(888, 619), Point(884, 589), Point(875, 546),
                   Point(866, 503), Point(861, 463), Point(858, 415), Point(826, 375), Point(784, 375), Point(733, 387),
                   Point(745, 418), Point(719, 439), Point(703, 473), Point(691, 503), Point(684, 523), Point(672, 557),
                   Point(659, 607), Point(668, 644), Point(680, 666), Point(684, 685))
    body.setFillColor('black')
    body_layer.add(body)

    arm = Polygon(Point(705, 500), Point(688, 526), Point(668, 516), Point(647, 520), Point(645, 538), Point(649, 562),
                  Point(629, 584), Point(560, 535), Point(545, 535), Point(519, 561), Point(497, 588), Point(555, 643),
                  Point(606, 673), Point(633, 693), Point(671, 675), Point(693, 652), Point(723, 609), Point(731, 541))
    arm.setFillColor('black')

    sleeves = Polygon(Point(545, 535), Point(513, 565), Point(486, 620), Point(485, 673), Point(472, 718),
                      Point(673, 718),
                      Point(680, 685), Point(681, 618), Point(627, 585), Point(574, 546))
    sleeves.setFillColor('black')

    hand = Polygon(Point(521, 603), Point(497, 585), Point(467, 581), Point(439, 568), Point(431, 554), Point(422, 542),
                   Point(420, 526), Point(418, 515), Point(412, 504), Point(421, 481), Point(425, 467), Point(437, 472),
                   Point(437, 487), Point(450, 503), Point(473, 521), Point(493, 523), Point(514, 524), Point(531, 516),
                   Point(539, 519), Point(544, 528), Point(549, 536), Point(568, 553), Point(569, 595))
    hand.setFillColor('black')

    sleeves_layer = Layer()
    sleeves_layer.add(sleeves)
    hand_layer = Layer()
    hand_layer.add(hand)
    hand_layer.add(apple())

    arm_layer.add(arm)
    arm_layer.add(hand_layer)
    arm_layer.add(sleeves_layer)

    head = Polygon(Point(668, 372), Point(661, 371), Point(658, 357), Point(646, 354), Point(640, 345), Point(650, 333),
                   Point(654, 317), Point(653, 297), Point(634, 263), Point(643, 204), Point(677, 168), Point(733, 139),
                   Point(790, 130), Point(849, 137), Point(874, 165), Point(890, 202), Point(905, 247), Point(913, 293),
                   Point(911, 336), Point(875, 362), Point(832, 374), Point(839, 424), Point(804, 422), Point(767, 422),
                   Point(747, 414), Point(730, 383), Point(760, 361), Point(757, 315), Point(719, 305), Point(690, 327),
                   Point(679, 353))
    head.setFillColor('black')
    chin = Polygon(Point(671, 375), Point(673, 351), Point(684, 320), Point(712, 288), Point(774, 298), Point(778, 344),
                   Point(766, 369), Point(735, 394), Point(725, 382), Point(708, 398), Point(696, 406), Point(685, 400),
                   Point(680, 385))
    chin.setFillColor('black')
    side_hair = Polygon(Point(648, 251), Point(682, 239), Point(714, 321), Point(720, 321), Point(714, 326),
                        Point(722, 378),
                        Point(729, 378), Point(722, 384), Point(727, 449), Point(715, 479), Point(698, 473),
                        Point(693, 444),
                        Point(685, 391), Point(673, 389), Point(679, 386), Point(677, 329), Point(667, 327),
                        Point(675, 320),
                        Point(656, 285))
    side_hair.setFillColor('black')
    back_hair = Polygon(Point(899, 175), Point(914, 206), Point(931, 261), Point(942, 323), Point(944, 371),
                        Point(948, 415),
                        Point(947, 447), Point(953, 480), Point(927, 441), Point(931, 468), Point(938, 497),
                        Point(919, 466),
                        Point(910, 443), Point(903, 418), Point(902, 443), Point(910, 468), Point(915, 495),
                        Point(902, 475),
                        Point(894, 456), Point(895, 482), Point(897, 519), Point(900, 540), Point(885, 521),
                        Point(855, 501),
                        Point(837, 430), Point(843, 305), Point(868, 218))
    back_hair.setFillColor('black')
    front_hair = Polygon(Point(661, 267), Point(647, 297), Point(650, 316), Point(637, 298), Point(642, 316),
                         Point(624, 299),
                         Point(623, 305), Point(613, 287), Point(613, 300), Point(605, 281), Point(595, 297),
                         Point(601, 268),
                         Point(595, 268), Point(599, 252), Point(586, 259), Point(597, 238), Point(602, 217),
                         Point(606, 197),
                         Point(618, 176), Point(635, 157), Point(653, 142), Point(672, 132), Point(689, 122),
                         Point(712, 116),
                         Point(759, 105), Point(783, 124), Point(795, 153), Point(776, 177), Point(709, 220))
    front_hair.setFillColor('black')
    ribbon = Polygon(Point(693, 120), Point(686, 107), Point(681, 92), Point(679, 75), Point(682, 60), Point(690, 49),
                     Point(705, 41),
                     Point(720, 41), Point(738, 50), Point(754, 60), Point(767, 69), Point(784, 85), Point(798, 92),
                     Point(816, 87),
                     Point(841, 87), Point(862, 99), Point(878, 114), Point(892, 133), Point(897, 148), Point(899, 170),
                     Point(898, 183),
                     Point(864, 188), Point(803, 189), Point(723, 173), Point(702, 144))
    ribbon.setFillColor('black')

    chin_layer = Layer()
    chin_layer.add(chin)
    side_hair_layer = Layer()
    side_hair_layer.add(side_hair)
    side_hair_layer.move(10, 20)

    for la in [head, chin_layer, side_hair_layer, back_hair, front_hair, ribbon]:
        head_layer.add(la)

    for la in [body_layer, arm_layer, head_layer]:
        layer.add(la)

    return layer


def apple():
    layer = Layer()
    apple_ = Polygon(Point(467, 429), Point(471, 449), Point(487, 445), Point(504, 444), Point(515, 448),
                     Point(524, 457),
                     Point(530, 472), Point(535, 495), Point(533, 514), Point(532, 531), Point(516, 545),
                     Point(501, 551),
                     Point(488, 547), Point(481, 556), Point(464, 563), Point(441, 561), Point(434, 550),
                     Point(424, 532),
                     Point(419, 515), Point(416, 498), Point(416, 481), Point(422, 470), Point(428, 462),
                     Point(440, 455),
                     Point(461, 449), Point(459, 430))
    apple_.setFillColor('black')

    layer.add(apple_)

    return layer


def rotate_body(obj, obj2, second, one_frame):
    arm_layer = obj2.getContents()[1]  # amr_layer get
    arm_layer.adjustReference(732, 551)
    arm_layer.rotate(math.pi * -3)
    arm_layer.move(50, 0)

    for i in range(second // 2):
        obj.scale(1.03 if i < (second // 4) - 2 else 0.96)
        obj.move(9, 4)
        obj.stretch(0.9, 1)
        val = (2 ** 0.6) / 1.43
        obj2.stretch(val, 1)
        time.sleep(one_frame)


#  사과 먹을랑 말랑
def throw_apple(obj, s_arm_layer, seconds, one_frame):
    head_layer = obj.getContents()[2]
    arm_layer = obj.getContents()[1]

    chin_layer = head_layer.getContents()[1]
    side_hair_layer = head_layer.getContents()[2]
    back_hair_layer = head_layer.getContents()[3]

    sleeves_layer = arm_layer.getContents()[2]

    head_layer.adjustReference(781, 273)
    chin_layer.adjustReference(717, 342)
    side_hair_layer.adjustReference(781, 273)
    back_hair_layer.adjustReference(864, 208)

    sleeves_layer.adjustReference(589, 623)

    chin_layer.rotate(math.pi / 12)

    # 먹으려고 가져다 댐1
    for s in range(seconds // 2):
        angle = math.sin(2 * math.pi * (s / seconds)) * 0.9

        head_layer.rotate(-angle * 0.3)
        arm_layer.rotate(angle)

        side_hair_layer.rotate(angle * 0.4)

        time.sleep(one_frame)

    for s in range(seconds // 2):
        angle = math.sin(5 * math.pi * (s / seconds)) * 0.08

        arm_layer.rotate(angle)

        side_hair_layer.rotate(angle * 0.4)

        time.sleep(one_frame)

    # 먹으려고 가져다 댐2
    for s in range(seconds):
        obj.scale(1.007)

        angle = math.sin(math.pi * (s / seconds)) * 0.35

        head_layer.rotate(-angle * 0.22)
        arm_layer.rotate(angle * 1.2)

        chin_layer.rotate(-angle * 1.7)

        sleeves_layer.stretch(1, 1.005)
        sleeves_layer.move(0, 1)

        time.sleep(one_frame)

    # 사과를 내리고 던질 준비
    for s in range(seconds):
        angle = math.sin(0.5 * math.pi * (s / seconds)) * 1.2

        chin_layer.rotate(angle * 1.7)

        if s > seconds // 2:
            arm_layer.rotate(-angle * 2.9)
            head_layer.rotate(-angle * 0.5)
            head_layer.move(-2, 1)

            side_hair_layer.rotate(angle * 1.8)

            obj.move(12, 4)
            obj.rotate(-angle * 1.3)

        time.sleep(one_frame)

    apple_ = arm_layer.getContents()[1].getContents()[1]
    s_arm_layer.scale(0.9)

    # 사과 던지기
    for s in range(seconds):
        obj.scale(1.001)
        obj.move(0, 2)
        s_arm_layer.scale(1.001)

        arm_layer.move(0, 20)

        angle = math.sin(0.5 * math.pi * (s / seconds)) * 1.2

        head_layer.rotate(angle * 2)

        arm_layer.rotate(angle * 0.8)
        arm_layer.move(0, -20)

        obj.rotate(angle * 1.3)

        if s == seconds // 2 + 1:
            s_arm_layer.move(0, -340)
            apple_.moveTo(250, -100)

        if s >= seconds // 2:
            s_arm_layer.move(0, -18)
            s_arm_layer.rotate(angle * 2)

            side_hair_layer.rotate(angle * 2.6)

            apple_.move(0, -210)

            if s >= seconds // 2 + 8:
                obj.move(0, 100)
                s_arm_layer.move(0, 100)
            else:
                obj.move(0, 20)
                s_arm_layer.move(0, 20)

        time.sleep(one_frame)
