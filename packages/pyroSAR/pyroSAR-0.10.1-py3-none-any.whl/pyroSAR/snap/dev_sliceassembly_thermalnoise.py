import os
from pyroSAR.snap import geocode
from spatialist.ancillary import finder

import logging
logging.basicConfig(level=logging.DEBUG)

files = ['/home/truc_jh/Desktop/Projects/S1_ARD/data/S1/S1A_IW_GRDH_1SDV_20180826T053453_20180826T053518_023413_028C38_716B.zip',
         '/home/truc_jh/Desktop/Projects/S1_ARD/data/S1/S1A_IW_GRDH_1SDV_20180826T053518_20180826T053543_023413_028C38_5AAF.zip']

workflows = finder('/home/truc_jh/Desktop/test/sliceassembly', ['*'])
for workflow in workflows:
    os.remove(workflow)

geocode(infile=files, outdir='/home/truc_jh/Desktop/test/sliceassembly', removeS1BorderNoiseMethod='ESA', test=True)
