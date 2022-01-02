from typing import Union
import numpy as np
from meshpy.geometry import Geometry
from enum import Enum

class ExportType(Enum):
    Geo = 1

class Point:
    def __init__(self, index: int, x: float, y: float, z: float = 0, other=1):
        self.index = index
        self.x = x
        self.y = y
        self.z = z
        self.other = other


class Line:
    def __init__(self, index: int, point1: Point, point2: Point):
        self.index = index
        self.point1 = point1
        self.point2 = point2


class Mesh:
    def __init__(self, points: list[Point], lines: list[Line]) -> None:
        self.points = points
        self.lines = lines

    @staticmethod
    def from_geometry(geometry: Geometry) -> "Mesh":
        points = [
            Point(i, x, y, z)
            for (i, x, y, z) in geometry.grouped
        ]

        lines = [
            Line(i, points[i], points[i+1 if (i+1) < geometry.point_quantity else 0])
            for i in range(0, geometry.point_quantity)
        ]

        return Mesh(points, lines)

    @staticmethod
    def from_coords(x: np.ndarray, y: np.ndarray, z: np.ndarray = None) -> "Mesh":
        geometry = Geometry(x, y, z)
        return Mesh.from_geometry(geometry)

    def export(self, to: ExportType, filename:str=None) -> Union[str, None]:
        if to == ExportType.Geo:
            from meshpy.generators.geo import GeoCFDMesh
            export = GeoCFDMesh.export(self)
            if filename:
                with open(filename, "w") as f:
                    f.write(export)
            else:
                return export
        else:
            raise NotImplementedError("Other CFD meshes not yet implemented")
