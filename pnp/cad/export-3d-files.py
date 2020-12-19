FREECADPATH = '/usr/lib/freecad/lib/'
import sys
sys.path.append(FREECADPATH)
import FreeCAD
import MeshPart

# Open Assembly
assembly = FreeCAD.open("assembly.FCStd")

for obj in assembly.Objects:
    if ("b_FDM" in obj.Name and not ("Body_001_" in obj.Name)):
        shape = obj.Shape
        shape.Placement = obj.getGlobalPlacement()
        mesh = assembly.addObject("Mesh::Feature", "Mesh")
        mesh.Mesh=MeshPart.meshFromShape(Shape=shape, LinearDeflection=0.01, AngularDeflection=0.025, Relative=False)
        mesh.Label=obj.Name
        mesh.Mesh.write("3D-Prints/" + obj.Name.split("00_")[1].split("_001_")[0] + ".stl")

FreeCAD.closeDocument(assembly.Name)