import os
from pyroSAR import identify
from pyroSAR.snap import geocode
from spatialist import Vector
from pyroSAR.auxdata import dem_autoload, dem_create

# maindir = '/home/truc_jh/Desktop/test/issue97'
maindir = '/home/ve39vem/DATA/test/issue97'

scene = 'S1B_IW_GRDH_1SDV_20180317T091416_20180317T091441_010069_01244C_EB9B.zip'
scene = os.path.join(maindir, scene)

bbox = os.path.join(maindir, 'bbox.shp')

if not os.path.isfile(bbox):
    id = identify(scene)
    id.bbox(bbox)

externaldem = os.path.join(maindir, 'dem.tif')
if not os.path.isfile(externaldem):
    vrt = os.path.join(maindir, 'dem.vrt')
    with Vector(bbox) as site:
        vrt = dem_autoload([site], 'SRTM 1Sec HGT', vrt=vrt)
        dem_create(src=vrt, dst=externaldem,
                   t_srs=32721, tr=(20, 20),
                   resampling_method='bilinear',
                   geoid_convert=True, geoid='EGM96')
    os.remove(vrt)

outdir = os.path.join(maindir, 'proc')

with Vector(bbox) as site:
    wf = geocode(infile=scene, outdir=outdir, t_srs=32721, shapefile=site,
                 removeS1ThermalNoise=False, scaling='db', tr=100,
                 externalDEMFile=externaldem, externalDEMApplyEGM=False,
                 returnWF=True, test=False)
