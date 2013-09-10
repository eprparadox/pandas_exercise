#def pattern_stats(file_IN):

### this is script that i'll use as a pandas exercise .  it takes one of the text files that the matlab  ### create pivot files creates as input and then will create all the standard plots we need.  BOLD time 
### series by ROI (also by trial type?), accuracy time series by ROIs, bar plots of mean delay BOLD by ### rois, bar plots of mean accuracy in the delay period by ROI,  distintiveness time series and bar 
### plots by ROI, then comparisons of all the above amongst span and drug groups

file_IN = 'Dopamine_pattern_scheme3_resultsX_concise_logreg_bp_mr_pfc_pen10K.txt'

### import relevant modules 
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt

### read in data
data = pd.read_table(file_IN, sep='\t')

### parse name and report
#metadata = file_IN.rsplit('_')
#the_pen = metadata[-1]; last = the_pen.split('.')[0]; last = test.split('.')[0]

#	print '-{0}- data set using -{1}- and the -{2}- classifier, -{3}- filtering \
#		and penalty -{4}-.'.format(metadata[0],metadata[2],metadata[5],metadata[6],last)

### remove column of NaNs
del data['Unnamed: 9']


## get a list of all the metrics we recorded 
metrics = set(data.measure)
metrics = list(metrics)


## ok, the 1st thing we want to do is get a plot of average acc in each ROI
## to do this, we select out the measure we want (total_accuracy) then
## select the ROI we want, then do something else 
#stage1 = data[data['measure'] == 'total_BOLD']

for metric in metrics:
	stage1 = data[data['measure'] == metric]	
	stage1.set_index('TR')
	table = pd.pivot_table(stage1,values='data',rows=['TR'],cols=['mask'])
	
	## plot this metric over the entire trial
	table.plot()
	time.sleep(5.5)    # pause 5.5 seconds
	plt.close("all")