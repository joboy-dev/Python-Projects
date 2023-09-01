
# class User:
#     def __init__(self, name):
#         self.name = name
#         self.is_logged_in = False

# def is_authenticated_decorator(function):
#     def wrapper(*args, **kwargs):
#         if args[0].is_logged_in == True:
#             function(args[0])
#     return wrapper

# @is_authenticated_decorator
# def create_blog_post(user):
#     print(f"This is {user.name}'s new blog post.")

# new_user = User("Joseph")
# new_user.is_logged_in = True
# create_blog_post(new_user)


# CHALLENGE
def logging_decorator(func):
    def wrapper(*args, **kwargs):
        print(func.__name__)
        print(args)
        result = func(args[0])
        print(f'Result is {result}')
    return wrapper

@logging_decorator
def new_function(number):
    print(f'This is number {number}')
    return number
    
new_function(3)