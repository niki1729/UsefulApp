def unique_in_order(iterable):
    iterable = list(iterable)
    print(iterable)
    for i in range(len(iterable)):
        for i in range(len(iterable) - 1):
            try:
                if iterable[i] == iterable[i + 1]:
                    iterable.pop(i)
            except:
                pass
    return iterable


print(unique_in_order('AAAABBBCCcccDDAABBB'))
