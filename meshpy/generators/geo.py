from meshpy.mesh import Mesh
from meshpy.utils.str import newline

class GeoCFDMesh:

    @staticmethod
    def export(mesh: Mesh) -> str:
        points = newline.join(
            [
                f"Point({point.index + 1}) = {{{point.x}, {point.y}, {point.z}, {point.other}}};"
                for point in mesh.points
            ]
        )

        lines = newline.join(
            [
                f"Line({line.index + 1}) = {{{line.point1.index + 1}, {line.point2.index + 1}}};"
                for line in mesh.lines
            ]
        )

        return newline.join(
            [points, lines]
        )
