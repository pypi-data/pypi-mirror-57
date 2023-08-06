
# Copyright (C) 2019 Frank Sauerburger

import unittest

import numpy as np
import matplotlib.pyplot as plt

from atlasify import atlasify

class SurvivalTestCase(unittest.TestCase):
    """
    Test that the method does not crash..
    """
    def setUp(self):
        """
        Call plt.plot().
        """
        x = np.linspace(-3, 3, 200)
        y = np.exp(-x**2)
        
        plt.plot(x, y, label="Something")

    def tearDown(self):
        """
        Clear the figure.
        """
        plt.clf()

    def test_default(self):
        """
        Check that calling atlasify() without arguments does not crash.
        """
        try:
            atlasify()
        except:
            sef.assertFail("Calling atlasify() raised an exception")

    def test_False(self):
        """
        Check that calling atlasify() without badge does not crash.
        """
        try:
            atlasify(False)
        except:
            sef.assertFail("Calling atlasify() raised an exception")

    def test_label(self):
        """
        Check that calling atlasify() with a label does not crash.
        """
        try:
            atlasify("Internal")
        except:
            sef.assertFail("Calling atlasify() raised an exception")

    def test_subtext(self):
        """
        Check that calling atlasify() with a subtext does not crash.
        """
        try:
            atlasify("Internal", "Hello\nWorld\nHow are you")
        except:
            sef.assertFail("Calling atlasify() raised an exception")

    def test_enlarge(self):
        """
        Check that calling atlasify() with different enalrge does not crash.
        """
        try:
            atlasify("Internal", enlarge=2)
        except:
            sef.assertFail("Calling atlasify() raised an exception")
