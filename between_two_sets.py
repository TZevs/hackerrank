import math

def getTotalX(a, b):
    allCFS = []
    
    for i in b:
        for x in range(1, i+1):
            if x % i == 0:
                allCFS.append(x)

    cfs = set(allCFS)
    print("CFS: ", cfs)
    cms = []

    if len(a) == 1 and a[0] in cfs:
        cms.append(a[0])
    elif len(a) == 0 or (len(a) == 1 and a[0] not in cfs):        
        return 0
    else:
        for j in a:
            for x in cfs:
                if x % j == 0:
                    cms.append(x)

    cmsAlsoCfs = set(cms)
    print("CMs: ", cmsAlsoCfs)
    final = cfs.intersection(cmsAlsoCfs)
    print(final)
    return len(final)

# print(getTotalX([2], [20, 30, 12]))
# print(getTotalX([2, 4], [24, 32, 96]))

def getMultiplesFactors(a, b):
    cfs = []
    cms = []

    if len(a) == 0 or len(b) == 0:
        return 0
    elif len(a) == 1:
        cfs.append(a[0])
        for i in b:
            if i % cfs[0] == 0:
                continue
            else:
                return 0
        return 1
    else:
        LCM = math.lcm(a[0], a[1])
        GCF = math.gcd(b[0], b[1])

        if len(a) > 2:
            for i in range(2, len(a)):
                LCM = math.lcm(LCM, a[i])

        if len(b) > 2:
            for j in range(2, len(b)):
                GCF = math.gcd(GCF, b[j])

        cfs.append(LCM)
        cms.append(GCF)
        print("LCM: ", LCM)
        print("GCF: ", GCF)

        for i in range(2, GCF):
            if GCF % i == 0:
                cfs.append(i)

        cfsSet = set(cfs)

        for k in a:
            for j in range(LCM+1, min(b)):
                if k % j == 0:
                    cms.append(k)

        # for j in range(LCM+1, min(b)):
        #     #print('Possible CMs: ', j)
        #     for k in a:
        #         #print("In A: ", k)
        #         if j % k == 0:
        #             #print("CM to add:", k)
        #             cms.append(k)        

        cmsSet = set(cms)

        combined = cfsSet.intersection(cmsSet)

        print("CFs: ", cfs)
        print("CMs: ", cms)
        print("Set: ", combined)
        return len(combined)

# print("First:")
# print(getMultiplesFactors([2], [20, 30, 12]))
# print("Second:")
# print(getMultiplesFactors([2, 4], [16, 32, 96]))

def getFactors(a, b): 
    cfs = []
    cms = []

    if len(a) == 0 or len(b) == 0:
        return 0
    elif len(a) == 1:
        cfs.append(a[0])
        for i in b:
            if i % cfs[0] == 0:
                continue
            else:
                return 0
        return 1
    else:
        LCM = math.lcm(a[0], a[1])
        GCF = math.gcd(b[0], b[1])

        if len(a) > 2:
            for i in range(2, len(a)):
                LCM = math.lcm(LCM, a[i])

        if len(b) > 2:
            for j in range(2, len(b)):
                GCF = math.gcd(GCF, b[j])
        
        cfs.append(LCM)
        cms.append(GCF)
        print("LCM: ", LCM)
        print("GCF: ", GCF)

        for i in range(2, GCF):
            if GCF % i == 0:
                cfs.append(i)

        cfsSet = set(cfs)
        print("CFs: ", cfsSet)

        for i in a:
            for j in cfsSet:
                if j % i == 0:
                    cms.append(j)

        cmsSet = set(cms)
        print("CMs: ", cmsSet)
        combined = cfsSet.intersection(cmsSet)
        print(combined)
        return len(combined)

# print("First:")
# print(getFactors([2], [20, 30, 12]))
# print("Second:")
# print(getFactors([2, 4], [16, 32, 96]))
# print("Third:")
# print(getFactors([3, 4], [24, 48]))

def actuallyGetFactors(a, b):
    maxFactor = min(b)
    factors = []
    
    for i in b:
        for j in range(1, maxFactor):
            if i % j == 0:
                factors.append(j)

    factors = set(factors)
    print("Before:", factors)
    for i in a:
        for j in list(factors):
            if j % i == 0:
                continue
            else:
                factors.add(j)

    return len(factors)

print("1st")
print(actuallyGetFactors([2], [20, 30, 12]))
print("2nd:")
print(actuallyGetFactors([2, 4], [16, 32, 96]))
print("3rd:")
print(actuallyGetFactors([3, 4], [24, 48]))