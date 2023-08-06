import os.path
import os
import sentinel_api as api
from pyroSAR import Archive, identify
from spatialist.ancillary import finder
from spatialist import Vector, stack
from pyroSAR.snap import geocode

rawdir = "/geonfs02_vol3/le67hed/delta/test/"
tempdir = "/tmp/"
area = "/home/le67hed/shapefiles/delta_latlong.shp"
testsite = "/home/le67hed/shapefiles/delta_latlong.shp"
dbfile = os.path.join(rawdir, "scenelist.db")
outdir = "/home/le67hed/outdir/"

for dir in [tempdir, outdir, rawdir]:
    if not os.path.isdir(dir):
        os.makedirs(dir)

username = ""
password = ""
s1 = api.SentinelDownloader(username, password, api_url='https://scihub.copernicus.eu/dhus/')
scenelist = finder(rawdir, ["S1*GRDH*.zip"])
with Archive(dbfile) as archive:
    archive.insert(scenelist)
    # Retrieval of the data for a smaller testsite
    site = Vector(testsite)
    mindate = "20140430T000000"
    maxdate = "20190630T235959"
    processlist = archive.select(vectorobject=site, processdir=outdir, mindate=mindate, maxdate=maxdate,
                                 sensor=("S1A", "S1B"), product='GRD', acquisition_mode="IW")

print(processlist)

for scene in processlist:
    geocode(infile=scene, outdir=outdir, shapefile=testsite, tr=10, polarizations='VH', scaling="dB",
            removeS1ThermalNoise=False)

#######################################################
import os
from pyroSAR.snap import geocode
from pyroSAR import identify
from spatialist import Vector
from pyroSAR.snap import ExamineSnap
from pyroSAR.S1 import OSV

scene = '/geonfs01_vol1/ve39vem/S1_ARD/data/S1/S1A_IW_GRDH_1SDV_20180101T170648_20180101T170713_019964_021FFD_DA78.zip'
outdir = '/geonfs01_vol1/ve39vem/test/Mariela'
shp = '/geonfs01_vol1/ve39vem/S1_ARD/data/testsite_alps.shp'

id = identify(scene)

# id.quicklook(os.path.join(outdir, 'quicklook.kmz'))

osvdir = os.path.join(ExamineSnap().auxdatapath, 'Orbits', 'Sentinel-1')

id.getOSV(osvdir)


with Vector(shp) as site:
    geocode(infile=scene, outdir=outdir, shapefile=site, tr=10, polarizations='VH', scaling="dB",
            removeS1ThermalNoise=False)
