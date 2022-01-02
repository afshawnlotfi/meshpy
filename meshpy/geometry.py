import numpy as np


class Geometry:
    def __init__(self, x: np.ndarray, y: np.ndarray, z: np.ndarray = None) -> None:
        assert len(x) == len(y), "geometry point length must match"
        self.x = x
        self.y = y
        self.z = z
        self.point_quantity = len(self.x)

    @property
    def grouped(self) -> list[tuple[int, float, float]]:
        return [
            tuple((i, self.x[i], self.y[i], self.z[i] if self.z else 0))
            for i in range(0, self.point_quantity)
        ]
