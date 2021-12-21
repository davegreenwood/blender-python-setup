"""
Install and reload development addons. 
Addons are python modules.

    blender --background --python reload_addons.py

NOTE: this is not very robust and should be made so.
"""

from pathlib import Path
import bpy

addon_files = ["dg_module_01.py"]
root = Path().absolute()

for path in addon_files:
    bpy.ops.preferences.addon_install(
        overwrite=True, target='DEFAULT',
        filepath=root.joinpath(path).as_posix(),
        filter_folder=True,
        filter_python=False,
        filter_glob="*.py;*.zip")


modules = ["dg_module_01", ]

for a in modules:
    bpy.ops.preferences.addon_disable(module=a)
    bpy.ops.preferences.addon_enable(module=a)
