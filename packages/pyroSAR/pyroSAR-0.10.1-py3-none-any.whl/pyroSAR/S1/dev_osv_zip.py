from pyroSAR import identify

scene = '/home/truc_jh/Desktop/Projects/S1_ARD/data/S1/S1A_IW_GRDH_1SDV_20180101T170648_20180101T170713_019964_021FFD_DA78.zip'

id = identify(scene)

id.getOSV(outdir='/home/truc_jh/Desktop/osv_test')
