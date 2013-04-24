###############################
import pandas as pd
import matplotlib.pyplot as plt
from pylab import figure, show


#######################
###   Data Import   ###
#######################

# read Excel (2003) File:
daten_xls = pd.ExcelFile('plot.xls')

# parse file into panda dataframe
daten = daten_xls.parse('summary', index_col='id', na_values=['NA'])


#######################
###   Plotting   ######
#######################


fig = plt.figure(figsize=(20, 8))
fig.suptitle('Ergebnisse Elementbestimmung')
fig.subplots_adjust(wspace=0.3) # space between subplots in [inch]


### Sub-Plot: loi_toc_perc (1)

ax = fig.add_subplot(1,13,1) ## (rows,columns,idx)
ax.plot(daten['loi_toc_perc'], daten['depth'], 'ro--')
plt.xlabel('%')
plt.ylabel('Tiefe [cm]') # only for the first subplot!!!
plt.title('TOC (LOI)')
plt.locator_params(axis='x', tight=False, nbins=3) # Einstellen der Ticks auf x-Achse
plt.grid(True)
plt.ylim(ymax=223) # adjust the max leaving min unchanged
plt.ylim(ymin=0) # adjust the min leaving max unchanged
plt.gca().invert_yaxis() #invert the y-axis


### Sub-Plot: calcit_perc (2)

ax = fig.add_subplot(1,13,2) ## (rows,columns,idx)
ax.plot(daten['calcit_perc'], daten['depth'], 'ro--')
plt.xlabel('%')
plt.title('Calcit (LOI)')
plt.locator_params(axis='x', tight=False, nbins=3) # Einstellen der Ticks auf x-Achse
plt.grid(True)
plt.ylim(ymax=223) # adjust the max leaving min unchanged
plt.ylim(ymin=0) # adjust the min leaving max unchanged
plt.gca().invert_yaxis() # invert the y-axis
ax.set_yticklabels( () ) # no yticklabels for the other axes 

### Sub-Plot: loi_tc_perc (3)

ax = fig.add_subplot(1,13,3) ## (rows,columns,idx)
ax.plot(daten['loi_tic_perc'], daten['depth'], 'ro--')
plt.xlabel('%')
plt.title('TIC (LOI)')
plt.locator_params(axis='x', tight=False, nbins=3) # Einstellen der Ticks auf x-Achse
plt.grid(True)
plt.ylim(ymax=223) # adjust the max leaving min unchanged
plt.ylim(ymin=0) # adjust the min leaving max unchanged
plt.gca().invert_yaxis() # invert the y-axis
ax.set_yticklabels( () ) # no yticklabels for the other axes


### Sub-Plot: loi_tc_perc (3)

ax = fig.add_subplot(1,13,4) ## (rows,columns,idx)
ax.plot(daten['loi_tc_perc'], daten['depth'], 'ro--')
plt.xlabel('%')
plt.title('TC (LOI)')
plt.locator_params(axis='x', tight=False, nbins=3) # Einstellen der Ticks auf x-Achse
plt.grid(True)
plt.ylim(ymax=223) # adjust the max leaving min unchanged
plt.ylim(ymin=0) # adjust the min leaving max unchanged
plt.gca().invert_yaxis() # invert the y-axis
ax.set_yticklabels( () ) # no yticklabels for the other axes 


### Sub-Plot: woest_toc_perc (4)

ax = fig.add_subplot(1,13,5) ## (rows,columns,idx)
ax.plot(daten['woest_toc_perc'], daten['depth'], 'ro--')
plt.xlabel('%')
plt.title('TOC (Woest.)')
plt.locator_params(axis='x', tight=False, nbins=3) # Einstellen der Ticks auf x-Achse
plt.grid(True)
plt.ylim(ymax=223) # adjust the max leaving min unchanged
plt.ylim(ymin=0) # adjust the min leaving max unchanged
plt.gca().invert_yaxis() # invert the y-axis
ax.set_yticklabels( () ) # no yticklabels for the other axes 


### Sub-Plot: woest_tic_perc (5)

ax = fig.add_subplot(1,13,6) ## (rows,columns,idx)
ax.plot(daten['woest_tic_perc'], daten['depth'], 'ro--')
plt.xlabel('%')
plt.title('TIC (Woest.)')
plt.locator_params(axis='x', tight=False, nbins=3) # Einstellen der Ticks auf x-Achse
plt.grid(True)
plt.ylim(ymax=223) # adjust the max leaving min unchanged
plt.ylim(ymin=0) # adjust the min leaving max unchanged
plt.gca().invert_yaxis() # invert the y-axis
ax.set_yticklabels( () ) # no yticklabels for the other axes 


### Sub-Plot: woest_tc_perc (6)

ax = fig.add_subplot(1,13,7) ## (rows,columns,idx)
ax.plot(daten['woest_tc_perc'], daten['depth'], 'ro--')
plt.xlabel('%')
plt.title('TC (Woest.)')
plt.locator_params(axis='x', tight=False, nbins=3) # Einstellen der Ticks auf x-Achse
plt.grid(True)
plt.ylim(ymax=223) # adjust the max leaving min unchanged
plt.ylim(ymin=0) # adjust the min leaving max unchanged
plt.gca().invert_yaxis() # invert the y-axis
ax.set_yticklabels( () ) # no yticklabels for the other axes 


### Sub-Plot: icp_ca (7)

ax = fig.add_subplot(1,13,8) ## (rows,columns,idx)
ax.plot(daten['icp_ca'], daten['depth'], 'ro--')
plt.xlabel('mg/g')
plt.title('Ca (ICP)')
plt.locator_params(axis='x', tight=False, nbins=3) # Einstellen der Ticks auf x-Achse
plt.grid(True)
plt.ylim(ymax=223) # adjust the max leaving min unchanged
plt.ylim(ymin=0) # adjust the min leaving max unchanged
plt.gca().invert_yaxis() # invert the y-axis
ax.set_yticklabels( () ) # no yticklabels for the other axes 


### Sub-Plot: icp_mg (8)

ax = fig.add_subplot(1,13,9) ## (rows,columns,idx)
ax.plot(daten['icp_mg'], daten['depth'], 'ro--')
plt.xlabel('mg/g')
plt.title('Mg (ICP)')
plt.locator_params(axis='x', tight=False, nbins=3) # Einstellen der Ticks auf x-Achse
plt.grid(True)
plt.ylim(ymax=223) # adjust the max leaving min unchanged
plt.ylim(ymin=0) # adjust the min leaving max unchanged
plt.gca().invert_yaxis() # invert the y-axis
ax.set_yticklabels( () ) # no yticklabels for the other axes 

### Sub-Plot: icp_fe (9)

ax = fig.add_subplot(1,13,10) ## (rows,columns,idx)
ax.plot(daten['icp_fe'], daten['depth'], 'ro--')
plt.xlabel('mg/g')
plt.title('Fe (ICP)')
plt.locator_params(axis='x', tight=False, nbins=3) # Einstellen der Ticks auf x-Achse
plt.grid(True)
plt.ylim(ymax=223) # adjust the max leaving min unchanged
plt.ylim(ymin=0) # adjust the min leaving max unchanged
plt.gca().invert_yaxis() # invert the y-axis
ax.set_yticklabels( () ) # no yticklabels for the other axes 


### Sub-Plot: icp_sr (10)

ax = fig.add_subplot(1,13,11) ## (rows,columns,idx)
ax.plot(daten['icp_s'], daten['depth'], 'ro--')
plt.xlabel('mg/g')
plt.title('S (ICP)')
plt.locator_params(axis='x', tight=False, nbins=3) # Einstellen der Ticks auf x-Achse
plt.grid(True)
plt.ylim(ymax=223) # adjust the max leaving min unchanged
plt.ylim(ymin=0) # adjust the min leaving max unchanged
plt.gca().invert_yaxis() # invert the y-axis
ax.set_yticklabels( () ) # no yticklabels for the other axes 


### Sub-Plot: icp_po4 

ax = fig.add_subplot(1,13,12) ## (rows,columns,idx)
ax.plot(daten['icp_po4'], daten['depth'], 'ro--')
plt.xlabel('mg/g')
plt.title('PO4 (ICP)')
plt.locator_params(axis='x', tight=False, nbins=3) # Einstellen der Ticks auf x-Achse
plt.grid(True)
plt.ylim(ymax=223) # adjust the max leaving min unchanged
plt.ylim(ymin=0) # adjust the min leaving max unchanged
plt.gca().invert_yaxis() # invert the y-axis
ax.set_yticklabels( () ) # no yticklabels for the other axes 


### Sub-Plot: photo_po4 

ax = fig.add_subplot(1,13,13) ## (rows,columns,idx)
ax.plot(daten['photo_po4'], daten['depth'], 'ro--')
plt.xlabel('mg/g')
plt.title('PO4 (Photom.)')
plt.locator_params(axis='x', tight=False, nbins=3) # Einstellen der Ticks auf x-Achse
plt.grid(True)
plt.ylim(ymax=223) # adjust the max leaving min unchanged
plt.ylim(ymin=0) # adjust the min leaving max unchanged
plt.gca().invert_yaxis() # invert the y-axis
ax.set_yticklabels( () ) # no yticklabels for the other axes

##################################
###  Exporting to SVG and PNG  ###
##################################
plt.savefig("plot.svg")
plt.savefig("plot.png",dpi=(640/8))

#reset the graphic device:
figure()
