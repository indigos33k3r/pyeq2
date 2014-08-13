from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

import os, sys, inspect, scipy

# ensure pyeq2 can be imported
if -1 != sys.path[0].find('pyeq2-read-only'):raise Exception('Please rename SVN checkout directory from "pyeq2-read-only" to "pyeq2"')
exampleFileDirectory = sys.path[0][:sys.path[0].rfind(os.sep)]
pyeq2IimportDirectory =  os.path.join(os.path.join(exampleFileDirectory, '..'), '..')
if pyeq2IimportDirectory not in sys.path:
    sys.path.append(pyeq2IimportDirectory)
    
import pyeq2


simpleObject = pyeq2.IModel.IModel()
simpleObject._dimensionality = 1

# example data is generated from a Rayleigh distribution (5.0, 2.0)
asciiTextData = '''
6.80743717445
5.73241246041
8.4371492305
8.11050207076
7.10033762532
5.8833830302
9.10112025231
9.50219410606
10.774884079
7.4082084536
5.35255402605
8.00196064187
8.99642299141
8.18388488915
9.86578767427
8.37112414641
6.13144892263
9.05829466686
5.75817168173
5.82981176259
8.44663586273
5.25995232797
6.97164892124
6.26353911696
8.16620096948
6.77252636062
7.04845096309
9.99697841758
8.15499367781
9.34244313148
6.68033297825
9.48961522454
5.08439247826
9.77175637074
7.73428671372
8.49959935043
8.75391049053
10.2400354029
7.35780460231
6.04305593659
9.31606647916
6.68582523623
6.02345405553
6.56695016148
6.49474803994
8.61455664294
6.41990414821
6.44988977687
10.84710726
7.9020720225
6.2996000129
7.12518299189
6.68993054905
8.10565394474
8.26776286137
11.6282354593
7.60835242611
8.12767486439
9.45316771283
8.97430667194
9.9631651169
5.43945601073
6.96592159181
6.83885306755
6.35536133786
7.26444949322
9.53668246269
6.32323405069
8.38237493572
7.09587637555
7.2446421534
6.71774491045
10.0244909017
8.2728253294
6.3033688128
6.02267056884
6.78581983402
6.14731028716
7.22033524811
9.17390324318
7.32769078298
6.48628412401
5.95797608298
7.48459119804
6.71813939682
6.04461711517
8.50627495998
7.33743802168
8.51884412491
10.1957707094
9.04660920884
5.42118088271
9.28950714917
9.16916439113
8.10040098473
6.63474808453
7.14589243662
6.60546061464
6.8406556912
6.09179714942
6.57259704578
6.69538637559
6.69452301658
7.55937468903
6.31407655431
8.16173165484
7.43836064991
6.79104414172
7.02641788456
10.3763849709
7.41759729425
7.58397109228
7.29240600133
7.10024681296
6.47484415229
8.03474059957
5.68368872332
8.15560509988
6.29573932417
6.80517750718
10.0629163617
7.20904082226
6.76654301695
6.16370381506
6.50233207259
8.59285796884
7.47619103431
8.87207548343
6.90818067426
7.7811401087
11.8469345332
5.49858080068
9.04662337992
7.33904642762
7.96959179147
7.52650521145
5.16784413359
9.55920124275
8.24306019945
7.9318249141
9.57246613925
6.58146965059
5.60990756287
9.53792438164
5.79102705637
5.33559365272
6.48809806813
7.66644773214
7.60246282819
7.23133792963
'''

pyeq2.dataConvertorService().ConvertAndSortColumnarASCII(asciiTextData, simpleObject, False)

resultList = []
solver = pyeq2.solverService()
criteriaForUseInListSorting = 'AIC' # ['AIC', 'AICc_BA', 'nnlf'] from top of SolverService.SolveStatisticalDistribution()
for distribution in inspect.getmembers(scipy.stats): # try to fit every distribution
    if isinstance(distribution[1], scipy.stats.rv_continuous):
        print("Fitting", distribution[0])
        try:
            result = solver.SolveStatisticalDistribution(distribution[0], simpleObject.dataCache.allDataCacheDictionary['IndependentData'][0], criteriaForUseInListSorting)
        except:
            continue
        if result:
            resultList.append(result)

print()
resultList.sort()
print(resultList[0])
