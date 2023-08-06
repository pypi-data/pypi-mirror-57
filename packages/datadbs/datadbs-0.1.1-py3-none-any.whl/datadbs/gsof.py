from networktools.geo import rad2deg, deg2rad, radius, sph_rotation_matrix, llh2ecef
from networktools.time import timestamp, gps_week2time, gps_time
from networktools.statistics import matrix_VCV, rotate
from .general import GeneralData

import math
import asyncio
import numpy as np


class GsofData(GeneralData):
    def __init__(self, *args, **kwargs):
        super(GsofData, self).__init__(*args, **kwargs)

    def manage_data(self, data):
        # get timestamp from data generated on gps
        time = gps_time(data).timestamp()
        # get position
        result = {}
        if 'ECEF' in data.keys():
            X = data['ECEF']['X_POS']
            Y = data['ECEF']['Y_POS']
            Z = data['ECEF']['Z_POS']
            XYZ = dict(zip(['X', 'Y', 'Z'], [X, Y, Z]))
        if 'LATLONHEIGHT' in data.keys():
            LAT = data['LATLONHEIGHT']['LATITUDE']
            LON = data['LATLONHEIGHT']['LONGITUDE']
            HEIGHT = data['LATLONHEIGHT']['HEIGHT']
            this_radius = radius(LAT)
            XYZ = llh2ecef(LAT, LON, HEIGHT)
            (dLAT, dLON) = rad2deg(LAT, LON)
        if 'POSITION_VCV' in data.keys():
            VCV = data['POSITION_VCV']
            Vxx = VCV['VCV_XX']
            Vyy = VCV['VCV_YY']
            Vzz = VCV['VCV_ZZ']
            Vxy = VCV['VCV_XY']
            Vxz = VCV['VCV_XZ']
            Vyz = VCV['VCV_YZ']
            M = matrix_VCV(Vxx, Vyy, Vzz, Vxy, Vxz, Vyz)
            # R=sph_rotation_matrix(LAT,LON)
            VCV = M  # rotate(R,M)
            result = dict(TIME=time,
                          ECEF=XYZ,
                          ERROR=VCV)
        return result
