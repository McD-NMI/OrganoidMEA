import numpy as np
import spikeinterface.extractors as se
import spikeinterface.widgets as sw
import matplotlib.pyplot as plt

recording, sorting_true = se.example_datasets.toy_example(duration=10, num_channels=256, seed=0)

recording_OrgMEA = recording.load_probe_file(probe_file='OrgMEA_252.prb')

print('Channel ids:', recording_OrgMEA.get_channel_ids())
print('Loaded properties', recording_OrgMEA.get_shared_channel_property_names())
print('Label of channel 60:', recording_OrgMEA.get_channel_property(channel_id=60, property_name='label'))

w_el_OrgMEA = sw.plot_electrode_geometry(recording_OrgMEA)
plt.show()
