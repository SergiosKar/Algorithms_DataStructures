S=[3,5,6,2]

def powerset(seq):
    """
    Returns all the subsets of this set. This is a generator.
    """
    if len(seq) <= 1:
        yield seq
        yield []
    else:
        for item in powerset(seq[1:]):
            yield [seq[0]]+item
            yield item

pSet=powerset(S)# pSet is a generator due to yields
for i in pSet:
    print(i)


