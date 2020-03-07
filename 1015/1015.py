# -*- coding: utf-8 -*-

import math
x1, y1 =  [float(j) for j in (input().split(' '))]
x2, y2 =  [float(j) for j in (input().split(' '))]

r = math.sqrt((x2 - x1)*(x2 - x1) + (y2-y1)*(y2-y1))
print("%.4f" % r)
