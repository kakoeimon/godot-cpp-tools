import sys
import os
import subprocess

platform = ""

if "win" in sys.platform:
    platform = "windows"
elif "linux" in sys.platform:
    platform = "linux"

godot_executable = open("godot_executable.txt", "r").readline()

subprocess.call("scons p=" + platform, shell=True)

path = os.path.abspath(os.getcwd())
path = os.path.abspath(os.path.join(path, os.pardir))

subprocess.Popen(godot_executable, cwd=path)