class Vector:

    def __init__(self, vector):
            self.vector = list(vector)

    def __iter__(self):
        self.iteration = 0
        return self

    def __next__(self):
        if self.iteration < self.__len__():
            self.iteration += 1
            return self.iteration - 1
        else:
            raise StopIteration


    def __len__(self):
        return len(self.vector)

    def __getitem__(self, item):
        return self.vector[item]

    def sum(self, vec2):
        for index in range(0, len(self.vector)):
            self.vector[index] += vec2[index]

    def sub(self, vec2):
       for index in range(0, len(self.vector)):
            self.vector[index] -= vec2[index]

    def mul_const(self, const):
        for index in range(0, len(self.vector)):
            self.vector[index] *= const

    def mul_scal(self, vec2):

        result = 0
        for index in range(0, len(self.vector)):
            result += vec2[index] * self.vector[index]
        return result
    def compare(self, vec2):
        for index in range(0, len(self.vector)):
            if self.vector[index] != vec2[index]:
                return False

        return True

    def len(self):
        result = 0;
        for arg in self.vector:
            result += arg ** 2
        return result ** (1/2)
    def __str__(self):
        string = ""
        for arg in self.vector:
            string += str(arg) + ", "
        return string

vector1 = Vector([4, -5, 9, 7])
vector2 = Vector([3, 6, -4, 2])
vector1.sum(vector2)
print(vector1)
vector1.sub(vector2)
print(vector1)
vector1.mul_scal(vector2)
print(vector1)
vector1.mul_const(2)
print(vector1)
print(vector1.compare(vector2))
vec3 = vector1
print(vector1.compare(vec3))
print(vector1.len())