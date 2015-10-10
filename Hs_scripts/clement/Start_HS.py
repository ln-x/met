"""DO NOT DELETE THIS FILE. This script imports the heatsource module and executes the program """

from heatsource900 import BigRedButton
from os.path import dirname, exists, join, realpath

def getScriptPath():
    """Gets the path to the directory where the script is being executed from."""
    return dirname(realpath(__file__))

inputdir = getScriptPath() + '/'
control_file = 'HeatSource_Control.csv'

if exists(join(inputdir,control_file)) == False:
	raise Exception("HeatSource_Control.csv not found. Move the executable or place the control file in this directory: %s." % inputdir)

# Run Heat Source Temperature, run_type = 0
BigRedButton.RunHS(inputdir,control_file)

# Run Heat Source Solar only, run_type = 1
#BigRedButton.RunSH(inputdir,control_file)

# Run Heat Source Hydraulics only, run_type = 2
#BigRedButton.RunHY(inputdir,control_file)
