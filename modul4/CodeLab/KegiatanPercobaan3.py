def title_decorator(text):
    def wrapper():
        func = text()
        make_title = func.title()
        print(make_title + " - Data is converted to title case")
        return make_title
    return wrapper

def split_string(text):
    def wrapper():
        func = text()
        splitted_string = func.split()
        print(str(splitted_string) + " - Then data is splitted")
        return splitted_string
    return wrapper

@split_string
@title_decorator

def say_hi():
    return 'hello there'

say_hi()