def point(x, y):
    return x, y

def line_equation_of(p1, M):
    x1, y1 = p1

    def calc_constanta(x, y, m):
        return y - m * x
    
    def result():
        C = calc_constanta(x1, y1, M)
        print(f"y = {M:.2f}x + {C:.2f}") 

    return result

print("Persamaan garis yang melalui titik (0, 6) dan bergradien 7:")
hasil = line_equation_of(point(0, 6), 7)
# del line_equation_of
hasil()