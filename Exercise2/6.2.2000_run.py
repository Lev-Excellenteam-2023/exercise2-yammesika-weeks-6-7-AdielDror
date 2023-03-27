import timeit


# The function measures how long the function f ran on the given parameters
def timer(f, *args, **kwargs):
    if kwargs:  # If the passed parameter is a dictionary
        start = timeit.default_timer()  # The start of the function's runtime
        f(**kwargs)
    else:
        start = timeit.default_timer()
        f(args)
    stop = timeit.default_timer()  # End of function runtime
    print('Time: ', stop - start)


timer(print, "Hello")
timer(zip, [1, 2, 3], [4, 5, 6])
timer("Hi {name}".format, name="Bug")
