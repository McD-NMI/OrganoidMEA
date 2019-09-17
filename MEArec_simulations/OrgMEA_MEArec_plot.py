import MEArec as mr
import matplotlib.pyplot as plt


# load recordings
recgen = mr.load_recordings('recordings/OrgMEA_recording_test_02.h5')

#mr.plot_templates(recgen, single_axes=False, ncols=4)
#mr.plot_templates(recgen, single_axes=True, cmap='rainbow')
#mr.plot_recordings(recgen)
mr.plot_recordings(recgen, start_time=0, end_time=0.01)#, overlay_templates=True)
#mr.plot_waveforms(recgen, electrode='max', cmap='rainbow')
#mr.plot_rasters(recgen.spiketrains)
plt.show()