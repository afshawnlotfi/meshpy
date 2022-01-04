import numpy as np
from meshpy import Geometry

class RectangleGeometry(Geometry):
    def __init__(
        self,
        length: float,
        width: float,
        x_offset: float = 0.0,
        y_offset: float = 0.0
    ) -> None:
        x = np.array([-length/2, length/2, length/2, -length/2]) + x_offset
        y = np.array([width/2, width/2, -width/2, -width/2]) + y_offset
        super().__init__(x, y)