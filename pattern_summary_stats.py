#def pattern_stats(file_IN):

### this is script that i'll use as a pandas exercise .  it takes one of the text files that the matlab  ### create pivot files creates as input and then will create all the standard plots we need.  BOLD time 
### series by ROI (also by trial type?), accuracy time series by ROIs, bar plots of mean delay BOLD by ### rois, bar plots of mean accuracy in the delay period by ROI,  distinctiveness time series and bar 
### plots by ROI, then comparisons of all the above amongst span and drug groups

file_IN = 'Dopamine_pattern_scheme3_resultsX_concise_logreg_bp_mr_pfc_pen10K.txt'

### import relevant modules 
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
import os


## make sure we have space to save
directory, dummy = os.path.split(os.path.realpath(file_IN))
if not os.path.exists(directory + '/figures/'):
	os.mkdir(directory + '/figures/')
	os.mkdir(directory + '/figures/accuracy')
	os.mkdir(directory + '/figures/BOLD')
	os.mkdir(directory + '/figures/distinctiveness')
	
### read in data
data = pd.read_table(file_IN, sep='\t')

### parse name and report
metadata = file_IN.rsplit('_')
the_pen = metadata[-1]; last = the_pen.split('.')[0]; the_pen = last
dataset = metadata[0]; scheme = metadata[2];
classifier_method = metadata[5]; filter_type = metadata[6]

print '-{0}- data set using -{1}- and the -{2}- classifier, -{3}- filtering,' \
'and penalty -{4}-.'.format(dataset, scheme, classifier_method, filter_type, the_pen)
	#metadata[0],metadata[2],metadata[5],metadata[6],last)

### remove column of NaNs
del data['Unnamed: 9']


## get a list of all the metrics we recorded 
metrics = set(data.measure)
metrics = list(metrics)


## ok, the 1st thing we want to do is get a plot of average acc in each ROI
## to do this, we select out the measure we want (total_accuracy) then
## select the ROI we want, then do something else 
#stage1 = data[data['measure'] == 'total_BOLD']

os.chdir(directory + '/figures/')

for metric in metrics:
	
	#############################
	## first do the line plots ##
	#############################

	stage1 = data[data['measure'] == metric]	
	stage1.set_index('TR')
	table = pd.pivot_table(stage1,values='data',rows=['TR'],cols=['mask'])
	
	## lower the lengend case 
	table.rename(columns=lambda x: x.lower(), inplace=True)
	## plot this metric over the entire trial
	ax = table.plot()
	# later
	#ax.set_xticklabels(str(np.arange(1,25,2)),fontsize=18)

	## fancy up the plot
	plt.legend(frameon=False)
	plt.grid('off')

	## fonts
	plt.xlabel(ax.get_xlabel(),fontsize=20)
	plt.ylabel(ax.get_ylabel(),fontsize=20)

	# limits
	plt.xlim(ax.get_xlim()[0]+1,ax.get_xlim()[1]-1)


	if metric == 'total_accuracy':
		plt.ylim(0.30,plt.ylim()[1])

	## clean up metric name	
	plt.ylabel(metric.replace('_',' '))

	plt.show()
	time.sleep(3)
	
	## save
	plot_name = classifier_method + '_' + filter_type + '_' + metric + '_line.png'
	plt.savefig(plot_name)
	plt.close('all')


# moves to appropriate folder
import shutil
import glob

bold_files = glob.glob('*BOLD*png')
acc_files = glob.glob('*acc*png')
dist_files = glob.glob('*dist*png')

for file in bold_files: 
	shutil.move(file,'BOLD/'+file)
for file in acc_files: 
	shutil.move(file,'accuracy/'+file)
for file in bold_files: 
	shutil.move(file,'distinctiveness/'+file)	

	