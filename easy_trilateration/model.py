class Point:
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        self.x = x_init
        self.y = y_init

    def __repr__(self):
        return "".join(["Point(", str(self.x), ",", str(self.y), ")"])

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Point):
            return (self.x == other.x) & (self.y == other.y)
        return False

    def __hash__(self):
        return hash(str(self))


class Circle:
    center: Point
    radius: float

    def __init__(self, x: float, y: float, r: float):
        self.center = Point(x, y)
        self.radius = r

    def __repr__(self):
        return "".join(["Circle(", str(self.center.x), ", ", str(self.center.y), ", ", str(self.radius), ")"])

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Circle):
            return (self.center.x == other.center.x) & (self.center.y == other.center.y) & (self.radius == other.radius)
        return False


class Trilateration:
    sniffers: [Circle]
    result: Circle

    def __init__(self, sniffers: [Circle], result: Circle = None):
        self.sniffers = sniffers
        self.result = result
