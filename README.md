
# Alembic Export - Import Tool
## Overview
### Alpha Version
A Qt tool that exports Alembic geometric caches from Maya DCC and imports it in the Unreal Engine.

The Import tool in Unreal can import .abc, .png. jpg, .tiff, .tiff and .tga therefore it is not exclusive for Alembic imports as it imports the whole directory's contents.


More DCC (Digital Content Creator) softwares are to be added in the upcoming versions. 


## Installation
### Maya and rez friendly environments
The project makes use of the [@rez](https://github.com/AcademySoftwareFoundation/rez) tool to have an environment of packages communicate with one another. The main tool is dependent on several python packages like PySide2 (which requires shiboken2), PyQt5, Qt.py and six.py.

The creation and configuration of rez packages is explained in great detail in the github repository linked above.

Once the tool has been packaged in a rez environment package. The package.py currently in use for the project is the following:
```
    # -*- coding: utf-8 -*-

    name = 'qt_tutorial'

    version = '0.0.1'

    description = 'Qt Tutorial.'

    authors = []

    requires = [
        'Qt.py',
        'six'
    ]

    def commands():
        env.PYTHONPATH.append('{root}/python')
```

As shown above, this package already references the Qt.py and six.py which need to be present in a rez package for the environment to be usable.

Finally, to make sure everything works as expected you can run the following command:
```
    rez-env qt_tutorial
```

The rez command to run the tool with Maya and the Pycharm code editor is:
```
    rez-env maya pycharm qt_tutorial
```

Then run the following command to launch maya, the command can be changed with pycharm to open the Pycharm editor and so on.
```
    maya
```

In a Maya Python console you can run the following command to launch the tool:
```
    from pipeline import launch_tool
    launch_tool()
```

### Unreal Engine
#### Setup
First and foremost, for Unreal Engine's Python functionalities to work, we must turn on the Python plugins. To enable this plugin, click on the **Edit** dropdown menu and then click on **Plugins**. Search for Python in the search bar and activate the **Python Editor Script Plugin**.

Secondly, while Unreal Engine can be packaged in a rez environment to launch from a Powershell window, Unreal would still not recognize the external rez-packaged libraries. Meaning that you can package Unreal Engine in a rez configuration like the following:
```
    name = "ue5"

    tools = [
        "UnrealEditor-Cmd",
        "UnrealEditor",
        "start_engine"
    ]

    def commands():
        env.PATH.append(
            r"D:\UnrealEngine\UE_5.0\Engine\Binaries\Win64"
        )

```

This package.py configuration registers the Unreal Engine as a package in Rez, and if you run the following commands you can run the Unreal Editor but even then if you try to call another rez package from inside Unreal, Unreal will not be aware of the package.
```
    rez-env ue5
    UnrealEditor
```

In order for Unreal to be aware of external Python packages, there are several paths or options to choose from:

#### Option A: Unreal Engine Python Content Folder
Go to your local Unreal Engine installation on your machine, if the Unreal Engine installation is at *D:/UnrealEngine/UE5.0* for example, go into the Engine folder and into the Content folder and create a Python folder. The python folder in this case would be at: *D:/UnrealEngine/UE5.0/Engine/Content/Python*.

The packages placed in this folder will be visible to the Unreal Engine on your local machine **regardless of the project you are working on**.

#### Option B: Project Specific Python Content Folder
Similar to the solution above, in this solution we create a directory to contain the python packages that our tool requires. The packages put within this folder will be accessible **within the project**. Therefore if you have project specific requirements and do not want to make the packages available to the whole engine, this is also an option.

If the project is at *D:/UnrealProjects/MyProject* then the python packages should be placed in *D:/UnrealProjects/MyProject/Content/Python*.

#### Option C: Adding Our Package Path To The Unreal Editor Python Paths
Open your project in the Unreal Editor. Go to the 
**Edit** dropdown menu and click on it. Click on 
Project Settings. Scroll down on the left side of 
the window until you find the **Plugins** menu. In the 
Plugins menu click on **Python**. On the right 
hand side of the window, click the **+** button next 
to Additional Paths. Click on the **...** button 
and navigate the window to your package folder and 
select it. Your package is now visible within 
your project to Unreal Engine.

#### Usage

With the above steps taken into consideration,
go to the terminal in your UnrealEditor, click on
the Cmd Menu and select Python. It is important
to note the difference between Python and Python(REPL). 
Whereas Python can run a Python script, Python (REPL)
is a Python console with built in memory, meaning you
can run one python command at a time, and the command
is saved in the terminal's memory. In order to run
an external python file in the terminal, you need
to be on the **Python** termina. Afterwards, copying
the path to your project and pressing enter runs
the tool.

Example: the path to the tool is:
```
D:/rez/dev_packages/qt_tutorial/0.0.1/python/pipeline/tools/ui/import_window.py
```
So you insert the above line in the console and press enter.

You can also create a BluePrint Editor Widget and
run the project through it. Create a BluePrint Editor
Widget, create a button within it and in the BluePrint
event on the click of a button, create a node that runs
a python command and as the python command pass the
path to the project.
## Features

- Alembic Export of one or multiple objects from a Maya scene.
- Import of a directory of files from your machine to the project. The tool can import textures, alembic and other supported formats mentioned above.


## Authors

- [@Zaatar](https://www.github.com/Zaatar)

