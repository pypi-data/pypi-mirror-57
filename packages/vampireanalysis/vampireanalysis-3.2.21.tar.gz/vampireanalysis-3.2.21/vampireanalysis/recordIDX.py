#!/usr/bin/env python

# built-in libraries
import os
# from time import sleep
# external libraries
import pandas as pd


def recordIDX(IDX, IDX_dist, UI, cellornuc, setpath, inertia):
	print('## recordIDX.py')
	if cellornuc == 'ch1':
		ledgername = UI['ch1'][0] + '_registry.csv'
		# picklename =  UI['ch1'][0] + '_boundary_coordinate_stack.pickle'
	else: 
		ledgername =  UI['ch2'][0] + '_registry.csv'
		# picklename =  UI['ch2'][0] + '_boundary_coordinate_stack.pickle'
	if os.path.exists(os.path.join(setpath,ledgername)): 
		obj_ledger = pd.read_csv(os.path.join(setpath,ledgername))
		obj_ledger['Shape mode']=pd.Series(IDX) #write
		obj_ledger['Contour fit']=pd.Series(IDX_dist)
		# obj_ledger['Inertia']=pd.Series(inertia)
		obj_ledger.to_csv(os.path.join(setpath,ledgername), index=False)
	else: 
		d = {'Shape mode':pd.Series(IDX),'Contour fit':pd.Series(IDX_dist)}
		obj_ledger = pd.DataFrame(data=d)
		obj_ledger.to_csv(os.path.join(setpath,ledgername), index=False, columns =["Shape mode","Contour fit"])
