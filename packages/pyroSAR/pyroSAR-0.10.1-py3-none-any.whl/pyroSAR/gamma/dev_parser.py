# import os
#
# print('\n'.join(sorted(os.environ.keys())))
#
from pyroSAR.gamma.parser import parse_command
#
# cmd = parse_command('/home/truc_jh/GAMMA_SOFTWARE-20181130/DIFF/bin/coord_to_sarpix')
cmd = parse_command('/home/truc_jh/GAMMA_SOFTWARE-20191203/DIFF/bin/coord_to_sarpix')

print(cmd)

# from pyroSAR.gamma.api import diff