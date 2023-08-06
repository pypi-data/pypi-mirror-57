#!/usr/bin/env python

# internal libraries
import os
from time import sleep
# interface libraries
from Tkinter import *
from ttk import *
import tkFileDialog as fd
# my files
from main import *
from getboundary import *

def makeform(root, fields):
	entries = {}
	rows= []
	for field in fields:
		row = Frame(root)
		row.pack(side=TOP, fill=X, padx=5, pady=5)
		if  field =='Merge CellProfiler Segmented Objects' or field == 'Build Model' or field =='' or field == 'Apply Model': 
			lab = Label(row, width=30, text=field, anchor='w',font=("Helvetica", 16))
			lab.pack(side=LEFT)
		else:
			ent = Entry(row)
			if field == 'Number of shape modes':
				ent.insert(0,"choose a number")
			elif field == 'Status':
				ent.insert(0,'welcome to the vampire analysis')
			elif field == 'Name of the model':
				ent.insert(0,'name your model')
			elif field == 'Image sets for building' or field == 'Image sets for applying':
				ent.insert(0,'<--- click to load csv')
			elif field == 'Number of coordinates':
				ent.insert(0,'50')
			else:ent.insert(0,"<--- click to load model")
			ent.pack(side=RIGHT, expand=YES, fill=X)
			entries[field] = ent
			lab = Label(row, width=24, text=field, anchor='w')
			lab.pack(side=LEFT)
		rows.append(row)
	return entries,rows

def getdir(entries,target):
	entries['Status'].delete(0,END)
	entries['Status'].insert(0,'searching...')
	#################################################################
	folder = StringVar()
	foldername = fd.askdirectory()
	folder.set(foldername)
	folder = folder.get()
	entries[target].delete(0,END)
	entries[target].insert(0,folder)
	#################################################################
	entries['Status'].delete(0,END)
	entries['Status'].insert(0,'directory found...')

def getcsv(entries,target):
	entries['Status'].delete(0,END)
	entries['Status'].insert(0,'searching...')
	#################################################################
	folder = StringVar()
	foldername = fd.askopenfilename()
	folder.set(foldername)
	folder = folder.get()
	entries[target].delete(0,END)
	entries[target].insert(0,folder)
	#################################################################
	entries['Status'].delete(0,END)
	entries['Status'].insert(0,'directory found...')
	
def Model(entries,BuildModel,progress_bar):
	entries['Status'].delete(0,END)
	entries['Status'].insert(0,'modeling initiated...')
	#################################################################
	coord_num = entries['Number of coordinates'].get() 
	
	# input definition
	if BuildModel == True:
		csv = entries['Image sets for building'].get() 
		clnum = entries['Number of shape modes'].get()
		modelname = entries['Name of the model'].get() #name
		getboundary(csv,progress_bar,entries)	#create registry csv and boundary stack
		main(BuildModel,csv,entries,modelname,clnum,progress_bar)
	else:
		csv = entries['Image sets for applying'].get()
		modelname = entries['Model to apply'].get()
		clnum=None 
		getboundary(csv,progress_bar,entries)	#create registry csv and boundary stack
		main(BuildModel,csv,entries,modelname,clnum,progress_bar)
	#################################################################
	progress_bar["value"] = 100
	progress_bar.update()
	entries['Status'].delete(0,END)
	entries['Status'].insert(0,'modeling completed...')

def vampire(): 
	root = Tk()
	root.style = Style()
	root.style.theme_use('clam')
	root.configure(background='#dcdad5')
	root.style.configure("red.Horizontal.TProgressbar", troughcolor ='gray',  background='#EA6676')
	root.title("Vampire Analysis")
	fields = (
		'Build Model','Image sets for building', 'Number of shape modes','Number of coordinates','Name of the model','', #build model button
		'Apply Model','Image sets for applying','Model to apply','',
		'Status','')
	ents,rows = makeform(root, fields)
	root.bind('<Return>', (lambda event, e=ents: fetch(e))) 
	#####################################################################################################################
	progress_bar = Progressbar(rows[11], style="red.Horizontal.TProgressbar", orient="horizontal", mode="determinate",maximum=100,length=150)
	progress_bar.pack(side=LEFT,padx=5,pady=5)
	#####################################################################################################################
	#function 5 : Model 
	b5 = Button(rows[1],text='load csv', width=12,command=(lambda e=ents: getcsv(e,'Image sets for building')))
	b5.pack(side=RIGHT,padx=5,pady=5)
	#function 6
	b6 = Button(rows[5],text='build model',width=12,command=(lambda e=ents: Model(e,True,progress_bar)))
	b6.pack(side=RIGHT,padx=5,pady=5)
	#function 7
	b7 = Button(rows[7],text='load csv', width=12,command=(lambda e=ents: getcsv(e,'Image sets for applying')))
	b7.pack(side=RIGHT,padx=5,pady=5)
	#function 8
	b8_a = Button(rows[8],text='load model', width=12,command=(lambda e=ents: getdir(e,'Model to apply')))
	b8_a.pack(side=RIGHT,padx=5,pady=5)
	# b8_b = Button(rows[9],text='load model', width=12,command=(lambda e=ents: getdir(e,'Model for ch2')))
	# b8_b.pack(side=RIGHT,padx=5,pady=5)
	#function 9
	b9 = Button(rows[9],text='apply model',width=12,command=(lambda e=ents: Model(e,False,progress_bar)))
	b9.pack(side=RIGHT,padx=5,pady=5)
	#####################################################################################################################
	#terminate
	quit = Button(root, text='Quit',width=6, command=root.quit)
	quit.pack(side=LEFT, padx=5, pady=5)
	root.mainloop()
