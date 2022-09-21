# código para ver se duas retas formadas por quatro pontos se interceptam

x1 = float( input("x1: ") )
y1 = float( input("y1: ") )
 
x2 = float( input("x2: ") )
y2 = float( input("y2: ") )
 
x3 = float( input("x3: ") )
y3 = float( input("y3: ") )
 
x4 = float( input("x4: ") )
y4 = float( input("y4: ") )
 
# Posição de P3 em relação a P1 e P2
pt3 = (y2 - y1) * (x3 - x1) - (x2 - x1) * (y3 - y1)
 
# Posição de P4 em relação a P1 e P2
pt4 = (y2 - y1) * (x4 - x1) - (x2 - x1) * (y4 - y1)
 
 
if (pt3 == 0.0) and (pt4 == 0.0):   # Trata-se de segmentos colineares?
    if x1 == x2: # se s1 é vertical => s2 também é vertical!
      result = (min(y1, y2) <= max(y3, y4)) and (min(y3, y4) <= max(y1, y2))
    else:        # os segmentos não são verticais
      result = (min(x1, x2) <= max(x3, x4)) and (min(x3, x4) <= max(x1, x2))
 
else:  # os segmentos não são colineares
    # Posição de P1 em relação a P3 e P4
    pt1 = (y4 - y3) * (x1 - x3) - (x4 - x3) * (y1 - y3)
 
    # Posição de P2 em relação a P3 e P4
    pt2 = (y4 - y3) * (x2 - x3) - (x4 - x3) * (y2 - y3)
 
    # os segmentos só irão se interceptar se os sinais forem todos opostos
    result = ((pt3 * pt4) <= 0.0) and ((pt1 * pt2) <= 0.0)
 
 
if result:
    print("Os segmentos s e t se interceptam!")
else:
    print("Os segmentos s e t não se interceptam!")