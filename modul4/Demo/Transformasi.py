import math

def transformasi_decorator(trans_func, rot_func, scale_func):
    def decorator(func):
        def wrapper(x, y):
            trans_result = trans_func(x, y)
            rot_result = rot_func(*trans_result)
            scale_result = scale_func(*rot_result)
            return func(*scale_result)
        return wrapper
    return decorator

def translasi(tx, ty):
    return lambda x, y: (x + tx, y + ty)

def rotasi(sudut):
    return lambda x, y: (
        x * math.cos(math.radians(sudut)) - y * math.sin(math.radians(sudut)),
        x * math.sin(math.radians(sudut)) + y * math.cos(math.radians(sudut))
    )

def dilatasi(sx, sy):
    return lambda x, y: (x * sx, y * sy)

def line_equation(x, y, M):
    C = y - M * x
    return f"y = {M:.2f}x + {C:.2f}"

def get_user_input():
    return (
        float(input("Masukkan nilai x titik A: ")),
        float(input("Masukkan nilai y titik A: ")),
        float(input("Masukkan gradien awal: ")),
        float(input("Masukkan nilai translasi tx: ")),
        float(input("Masukkan nilai translasi ty: ")),
        float(input("Masukkan nilai sudut rotasi: ")),
        float(input("Masukkan nilai skala pada sumbu x: ")),
        float(input("Masukkan nilai skala pada sumbu y: "))
    )

def main(user_input, trans, rot, dil, eq):
    x_input, y_input, gradien_awal, tx_input, ty_input, sudut_rotasi, sx_input, sy_input = user_input()
    
    @transformasi_decorator(trans(tx_input, ty_input), rot(sudut_rotasi), dil(sx_input, sy_input))
    def transformed_line_equation(x, y):
        return eq(x, y, gradien_awal)

    result_equation = transformed_line_equation(x_input, y_input)

    print(f"Persamaan garis yang melalui titik ({x_input},{y_input}) dan bergradien {gradien_awal:.2f}:")
    print(eq(x_input, y_input, gradien_awal))
    print("Persamaan garis baru setelah transformasi:")
    print(result_equation)

if __name__ == "__main__":
    main(get_user_input, translasi, rotasi, dilatasi, line_equation)