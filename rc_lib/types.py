"""
    A collection of semantic aliases for type hinting used throughout the library.

    These should remain collected in a module namespace, rather than being
    put in to the global namespace, as some names may overlap with those
    used in the library.
"""
import numpy as np
import manim

__all__ = []  # no public names, access via module namespace

# To avoid conflicts with manim's Vector, we do not have any public names
Vector = np.ndarray
# For compatability with manim, a 2d vector is defined as 3d vector with its third coordinate equal to zero.
Vector2d = np.ndarray
Vector3d = np.ndarray

Point = np.ndarray
# For compatability with manim, a 2d point is defined as a 3d point with its third coordinate equal to zero.
Point2d = np.ndarray
Point3d = np.ndarray

Direction2d = np.ndarray
Direction3d = np.ndarray