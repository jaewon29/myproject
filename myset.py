class Set:
    def __init__(self, value = []):    # Constructor
        self.data = []                 # Manages a list
        self.concat(value)

    def intersection(self, other):        # other is any sequence
        res = []                       # self is the subject
        for x in self.data:
            if x in other:             # Pick common items
                res.append(x)
        return Set(res)                # Return a new Set

    def union(self, other):            # other is any sequence
        res = self.data[:]             # Copy of my list
        for x in other:                # Add items in other
            if not x in res:
                res.append(x)
        return Set(res)

    def concat(self, value):
        for x in value:                
            if not x in self.data:     # Removes duplicates
                self.data.append(x)
    
    def issubset(self, other):
        res = []
        for x in self.data:
            if x in other:
                res.append(x)
        if sorted(res) == sorted(self):
            return True
        else:
            return False
    
    def ispropersubset(self, other):
        res = []
        for x in self.data:
            if x in other:
                res.append(x)
        if sorted(res) == sorted(self):
            if sorted(self) == sorted(other):
                return False
            else:
                return True
        else:
            return False

    def issuperset(self, other):
        res = []
        for x in other.data:
            if x in self:
                res.append(x)
        if sorted(res) == sorted(other):
            return True
        else:
            return False

    def ispropersuperset(self, other):
        res = []
        for x in other.data:
            if x in self:
                res.append(x)
        if sorted(res) == sorted(other):
            if sorted(other) == sorted(self):
                return False
            else:
                return True
        else:
            return False

    def update(self, other):
        for x in other.data:
            self.append(x)
        return self

    def intersection_update(self, other):
        for x in self.data:
            if x not in other.data:
                x.remove(self)
            else:
                pass
        return self

    def symmetric_difference_update(self, other):
        for x in self.data:
            if x in other.data:
                self.remove(x)
            else:
                pass
        for y in other.data:
            if y not in self.data:
                self.append(y)
            else:
                pass
        return self
    
    def add(self, elem):
        self.data.append(elem)
        return self
    
    def remove(self, elem):
        try:
            if elem in self.data:
                self.data.remove(elem)
                return self
            else:
                raise Exception("ValueError: list.remove(x): x not in list")
        except Exception as e:
            print('유효한 값이 아닙니다.', e)



    def __len__(self):          return len(self.data)        # len(self)
    def __getitem__(self, key): return self.data[key]        # self[i], self[i:j]
    def __and__(self, other):   return self.intersection(other) # self & other
    def __or__(self, other):    return self.union(other)     # self | other
    def __repr__(self):         return 'Set({})'.format(repr(self.data))  
    def __iter__(self):         return iter(self.data)       # for x in self:
    def __le__(self, other):    return self.issubset(other)
    def __lt__(self, other):    return self.ispropersubset(other)
    def __ge__(self, other):    return self.issuperset(other)
    def __gt__(self, other):    return self.ispropersuperset(other)




x = Set([1,3,5,7, 1, 3])
y = Set([2,1,4,5,6])
a = Set([1, 2, 3, 4])
b = Set([1, 2, 3, 4])
print(x, y, len(x))
print(x.intersection(y), y.union(x))
print(x & y, x | y)
print(x[2], y[:2])
for element in x:
    print(element, end=' ')
print()
print(3 not in y)  # membership test
print(list(x))   # convert to list because x is iterable
print(x.remove(9))