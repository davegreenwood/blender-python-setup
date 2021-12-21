# Developing Scripts in Blender

Some tips for setting up blender for development.

The Blender documentation is the best place to start.
For the application the docs are at [https://docs.blender.org](https://docs.blender.org).

The link for the API docs is at [https://docs.blender.org/api/current/](https://docs.blender.org/api/current/).

## Add Ons

For anything beyond the simplest scripts, you'll need to create an add-on.

https://docs.blender.org/api/blender_python_api_current/info_overview.html#addons

Refer to the Blender documentation for your operating system. When developing add-ons, you'll often need to reload the plugin.

If you use VScode you might find [this extension](https://marketplace.visualstudio.com/items?itemName=JacquesLucke.blender-development) useful.

Some setup can be difficult to achieve, for example this [post](https://developer.blender.org/T67387) explains some ways of adding and reloading scripts.

There is a simple script included [here](reload_addons.py) to load and reload addons.

### Simple Add-on

The simplest add-on is a single file,
it requires `bl_info`, and `register`, `deregister` functions.

There is an example [here](dg_module.py).

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

## Debugging

It is possible to use the standard Python debugger to debug scripts,
following this rather old stack [answer](https://blender.stackexchange.com/a/2504/100373).

1. Launch blender from a terminal emulator.
2. Add `import pdb; pdb.set_trace()` to your code where you wish to start debugging from.
3. Run your code and you'll be put into the
   Python [debugger](https://docs.python.org/3/library/pdb.html), where you can
   use `s` `Enter` to step through the code.

See the `pdb` [documentation](http://docs.python.org/3.9/library/pdb.html#debugger-commands)
for more info on usage. Also for the nicer _ipython_ debugger, you can use `ipdb`.
