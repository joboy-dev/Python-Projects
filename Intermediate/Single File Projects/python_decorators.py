import time
current_time = time.time()
print(current_time)

def speed_calc_decorator(func):
    def calculate_speed():
        func()
        running_time = time.time() - current_time
        print(f'Total running time: {running_time}')
    return calculate_speed

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i
