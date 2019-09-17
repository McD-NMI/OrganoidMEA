
import MEArec as mr
from pprint import pprint
import matplotlib.pyplot as plt

def main():

    recordings_params = mr.get_default_recordings_params()
    pprint(recordings_params)

    recordings_params['spiketrains']['n_exc'] = 50
    recordings_params['spiketrains']['n_inh'] = 120
    recordings_params['templates']['min_dist'] = 25
    recordings_params['templates']['overlap_threshhold'] = 0.9
    recordings_params['templates']['n_jitters'] = 5

    pprint(recordings_params)

    recgen = mr.gen_recordings(templates='templates/OrgMEA_n60_templates.h5', params=recordings_params)

    print('Recordings shape', recgen.recordings.shape)
    print('Selected templates shape', recgen.recordings.shape)
    print('Sample template locations', recgen.template_locations[:3])
    print('Number of neurons', len(recgen.spiketrains))
    print('Sample spike train', recgen.spiketrains[0].times)

    mr.save_recording_generator(recgen, filename='recordings/OrgMEA_recording_test_01.h5')

    mr.plot_templates(recgen, single_axes=False, ncols=4)
    mr.plot_templates(recgen, single_axes=True, cmap='rainbow')
    mr.plot_recordings(recgen)
    mr.plot_recordings(recgen, start_time=0, end_time=1, overlay_templates=True)
    mr.plot_waveforms(recgen, electrode='max', cmap='rainbow')
    mr.plot_rasters(recgen.spiketrains)
    plt.show()

if __name__ == '__main__':
    main()