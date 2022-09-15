"""
Functions for computing areas of various shapes
"""

def triangle_area(height, base):
    if base < 0 or height < 0:
        raise ValueError('Base and height must be 0 or positive')
    return height * base * 0.5

