from pyroSAR.datacube_util import Product, Dataset
from pyroSAR.ancillary import find_datasets

# find pyroSAR files by metadata attributes
archive_s1 = '/home/truc_jh/Desktop/Projects/S1_ARD/data/GAMMA/S1A__IW___A_20180829T170656_AW3D30'
scenes_s1 = find_datasets(archive_s1, sensor=('S1A', 'S1B'), acquisition_mode='IW')

# define the polarization units describing the data sets
units = {'VV': 'backscatter VV', 'VH': 'backscatter VH'}

# create a new product
with Product(name='S1_GRD_index',
             product_type='gamma0',
             description='Gamma Naught RTC backscatter') as prod:
    for dataset in scenes_s1:
        with Dataset(dataset, units=units) as ds:
            # add the dataset to the product
            prod.add(ds)
            
            # parse datacube indexing YMLs from product and data set metadata
            try:
                prod.export_indexing_yml(ds, '/home/truc_jh/Desktop/datacube_test')
            except RuntimeError:
                continue
    
    # write the product YML
    prod.write('prod.yml')
    
    # print the product metadata which is written to the product YML
    print(prod)
