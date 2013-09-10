def pattern_stats(file_IN):

### this is script that i'll use as a pandas exercise .  it takes one of the text files that the matlab  ### create pivot files creates as input and then will create all the standard plots we need.  BOLD time 
### series by ROI (also by trial type?), accuracy time series by ROIs, bar plots of mean delay BOLD by ### rois, bar plots of mean accuracy in the delay period by ROI,  distintiveness time series and bar 
### plots by ROI, then comparisons of all the above amongst span and drug groups

	### import relevant modules 
	import pandas as pd
	import numpy as numpy

	### read in data
	data = pd.read_table(file_IN, sep='\t')

	### parse name and report
	metadata = file_IN.rsplit('_')
	the_pen = metadata[-1]; last = the_pen.split('.')[0]; last = test.split('.')[0]

	print '-{0}- data set using -{1}- and the -{2}- classifier, -{3}- filtering \
	and penalty -{4}-.'.format(metadata[0],metadata[2],metadata[5],metadata[6],last)

	### remove column of NaNs
	del data['Unnamed: 8']

stage1 = data[data['measure'] == 'total_accuracy']
stage1.head
stage1.head()
stage2 = stage1[stage1['mask'] == 'VAC']
stage2
stage2.head()
stage2.head(35)	
	