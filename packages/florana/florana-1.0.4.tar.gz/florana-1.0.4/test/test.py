def gen(n):
    if not n or n < 0:
        raise StopIteration("hello, error")
    for i in range(n):
        yield i

try:
    for e in gen(-1):
        print(e)
except Exception as e:
    raise e.__context__
