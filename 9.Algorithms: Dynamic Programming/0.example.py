def memoize_add_to_80():
    cache = {}
    def inner_memo(n):
        if n in cache:
            print('short time')
            return cache[n]
        else:
            print('long time')
            cache[n] = n + 80
            return cache[n]
    return inner_memo

memo = memoize_add_to_80()
print(memo(5))
print(memo(6))
print(memo(5))
