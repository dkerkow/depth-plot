###############################
import pandas as pd
import matplotlib.pyplot as plt
from pylab import figure, show


#######################
###   Data Import   ###
#######################

# read Excel (2003) File:
daten_xls = pd.ExcelFile('plot.xls')

# parse file into panda dataframe ('datasheet_name', index_col='index_column_name' , na_values=['NA'])
daten = daten_xls.parse('summary', index_col='id', na_values=['NA'])


#######################
###   Plotting   ######
#######################

fig = plt.figure(figsize=(20, 8)) # manually adjust x,y dimension of plot canvas
fig.suptitle('Ergebnisse Elementbestimmung')
fig.subplots_adjust(wspace=0.3) # space between subplots in [inch]


### Sub-Plot 1

ax = fig.add_subplot(1,3,1) ## (total number of rows,columns, index of this subplot)
ax.plot(daten['loi_toc_perc'], daten['depth'], 'ro--') # column names of the data and depth values, last argument is for the line properties.
plt.xlabel('%') # Label on the x-axis of this subplot
plt.ylabel('Tiefe [cm]') # only for the first subplot!!!
plt.title('TOC (LOI)')
plt.locator_params(axis='x', tight=False, nbins=3) # adjustment of ticks on the x-axis of this subplot, tight=False/True, nbins=count of bins
plt.grid(True) # turn on/off the grid for this subplot
plt.ylim(ymax=223) # manually set the range for the depth axis. set the max depth here.
plt.ylim(ymin=0) # manually set the range for the depth axis. set the min depth here.
plt.gca().invert_yaxis() # inverts the y-axis. Dont change this unless you want to change bottom/top.


### Sub-Plot 2

ax = fig.add_subplot(1,3,2)
ax.plot(daten['calcit_perc'], daten['depth'], 'ro--')
plt.xlabel('%')
plt.title('Calcit (LOI)')
plt.locator_params(axis='x', tight=False, nbins=3) 
plt.grid(True)
plt.ylim(ymax=223)
plt.ylim(ymin=0)
plt.gca().invert_yaxis() 
ax.set_yticklabels( () ) # no tick labels on y-axis for the other axes than the first one. 

### Sub-Plot 3

ax = fig.add_subplot(1,3,3)
ax.plot(daten['loi_tic_perc'], daten['depth'], 'ro--')
plt.xlabel('%')
plt.title('TIC (LOI)')
plt.locator_params(axis='x', tight=False, nbins=3)
plt.grid(True)
plt.ylim(ymax=223)
plt.ylim(ymin=0)
plt.gca().invert_yaxis()
ax.set_yticklabels( () ) # no tick labels on y-axis for the other axes than the first one.


##################################
###  Exporting to SVG and PNG  ###
##################################

plt.savefig("plot.svg")
plt.savefig("plot.png",dpi=(640/8))

#reset the graphic device:
figure()
