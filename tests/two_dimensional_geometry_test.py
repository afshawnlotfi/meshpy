import unittest
import numpy as np
from meshpy import ExportType, Mesh


class TwoDimensionalGeometryTest(unittest.TestCase):

    def test_square(self):
       x = np.array([1, 3, 3, 1])
       y = np.array([4, 4, 2, 2])
       mesh = Mesh.from_coords(x, y)
       actual = mesh.export(ExportType.Geo)
       with open("tests/outputs/square.geo", "r") as f:
        expected = f.read()
        self.assertEqual(actual, expected)
       
if __name__ == '__main__':
    unittest.main()
