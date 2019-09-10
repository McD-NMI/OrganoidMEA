import MEArec as mr
import MEAutility as mu
import yaml
from pprint import pprint
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # First lets load the default configuration of MEArec
    default_info, mearec_home = mr.get_default_config()
    pprint(default_info)

    # define cell_models folder
    cell_folder = default_info['cell_models_folder']
    template_params = mr.get_default_templates_params()

    # Now let's change a few parameters
    template_params['n'] = 60
    template_params['probe'] = 'OrgMEA'
    template_params['xlim'] = None
    template_params['ylim'] = None
    template_params['zlim'] = [10, 80]

    tempgen = mr.gen_templates(cell_models_folder=cell_folder, params = template_params)

    print('Templates shape', tempgen.templates.shape)
    print('Sample locations', tempgen.locations[:3])
    print('Sample rotations', tempgen.rotations[:3])
    print('Sample cell types', tempgen.celltypes[:3])

    mr.save_template_generator(tempgen, filename='templates/OrgMEA_n60_templates.h5')
