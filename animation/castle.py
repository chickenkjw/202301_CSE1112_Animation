from cs1graphics import *
import time
import math


def castle():
    layers = Layer()

    left_castle = Polygon(Point(133, 613), Point(178, 613), Point(183, 554), Point(174, 553), Point(187, 526),
                          Point(215, 524), Point(218, 495), Point(212, 491), Point(212, 488), Point(230, 480),
                          Point(231, 466), Point(224, 465), Point(224, 461), Point(230, 461), Point(230, 455),
                          Point(234, 455), Point(235, 461), Point(240, 461), Point(240, 466), Point(236, 466),
                          Point(238, 481), Point(257, 485), Point(257, 492), Point(251, 495), Point(252, 523),
                          Point(277, 526), Point(290, 554), Point(284, 554), Point(283, 611), Point(409, 617),
                          Point(414, 742), Point(137, 744))
    left_castle.setFillColor('white')
    left_castle.setBorderColor('white')

    left_castle_layer = Layer()
    left_castle_layer.add(left_castle)

    right_castle = Polygon(Point(541, 745), Point(545, 564), Point(524, 532), Point(501, 560), Point(503, 640),
                           Point(472, 609), Point(337, 603), Point(338, 574), Point(316, 543), Point(297, 575),
                           Point(295, 743))
    right_castle.setFillColor('white')
    right_castle.setBorderColor('white')

    right_castle_layer = Layer()
    right_castle_layer.add(right_castle)

    layers.add(left_castle_layer)
    layers.add(right_castle_layer)

    return layers

