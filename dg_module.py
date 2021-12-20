import numpy as np
import logging

LOG = logging.getLogger(__name__)

bl_info = {
    "name": "DG Test Add-on",
    "blender": (3, 0, 0),
    "category": "Object",
}


def mean_vertex(obj, world_space=False):
    """
    Return the mean vertex of a mesh object as an ndarray.
    If world_space is True, the returned vertex is in world space, 
    i.e it is affected by the transforms on the object.

    NOTE: no checks are performed to ensure that the object is a mesh.
    """
    if world_space:
        vts = np.array([(obj.matrix_world @ v.co) for v in obj.data.vertices])
    else:
        vts = np.array([v.co for v in obj.data.vertices])
    mean = np.mean(vts, axis=0)
    LOG.debug("mean vertex: %s", mean)
    return mean


def register():
    LOG.info("Registering DG Test Add-on")


def unregister():
    LOG.info("Deregistering DG Test Add-on")


if __name__ == "__main__":
    register()
