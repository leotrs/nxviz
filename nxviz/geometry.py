"""
Utility geometry functions that can help with drawing to screen.
"""
from polcart import to_cartesian
import numpy as np


def node_theta(nodelist, node):
    """
    Maps node to Angle.
    """
    assert len(nodelist) > 0, 'nodelist must be a list of items.'
    assert node in nodelist, 'node must be inside nodelist.'

    i = nodelist.index(node)
    theta = i*2*np.pi/len(nodelist)

    if theta > np.pi:
        theta = np.pi - theta

    return theta


def get_cartesian(r, theta):
    """
    Returns the cartesian (x,y) coordinates of (r, theta).
    """
    # x = r*np.sin(theta)
    # y = r*np.cos(theta)

    return to_cartesian(r, theta)


def correct_negative_angle(angle):
    """
    Corrects a negative angle to a positive one.
    """
    if angle < 0:
        angle = 2 * np.pi + angle
    else:
        pass

    return angle
