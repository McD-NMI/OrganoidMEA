import MEAutility as mu
import matplotlib.pylab as plt
import numpy as np

#Get the OrgMEA mea object info
OrgMEA_info = mu.return_mea_info('OrgMEA')

#Check the info about this mea object
#pprint(OrgMEA_info)

# Get the OrgMEA mea object info
OrgMEA = mu.return_mea('OrgMEA')

#Check the type and # of electrodes of the mea object, also plot the electrode positions
# print(type(OrgMEA))
# print(OrgMEA.number_electrodes)
# #OrgMEA.move([500,500, 0])
# #OrgMEA.rotate([0,1,0], 45)
# plt.plot(OrgMEA.positions[:,0], OrgMEA.positions[:,1], 'b*')
# plt.axis('equal')
# plt.show()

#Check the positions of a few electrodes
# print(OrgMEA[0].position)
# print(OrgMEA[1].position)
# print(OrgMEA[2].position)
# print(OrgMEA[3].position)

#Check the plane of the mea
# print(OrgMEA.plane)

#PLot a probe view of the mea
# mu.plot_probe(OrgMEA)
# plt.show()

#Plot some randsom noise recordings
signals = np.random.randn(OrgMEA.number_electrodes, 10000)
mu.plot_mea_recording(signals, OrgMEA, lw=0.1)
plt.show()