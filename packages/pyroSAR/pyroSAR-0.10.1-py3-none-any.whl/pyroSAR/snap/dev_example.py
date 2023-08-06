import os
from pyroSAR import identify
from pyroSAR.snap.auxil import parse_recipe, parse_node, groupbyWorkers

scene = '/home/truc_jh/Desktop/Projects/S1_ARD/data/S1/S1A_IW_GRDH_1SDV_20180101T170648_20180101T170713_019964_021FFD_DA78.zip'
id = identify(scene)
outname = os.path.join('/home/truc_jh/Desktop', id.outname_base())

workflow = parse_recipe('blank')

read = parse_node('Read')
read.parameters['file'] = scene
read.parameters['formatName'] = 'SENTINEL-1'
workflow.insert_node(read)

tnr = parse_node('ThermalNoiseRemoval')
workflow.insert_node(tnr, before=read.id)

bnr = parse_node('Remove-GRD-Border-Noise')
bnr.parameters['selectedPolarisations'] = ['VV']
workflow.insert_node(bnr, before=tnr.id)

write = parse_node('Write')
write.parameters['file'] = 'outname'
write.parameters['formatName'] = 'BEAM-DIMAP'
workflow.insert_node(write, before=bnr.id)

workflow.write('/home/truc_jh/Desktop/outname_proc')

print(groupbyWorkers('/home/truc_jh/Desktop/outname_proc.xml', n=1))
