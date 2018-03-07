"""
File: matrixcanvas.py
Presents a view of a matrix
"""

from breezypythongui import EasyCanvas

class MatrixCanvas(EasyCanvas):
    """Represents a canvas for a character in a matrix view."""

    def __init__(self, parent, width, height, text):
        """Sets up the canvas for drawing text."""
        EasyCanvas.__init__(self, parent,
                            width = width,
                            height = height)
        self.width = width
        self.height = height
        x = self.width // 2
        y = self.height // 2
        self.id = self.drawText(text, x, y)

    def draw(self, text):
        """Replaces the old text with the new text."""
        self.delete(self.id)
        x = self.width // 2
        y = self.height // 2
        self.id = self.drawText(text, x, y)
