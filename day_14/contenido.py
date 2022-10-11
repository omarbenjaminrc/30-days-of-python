# Higher Order Functionsd

def uppercase_decorator(function):
    def wrapper(n):
        func = function(n)
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper


@uppercase_decorator
def greeting(nombre):
    return f'Welcome to Python {nombre}'
print(greeting('Omar'))

def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(
        first_name, last_name, country))

print_full_name("Asabeneh", "Yetayeh",'Finland')