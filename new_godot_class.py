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
if not path.exists(godot_class.lower() + ".h"):
    h.write("#include <Godot.hpp>\n")
    h.write("#include <" + godot_class + ".hpp>\n\n")
else:
    h.write("#include \"" + godot_class.lower() + ".h\"\n\n")
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

######### GDNS START #########
if not path.exists("../scripts"):
    scripts_path = os.path.abspath(os.getcwd())
    scripts_path = os.path.abspath(os.path.join(scripts_path, os.pardir))
    scripts_path = os.path.abspath(os.path.join(scripts_path, "scripts"))
    os.mkdir(scripts_path)

gdn = open("../scripts/" + class_name.lower() + ".gdns", "w")
gdn.write("[gd_resource type=\"NativeScript\" load_steps=2 format=2]\n\n")
gdn.write("[ext_resource path=\"res://gdlibrary.gdnlib\" type=\"GDNativeLibrary\" id=1]\n\n")
gdn.write("[resource]\n")
gdn.write("class_name = \"" + class_name + "\"\n")
gdn.write("library = ExtResource( 1 )\n")

gdn.close()
######### GDNS END #########

######## gdlibrary.cpp START ##########
gd = open("gdlibrary.cpp", "r")
h_file = "#include \"" + h_file + "\""
for line in gd:
    if h_file in line:
        print(h_file + " exists in the gdlibrary.")
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

########## gdlibrary.cpp END ########

########## GDNLIB START ###########

gdnlib_file = "../gdlibrary.gdnlib"

if not path.exists(gdnlib_file):
    gdnlib = open(gdnlib_file, "w")

    gdnlib.write("[general]\n\n")
    gdnlib.write("singleton=false\n")
    gdnlib.write("load_once=true\n")
    gdnlib.write("symbol_prefix=\"godot_\"\n")
    gdnlib.write("reloadable=true\n\n")
    gdnlib.write("[entry]\n\n")
    gdnlib.write("Windows.64=\"res://bin/win64/libgdlibrary.dll\"\n")
    gdnlib.write("X11.64=\"res://bin/x11/libgdlibrary.so\"\n")
    gdnlib.write("\n[dependencies]\n\n")
    gdnlib.write("Windows.64=[  ]\n")
    gdnlib.write("X11.64=[  ]\n")

    gdnlib.close()

########## GDNLIB END ###########