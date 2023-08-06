# adobo.
#
# Description: An analysis framework for scRNA-seq data.
#  How to use: https://oscar-franzen.github.io/adobo/
#     Contact: Oscar Franzen <p.oscar.franzen@gmail.com>
"""
Summary
-------
Internal functions used for adobo colors.
"""

import numpy as np
from sklearn.cluster import KMeans

def unique_colors(n_colors, seed=None):
    """
    Generates unique colors
    
    Note
    ----
    C code is borrowed from the R package colorspace and ported to Python.
    The kmeans concept is borrowed from the R package randomcoloR.

    Parameters
    ----------
    n_colors : `int`
        Number of colors to generate
    seed : `int`
        For reproducibility.

    Returns
    -------
    list
        Colors as hex values
    """
    np.random.seed(seed)
    # generate an array with random values
    color_space = np.random.rand(2000, 3)

    # Use D65 by default
    Xn = 95.047
    Yn = 100.000
    Zn = 108.883

    EPSILON = 216.0/24389.0
    KAPPA = 24389.0/27.0

    def f(t):
        return pow(t, 1.0/3.0) if t > EPSILON else (KAPPA / 116.0) * t + 16.0/116.0

    def lab(x):
        R = x[0]
        G = x[1]
        B = x[2]
        # RGB to XYZ
        X = Yn * (0.412453 * R + 0.357580 * G + 0.180423 * B)
        Y = Yn * (0.212671 * R + 0.715160 * G + 0.072169 * B)
        Z = Yn * (0.019334 * R + 0.119193 * G + 0.950227 * B)
        # XYZ to LAB
        xr = X / Xn
        yr = Y / Yn
        zr = Z / Zn
        if yr > EPSILON:
            L = 116.0 * (yr**(1.0/3.0)) - 16.0
        else:
            L = KAPPA * yr
        xt = f(xr)
        yt = f(yr)
        zt = f(zr)
        A = 500.0 * (xt - yt)
        B = 200.0 * (yt - zt)

        return [L, A, B]

    # Axis 0 will act on all the ROWS in each COLUMN
    # Axis 1 will act on all the COLUMNS in each ROW
    z = np.apply_along_axis(lab, axis=1, arr=color_space)
    km = KMeans(n_clusters=n_colors, random_state=0, max_iter=20).fit(z)
    centers = km.cluster_centers_

    def lab_to_xyz(x):
        L = x[0]
        A = x[1]
        B = x[2]
        X = 0
        Y = 0
        Z = 0

        if L <= 0:
            Y = 0.0
        elif L <= 8.0:
            Y = L * Yn / KAPPA
        elif L <= 100:
            Y = Yn * ((L + 16) / 116)**3
        else:
            Y = Yn

        if Y <= EPSILON * Yn:
            fy = (KAPPA / 116.0) * Y / Yn + 16.0 / 116.0
        else:
            fy = (Y / Yn)**(1.0/3.0)

        fx = fy + (A / 500.0)

        if fx**3 <= EPSILON:
            X = Xn * (fx - 16.0 / 116.0) / (KAPPA / 116.0)
        else:
            X = Xn * fx**3

        fz = fy - (B / 200.0)

        if fz**3 <= EPSILON:
            Z = Zn * (fz - 16.0 / 116.0) / (KAPPA / 116.0)
        else:
            Z = Zn * fz**3

        return [X, Y, Z]

    z2 = np.apply_along_axis(lab_to_xyz, axis=1, arr=centers)

    def gtrans(u, gamma):
        if u > 0.00304:
            return 1.055 * u**(1 / gamma) - 0.055
        return 12.92 * u

    def xyz_to_srgb(x):
        X = x[0]
        Y = x[1]
        Z = x[2]

        R = gtrans((3.240479 * X - 1.537150 * Y - 0.498535 * Z) / Yn, 2.4)
        G = gtrans((-0.969256 * X + 1.875992 * Y + 0.041556 * Z) / Yn, 2.4)
        B = gtrans((0.055648 * X - 0.204043 * Y + 1.057311 * Z) / Yn, 2.4)
        return [R, G, B]

    z3 = np.apply_along_axis(xyz_to_srgb, axis=1, arr=z2)

    HEXDIG = '0123456789ABCDEF'

    def srgb_to_hex(x):
        r = x[0]
        g = x[1]
        b = x[2]
        hex_ = ['#']

        ir = int(255 * r + .5)
        ig = int(255 * g + .5)
        ib = int(255 * b + .5)

        hex_.append(HEXDIG[int((ir / 16) % 16)])
        hex_.append(HEXDIG[int(ir % 16)])
        hex_.append(HEXDIG[int((ig / 16) % 16)])
        hex_.append(HEXDIG[int(ig % 16)])
        hex_.append(HEXDIG[int((ib / 16) % 16)])
        hex_.append(HEXDIG[int(ib % 16)])

        return ''.join(hex_)

    z4 = np.apply_along_axis(srgb_to_hex, axis=1, arr=z3)

    return z4
