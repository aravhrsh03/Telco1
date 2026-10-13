from pydantic import BaseModel

class SetOperations(BaseModel):
    setList: set

    def intersection(self, setAnother: set):
        intersection = []

        for item in self.setList:
            if item in setAnother:
                intersection.append(item)

        return intersection

    def union(self, setAnother: set):
        union = []

        for item in self.setList:
            if item not in union:
                union.append(item)

        for item in setAnother:
            if item not in union:
                union.append(item)

        return union

    def difference(self, setAnother: set):
        difference = []

        for item in self.setList:
            if item not in setAnother:
                difference.append(item)

        return difference

    def symmetric_difference(self, setAnother: set):
        symmetric_difference = []

        for item in self.setList:
            if item not in setAnother:
                symmetric_difference.append(item)

        for item in setAnother:
            if item not in self.setList:
                symmetric_difference.append(item)

        return symmetric_difference

A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}

setA = SetOperations(setList=A)

intersection = setA.intersection(B)
union = setA.union(B)
difference = setA.difference(B)
symmetric_difference = setA.symmetric_difference(B)

print("Intersection : ",intersection)
print("Union : ", union)
print("Difference : ", difference)
print("Symmetric Difference : ", symmetric_difference)