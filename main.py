def point_in(xa, ya, xb, yb, xc,yc,xd,yd) :
        t1 = ((xd - xa)*(yb-ya)-(yd-ya)*(xb-xa))
        t2 = ((xd - xb)*(yc-yb)-(yd-yb)*(xc-xb))
        t3 = ((xd - xc)*(ya-yc)-(yd-yc)*(xa-xc))
        t4 =((xa - xc)*(yb-yc)-(ya-yc)*(xb-xc))
        return t1 * t2 * t3 * t4 > 0

xa, ya = map(int,input().split())
xb, yb = map(int,input().split())
xc, yc = map(int,input().split())
xd, yd = map(int,input().split())

if point_in(xa, ya, xb, yb, xc,yc,xd,yd) :
    print('Выпуклый')
    # вычисление длин сторон четырехугольника
    
    from math import sqrt
    
    dist_ab = sqrt((xa - xb)**2 + (ya - yb)**2)
    dist_bc = sqrt((xb - xc)**2 + (yb - yc)**2)
    dist_cd = sqrt((xc - xd)**2 + (yc - yd)**2)
    dist_da = sqrt((xd - xa)**2 + (yd - ya)**2)
    
    # вычисление площади четырехугольника через два трёхугольника по формуле Герона
    t = sqrt (dist_ab ** 2 + dist_bc ** 2)
    p = (dist_cd + dist_da + t) / 2
    s1 = sqrt (p * (p - dist_cd) * (p - dist_da) * (p - t))
    
    t = sqrt (dist_cd ** 2 + dist_da ** 2)
    p = (dist_ab + dist_bc + t) / 2
    s2 = sqrt (p * (p - dist_ab) * (p - dist_bc) * (p - t))
    
    s = s1 + s2
    print('Площадь четырехугольника = ', s)
else :
    print('Невыпуклый или не четырехугольник')
	
