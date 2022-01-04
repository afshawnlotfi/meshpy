from typing import Union
import numpy as np
from meshpy.geometry import Geometry


class Point:
    def __init__(self, index: int, x: float, y: float, z: float = None, other: float = 1.0):
        self.index = index
        self.x = x
        self.y = y
        self.z = z if z else 0.0
        self.other = other


class Line:
    def __init__(self, index: int, point1: Point, point2: Point):
        self.index = index
        self.point1 = point1
        self.point2 = point2


class Mesh:
    def __init__(self, name: str, points: list[Point], lines: list[Line]) -> None:
        self.name = name
        self.points = points
        self.lines = lines

    @staticmethod
    def from_geometry(name: str, geometry: Geometry) -> "Mesh":
        points = [
            Point(i, x, y, z)
            for (i, x, y, z) in geometry.grouped
        ]

        lines = [
            Line(i, points[i], points[i+1 if (i+1)
                 < geometry.point_quantity else 0])
            for i in range(0, geometry.point_quantity)
        ]

        return Mesh(name, points, lines)

    @staticmethod
    def from_coords(name: str, x: np.ndarray, y: np.ndarray, z: np.ndarray = None) -> "Mesh":
        geometry = Geometry(x, y, z)
        return Mesh.from_geometry(name, geometry)

    def export(mesh: Union["Mesh", list["Mesh"]], filename: str) -> Union[str, None]:
        meshes = mesh if isinstance(mesh, list) else [mesh]
        if filename.endswith(".geo"):
            from meshpy.exporters.geo import GeoCFDMeshExporter
            GeoCFDMeshExporter.export(meshes, filename)
        else:
            raise NotImplementedError("Other CFD meshes not yet implemented")
