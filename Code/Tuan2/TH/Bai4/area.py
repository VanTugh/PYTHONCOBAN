import math
from Bai4.distance import tinhkc
def area(x1,x2,x3,y1,y2,y3):
    AB = tinhkc(x1,x2,y1,y2)
    BC = tinhkc(x2,x3,y2,y3)
    AC = tinhkc(x1,x3,y1,y3)
    p = (AB + AC + BC)/2
    dtich = math.sqrt(p*(p-AB)*(p-AC)*(p-BC))
    return dtich