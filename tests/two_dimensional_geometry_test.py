import unittest
import numpy as np
from meshpy import Mesh
from meshpy.geometries.two.rectangle import RectangleGeometry


class TwoDimensionalGeometryTest(unittest.TestCase):

    def test_square_coords(self):
        x = np.array([1.0, 3.0, 3.0, 1.0])
        y = np.array([4.0, 4.0, 2.0, 2.0])
        mesh = Mesh.from_coords("square", x, y)
        Mesh.export(mesh, "/tmp/square.geo")
        with open("/tmp/square.geo") as f:
            actual = f.read()
        with open("tests/outputs/square.geo", "r") as f:
            expected = f.read()
        self.assertEqual(actual, expected)

    def test_square_geometry(self):
        square = RectangleGeometry(2, 2, x_offset=2, y_offset=3)
        mesh = Mesh.from_geometry("square", square)
        Mesh.export(mesh, "/tmp/square.geo")
        with open("/tmp/square.geo") as f:
            actual = f.read()
        with open("tests/outputs/square.geo", "r") as f:
            expected = f.read()
        self.assertEqual(actual, expected)

    def test_multiple_meshes(self):
        smaller_square = RectangleGeometry(2, 2)
        larger_square = RectangleGeometry(4, 4)

        smaller_square_mesh = Mesh.from_geometry("smaller_square", smaller_square)
        larger_square_mesh = Mesh.from_geometry("larger_square", larger_square)

        Mesh.export([smaller_square_mesh, larger_square_mesh], "/tmp/multiple_squares.geo")
        with open("/tmp/multiple_squares.geo") as f:
            actual = f.read()
        with open("tests/outputs/multiple_squares.geo", "r") as f:
            expected = f.read()
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
