import sys
import os
import os.path
from os import path
import fileinput

if len(sys.argv) < 3:
    print("Please enter class name argument and godot calss to extent.")
    print("For example : \npython new_file.py Enemy KinematicBody2D")
    exit(0)

tab = "    "
class_name = sys.argv[1]
cpp_file = class_name.lower() + ".cpp"
h_file = class_name.lower() + ".h"
godot_class = sys.argv[2]

if path.exists(cpp_file) or path.exists(h_file):
    print(cpp_file + " or " + h_file + " exists. Creation of files is aborded.")
    exit()

######### H START #########
h = open(h_file, "w")

h.write("#ifndef " + class_name.upper() + "_H\n")
h.write("#define " + class_name.upper() + "_H\n\n")
h.write("#include <Godot.hpp>\n")
h.write("#include <" + godot_class + ".hpp>\n\n")
h.write("namespace godot {\n\n")
h.write("class " + class_name + " : public " + godot_class + " {\n")
h.write(tab + "GODOT_CLASS(" + class_name + ", " + godot_class + ")\n\n")
h.write("public:\n")
h.write(tab + "static void _register_methods();\n\n")
h.write(tab + class_name + "();\n")
h.write(tab + "~" + class_name + "();\n\n")
h.write(tab + "void _init();\n\n")
h.write(tab + "void _ready();\n\n")
h.write("};\n")
h.write("}\n")
h.write("#endif")

h.close()

######### H END #########


######### CPP START #########
cpp = open(cpp_file, "w")
cpp.write("#include \"" + h_file + "\"\n\n")
cpp.write("using namespace godot;\n\n")
cpp.write("void " + class_name + "::_register_methods() {\n")
cpp.write(tab + "register_method(\"_int\", &" + class_name + "::_init);\n")
cpp.write(tab + "register_method(\"_ready\", &" + class_name + "::_ready);\n}\n\n")
cpp.write(class_name + "::" + class_name + "() {\n\n}\n\n")
cpp.write(class_name + "::~" + class_name + "() {\n\n}\n\n")
cpp.write("void " + class_name + "::_init() {\n\n}\n")
cpp.write("void " + class_name + "::_ready() {\n\n}\n")
cpp.close()
######### CPP END #########

######## gdlibrary.cpp START ##########
gd = open("gdlibrary.cpp", "r")
h_file = "#include \"" + h_file + "\""
for line in gd:
    if h_file in line:
        print(h_file + " exists in the gdlibrary.\n")
        print("gdlibrary.cpp have not been modified.")
        exit(0)

gd = fileinput.FileInput("gdlibrary.cpp", inplace=1)

for linenum, line in enumerate( gd ):
    if linenum == 0:
        print(h_file)
    if "godot::Godot::nativescript_init(handle);" in line:
        line=line.replace(line,
                line + tab + "godot::register_class<godot::" + class_name + ">();\n")

    print(line, end='')

gd.close()