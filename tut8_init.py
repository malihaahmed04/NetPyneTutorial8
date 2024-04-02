from netpyne import sim
import matplotlib.pyplot as plt

# read cfg and netParams from command line arguments if available; otherwise use default
simConfig, netParams = sim.readCmdLineArgs(simConfigDefault='tut8_cfg.py', netParamsDefault='tut8_netParams.py')

randomname = 3
randomname2 = 4
with open('tut8_output.txt', "a") as tut8_output_txt:
    l1 = '\n [%.3f,' % randomname
    l2 = '%.3f],' % randomname2
    tut8_output_txt.writelines([l1,l2])
    
    
# Create network and run simulation
sim.create(netParams, simConfig)
sim.simulate()
sim.analyze()

#print(sim.allSimData.t)
stimtimevec = sim.allSimData.t

VavgM=np.zeros(len(sim.allSimData.t))
for i in range(20,40):
    arrayname = f'cell_{i}'
    VavgM = np.add(VavgM,sim.allSimData.V_soma[arrayname])
VavgM = (1/20)*VavgM

plt.figure(figsize=(10,6))
plt.plot(stimtimevec,VavgM)
plt.xlabel("Time (ms)")
plt.ylabel("Voltage (mV)")
#plt.rcParams['font.size'] = 16
#plt.savefig(f'LFP.png')
plt.savefig("{}.png".format(cfg.simLabel))

randomname = 3
randomname2 = 4
with open('tut8_output.txt', "a") as tut8_output_txt:
    l1 = '\n [%.3f,' % randomname
    l2 = '%.3f],' % randomname2
    tut8_output_txt.writelines([l1,l2])
