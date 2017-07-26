#! /bin/python

import numpy as np
from matplotlib import pyplot as plt
import matplotlib 
import os
import sys

def watplot(path):
    plotpath='plots_output'
    if not os.path.exists(plotpath):
        os.makedirs(plotpath)
    
    fld = str(path[7:11])
    #patch = patch + '1'
    #print str(path[12:22]) + patch 
    
    fh = np.genfromtxt(path)
    x = fh[:,0]
    y = fh[:,1]

    #print "fld is", fld
    #print "Patch is", patch

    if fld == 'inv1':
        TD = str(path[19:20])
        #print TD

        z = fh[:,2]

        plt.scatter(x,z)
        plt.xlabel('Inversion Coordinate 1')
        plt.ylabel('Bondlength difference')
        plt.savefig(plotpath+'/Zundel-'+TD+'ZVP-inv1-'+str(path[24:27]))
        #plt.show()

        plt.scatter(y,z)
        plt.xlabel('Inversion Coordinate 2')
        plt.ylabel('Bondlength difference')
        plt.savefig(plotpath+'/Zundel-'+TD+'ZVP-inv2-'+str(path[24:27]))
        #plt.show()
        
    elif fld == 'eigi': 

        TD = str(path[20:21])
        #print TD
         
        fld = str(path[29:32])
        #print fld

        if fld=="tim":
            plt.plot(x,y, label="Time Series")
            plt.xlabel('Steps')
            plt.ylabel('Probabilities')
            plt.title("timeseries")
            plt.legend() 
            plt.savefig(plotpath+'/Eigen-'+TD+'ZVP-tim-'+str(path[25:28]))

        else:

            plt.plot(x,y)
            plt.xlabel('Bins ')
            plt.ylabel('Probabilities')
            plt.savefig(plotpath+'/Eigen-'+TD+'ZVP-inv-'+str(path[25:28]))

    elif fld == 'gen/':

        print fld
        TD = str(path[20:21])
        print TD

        fh = np.genfromtxt(path,skip_header=1)
        x = fh[:,0]
        y = fh[:,3]
        z = fh[:,4]
       
        plt.plot(x,y,label='Temperature')
        plt.legend()
        plt.xlabel('Steps')
        plt.ylabel('Temp [K]')
        plt.savefig(plotpath+'/Eigen-'+TD+'ZVP-temp-'+ str(path[25:28]) )
        plt.show(block=False)

        plt.plot(x,z,label='Potential', color='r')
        plt.xlabel('Steps')
        plt.ylabel('Potential Energy [a.u.]')
        #plt.ticklabel_format(useOffset=False)
        plt.legend()
        plt.savefig(plotpath+'/Eigen-'+TD+'ZVP-pot-'+ str(path[25:28]) )

    elif fld == 'ndel':

        print fld
        TD = str(path[28:29])
        print TD

        fh1 = np.genfromtxt(path,skip_header=1)
        x1 = fh1[:,0]
        y1 = fh1[:,3]
        z1 = fh1[:,4]
       
        plt.plot(x1,y1,label='Temperature')
        plt.legend()
        plt.xlabel('Steps')
        plt.ylabel('Temp [K]')
        #plt.title('Eigen DZVP @ 150 K Temp')
        plt.savefig(plotpath+'/Zundel-'+TD+'ZVP-temp-'+ str(path[33:36]) )

        plt.plot(x1,z1,label='Potential', color='r')
        plt.legend()
        plt.xlabel('Steps')
        plt.ylabel('Potential Energy [a.u.]')
        plt.ticklabel_format(useOffset=False)
        #plt.title('Eigen DZVP @ 050 K Temp')
        plt.savefig(plotpath+'/Zundel-'+TD+'ZVP-pot-'+ str(path[33:36]) )


    else:

        TD = str(path[19:20])
        #print TD

        print fld

        plt.scatter(x,y)
        plt.xlabel('Bondlength ')
        plt.ylabel('Cosine $\Theta$')
        plt.savefig(plotpath+'/Zundel-'+TD+'ZVP-dotp-'+str(path[24:28]))
        #plt.show()

if __name__ == '__main__':
    watplot(sys.argv[1])
