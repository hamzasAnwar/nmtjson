import functools
print = functools.partial(print, flush=True)

print('haz',flush=True)
