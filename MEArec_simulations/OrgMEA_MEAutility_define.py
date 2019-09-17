import MEAutility as mu
import numpy as np

# Here we define the positions of the electrode. I've put each row as a ring of the web
web_positions = np.array([[0, 0],
                     [-176, 176], [0, 250], [176, 176], [250, 0], [176, -176], [0, -250], [-176, -176], [-250, 0],
                     [-462, 191], [-304, 397], [-65, 496], [191, 462], [397, 304], [496, 65], [462, -191], [304, -397], [65, -496], [-191, -462], [-397, -304], [-496, -65],
                     [-624, 417], [-417, 624], [-146, 736], [146, 736], [417, 624], [624, 417], [736, 146], [736, -146], [624, -417], [417, -624], [146, -736], [-146, -736], [-417, -624], [-624, -417], [-736, -146], [-736, 146],
                     [-866, 500], [-707, 707], [-500, 866], [-259, 966], [0, 1000], [258, 965], [500, 866], [707, 707], [866, 500], [966, 259], [1000, 0], [966, -259], [866, -500], [707, -707], [500, -866], [259, -966], [0, -1000], [-259, -966], [-500, -866], [-707, -707], [-866, -500], [-966, -259], [-1000, 0], [-966, 259]])

well_positions = np.array([[-4500, -6750], [4500, -6750], [4500, 6750], [-4500, 6750]])

positions =

# Here we define the dictionary with the definitions for the mea object to pass
probe_info = {'electrode_name': 'OrgMEA',
              'description': 'Organoid MEA',
              'pos': positions,
              'size': 30,
              'shape': 'circle',
              'type': 'mea',
              'sortlist': None,
              'plane': 'xy'}

#Here we create the mea object based on the dictionary (and positions)
mea_object = mu.return_mea(info=probe_info)

#Here we create the .yaml file that is available to the whole system to use
mu.add_mea(mea_object)
