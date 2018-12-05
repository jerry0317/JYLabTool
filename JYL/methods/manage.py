def verifySingularity(names, returnSet=False, exception=False, exceptionText=None):
    nameSet = set()
    for n in names:
        if n in nameSet:
            if exception is True:
                if exceptionText is None:
                    return Exception("Input is not singular.")
                else:
                    return Exception(exceptionText)
            else:
                return False
        else:
            nameSet.add(n)
    if returnSet is True:
        return nameSet
    else:
        return True

def verifyEqualityOfSets(sets, returnSet=False):
    l = len(sets)
    bl = True
    if l == 0:
        bl = True
        rSet = set()
    elif l == 1:
        bl = True
        rSet = sets[0]
    else:
        rSet = sets[0]
        for i in range(1, l):
            if sets[i] != sets[i-1]:
                bl = False
    if bl is True:
        if returnSet is True:
            return rSet
        else:
            return True
    else:
        return False
