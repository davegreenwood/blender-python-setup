# Developing Scripts in Blender

Some tips for setting up blender for development.

## Add Ons

For anything beyond the simplest scripts, you'll need to create an add-on.

https://docs.blender.org/api/blender_python_api_current/info_overview.html#addons

Refer to the Blender documentation for your operating system. When developing add-ons, you'll often need to reload the plugin.

If you use VScode you might find [this extension](https://marketplace.visualstudio.com/items?itemName=JacquesLucke.blender-development) useful.

## Logging

Create a startup script that sets up logging.

    import logging

    fmt = "%(asctime)-12s %(levelname)-8s %(name)-8s: %(message)s"
    dfmt = "%Y-%m-%d %H:%M:%S"
    logging.basicConfig(level=logging.DEBUG, format=fmt, datefmt=dfmt)

    def register():
        pass

The script needs to be in the startup folder, eg. for MacOS:

    ~/Library/Application Support/Blender/3.0/scripts/startup/logging.py

## Unit tests

For scripts that are not interactive it can end up being more efficient not to
use Blender's interface at all and instead execute the script on the command line.

    blender --background -noaudio --python tests/test_01.py -- --verbose

Here we pass arguments to the python script as described in this [post](https://blender.stackexchange.com/a/8405/100373).

Having spaces around `--` is important, this is a signal that Blender should
stop parsing the arguments and allows you to pass your own arguments to Python.