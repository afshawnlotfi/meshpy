from meshpy.mesh import Mesh
from meshpy.utils.str import newline, indent


class GeoCFDMeshExporter:

    @staticmethod
    def mesh_macro(mesh: Mesh, start_index: int = 0.0) -> str:
        points = newline.join(
            [
                f"{indent}Point({point.index + 1 + start_index}) = {{{point.x}, {point.y}, {point.z}, {point.other}}};"
                for point in mesh.points
            ]
        )

        lines = newline.join(
            [
                f"{indent}Line({line.index + 1 + start_index}) = {{{line.point1.index + 1 + start_index}, {line.point2.index + 1 + start_index}}};"
                for line in mesh.lines
            ]
        )

        return newline.join(
            [
                f"Macro {mesh.name}",
                points,
                lines,
                "Return",
                f"Call {mesh.name};",
            ]
        )

    @staticmethod
    def export(meshes: list[Mesh], filename: str) -> str:
        macros = []
        start_index = 0
        for mesh in meshes:
            macro = GeoCFDMeshExporter.mesh_macro(mesh, start_index)
            start_index += len(mesh.points)
            macros.append(macro + newline)


        with open(filename, "w") as f:
            f.write(
                newline.join(macros)
            )
