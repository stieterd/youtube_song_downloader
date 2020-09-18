import selenium
from selenium import webdriver
import os
import sys
import time
import random
import classes

with open('liedjes.txt', 'r') as reader:

	liedjeslist = reader.readlines()

for keuze in liedjeslist:
	
	app = classes.MainApp()
	link_liedje = app.youtube(keuze)
	app.downloadproces(link_liedje)
	time.sleep(10)
	app.driver.close()

print('Ik ben klaar met het downloaden van je liedjes')