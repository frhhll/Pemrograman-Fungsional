def uppercase_decorator(function):
    def wrapper():
        func = function()
        return func.upper()
    
    return wrapper

@uppercase_decorator
def say_hi():
    return 'hello there'

result = say_hi()
print(result)