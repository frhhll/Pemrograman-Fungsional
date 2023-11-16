def konversi(j=0):
    def menit(m=0):
        def detik (d=0):
            return ((j*60)+m)*60+d
        return detik
    return menit

data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]

output = []

for item in data:
    components = item.split()  
    minggu = int(components[0])  
    hari = int(components[2])  
    jam = int(components[4])  
    menit = int(components[6])  
    
    total_seconds = ((minggu * 7 * 24 * 60) + (hari * 24 * 60) + (jam * 60) + menit)
    output.append(total_seconds)

print(output)