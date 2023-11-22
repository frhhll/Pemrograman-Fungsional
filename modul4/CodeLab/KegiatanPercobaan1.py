def perkalian (a):
    def dengan (b):
        return a*b
    return dengan

hasil_perkalian = perkalian(5)
print(hasil_perkalian(3))

hasil_perkalian = perkalian(5)(3)
print(hasil_perkalian)