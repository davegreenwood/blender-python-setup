import unittest
import sys
import bpy
import numpy as np
import logging
from dg_module_01 import mean_vertex

# it may be better to get an object by name - or some other way
OBJ = bpy.context.active_object
LOG = logging.getLogger(__name__)


def copy_object(obj, name):
    """
    Copy an object and return the new object.
    """
    obj = bpy.data.objects.new(name, OBJ.data)
    bpy.context.scene.collection.objects.link(obj)
    bpy.context.view_layer.objects.active = obj
    obj.select_set(state=True)
    return obj


class TestInterpreter(unittest.TestCase):
    """This test reports the Blender environment"""

    def test_interpreter(self):
        LOG.info("interpreter: %s", sys.executable)
        LOG.info("version: %s", sys.version)
        LOG.info("blender: %s", bpy.app.version)
        self.assertTrue(True)


class TestObjects(unittest.TestCase):
    """This test works on functions in our add-on module"""

    def test_object_name(self):
        LOG.debug("object name: %s", OBJ.name)
        self.assertTrue(True)

    def test_mean_vertex(self):
        mv = mean_vertex(OBJ)
        self.assertAlmostEqual(mv.all(), np.zeros(3).all())

    def test_mean_vertex_moved_world(self):
        obj = copy_object(OBJ, "cube_01")
        bpy.ops.transform.translate(value=(1, 2, 3))
        mv = mean_vertex(obj, world_space=True)
        self.assertAlmostEqual(mv.all(), np.array([1., 2., 3.]).all())

    def test_mean_vertex_moved_world_false(self):
        obj = copy_object(OBJ, "cube_02")
        bpy.ops.transform.translate(value=(1, 2, 3))
        mv = mean_vertex(obj, world_space=False)
        self.assertNotEqual(mv.any(), np.array([1., 2., 3.]).any())


if __name__ == '__main__':

    # see: https://blender.stackexchange.com/a/8405/100373
    pargs = (sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else [])
    sys.argv = [__file__] + pargs

    # always a good idea to keep logs
    logging.basicConfig(level=logging.INFO)

    unittest.main()
