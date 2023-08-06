#! /usr/bin/env python
from __future__ import absolute_import, division, print_function
# quaternion module

"""Version 4 September 9, 2010 WMK
Flipped sign of the angle in the QX,QY,QZ,QJX,QJY,QJZ, set_values, set_as_QX,...
functions to be consistent with the corrected multiplication. Also updated
the doc strings."""

"""Version 3 September 8, 2010 RLH
Backed out change to cnvrt in version 2."""

"""Version 2 September 3, 2010 RLH
Fixed sign error in quaternion multiplication functions.
Added quaternion __str__ method.
Modified cnvrt method to return a CelestialVector."""


# 4/9/2010 WMK
# Redefined the __init__ inputs
# Changed from a Vector internal representation to 3 scalers
# Fixed an error in cvt_att_Q_to_angles, was assuming an att2inertial Quaternion!
# Streamlined some of the functions
#  Version 1.0 August 3, 2010
#  Got rid of degrees trig functions.

#from math import *
import math
from .math_extensionsx import *
from . import rotationsx as rot

D2R = pi / 180.
R2D = 180. / pi
PI2 = 2. * pi


def unit_limit(x): return min(max(-1., x), 1.)


def QX(angle):
    """Creates rotation quaternion about X axis, assuming coordinate frame is rotated"""
    return Quaternion(rot.Vector(math.sin(-angle / 2.),
                                 0., 0.), math.cos(angle / 2.))


def QY(angle):
    """Creates rotation quaternion about Y axis, assuming coordinate frame is rotated"""
    return Quaternion(rot.Vector(
        0., math.sin(-angle / 2.), 0.), math.cos(angle / 2.))


def QZ(angle):
    """Creates rotation quaternion about Z axis, assuming coordinate frame is rotated"""
    return Quaternion(rot.Vector(
        0., 0., math.sin(-angle / 2.)), math.cos(angle / 2.))


def Qmake_a_point(V):
    """Creates a pure Q, i.e. defines a pointing not a rotation"""
    return Quaternion(V, 0.)


def cvt_pt_Q_to_V(Q):
    """Converts a pure (pointing) Q to a unit position Vector"""
    return rot.Vector(Q.q1, Q.q2, Q.q3)


# The following functions are dependent upon the spacecraft definitions
# and perhaps should be moved to that module

def Qmake_an_attitude(ra, dec, pa):
    """Creates a rotation Q, going from the inertial to the attitude"""
    return QX(-pa) * QY(-dec) * QZ(ra)


def Qmake_inertial2att(coord1, coord2, pa):
    """Creates a rotation Q, going from the inertial to the attitude"""
    return QX(-pa) * QY(-coord2) * QZ(coord1)


def Qmake_an_attitude_w_v2v3(ra, dec, pa, v2, v3):
    return QZ(-v2) * QY(v3) * QX(-pa) * QY(-dec) * QZ(ra)


def Qmake_inertial2att_full(ra, dec, pa, xa, ya, s, ta, v2a, v3a):
    """ Where
        ra - right ascension of target
        dec - declination of target
        pa - position angle of the +y-axis of the aperture coordinate system
        xa,ya - coordinates of the target in the aperture coordinate system
        s - parity of the x-axis of the aperture coordinate system (s = +/- 1)
        ta - position angle of the +y-axis of the aperture coordinate system at
             the origin of the aperture coordinate with respect to the +V3 axis.
        v2a,v3a - coordinates of the origin of the aperture coordinate system in
             the vehicle frame
        Orientation Matrix John C. Isaacs Sep. 16, 2010

    """
    return QZ(-v2a) * QY(v3a) * QX(ta) * QZ(-s * xa) * \
        QY(ya) * QX(-pa) * QY(-dec) * QZ(ra)


def cvt_inert2att_Q_to_angles(Q):
    """Creates a angle tuple from Q, assuming an inertial to attitude Q"""
    V1_body = rot.Vector(1., 0., 0.)
    V1_eci_pt = Q.inv_cnvrt(V1_body)
    coord1 = math.atan2(V1_eci_pt.y, V1_eci_pt.x)
    if coord1 < 0.:
        coord1 += PI2
    coord2 = math.asin(unit_limit(V1_eci_pt.z))

    V3_body = rot.Vector(0., 0., 1.)
    V3_eci_pt = Q.inv_cnvrt(V3_body)
    NP_eci = rot.Vector(0., 0., 1.)
    V_left = rot.cross(NP_eci, V1_eci_pt)
    V_left = V_left / V_left.length()
    NP_in_plane = rot.cross(V1_eci_pt, V_left)
    x = rot.dot(V3_eci_pt, NP_in_plane)
    y = rot.dot(V3_eci_pt, V_left)
    pa = math.atan2(y, x)
    if pa < 0.:
        pa += PI2
    return (coord1, coord2, pa)


def cvt_att_Q_to_angles2(Q):
    """This assumes the quaternion is inertial to S/C and the Euler angles
 are 321 mapped to ra,-dec,-pa"""
    q1 = Q.q1
    q2 = Q.q2
    q3 = Q.q3
    q4 = Q.q4
    ra = math.atan2(2. * (q1 * q2 - q3 * q4),
                    q1 * q1 - q2 * q2 - q3 * q3 + q4 * q4)
    if ra < 0.:
        ra += PI2
    arg = min(1., max(-1., 2. * (q1 * q3 + q2 * q4)))
    dec = math.asin(arg)
    pa = math.atan2(-2. * (q2 * q3 - q1 * q4), -q1 *
                    q1 - q2 * q2 + q3 * q3 + q4 * q4)
    if pa < 0.:
        pa += PI2
    return (ra, dec, pa)


def Qmake_body2inertial(coord1, coord2, V3pa):
    """Creates a rotation Q, going from the body frame to inertial"""
    return QZ(coord1) * QY(-coord2) * QX(-V3pa)


def Qmake_v2v3_2body(v2, v3):
    """Creates a rotation Q, going from v2 and v3 in the body frame to inertial"""
    return QY(v3) * QZ(-v2)


def Qmake_v2v3_2inertial(coord1, coord2, V3pa, v2, v3):
    """Creates a rotation Q, going from v2 and v3 in the body frame to inertial"""
    return QZ(coord1) * QY(-coord2) * QX(-V3pa) * QY(v3) * QZ(-v2)


def Qmake_aperture2inertial(
        coord1, coord2, APA, xoff, yoff, s, YapPA, V3ref, V2ref):
    """Creates a rotation Q, going from the target in aperture frame to body"""
    return QZ(coord1) * QY(-coord2) * QX(-APA) * QY(-yoff) * \
        QZ(s * xoff) * QX(YapPA) * QY(V3ref) * QZ(-V2ref)


def cvt_body2inertial_Q_to_c1c2pa_tuple(Q):
    """Creates a angle tuple from Q, assuming body frame to inertial Q and 321 rotation sequence"""
    # Conversion from Euler symmetric parameters to matrix elements and matrix elements to rotation angles
    # is given in Isaac's papers
    r11 = Q.q1 * Q.q1 - Q.q2 * Q.q2 - Q.q3 * Q.q3 + Q.q4 * Q.q4
    r21 = 2. * (Q.q1 * Q.q2 + Q.q3 * Q.q4)
    r31 = 2. * (Q.q1 * Q.q3 - Q.q2 * Q.q4)
    r32 = 2. * (Q.q2 * Q.q3 + Q.q1 * Q.q4)
    r33 = -Q.q1 * Q.q1 - Q.q2 * Q.q2 + Q.q3 * Q.q3 + Q.q4 * Q.q4
    coord1 = atan2(r21, r11)
    if coord1 < 0.:
        coord1 += PI2
    coord2 = asin2(r31)  # use "safe" version of sine
    pa = atan2(-r32, r33)
    if pa < 0.:
        pa += PI2
    return (coord1, coord2, pa)


def cvt_v2v3_using_body2inertial_Q_to_c1c2pa_tuple(Q, v2, v3):
    """Given Q and v2,v3 gives pos on sky and V3 PA """
    Vp_body = rot.Vector(0., 0., 0.)
    Vp_body.set_xyz_from_angs(v2, v3)
    Vp_eci_pt = Q.cnvrt(Vp_body)
    coord1 = atan2(Vp_eci_pt.y, Vp_eci_pt.x)
    if coord1 < 0.:
        coord1 += PI2
    coord2 = asin(unit_limit(Vp_eci_pt.z))

    V3_body = rot.Vector(0., 0., 1.)
    V3_eci_pt = Q.cnvrt(V3_body)
    NP_eci = rot.Vector(0., 0., 1.)
    V_left = cross(NP_eci, Vp_eci_pt)
    if V_left.length() > 0.:
        V_left = V_left / V_left.length()
    NP_in_plane = cross(Vp_eci_pt, V_left)
    x = dot(V3_eci_pt, NP_in_plane)
    y = dot(V3_eci_pt, V_left)
    pa = atan2(y, x)
    if pa < 0.:
        pa += PI2

    return (coord1, coord2, pa)


def cvt_c1c2_using_body2inertial_Q_to_v2v3pa_tuple(Q, coord1, coord2):
    """Given Q and a position, returns v2,v3,V3PA tuple """
    Vp_eci = rot.Vector(1., 0., 0.)
    Vp_eci.set_xyz_from_angs(coord1, coord2)
    Vp_body_pt = Q.inv_cnvrt(Vp_eci)
    v2 = atan2(Vp_body_pt.y, Vp_body_pt.x)
    v3 = asin(unit_limit(Vp_body_pt.z))
    V3_body = rot.Vector(0., 0., 1.)
    V3_eci_pt = self.cnvrt(V3_body)
    NP_eci = rot.Vector(0., 0., 1.)
    V_left = cross(NP_eci, Vp_eci)
    if V_left.length() > 0.:
        V_left = V_left / V_left.length()
    NP_in_plane = cross(Vp_eci, V_left)
    x = dot(V3_eci_pt, NP_in_plane)
    y = dot(V3_eci_pt, V_left)
    pa = atan2(y, x)
    if pa < 0.:
        pa += PI2
    return (v2, v3, pa)


############################################################


class Quaternion:
    """This representation is used by Wertz and Markley """

    def __init__(self, V, q4):
        """Quaternion constructor """
        self.q1 = V.x
        self.q2 = V.y
        self.q3 = V.z
        self.q4 = q4

    def __str__(self):
        """Returns a string representation of the quaternion."""

        return('Quaternion: q1: %.3f, q2: %.3f, q3: %.3f, q4: %.3f'
               % (self.q1, self.q2, self.q3, self.q4))

    def length(self):
        """Returns length of the Q """
        return math.sqrt(self.q1 * self.q1 + self.q2 *
                         self.q2 + self.q3 * self.q3 + self.q4 * self.q4)

    def normalize(self):
        """Returns a copy of the Q normalized """
        scale = self.length()
        return Quaternion(rot.Vector(self.q1 / scale, self.q2 /
                                     scale, self.q3 / scale), self.q4 / scale)

    def conjugate(self):
        """Returns a copy of the conjugated Q """
        return Quaternion(rot.Vector(-self.q1, -self.q2, -self.q3), self.q4)

    def __mul__(self, rs):
        """Defines Q*Q for quaternion multiplication """
        Q = Quaternion(rot.Vector(0., 0., 0.), 0.)
        #Q.V = rs.V * self.q4 + self.V * rs.q4 + cross(self.V,rs.V)
        Q.q1 = rs.q1 * self.q4 + self.q1 * rs.q4 + \
            (self.q2 * rs.q3 - self.q3 * rs.q2)
        Q.q2 = rs.q2 * self.q4 + self.q2 * rs.q4 + \
            (self.q3 * rs.q1 - self.q1 * rs.q3)
        Q.q3 = rs.q3 * self.q4 + self.q3 * rs.q4 + \
            (self.q1 * rs.q2 - self.q2 * rs.q1)
        Q.q4 = self.q4 * rs.q4 - \
            (self.q1 * rs.q1 + self.q2 * rs.q2 + self.q3 * rs.q3)
        return Q

    def cnvrt(self, V):
        """Rotates a vector from the starting frame to the ending frame defined by the Q """
        QV = Qmake_a_point(V)
        QV = self * QV * self.conjugate()
        return rot.Vector(QV.q1, QV.q2, QV.q3)

    def inv_cnvrt(self, V):
        """Rotates a vector from the ending frame to the starting frame defined by the Q"""
        QV = Qmake_a_point(V)
        QV = self.conjugate() * QV * self
        return rot.Vector(QV.q1, QV.q2, QV.q3)

    def set_values(self, V, angle):
        """Sets quaterion values using a direction vector and a rotation of the coordinate frame about it."""
        S = sin(-angle / 2.)
        self.q1 = V.x * S
        self.q2 = V.y * S
        self.q3 = V.z * S
        self.q4 = cos(angle / 2.)

    def set_as_QX(self, angle):
        """Sets quaterion in place like QX function"""
        self.q1 = sin(-angle / 2.)
        self.q2 = 0.
        self.q3 = 0.
        self.q4 = cos(angle / 2.)

    def set_as_QY(self, angle):
        """Sets quaterion in place like QY function"""
        self.q1 = 0.
        self.q2 = sin(-angle / 2.)
        self.q3 = 0.
        self.q4 = cos(angle / 2.)

    def set_as_QZ(self, angle):
        """Sets quaterion in place like QZ function"""
        self.q1 = 0.
        self.q2 = 0.
        self.q3 = sin(-angle / 2.)
        self.q4 = cos(angle / 2.)

    def set_as_mult(self, QQ1, QQ2):
        """Sets self as QQ1*QQ2 in place for quaternion multiplication """
        self.q1 = QQ2.q1 * QQ1.q4 + QQ1.q1 * QQ2.q4 + \
            (QQ1.q2 * QQ2.q3 - QQ1.q3 * QQ2.q2)
        self.q2 = QQ2.q2 * QQ1.q4 + QQ1.q2 * QQ2.q4 + \
            (QQ1.q3 * QQ2.q1 - QQ1.q1 * QQ2.q3)
        self.q3 = QQ2.q3 * QQ1.q4 + QQ1.q3 * QQ2.q4 + \
            (QQ1.q1 * QQ2.q2 - QQ1.q2 * QQ2.q1)
        self.q4 = QQ1.q4 * QQ2.q4 - \
            (QQ1.q1 * QQ2.q1 + QQ1.q2 * QQ2.q2 + QQ1.q3 * QQ2.q3)

    def set_as_point(self, V):
        self.q1 = V.x
        self.q2 = V.y
        self.q3 = V.z
        self.q4 = 0.

    def set_equal(self, Q):
        """Assigns values from other Q to this one. """
        self.q1 = Q.q1
        self.q2 = Q.q2
        self.q3 = Q.q3
        self.q4 = Q.q4

    def set_as_conjugate(self):
        """Assigns conjugate values in place. """
        self.q1 *= -1.
        self.q2 *= -1.
        self.q3 *= -1.
