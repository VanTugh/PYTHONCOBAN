import math
from collections import namedtuple
from typing import Tuple , List

Point = namedtuple('Point',['x','y'])
def distance_to_origin(p : Point)-> float:
    return math.hypot(p.x,p.y)
def triangle_area(p1: Point , p2: Point, p3: Point)-> float:
    return 0.5 * abs(p1.x * (p2.y - p3.y)+
                     p2.x * (p3.y - p1.y)+
                     p3.x * (p1.y - p2.y))
