import numpy as np
import matplotlib.pyplot as plt
    
def cartesian():
    fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, sharex = True, sharey = True)
    fig.suptitle('1-Minute Waveforms: 6:24pm')  
    fig.text(0.5, -0.02, 'Time (s)', ha='center')
    fig.text(-0.04, 0.5, 'Voltage (mV)', va='center', rotation='vertical')
    
    fig.tight_layout()
    fig.subplots_adjust(top=0.88)
    
    ax1.axhline(y=0, lw = 0.5, ls = '--')
    ax1.yaxis.set_label_position('right')
    ax1.set_ylabel('Dagupan')
    ax1.set_ylim([-500, 500])
    
    ax2.axhline(y=0, lw = 0.5, ls = '--')
    ax2.yaxis.set_label_position('right')
    ax2.set_ylabel('Legazpi')
    
    ax3.axhline(y=0, lw = 0.5, ls = '--')
    ax3.yaxis.set_label_position('right')
    ax3.set_ylabel('Palawan')
    
    ax4.axhline(y=0, lw = 0.5, ls = '--')
    ax4.yaxis.set_label_position('right')
    ax4.set_ylabel('UPLB')


    return ax1, ax2, ax3, ax4

def plot_data(waves_stack, ax, col):
    for i in range(len(waves_stack)):
        ax.plot(waves_stack[i,:,0],waves_stack[i,:,1],'-', color = col)