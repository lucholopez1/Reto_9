import time

class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def set_x(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("El valor de x debe ser un número")
        self._x = value

    def get_y(self):
        return self._y

    def set_y(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("El valor de y debe ser un número")
        self._y = value

    def compute_distance(self, point):
        if not isinstance(point, Point):
            raise TypeError("El argumento debe ser una instancia de la clase Point")
        return ((self._x - point.get_x()) ** 2 + (self._y - point.get_y()) ** 2) ** 0.5


class Line:
    def __init__(self, start_point, end_point):
        if not isinstance(start_point, Point) or not isinstance(end_point, Point):
            raise TypeError("Los puntos de inicio y fin deben ser instancias de la clase Point")
        self._start_point = start_point
        self._end_point = end_point
        self._length = self.compute_length()

    def get_start_point(self):
        return self._start_point

    def set_start_point(self, point):
        if not isinstance(point, Point):
            raise TypeError("El argumento debe ser una instancia de la clase Point")
        self._start_point = point
        self._length = self.compute_length()

    def get_end_point(self):
        return self._end_point

    def set_end_point(self, point):
        if not isinstance(point, Point):
            raise TypeError("El argumento debe ser una instancia de la clase Point")
        self._end_point = point
        self._length = self.compute_length()

    def get_length(self):
        return self._length

    def compute_length(self):
        return self._start_point.compute_distance(self._end_point)


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time of {func.__name__}: {end_time - start_time:.6f} seconds")
        return result
    return wrapper


class Shape:
    shape_type = "Generic Shape"

    def __init__(self, vertices):
        if not vertices:
            raise ValueError("La lista de vértices no puede estar vacía")
        if not all(isinstance(vertex, Point) for vertex in vertices):
            raise TypeError("Todos los vértices deben ser instancias de la clase Point")
        self._vertices = vertices
        self._edges = self.compute_edges()
        self._inner_angles = []
        self._is_regular = False

    @property
    def vertices(self):
        return self._vertices

    @property
    def edges(self):
        return self._edges

    @property
    def inner_angles(self):
        return self._inner_angles

    @inner_angles.setter
    def inner_angles(self, inner_angles):
        self._inner_angles = inner_angles

    @property
    def is_regular(self):
        return self._is_regular

    @is_regular.setter
    def is_regular(self, is_regular):
        self._is_regular = is_regular

    @classmethod
    def set_shape_type(cls, shape_name):
        cls.shape_type = shape_name

    @timing_decorator
    def compute_area(self):
        pass

    def compute_perimeter(self):
        return sum(edge.get_length() for edge in self._edges)

    def compute_edges(self):
        edges = []
        for i in range(len(self._vertices)):
            start_point = self._vertices[i]
            end_point = self._vertices[(i + 1) % len(self._vertices)]
            edges.append(Line(start_point, end_point))
        return edges


class Rectangle(Shape):
    def __init__(self, width, height):
        if not (isinstance(width, (int, float)) and isinstance(height, (int, float))):
            raise ValueError("El ancho y el alto deben ser números")
        if width <= 0 or height <= 0:
            raise ValueError("El ancho y el alto deben ser valores positivos")
        bottom_left = Point(0, 0)
        bottom_right = Point(width, 0)
        top_right = Point(width, height)
        top_left = Point(0, height)
        vertices = [bottom_left, bottom_right, top_right, top_left]
        super().__init__(vertices)
        self.width = width
        self.height = height

    @timing_decorator
    def compute_area(self):
        return self.width * self.height

    def compute_perimeter(self):
        return 2 * (self.width + self.height)
