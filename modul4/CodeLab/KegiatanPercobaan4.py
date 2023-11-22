import math

def translasi(tx, ty):
    def calc_translasi(x, y):
        return x + tx, y + ty
    return calc_translasi

def dilatasi(sx, sy):
    return lambda x, y: (sx * x, sy * y)

def rotasi(sudut):
    radian = math.radians(sudut)
    return lambda x, y: (x * math.cos(radian) - y * math.sin(radian),
                        x * math.sin(radian) + y * math.cos(radian))

titik_awal = (3, 5)

translasi_function = translasi(2, -1)(*titik_awal)
dilatasi_function = dilatasi(2, -1)(*titik_awal)
rotasi_function = rotasi(30)(*titik_awal)

print("Setelah translasi:", translasi_function)
print("Setelah dilatasi:", dilatasi_function)
print("Setelah rotasi:", rotasi_function)