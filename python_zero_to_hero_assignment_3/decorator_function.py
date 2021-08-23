def div_function(a,b):
    return a/b


def mask_function(function):
    def smart_div_function(a,b):
        if a<b:
            a,b = b,a
        return function(a,b)
    return smart_div_function

new_div_func = mask_function(div_function)
print(new_div_func(8,16))