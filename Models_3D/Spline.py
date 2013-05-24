from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

#    pyeq2 is a collection of equations expressed as Python classes
#
#    Copyright (C) 2013 James R. Phillips
#    2548 Vera Cruz Drive
#    Birmingham, AL 35235 USA
#
#    email: zunzun@zunzun.com
#    web: http://zunzun.com
#
#    License: BSD-style (see LICENSE.txt in main source directory)

import sys, os, inspect
if -1 != sys.path[0].find('pyeq2-read-only'):raise Exception('Please rename SVN checkout directory from "pyeq2-read-only" to "pyeq2"')
if os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '..') not in sys.path:
    sys.path.append(os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '..'))
    
import numpy, scipy.interpolate
import pyeq2



import pyeq2.Model_3D_BaseClass



class Spline(pyeq2.Model_3D_BaseClass.Model_3D_BaseClass):
    splineFlag = True
    _baseName = "Spline"
    
    webReferenceURL = ''

    baseEquationHasGlobalMultiplierOrDivisor_UsedInExtendedVersions = False
    autoGenerateOffsetForm = False
    autoGenerateReciprocalForm = False
    autoGenerateInverseForms = False
    autoGenerateGrowthAndDecayForms = False

    
    def __init__(self, inSmoothingFactor = None, inXOrder = None, inYOrder = None):
        pyeq2.Model_3D_BaseClass.Model_3D_BaseClass.__init__(self, 'SSQABS') # call superclass      
        self.smoothingFactor = inSmoothingFactor
        self.xOrder = inXOrder
        self.yOrder = inYOrder
    
    
    def GetDisplayHTML(self):
        return 'z = B-Spline Interpolation Surface'


    def GetDataCacheFunctions(self):
        functionList = []
        functionList.append([pyeq2.DataCache.DataCacheFunctions.X(NameOrValueFlag=1), []])
        functionList.append([pyeq2.DataCache.DataCacheFunctions.Y(NameOrValueFlag=1), []])
        return functionList


    def ShouldDataBeRejected(self, inModel):
        return False # splines do not have data limits

    
    def AreCoefficientsWithinBounds(self, inCoeffs):
        return True # splines do not have coefficient bounds


    def CalculateModelPredictions(self, inCoeffs, inDataCacheDictionary):
        result = self.scipySpline.ev(inDataCacheDictionary['X'], inDataCacheDictionary['Y'])
        return result
        
        
    def GetCoefficientDesignators(self):
        raise NotImplementedError('The Spline class does not implement ' + inspect.stack()[0][3])


    def CalculateFittingTarget(self, in_coeffArray):
        raise NotImplementedError('Not implemented for splines')
