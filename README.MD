# Godot CPP Bindings Helper Tools

A collection of files to help starting a new GDNative Lib for Godot with the Godot-cpp bindings

### Compiling Godot-cpp

Decide for a directory where you are going to store your projects.
Let's say /home/projects/
Navigate to this directory and clone the Godot-cpp repository
```
git clone --recursive https://github.com/GodotNativeTools/godot-cpp
```

Enter the godot-cpp and compile
```
scons platform=<your platform> generate_bindings=yes bits=64
```

Now you have compiled the godot-cpp in debug mode
It is recomented that you compile it and in release mode.
```
scons platform=<your platform> target=release bits=64
```

This way you will not have to compile godot-cpp for every project you may create.


## Getting Started with the tools

Create a new Godot project in the projects directory.
For example your project.godot file will be in /home/projects/new_project/ directory
Remember your Godot-cpp is in /home/projects/godot-cpp/ directory
This is important for the compilation of the GDNative Library
Navigate in your projects dircetory (/home/projects/new_project)
And run this comand to clone this repository in src/ directory
```
git clone https://github.com/kakoeimon/godot-cpp-tools src
```
Now you can open the src directory with Visual Studio Code.
To create a new class enter this command
```
python new_godot_class Enemy KinematicBody2D
```
The script will create a head file named "enemy.h" and a source file named "enemy.cpp" 
Also it will modify the gdlibrary.cpp to include the new class.

Then you can run to build in debug mode
```
scons platform=<your platform>
```
or for release 
```
scons platform=<your platform> target=release
```
Alternative you can edit the file:
```
godot_executable.txt
```
and put in the first line the absolute path of your Godot executable. For example
```
/home/kakoeimon/programs/Godot_v3.2.1-stable_x11.64
```
and then run with python 3 (Ubuntu means you must write python3)
```
python debug.py
```
This will run scons for your platform and run Godot afterwards.
Or if you want released mode
```
python release.py
```

### Where are the libs?
When you compile your lib will be in the direcory of your project /bin/win64 for windows and /bin/x11 for linux you can then procced and create the GDNLib file and the GDNS file in Godot to use.


### To do :
In future version GDNLIB and GDNS files will be automatically created when new_godot_class is called.

#### The SConstruct file is a modified version of this file:
https://docs.godotengine.org/en/3.2/_downloads/bac79b8996cc2de2ada1a4a6a11e428d/SConstruct
