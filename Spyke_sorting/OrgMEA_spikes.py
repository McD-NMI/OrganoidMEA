import spikeinterface
import spikeinterface.extractors as se
import spikeinterface.toolkit as st
import spikeinterface.sorters as ss
import spikeinterface.comparison as sc
import spikeinterface.widgets as sw
import matplotlib.pylab as plt
import numpy as np
import nixio
from pathlib import Path

#Lists of Channel IDs for each well
ch_w1 = np.array([93, 228, 107, 114, 236, 213, 89, 97, 222, 224, 106, 229, 232, 235, 115, 85, 88, 214, 217, 221, 98, 103, 227, 108, 110, 111, 113, 237, 209, 210, 212, 90, 92, 218, 96, 99, 102, 225, 104, 105, 230, 109, 231, 233, 112, 234, 116, 208, 84, 86, 211, 87, 215, 91, 216, 94, 219, 220, 100, 101, 223])+1
ch_w2 = np.array([60, 183, 56, 64, 192, 198, 74, 81 , 206, 52, 55, 184, 187, 191, 65, 194, 73, 199, 202, 205, 82, 180, 182, 57, 59, 188, 63, 66, 69, 70, 197, 75, 77, 78, 80, 207, 179, 53, 181, 54, 185, 58, 186, 61, 189, 190, 67, 68, 193, 195, 71, 72, 200, 76, 201, 203, 79, 204, 83,])+1
ch_w2 = np.array([27, 168, 41, 48, 176, 153, 23, 31, 162, 164, 40, 169, 172, 175, 49, 19, 22, 154, 157, 161, 32, 37, 167, 42, 44, 45, 47, 177, 149, 150, 152, 24, 26, 158, 30, 33, 36, 165, 38, 39, 170, 43, 171, 173, 46, 174, 50, 148, 18, 20, 151, 21, 155, 25, 156, 28, 159, 160, 34, 35, 163,])+1
ch_w4 = np.array([126, 243, 122, 130, 252, 138, 8, 15, 146, 118, 121, 244, 247, 251, 131, 134, 7, 139, 142, 145, 16, 240, 242, 123, 125, 248, 129, 132, 3, 4, 137, 9, 11, 12, 14, 147, 239, 119, 241, 120, 245, 124, 246, 127, 249, 250, 1, 2, 133, 135, 5, 6, 140, 10, 141, 143, 13, 144, 17, 238, 117])+1

recordings_folder = Path.cwd().parent / 'recordings'
recording_file = recordings_folder / "2019-11-12T15-38-27McsRecording.h5"
recording = se.MCSH5RecordingExtractor(recording_file)
recording_prb = recording.load_probe_file(probe_file = 'OrgMEA_252.prb')

#remove ground electrodes
recording_gnd_rem = st.preprocessing.remove_bad_channels(recording_prb, bad_channel_ids=np.array([226, 95, 196, 62, 29, 166, 136, 128])+1)

#filter signal
recording_f = st.preprocessing.bandpass_filter(recording_gnd_rem, freq_min=200, freq_max=6000)

#remove bad channels
#recording_f_gnd_bad_rem = st.preprocessing.remove_bad_channels(recording_f_gnd_rem, bad_channels=np.array([XX, XX, XX, XX])+1)

#recording_rm_noise = st.preprocessing.remove_bad_channels(recording_f, bad_channels=[5])
recording_cmr = st.preprocessing.common_reference(recording_f, reference='median')

save_folder = Path.cwd().parent / 'saved__sort_test.npz'
sorting = se.NpzSortingExtractor(save_folder)

w_wf2 = sw.plot_unit_waveforms(recording_f, sorting, max_spikes_per_unit=100)
