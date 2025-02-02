import MEAutility as mu
import numpy as np

# Here we define the positions of the electrode. I've put each row as a ring of the web
positions = np.array([[-4500, -6750], [-4676, -6574], [-4500, -6500], [-4324, -6574], [-4250, -6750], [-4324, -6926],
                          [-4500, -7000], [-4676, -6926], [-4750, -6750], [-4962, -6559], [-4804, -6353], [-4565, -6254],
                          [-4309, -6288], [-4103, -6446], [-4004, -6685], [-4038, -6941], [-4196, -7147], [-4435, -7246],
                          [-4691, -7212], [-4897, -7054], [-4996, -6815], [-5124, -6333], [-4917, -6126], [-4646, -6014],
                          [-4354, -6014], [-4083, -6126], [-3876, -6333], [-3764, -6604], [-3764, -6896], [-3876, -7167],
                          [-4083, -7374], [-4354, -7486], [-4646, -7486], [-4917, -7374], [-5124,-7167], [-5236, -6896],
                          [-5236, -6604], [-5366, -6250], [-5207, -6043], [-5000, -5884], [-4759, -5784], [-4500, -5750],
                          [-4242, -5785], [-4000, -5884], [-3793, -6043], [-3634, -6250], [-3534, -6491], [-3500, -6750],
                          [-3534, -7009], [-3634, -7250], [-3793, -7457], [-4000, -7616], [-4241, -7716], [-4500, -7750],
                          [-4759, -7716], [-5000, -7616], [-5207, -7457], [-5366, -7250], [-5466, -7009], [-5500, -6750],
                          [-5466, -6491], [-7200, -9300], [-8260, -6800], [-7060, -4020],
                          [4500, -6750], [4324, -6574], [4500, -6500], [4676, -6574], [4750, -6750], [4676, -6926],
                          [4500, -7000], [4324, -6926], [4250, -6750], [4038, -6559], [4196, -6353], [4435, -6254],
                          [4691, -6288], [4897, -6446], [4996, -6685], [4962, -6941], [4804, -7147], [4565, -7246],
                          [4309, -7212], [4103, -7054], [4004, -6815], [3876, -6333], [4083, -6126], [4354, -6014],
                          [4646, -6014], [4917, -6126], [5124, -6333], [5236, -6604], [5236, -6896], [5124, -7167],
                          [4917, -7374], [4646, -7486], [4354, -7486], [4083, -7374], [3876, -7167], [3764, -6896],
                          [3764, -6604], [3634, -6250], [3793, -6043], [4000, -5884], [4241, -5784], [4500, -5750],
                          [4758, -5785], [5000, -5884], [5207, -6043], [5366, -6250], [5466, -6491], [5500, -6750],
                          [5466, -7009], [5366, -7250], [5207, -7457], [5000, -7616], [4759, -7716], [4500, -7750],
                          [4241, -7716], [4000, -7616], [3793, -7457], [3634, -7250], [3534, -7009], [3500, -6750],
                          [3534, -6491], [7200, -9300], [8260, -6800], [7060, -4020],
                          [4500, 6750], [4324, 6926], [4500, 7000], [4676, 6926], [4750, 6750], [4676, 6574],
                          [4500, 6500], [4324, 6574], [4250, 6750], [4038, 6941], [4196, 7147], [4435, 7246],
                          [4691, 7212], [4897, 7054], [4996, 6815], [4962, 6559], [4804, 6353], [4565, 6254],
                          [4309, 6288], [4103, 6446], [4004, 6685], [3876, 7167], [4083, 7374], [4354, 7486],
                          [4646, 7486], [4917, 7374], [5124, 7167], [5236, 6896], [5236, 6604], [5124, 6333],
                          [4917, 6126], [4646, 6014], [4354, 6014], [4083, 6126], [3876, 6333], [3764, 6604],
                          [3764, 6896], [3634, 7250], [3793, 7457], [4000, 7616], [4241, 7716], [4500, 7750],
                          [4758, 7715], [5000, 7616], [5207, 7457], [5366, 7250], [5466, 7009], [5500, 6750],
                          [5466, 6491], [5366, 6250], [5207, 6043], [5000, 5884], [4759, 5784], [4500, 5750],
                          [4241, 5784], [4000, 5884], [3793, 6043], [3634, 6250], [3534, 6491], [3500, 6750],
                          [3534, 7009], [7200, 9300], [8260, 6800], [7060, 4020],
                          [-4500, 6750], [-4676, 6926], [-4500, 7000], [-4324, 6926], [-4250, 6750], [-4324, 6574],
                          [-4500, 6500], [-4676, 6574], [-4750, 6750], [-4962, 6941], [-4804, 7147], [-4565, 7246],
                          [-4309, 7212], [-4103, 7054], [-4004, 6815], [-4038, 6559], [-4196, 6353], [-4435, 6254],
                          [-4691, 6288], [-4897, 6446], [-4996, 6685], [-5124, 7167], [-4917, 7374], [-4646, 7486],
                          [-4354, 7486], [-4083, 7374], [-3876, 7167], [-3764, 6896], [-3764, 6604], [-3876, 6333],
                          [-4083, 6126], [-4354, 6014], [-4646, 6014], [-4917, 6126], [-5124, 6333], [-5236, 6604],
                          [-5236, 6896], [-5366, 7250], [-5207, 7457], [-5000, 7616], [-4759, 7716], [-4500, 7750],
                          [-4242, 7715], [-4000, 7616], [-3793, 7457], [-3634, 7250], [-3534, 7009], [-3500, 6750],
                          [-3534, 6491], [-3634, 6250], [-3793, 6043], [-4000, 5884], [-4241, 5784], [-4500, 5750],
                          [-4759, 5784], [-5000, 5884], [-5207, 6043], [-5366, 6250], [-5466, 6491], [-5500, 6750],
                          [-5466, 7009], [-7200, 9300], [-8260, 6800], [-7060, 4020]])

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
