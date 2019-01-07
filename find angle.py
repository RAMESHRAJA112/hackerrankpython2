import math

degree_sign= u'\N{DEGREE SIGN}'

AB = int(raw_input())
BC = int(raw_input())
hyp = math.pow(((AB*AB) + (BC*BC)), 0.5)

num = (BC*BC) + (hyp*hyp) - (AB*AB)
den = (2*(BC*hyp))
angle_C = math.degrees(math.acos(num/den))

print (str(int(round(angle_C))) + degree_sign)
