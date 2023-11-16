data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]
def filter_integer_values(item):    
    return list(map(int, filter(str.isdigit, item.split())))

int_values = []
for item in data:
    integer_values = filter_integer_values(item)
    int_values.append(integer_values)

print(int_values)