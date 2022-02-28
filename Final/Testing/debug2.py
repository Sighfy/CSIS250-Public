"""
Fix the code below
"""


class Point4D():
    def __init__(self, w, x, y, z):
        self.w = w
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return '{}, {}, {}, {}'.format(self.w, self.x, self.y, self.z)


my_4d_point = Point4D(1, 2, 3, 1)
print(my_4d_point)  # should print '1, 2, 3, 1'
