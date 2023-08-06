from .general import GeneralData

import math
import asyncio
import numpy as np

class BNC_PPP(GeneralData):
    def __init__(self,*args,**kwargs):
        super(GsofData,self).__init__(*args,**kwargs)

    def manage_data(self, data):
        return data
