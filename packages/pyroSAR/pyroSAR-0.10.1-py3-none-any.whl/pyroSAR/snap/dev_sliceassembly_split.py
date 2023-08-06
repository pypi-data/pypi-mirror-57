import shutil
from pyroSAR.snap import geocode
from pyroSAR.snap.auxil import groupbyWorkers, split

import logging
logging.basicConfig(level=logging.DEBUG)

files = ['/home/truc_jh/Desktop/Projects/S1_ARD/data/S1/S1A_IW_GRDH_1SDV_20180826T053453_20180826T053518_023413_028C38_716B.zip',
         '/home/truc_jh/Desktop/Projects/S1_ARD/data/S1/S1A_IW_GRDH_1SDV_20180826T053518_20180826T053543_023413_028C38_5AAF.zip']

outdir = '/home/truc_jh/Desktop/test/sliceassembly'

shutil.rmtree(outdir)

wf = geocode(files, outdir=outdir, tr=20, test=True, returnWF=True)

groups = groupbyWorkers(wf, 4)

split(wf, groups)
