from functools import wraps

def add_wrapping_with_style(style):
    def add_wrapping(item):
        @wraps(item)
        def wrapped_item():
            return f'a {style} wrapped up box of {item()}'
        return wrapped_item
    return add_wrapping

@add_wrapping_with_style('horribly')
@add_wrapping_with_style('beautifully')
def new_gpu():
    return 'a new Tesla P100 GPU'

print(new_gpu())