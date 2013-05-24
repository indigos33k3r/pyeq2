from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

import os, sys, inspect

# ensure pyeq2 can be imported
if -1 != sys.path[0].find('pyeq2-read-only'):raise Exception('Please rename SVN checkout directory from "pyeq2-read-only" to "pyeq2"')
exampleFileDirectory = sys.path[0][:sys.path[0].rfind(os.sep)]
pyeq2IimportDirectory =  os.path.join(os.path.join(exampleFileDirectory, '..'), '..')
if pyeq2IimportDirectory not in sys.path:
    sys.path.append(pyeq2IimportDirectory)
    
    import pyeq2


for submodule in inspect.getmembers(pyeq2.Models_2D):
    if inspect.ismodule(submodule[1]):
        for equationClass in inspect.getmembers(submodule[1]):
            if inspect.isclass(equationClass[1]):
                for extendedVersionName in pyeq2.ExtendedVersionHandlers.extendedVersionHandlerNameList:
                    try:
                        equation = equationClass[1]('SSQABS', extendedVersionName)
                    except:
                        continue
                    print('2D ' + submodule[0] + ' --- ' + equation.GetDisplayName())
                    
print('Done.')