def point(x, y):
    return x, y

def line_equation_of(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    
    def calc_gradient():
        return (y2 - y1) / (x2 - x1)
    
    gradient = calc_gradient()
    c = y1 - gradient * x1
    
    return f"y = {gradient:.2f}x + {c:.2f}"

print("Persamaan garis yang melalui titik A dan B:")
print(line_equation_of(point(1, 0), point(6, 7)))