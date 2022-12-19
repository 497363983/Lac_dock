#!/usr/bin/env python
#
# Raccoon
#
# Tk Virtual Screening Interface for AutoDock
#
# v.1.0f  Stefano Forli
#
# Copyright 2009, Molecular Graphics Lab
#     The Scripps Research Institute
#        _  
#       (,)  T  h e
#      _/
#     (.)    S  c r i p p s
#      '\_
#       (,)  R  e s e a r c h
#      ./'
#     ( )    I  n s t i t u t e
#      "
#
#
#


#################################################################
#
# Hofstadter's Law: It always takes longer than you expect,
#                   even when you take Hofstadter's Law 
#                   into account.
#
#    The Guide is definitive. Reality is frequently inaccurate.
#        Douglas Adams 
#
#################################################################
#
#     This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
#
# List of easter eggs:
# -negative values on the filters
# -help on the about
# -

version = "1.0f " # try to keep the 6-char size
# TODO
# TODO
# TODO
# TODO
# TODO
# TODO
# TODO
# TODO
# move from "print >> fpointer" to f.write()!!!
# add a variable to count multi-mol2 entries only once...
# REMOVE THE OBJECT FOR PREPARING LIGAND (MEMORY CORRUPTION)
# UNICODE SUPPORT FOR NON-LATIN CHARACTERS! (bug reports)
# TODO
# TODO
# TODO
# TODO
# TODO
# TODO
# TODO
# TODO
# TODO
# TODO  

# - add progress bars...
# - add a button to start the calculation on the current machine
# - add automatic split value if ligands are more than 30k! (linux limit!)




# TODO

# 1.0c -> 1.1 RELEASE NOTES
# aestetical change in the editable windows for DPF and GPF
# changed the color of the GENERATE BUTTON
# overall improvement of memory management (no memory hog in generation phase, memory efficiency in mol2 splitting handling...)
# speed improvement in generation phase (~150 fold speed?): different code for generating parameter files...
# cosmetic change in the file selection allowed formats


# LIGANDS
# few default changes in PDBQT generation
# fixed bug for removing ligands from arbitrary selection
# fixed the Mol2 split bug (missing mol2 header)
# added support for improved partitioning of splitted Mol2

# RECEPTORS
# fix the multiple conformations receptor menu
# corrected bug for SingleRecFileAsk in the Multiple targets menu



# MAPS
# - mini-check for GPF parameters



# DOCKING
# added "Generate default DPF" button 
# 

# VS Generation
# protected the change-dir commands from the space-containing name dirs EXPERIMENTAL
# - job subfolder creation
# - improved scripting code and bug fixing for handling spaces and other weird user preferences
# - improved TSRI support for jobs submission on Scripps cluster
# - map files cleanup after jobs end
# - workstation calculation job code improvement
# fixed bug for non-Bash users in local VS job creation (Yasmine Moemen)
# fixed bug for AutoGrid run under Windows
# fixed bug for some Windows disk space calculations (Senem Avaz)
# fixed bug for non-latin Windows systems (see chinese guys in the forum)
# fixed the bug for the CygWin environments [open writing files in binary mode]
# added the TSRI-mode for the smuggler
# added a Delete grid maps option  GetOSoptions (DONE!)
# added the log file filename button on the VS_generation tab


# TODO TODO 
##### PRE-RELEASE CHECKS
# TODO TODO

# - add the creation of a PDBQT directory in the dir where a nonPDBQT file is parsed
# - test flex res import and checking (not working!)
# - test flex res atom types with new fastDPF
# - sub_folder job submission (cluster/workstation)
# - add MMsInc filename support?
# - new Raccon Session File RSF, check and test 
# - add icons?
# - fix the From template DPF bug (multiple invocations of the command will cause it to add more buttons...)
# - substitute all the os.makedirs instances with makeDir()
# ADD an option for setting charges for metals!
# Change the smuggler to generate a DONE/.lock file to avoid re-submissions...
# GPF/DPF mark useless keywords (ie. "map") in gray so they are known to be ignored
# Add a progress bar for when converting many non-PDBQT files
# add a preview of which filters are responsible for a ligand to be kicked out...
# Add a warning before generating when non-AD types are present but no parameter file has been defined.
# test that text in the "VS generation" are consistent with the options that are parsed by TheFunction

# TODO check icons here: http://art.gnome.org/themes/icon
# TODO rethink the pause after the Workstation mode...

"""
SUPER-TODO:

BABEL + OASA!


babel -L descriptors
HBA1    Number of Hydrogen Bond Acceptors 1 (JoelLib)
HBA2    Number of Hydrogen Bond Acceptors 2 (JoelLib)
HBD    Number of Hydrogen Bond Donors (JoelLib)
InChI    IUPAC InChI identifier
L5    Lipinski Rule of Five
logP    octanol/water partition coefficient
MR    molar refractivity
MW    Molecular Weight filter
nF    Number of Fluorine Atoms
nHal    Number of halogen atoms
s    SMARTS filter
smarts    SMARTS filter
spinMult    Total Spin Multiplicity
title    For comparing a molecule's title
TPSA    topological polar surface area
entropia@atara:~/Downloads$ 



"""

# TODO MANUAL UPDATES
# add the multi-receptor script mention
# multiMol2






# TODO TODO TODO
# LIGAND HANDLING Major change:
# - re-arrange the Great Book of Ligands to use name as a key.
# - use the ligand name os.path.splitext(os.path.basename("/c/d/e/f/file.pdb"))[0] as ligand key
# - add the filename to the keys
# - two ligands are identical if sharing the same name and the same path (therefore the latter is ignored)
# - if not, add the ligand with NAME_1, NAME_2, as in the new SplitMol2 file
# - add ligands clustered by directories (this would be really cool!), with a plus/minus sign on it to collapse the tree..
# - add an option in the importing PDBQT ligand to specify if there is a path where to save the generated files (or to leave them where they are)
# - redesign the LOG file format: more compact, more like a config file...( GOLD-like?)
# TODO handle duplicate/homonimous ligands ("xxx_1", "xxx_2"...) in:
#       - generation phase
#       - ligand registration phase DONE!!!
#       - 

# TODO FEATURE
# add a fox-like feature with graphs on ligand properties (useful for the next incoming OpenBabel!
# mw, rotatable bonds....
# hb acceptors
# TODO Add a double-click option to prompt the user residues that are in the current receptor (a-la-Fox) with a table with rotatable bonds and so on...

# TODO BUG TODO when loading a session, check for the parameter files in GPF/DPF...
# TODO BUG TODO deal with flex res when playing with map caching...
# TODO add different values to the splitting (custom too?)
# TODO fix bug that gives an error when converting PDB to PDBQT
# TODO add a handbrake to stop importing multiple MOL2/PDBQT molecules 
# TODO support for multiple GPF per multiple receptors...
# TODO add a Options topleve in the Summary to access to the cluster binaries settings (autodock/autogrid, $SCRATCH...)
# TODO add in the manual the WARNING for the mw count not including non-polar hydrogens...
# TODO BUG FIX mol2 splitting interface: output directory doesn't update automatically with new files!!!
# TODO add a menu entry for "Run the virtual screening and close Raccoon"
# TODO manage duplicate molecules! (ZINC-NCIdiv2 issue! 1880/1550 mols...)
# TODO add an option for guessing the Mol2 filename with a fallback
# TODO fix bug for non-AD atom types
# TODO add command line options for debug, importing sessions, and so on..
# TODO add a DEBUG mode in the Help menu
# TODO add multi-core support as the Yuri scheduler?
# TODO add a TopWindow for the generation phase, that's updated while the generation runs (while the interface is frozen) (USE PROGRESS BAR FROM COATI)
# TODO fix the GPF edit content to fully expand... IT DOESN'T WORK!
# TODO Change "Linux cluster" to "PBS cluster"
# TODO include the table to see the ligands properties (distribution? Histogram?)
# TODO add a parser for the *MANDATORY* gpf parameters
# TODO window for splitting mol2: ALMOST DONE
# TODO check that repeated filenames (from different dirs) doesn't generate the same directory... with overwriting effects... [DONE?]
# - check-button for numbering/naming of the mol2
# TODO create a function for managing splitted output subdirectories (generate the 000, 001...)
# TODO create a multiple DPF per ligand based on the complexity
# TODO normalize all the paths with os.path.normpath(xx)
# TODO autolog file for when a crash occurs...
# TODO add a charged-groups filter in the filter section
# TODO convert the windows that need to freeze the interface as Root depending windows... (no toplevel)
# TODO think about putting a self-grepping script for the virtual screening submission
# TODO eliminate the "set" buttons in the VS gen tab and in the flex res section
# TODO prompt the user for the LogFilename! (providing the default raccoon_xxxx.xxx.xxx.log format)
# TODO visualization of clashes! (exploiting distance calculations from ruth...)
# TODO Export Snapshots! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#       - add a button with the camera
#       - add the option to the exporter to include snapshots
#       - add the 2D plot interactions? seee.......
# TODO filtered ligands with over-strike: http://www.tutorialspoint.com/python/tk_fonts.htm
# TODTODO Generate default DPF -> toplevel window with settings: SHORT,LONG,MEDIUM... AUTO? (split the three modes for rigid, semiflexible and flexible ligands!!!
# TODO Change dir creation for SINGLE_PROTEIN mode. (do not create the target dir_name) # DONE
# TODO 
# TODO add a receptor types check! ( to avoid errors with H or O types atoms)
# TODO add a button to remove ligands that didn't pass the filtering process (icon = forbidden + filter_brush)

# TODO add the receptor status info (i.e. Metals? Y/N Total residues?)

# TODO TODO TODO TODO TODO TODO 
# TODO ??? change the OS options to a button for a toplevel window containing:
#      - script generation options
#      - package creation
#      - sub-folder generation (10, 100, 1000...)
#      - pbs options
#      - dlg per ligand?
#      - Lin/Win option to delete the maps after docking

# TODO TODO STATISTICS TODO TODO
#  ligand statistics:
#    AtypeList (distribution of ligand atom types)
# 
#


# CLEANUP ALL THE IMPORT MESS! (Tkinter, tkFileDialog...)
import glob
import os
from Tkinter import *
from tkFileDialog   import askopenfilename, askdirectory, asksaveasfilename
import tkMessageBox
import Pmw
import Tkinter 
import tarfile
import zipfile
import platform
import shutil # for shutil.copy2
import string
import datetime
import getopt
from math import log10
from base64 import b64decode
from random import choice
from numpy import sqrt
from sys import argv, exc_info
import gc # PYTHON GC BUG
#from pylab import *
#from matplotlib.widgets import  Slider, Button, RadioButtons


#TODO TEST MEMORY USAGE:
#import gc
#gc.enable()


# enable the Debug mode by setting this to "True"
DEBUG = False

try:
    options, object = getopt.getopt(argv[1:], 'ds:')
except getopt.GetoptError, err:
    pass
    exit()

opts = {}
for o, a in options: # populate the options
 opts[o] = a


if '-d' in opts: 
 DEBUG = True
 print "=== DEBUG MODE : ON ==="


# System identification
system_info = platform.uname()
if DEBUG: print system_info
system = system_info[0]


try:
    # MolKit stuff
    # from the prepare_ligand code
    from MolKit import Read
    from AutoDockTools.MoleculePreparation import AD4LigandPreparation, AD4ReceptorPreparation, AD4FlexibleReceptorPreparation
    
    # from the prepare_gpf code
    #from AutoDockTools.GridParameters import GridParameters, grid_parameter_list4
    #from AutoDockTools.GridParameters import GridParameter4FileMaker
    #from AutoDockTools.atomTypeTools import AutoDock4_AtomTyper

    

    # from the prepare_flexres code
    from MolKit.protein import ProteinSet, ResidueSet
    from MolKit.molecule import BondSet
    from MolKit.stringSelector import CompoundStringSelector
    
    from AutoDockTools.MoleculePreparation import AD4FlexibleReceptorPreparation
    from mglutil.gui.BasicWidgets.Tk.multiListbox import MultiListbox

except:
    #print "I'm sorry, MolKit is required for running Raccooon"    
    if system == "Windows":
        tkMessageBox.showerror("MolKit error!", ("Impossible to find the MolKit module.\n\nMGLTools is required to run Raccoon but is either \
misconfigured or not installed.\n\nPlease install it or be sure to use the right Python interpreter.")) 
    else:
        tkMessageBox.showerror("MolKit error!", ("Impossible to find the MolKit module.\n\nMGLTools is required to run Raccoon but is either \
misconfigured or not installed.\n\nPlease install it, or try to run Raccoon with:\n\n $MGLROOT/bin/pythonsh raccoon.py"))

    exit(1)    

try:
    # from the prepare_dpf code
    from AutoDockTools.DockingParameters import DockingParameters, genetic_algorithm_list4_2, \
                    genetic_algorithm_local_search_list4_2, local_search_list4_2,\
                    simulated_annealing_list4_2
except:
    tkMessageBox.showerror("MGL Tools error!", ("Raccoon needs a version of MGLTools\n\n>= 1.5.4."))
    exit(1)


LOGO_BASE64='''\
R0lGODlhXgFFAPcAAAAAAA4ODg8BABIAAB4AABEPEBERERsbGw8NEB8hICIAAC4AAjAAAT0AAC0b
GiIiIiwsLCcpKDIyMjw8PC4wLyEfIEEAAE4AAFcAAWYAAXEAAHsCA1cvLUA+QUJCQkxMTEZIR1JS
UlxcXFdZWFBQT19gYmJiYmtra2lpZXFwbnJycnx8fHl5dW5vb2BgXjtO+TtS7TpV6ztT9TRL60JM
/EJZ7ERV8kRU/URa/UlV9UpV/EtZ9Uxa+kRZ81Jb/FRa+0ti/U1p/Epj9VNj/lNq/Vps/lhl+VRx
/lxz/V16/lJm7mF0/mN7/Wp8/mZy93J8/GNp/3+AgmWB/WuE/W6I/XOF/XOL/XmO/nqG9nuT/XeS
/YQBAZcAAJUyMqkAAKkWFrQAALsBAboJCrUXFqolJac2N7MoKLQyMrk2Nq0wL65AP5dVVpBxcqpG
RqtWVbRISLdXVrNQT7FgXKdoZ6V6ebpjY7p5ebdvb8IAAcwAAcgJCckZGNQAAdsAAdoLC9kJCdYQ
DtQUE9MYF9MNEM8eIcE6OdIiIuMBAesAAOAHCPIAAP0AAP4ODv8SEc8gHcNWVspmZtF5eNpVVoB/
grt/gYGAfoGBgYyMjIeHiJOTk5ycnJyWlZKOjp+goqSbmreHh7SPj6KgnaOjo6ysrKinp7Snp7Gu
sLOzs729vbi4uK6vsJ6gn4SL+oWa/Yqc/YaU/ZKd/pWY/Yyi/pOj/puk/pur/pam+J6y/L6+waOr
/ams/qSm/KOy/auz/q26/Ki197S7/bm9/LC1/b3AwLzF+7zK/bbC+7/Q/sSHh9GQkMimp8S5uNax
s+Kur8agn8TDv8PCw8vLy8jHxs7Qzc/Q0tHNzdrFwtDRztPT09vb29fX18/O08PL/MrN/cLF/MzS
/cvU+tLV/dTZ/Nrc/dDV9d7f4d7g3tzh/dTh/t/g4uPc2+jFxuDf7+Hh3uPj4+zr7Ofn6OLk/OXp
/ers/O3w7uzx/evy+PDu7vDu9fDw7fPz8/P0/fX5/Pn2+/7+/vj49iH5BAAAAAAALAAAAABeAUUA
AAj+AP0JHEiwoMGDBvshXMiwocOHECNKnEixosWLGDNq3Mhx4j+CHwuGPDiyo8mTKFOqXMmypUuN
JV/KnEmzps2bDRXWPPeNG7hz9vbx+1gyJs6jSJMqhejO3TudK/W9m6oPqktwtWrdusXLWLGv6OrV
47e0rNmzSuG9g+cOXtWB/fRJlYpPblWrOaW+a1rO6T+jKcXVogWs2zdiwHz5Mkbsa7GwAgGjnUy5
ssV/78xlM+f3L7xs0YalGj0alWlUw6SpVh0NG7Zsdj9Hk/Y6Wzan+v7hNfkxXFZi8/zVE+ctWK9e
ubTSunUM3W7L0KNLN6jPHbbZ09K9+/vumqpNnC7+ieeUadOqVZ1EjVovqj2p9aNItR+Fqtrttu/k
Ss4Y0h4vWr2c408/PBUDTC+81DLLLLK0Iksx8ww13YQUWrZPd6iQQsop0rhTlT7ZjIKJCi2coMIK
k4i3SSYssigeJiusoMIJJl5ySjROTZWfPvnkt19ERtXTyyy1gCPQcNwQc9xgs8DSSitZyHJMPRVW
aaVHEaGyjCrDNCRVOahoYskKmIiCzTsC6WNKCyGEYAIKLaiQIifhTTKJCiycYEIIH3jQAQgniKLN
PXZRJRU8bvEmkDGyzGLMPsKh801xyO1CCyyyuPJKK1YYgw4/z10p6qj+oAAAACJII9AJAUTAQjT+
LBjQQAMXNJDAJQuxVc0oK4hAQggqpILmgKSUAMIHIqDwZgsrWKICCiKMMAIJIHggAQQQRAACJyFV
5xo2Hr6TjTahVhTSN7LIwks9/9QjaTfBHKjLYLBomkUWVjzIbmT8YlQuqQCbpJM6BCyyCBcm+FNO
wQebcAEiBht8yAKYIMRWNKKg0EG2HVwyEiYffFDCnSN8oIIKJogwQQQSfDDByxtDQMEqcGkTTXyi
kLKdO9DoAxNB4Dw5Czj8nANOkvEKo0tyTTZ4rxZW8IKOQP8GbDVlJIChyCIDvHOJBososgABWysS
Bh4G91HBQCW5kw00mYQAwQEHRBBCNAJFE0L+B3LO2IIJl7TwAQUPSOCBCCakbEIJJFhCUDbSnKLJ
JTJi89Eow2I0kj2yRMnLOed8ZQwwwgjTy9K7NAllFldcIYUWxex79ezTrZKBwRlokkAfixySQAMG
X+DnBgYTYM5B8GCTyiUgHGBAAAEYIMqAK3yAwgolllDCCSh8IEEFEUwAQgiIpwwCCCoQdLMoK5gg
sqruCNtRPbdokcUsovuC4OlL50LLpa5oxSuuYAUqUEEKtxAH7RZ4lucYAGJgIMECDKaBSwAvbF7A
AANm1bWDgCgVmACBAR7wgAIcYAXumMYJyHeCFaAgBCV4kwjm1gETgEAEJ0hWCCJwABBsQyD+2bBE
Cz0wgRGsAB79+Mx2NsIPY1AhC624RTEUlJVaJCc5/6vX6q5AhSpMQQqtKIaAGEjGyZyACwYbABq5
9o4BQCxii8ADA1iAkH7w7BIjoJvzDmACyaFgBCJwkwc+oCdMqEwCIWCBsqIVghFIwAAQmIRAVjA3
5z3gA6LYjn6qBhF0UMEKWtBCuqKUrgX9L4uu0BTUqDCFVjYhCUMziShOBQBNlJEgE/AAEf20y12+
TAWWGAXeKuSnDnhgmP4YyTUYYDAM8C6C/lgBAbiwtYgpggDpQMg7MFa9CYzwAIhUwQhMQCIQSGB8
J8jTB/h0gr+RAIcikAAJV4ANf6jAAAf+yBYEQHAJD+mmI76QAii1cAWCXuFJroDFgpqUyldkQQtd
lAITmtAEJEjBGFTiCARo+YBbDoSWIA2pSA0gglNMCKSoQMgE8qAI3i3iAqqYxgYbUIAFaOAQwRsF
Qj64CRaIIAImaAEFDuACE7hATxOggPhUMAoVvGwCJpgEC0owApSNQHyZOAU0SOGBBCTgABRAgSk8
1I8fTeQWSTCgWltnv1Zo6q0OLaAXp9AEJjBhCUs4wizCQRazOgQVITWpR0VK2MI+QKfRASk0EKKN
LjBCYgnwRxSIx7UoVOKCF0CsQf7hDoyxYIcfsEQIHjBIE9CoA96zm08/AIIOmCgTNOr+kwkkIAET
xKgTLDhA9EBgpsx1xBhHkMIXp1CF4rL1CveKkiuuUAWJSrSueF1CEKjgizFmxAQhnYBH/VHY7oqU
BPeADkrrCApJPJYLJ/CH7QyGhw1sIA8GU0A2FvIOapCiVyCAAG0PUAEKIO6FKDjfCi5xgquaNkaT
aJ+eXDYBZI2TtRI4QYfuwUkg+YMcSUiCFDbcSuJ+MpShHIzrkmBXuy4BCUgoAhGkAIypZeQdhE3p
LUH6gDFZ4sbNapYLPFAAwlLAZ5UZL0JK8YbHEkAbyTTBGuGIgfTSNxqdaJ8IPoBPExaRe90TgZ1O
8CsPANNZl2DBCE4gVe+dkwQfuMT+NCyximhcA4kdCYksjqDhDTeBw1NYa6OokIQioPjESyhCEaAQ
BCn44hsasQRhEzZjWnrgryIQKQV8exYhHwQbHNiABpzsD2mUgAHu1TQBOH2QfmTjFJlYwYIjYIAI
eMAFjDvWCTAxCUzsaZ0DtgQmOKGJTJAiE5cYkQiGzYlU+OM2qTgFbFASDiQcgc4lvrNEmSDcKciC
CkQIgqD9LOglZDsLuehGhRnygMK6o9Gn6kBDQuIOD4SUAkGm5WIXIg02XIIsBKlGgu2dTYbErxOU
m5H7aEuCGZFvBCwYESkMWa0xt+cUqxAFql0EoxVkAhXZSPZ6zjTuh4SkFkGgcxL+8MoEJNhVw8G1
AhKCIAQgDGHbgg5CEmoBDHxfZBQgDQFISS0TRrsEpI9eCF4uEVLHTcbSK0GFKDKBCRxPOcJkOgGv
R4ELaKAiE0I8lgkwcSN3nCIV2lDFKjaRilGoQuLRyEZZ3zENHAGZP0AL+RH+fOIkPPvZQXAFL4jg
8iEQwQiCHkIQtMALRGdkAiDNhrtPFYC3vwS7MgGpdiWyipDOFy1IT8k+ttoiYN9YFKl4xingMZDw
+gMVLHAfJjYxCrX0I7zloEbaXRON2qdiGpvxhz7c7teJ7KMJQng2t7d9hCAEgQny8AcsbgAEH/h9
CNCfeS+CgxF3gFQE/tAESI3+/pJIAyDyjqYIdmnpc7NkHiXbPEXOTJGKaEDjnww5hQj4KeNS/0Mu
bHEb6X3WltygpBhAEHJEcASBVgRGMIA4wAsCcQ5DwAM84HzQBwRaQHMacQKKJRAHQEsH0HO0BH6n
EnQS8Q4BkHiYJ28skUTRgAqpAA3bcG4Q8Q5iplkOoRD/oBYDkR/90HERoQUBSAREAH3Z1nJIkHwC
4Qo44AMP+ANDAASNEg69R18GQEsQMBDaR0vT0xA3dmOXZxBB1CzcNxDjdyo2NoYNAQ1iMian4IIN
IXkVoWi0hCsN8TZeeAn1FxGjMFscNQGXsIUfRUt1CBf5YGMxQmkQoQ/tcB3+aQcPTygQiFNP/gJ/
JwEOQdCDRRCBLecL/sAPZBEPPqADDxh9saCA/UIRs2SFA6EPI3gqU7iGJngQ0ABSBeF93oUQ2SAC
qRhSEGBLDAF0FQFjtDR5CCEKEkBYJFUOD3EKGdhdICgQ5ycQG2WKFVEd42IOTzERJOABSGYRU/EX
HFESClEFOAAELueDDtgEkEIQT/ACOjAEPgAErEALCpQR5XYqBeBbK3CBu+iHCAFYHQiG3tWPBeGG
3nUAjngQbFgRFACLBxENz+hd6VNqjPiPp1IQzRiGAPCFEtEP+ZB/+bEQ9/AOpnCFA3EACfBDBKGG
XqKRLREMLyCOLwcEPHD+A8LgD97wCqzQC/2gCzTgiTxQBK8wk2xTEfx4Kg95iiD1Aax4Kn84EEP5
fQJhkbNIEPqAeBJ5KiJJkeFXERbZbwQhClFYlRJAiE8pUgegS7folH14KvNGEBaJfZexkWoBGNlw
CdFyABNQAsj0Dg8QAcY2EKdmFv3AD+nockXgAzfAA/IgDD/wAzpwA69wDkSwkzyABFcQDhphkcdT
EBbJhwbRjP7wigCJClZHdH4omqZhdQVBlbQUApoADWZoAmcJAEvJXVlJEWyQeU0JAA9wAlYHDZbQ
kB94EDh3fSgZDeOHlUpZEPf4ixnRI28hlZjgUxJANyozASEwENEgARP+sJb+wAKEhDJwmBTdwAM4
MARLwAM6oAveoAM/8ASFqQPFcQM0gAM4UAXBsYgGYX20pG5U45cgVX6dqY8H0ZQGAZoTyRACCQAS
gJICkQ8qAFIGQIgHSRFRgHTv8JWnEp4EAQ3JeCorUBD5gKEAcJUniZQEgXSlqIqORxFxoR8DAQ+T
MAG/MjdaFgIHUAAQ4Iib4AEhsJbRkF8GYAkjEAInYAliSRO5cAPqqAPA4A9PoANQAAU/YJhP0A/A
wAMv0ATWdREJKoMEoXO0tKInKqAFqpAEQaALoZ+nEpYJIRBVeCoASpunAowTkaB1aJEkShDvMIy0
hJJvCgAa6hD4mH3+EHqkEjEXZWVHm3A+FMBqAWBEH7BHJgUPnGACLCBY2fdIBUAKJ/AyJHAJBYkT
3cAKr+AN/jAOPuADi4mE6NkNp+oN5yiPHLUQTfmhCDGoBYGmG2qmB2GBp2IAnGkQHwBSlMaLFQGm
p1KQ+gBSRYkQ2MCsBDGsqjgRQhYNEIpMGLEXblMNpEACSZUtBlAAASCukKRfJgVCeqKGLXAA7QQA
BlACtGUJfXkTI6ETrMCeqoqEOiADVWAPIIERKVqVtBQAC+GZusqUvGoQ8wgAzYoQalpLyAkAyygR
wEkQf2qoAyGLHZWWAEAzEjFe0SCis1kRnZUKYlICG1MBemQALMv+shGALLdxCioQbMMEDSrgrd6a
LQdAAmTCoC8REvUaDqrKA1PqAzuwAzYgA67KEaopsNAYoMk5oAl7elN7g56ZmrTUsBMqEdkAUqso
EA86pw9hoAAwLA+LrQ+BUtkgonl6EdhgCrBlLQ8APqxGN602AYZzAngzCuqnCaTggrjQPRAgOA+A
TxCQSJYgDYlyFP9wr4tZtDyQAzbwAqyQTBrxrE4bUhsLtQDAnbsKkANBtgshuiRhFcspsRE7sRCR
oLYqEIt3kRABUl3iD8tQtUkJAKPApx4aZ9EgJiEgPhKgVNnCMh9QVZOzoZnQfgTBAkQ0t/tkAu+E
Q+qhgjjxD/P+UASLmQOQywM1AANKsFlambkiNZsGO7UHm6u2axACSadyiroToQ8dCgB8qJqte7sy
NgzpW7BvKKJuuRH6gAoE9rsvw6PT4gGAgnVo6w6t53j6QGDHMmbV806iAA2jwHqhShO7oL07MKUO
iJ428MG/oBEiSEsScBpWdxomLJq3yL7MSKYFQbqfe6CuyKvlUgm12cJiOxG+Gpy4REuVELsC2pQY
a5DyFg1nGacWoQ/L0z0d8CdTBgIFhwmkcAmqsBv1FA2UJjmiYCIrwEKqMDlUpwmbQBMfQQ4bfLQ/
4IA6cLQ5UAMxoAREGJQSQZqnoosOYZFo276ei7CgKxDnq6f+uLoQHUB+qTsRfyqbBRG27jsgtApS
LrisLpy2+ogNR+y/V+dCtpUyyBIym+AaHnKoJjsi5IQCKjB2mTAM1UgT/YAFOYDGOxC5P7ADOSC5
NTADtjCKE9GhBAsRXUvIEbvHfmy++VsBWesQkJyhhRwRh8xzhEpLmSMZimwABIGhDSuorRiy/6kR
/SANk5MnOWYCpJBs2NAh+JkmJksK/aAJUQB6qHAdQ5wS5NDKq8oDsiy5O9AD+PzGsUoRTcnMDCGt
p8Kgt1i/ZyrMHSgZLTCwQ5zQtKQOEcufD5GgCkqIxwwAksQQ2XCL5ReGARCs+aiWA3EN/KsR0SA5
qpY4epL+ApdACuDynBJxf8ljDtCQbK1hG2KqEiNhCzbQyjuQqrIcy63cAzWgBEoQjxUB0ADgswxB
tgT9utd5ELKIlnx8KiZ5EL2sogUBFX/qApwL0QuhD5qwsIx3wf5IS50gGe8AnHzYlBJw07fqwkZ8
fRmRDcOgCp3At6mgKv7gDvvgohfBWa5JEDq4EdbrBDv9ykh4tDagA5LrvVWgBORgEQ9rohKhu41H
EIoMAHkMlUR8KilANZoIDysQEplNAdVwEAlaAMEKUhSQCqbh2ipoGqr2uiAVAHnslz1GSxj5Edeg
uwzLyAPRtBJw2+5gAnWYeZQs1xfRWaaRdpnxD/tsEKf+kGZRMMVkndX+MBVIQQ41YAM7UAP3bAMw
MN7jLQRIwAqxgAXxYBGZPbIMEbBXaa20ZACagCb6kLsidRAJSUsikGyZMAIIAAD5cBf7TUskwAmi
eQonQMwgZcdwIb4iBQGkxxDDyVEqcApacgkkgIuEmNEhFQIrcMIrwKf11w8gNa86Ede+TLLXsQ3a
8MkOwUMgIK+QE6hnERLBAAM14MY1IARK4ARO0AToHQu0sAuxsAuWSxG3uIEV0aFMniZITVgVWxD6
QAqFdQFcAAZabgbJoA4FLpGagBdyAeG0VAAE7UFg7bQSMOEGoeL/WH8VPa/qM9Ikmw2uQY1+dQ3O
0zj+mTBf0TDYNfEP8bADMVADTsAKu7ALtaALjK4LRp4L3MCNFPGnNg4RpwuxVOMOwBlSJ5AKUxsX
UQ0ACqABLGVNfAAJ67DD3VUBy0AV/TnmEH5CSi0SUzEPy+AACvCPJ/Ah1PEPDCmRcA5SmFoQbg4A
XE0R1uEa2aDdDRENHmAAtSUCpPC/t33jsDADMVAFsEDku8DopRMM5IAPGKG7BsDmEwEPK2wQKxCb
E5BSfzwQorCwNwVHEXMIkKAP1zACAHABGDAAXpsJa6EOkVAIj7AOfwHroLYFDdBd2rkC1Z4QF/IO
yVAIYiAGG0CMIuDRB6EJvg1SB6AC5n612ExLJUD+EaChGthggw3xDiawMQHQQzd7DdPhDb/gC97Q
DeEQD/OwD/igE+WME/CwxTN73UKHGZowAl0AX72DB1r+RmDgDunADI/AB3wQBl1wAqpwJp/BDHHQ
B4hwCGGwDlPhDtoACWGgB38QBpAwEH3VpkleVozMjVLhNmiwB4IQCGCADZ1AIyrACapQEadmIiZy
CkQvE53lmtHw4qco2F3pSNgyAiAwAtORROEwDuMQD/iwD/sAFT9fEOMsDbWHEauRdvlZe7MxG9jg
M/oA+tIAzMnkdaLACV8AMYrwBXQwCnQQBluTB84gDV0fMXjwCcNwms7wBjhlMIjwCOKCDW2AB4f+
cAiJkPbKAA3DbxpV52bLbhdVcfBz3wzrIBV2bgd8IAh7EAhiAA2gX3vpbw5ubRDJk/6sn/6cyfo9
4/a7N/oa3xDWkf60KJxt4t4A4U/gQIIFDR5EmBDhP3K/fnELF3GcuHHjzp2Tt0/gP4UJ30XDFi3a
u44J3YEMSZJgNpEhsYUU6U6fSJAIs6EypYlNmEWLFJG5NOoTmJ5hSnEi2nMRojPDUo2iU+aQ0kWH
HmWbBifMIUSHEiUKowwaqlOf3pxBg2zY2GHKIBUqlOwevHTIwogB84iZNmhw+AQKpAdOtGnXolUT
OS2ku479sBWm6RIkSH0EYWKrfPDf5WjlSib+hKcNm0x//Qxi+5xa9erU+4L98kWsW7iKtStSnMe6
oOiX2XQLzPYSm2+C7oS/FB28t3LUBmeiUqXJDZ+eiIB+ajNVURpNa6j77IlnDqlPUnv2CcMnbDSt
ihQhwpMnTxxoqU7FEaNnkB4xcVKlcgOMMfbYY4xHlInGjD0IIWSPOJxZZg4+/AAkjze20aYa0bTh
jUPiDtIHmw55601EzCwTLrOCNjNxtN8Gekc0ePRRMZrK4IHmRR131MwfeYIxhphggvGmyG7I6UYc
cc6JZ0kd4ckmymw4Yu0dKbNRaaArsRxIH3e2/HAlbKAZJZM2+qiODDqyK2qOTMxbBI+eFDH+AxQ4
+3jDrWeisQMP9xAJww07PpGGrDbE8MOPQAAJ7I04wBDEEEkN2eONO/LYQxBN9XgDlE3AUAQQP8Ko
ZsZ/9HnnyysZO0hKbbLRxp13+qERHlVV9OdKXLW8Eh4eQ8PmnX+oJMjLXXlE9jd7vCHGSGaJgdYb
brxJchxyNHoxmy9l1c0db70VyDR/9MnGHG/FJcjKbcPUcsxROiEDkerMMEM7PtoIBZMv5F0EDDQX
6YMMOZcqo5QMo0ElDX7DgAMVaUKC5pM8EklUVEAGCQNSTQXZwxBHxIh340AE4fQSqb7CI5mD3DE3
yiwHgtKccrwltqB3cGX5y2PdSYfldF7+frGf4GTVVh90STo2WaU7orIfJMHpJmqpo+amG2qtxfa3
VN2xtVtvZywIHlvhAbpLrsEtqB9zsiFTlHirC0NeRfBwg5RN1ghDkeqmmpPfPuBIRZponnpbETBS
gQYabKRJJTuKw9hqET/4A4wPfxfRFIxMAWPUDzHKWCOPRRLpYwx00/2a1eLO9lW1b9053Z+vbS37
RXdeLbqfU8Nduvff8ElSSSUjEl6ccMgxPnbWxBY76YT0Ibtrm5l33h/mWy/odmnefZsqRRimgw42
uqeq754O6fSTO94YA9Tw6gAFmTrOAAOMRA7Joww20jgkUT0A2QMZ2NAF0ZFsZIEYRKL+EvU5+x3i
EHhoBkKuh6t3vIN5VbogQaLXvKWRS0QyqZnvRLiaf0zENrWhCEUmcg4eQY9stfNIBW9mEBnCUCAW
rOBBoBSNU2iCfD3hQx7wMMT4eM+BSnFfVYbYh0PoTW8+EWIe+MAVRHRFDG64BN4oxgdA4KENmGAD
pAIziED4oX7y+koewvCHrvAhEv4I4bhqmC4ZVk+CFcSeP2o4w94ZBxvmeGGXRjjIkswjHoeMxzgQ
mUgmXQQfPDqVPvKRD9XQ6GZJs6QdaUSjg6RqGqeAF7/KN8o5haELZfhXEUl5CDCI0ifuUQR1EIEe
MKyxD3r4Q6IyBgY8IFAP/ivDHMj+wAdFMLErXOGDyhCCKk526ZK62aSKNvlMEW6rMnYkZDbDNQ95
yCMe8phHOOPBzW/KI1nRxGaXogmiTSpknTQ0DipI8UPw+GSWA/veHDZBB9EtJQ1hyEMfBMoHPITh
DHdIAx74INA+CPEL5qkiV7gCBurkUoFzQxOgQDEKUbQhbktBhHvCoI7ntVOdzVzNO2lEK33EcWl8
dI42ZTqQfsxjH+HEaTjrEU7lvWgfw+qH7mg11FMFtaU0+getFtLSng4kqS0FkZWiYYo5DIygeKgf
GMxQBje0oX5muIN9SGEIeaEvFXaAQx3gcAcIQQMX0AAFHNJah0+AQhXl6UMV72n+hjm0IQ967QMf
xuCGR50BGdGoDymE+YdX5gESLg2X7mpW1HQ6Z1gcEerutImrps40m/3YRz32YY99lNa0WfNdZz3b
JShJ4xReBcMbPlEKaEjDtrZtiWgQA41K0O9BGqrGlkRzDQ5xCBvUQCwulBGHMzQXDqB4BipScYfm
mgEOdhAcNbChjp5lCCeeeNQQIQHVxhCysqtFrwg5wo+gBnUf7g1qsiCbXoT0Ix+hEQlur1ENdUip
HFGana2Km4109MxWAR7b67yVjuAQ5hoighVvqDGN4L7KwDfLRwXNoQ1qSAMay3CGNWBKXxLH8bwk
Xtp8UTxIWlmwHSwzRzuYd4+Ve8gwH5s8VYbFVsFMGk0fP43kJadpQZ4Z+IWvY14Fb/xToc5lbeWS
ldFWTGLVTtnKV+4dP/Zx42gmFai8iyytvqxip25kXNHMx7D2sUkurxSOK9KdJHkcOzJj2c53xnOe
TVNlQiZ1RaUBdEl0V5o659nQh0Z0ohW9aEY32tGPhnSkJT1pSlfa0pfGdKY1vWnfoap3AQEAOw==
'''



# Icon set CleanUp from
# http// xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#
# plus some Gnome default Icons

icon_open_b64='''\
R0lGODlhFgAWAPYAAEt0R0x2SVF7SVZ+SVmDSV+ISmaOTWiPSmiQSWqRS22USmuSTWyUT3SaTG6V
UHCYUlumVHqgT2CpVmWrV2ywWnW1Xna1Xn25YH+7YXy6Y326Y4CmUYesVImtVoqvWY2wXI+yXpC0
X4a9Y4G7ZIO9ZYO9Zoe+ZYS/Z4W/Z4m/Z5W4ZJi6ZIrBaIzCaI7DaYzBaozCa4/Fa43DbJ/AZ5HG
bZLHbpTGbJPIb5TIcZXJcZvKdZzMdJ3NdaTFaanKaq7NarHRabLRabLSa7PTbaLOfqTReaTReqrW
favWfqjShq7UjbLagbnehbrfhrPYlb/hh8HjisjmlNXsqwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5
BAEAAFMALAAAAAAWABYAAAfegFOCg4SFhoeIiYdBQkNDQkCKhj9RUlJRP5KFPk9QUE8+moQ9TE1N
TD2igzNLrUszqoIrR0hIRyuKHB0eHyAhKkVGRkUqISAfHh0chBs2OkRJSk47PDw7TkpJRDo2G4QR
LS4xNDU3ODk5ODc1NDEuLRGEDSImKSwvMDL6MjAvLCkmRDQgpOAChhEkSpxAwRDFiRIkRmC4oIAQ
ggMJFjBw8CCDBg0ZHjhgsCDBAQSKDFSwYKGCgVhTClCYSaEATAITck4gAHOAhJ8SBsAUAKEoBAEw
AQRYGgAAzKdQpwQCADs=
'''


icon_add_dir_b64 ='''\
R0lGODlhFgAWAPcAAHpLGUhgSEtkS1d3VVl3V299T2d8UZxhH5tiIZxhIKJnJaZrKqpwL7B1NbV6
Obp/P89/KVqdUlybVGOAU2GHVGuOVm2PV3STW3yaWn2aWmioVnWpWtSCKdaHMdaHMteIM9iMOtiO
PNqPPduQP4CSVqGIQr+EQ4emXJKkWoO6X5SzX6KvW7moXI+9Ypa1YKq2YcCFRMSJScmOT9uRQNuR
QdmRQtuURtyVSN2XSdqWTNuWTN2XTN+ZTd2ZT86UU8+VVN6bUtybVN+dVN6dVtSaWeGfVt+hXuKg
WOOhWeOiWeCgWuGiXd6jYtujZNyjZN6lZt+mZ8WzYMm4Z+GjYuSlYOWmYuCjZOOmZuWoZOaoZOap
ZeepZuKnaeCoauGoa+aoaOOrbuSqbOerbOSsb+etbuitbumvb+WuceaucOStcuStc+avcumvcOex
deawduawd+mwc+qwcuuxcuqyduazfOizeum0eey0ee22e+q1fOq1feu3fei3f+64fe64fqTAY6TA
ZK/CY6jHY7DDZKHQaa3Ta7LabpG+hOi3hOq5g+y5gO25gO67g+28hu+9hu+/ivC/iPG/iuu/kJzF
ibLWkr/gmLjVq/HBjevAkO7FmfLEkPTGk/XHlfHLoPTPqPbUsPjZtvrcvcnis8TExMbGxsfHx8jI
yMnJycvLy/vgw+vr6/Dw8PHx8fPz8/T09PX19fj4+Pn5+f39/QAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAALMALAAAAAAWABYA
AAj+AGcJHEiwoMGDCBMqXMiw4axTpiJGPNWwFClUsDJmREWqo8eOpQiOekWypMmTr0YNZNLkSRcw
Z9rY2bNo0R47bdaM8QLFiRWBRBBJytTJ0ydQoVKlCgXqk6dOmTAhIiLQBx0+iRo9uqRpEydOmzRd
etQoER86PwTKUPOmjh5FjBxBihQJkiNGivLUcZNGhsAYXMKggTPnDp4+fvz0wXNnDhw0YbjEEGjC
yJQrX8SUYRNHjpw4ZshIGSQoUBQYAh8EGaJkCZUqWbRs2aIFywtAhQwV+rNCoIMcOnoAEVLkCJIk
SZCwcEGokqxKhFQIbFCjuo0bOHbw2M4DRQtKomJmiaLU4sQsBiDSgwghYsQMGjRmZEjBqpWrVqxS
YJi1oIP//x58IOAHJGwwiSWrWDLJBhfMogAEHEQo4YQlWKDBIaocokEFE8wCwAEJhCjiiAgUQIEE
EUhAgQEOCRTAAAQMIECLCQUEADs=
'''


icon_add_dir_recursive_b64 ='''\
R0lGODlhFgAWAOfSAHpLGZBZHk9tTlBuToVjLpxhH5xhIJ1iIZBpLlh3VqJnJaNoKKZrKqluLapw
L2eCVq5zM7B1NX+DSbV6OWGUVbp/P4+MSs9/Ka2HQr+EQ8CFRNSCKdSDKdWDKX2ZWX+aWXCfWMSJ
SZSXUNaHMdeINcaLS9eJNdiKN8mOT9iMOtiOPNmPP8ySUtmRQs6UU9uSQqKhVs+VVNyTRHKxWtuU
RtqUStyVSN2VRt2VR9qWTNuWS9uWTNOYWN2YTtSaWd2ZT9ybVN6bUt+bUuGcVN6dVt+dVNCiWN+e
Wc+jV+KeVuKeV9qgYuCgWtyhYt+hXuGiXNujZOGiXeCiYtyjZN6jYp23YeCjYuCjZOGjYpS6YZS6
Yt6lZuSkYOSlYN+mZ+OmZt+naeOnZeKnaeWnYuCoatasYeGoa+aoZeaoaOapZuOqbuSqbOaqaeOr
brq5YOerbOSsb+StcuStc7u7YuetbeitbuWuceaucOWuc+aucuavcqDAmuawduawd+mwcemwc+ex
deqxc6vGZOiyd+myduqyduazeuazfOizeuuzc6XJaJrNZ+m0eey0eei1fuq1e+q1fOq1feu1e+i3
f+i3hOu3fb+/v+24fuq5g+y5gOy5gu25gMDAwO66gem7huq7h+67g++7g+28hsPDw+69hu+9hsjD
vsTExOu/kMXFxe+/iuvAkMbGxvDAisvGwcfHx+3BlMnHxe7BlPHBjcvHwsjIyPLCjsnJyfLEkPPE
kLrTp+7FmcvLy/TGk/XHlfDInvHInvHLoPPPqPTPqPbUsPbVsvjZtvjauvrcvfrfwtbrtvvgw+7u
7vPz8/T09PX19fj4+Pr6+v//////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////yH+EUNyZWF0ZWQgd2l0aCBH
SU1QACH5BAEKAP8ALAAAAAAWABYAAAj+AP8JHEiwoEGCt2opVHjroMFXrHhBmziRF6uLGC++Injq
mcePIEM+OzWQCpQtZNrYAcSo0qZNlRgB0gPHjJcpVwT6oIRqV7BhxIwhW7YMmTFiw4LtWkXJh0AX
hyZhEqVqFq5evnz1wjVLlShMkw7FEIhCTh9EkTKBKkUro6tMkBDxiYNCYAgxa+78KdTIVCyK0GKN
Gkw41b8MTrB8QfOmDieRIi39qwCECJMoXZpMAaMGz6BHmTI9GoRHDZgpSybk2PEjSBEen2QBE1bs
WLJkx4oJ+wXLE48ILYLTsMHCkCNNpFrZypXLVitSmhwZYuEghfUUKkq0yUNI0qVOoUKjdbokiVCe
NiUYjFi/XoOVMGzo+AmUKFEgP3TYhJGiQcGFDQBuQNkRT3AxxhlppHFGGXMI4gYSFQBQgAEUGjBB
DTr0IMQQSSihhBFVKKKMIlVgYBAEK6T4ggw34IADDFosEs0iWYhgUAMk5EiCCSf0+IEuzTjTjC4e
GLQABx0kqWQHFoAwAzMzgCCBQQEcYOWVViLwAAV7UPAAAQ6FKUACAwgUEAA7
'''

icon_remove_sel_b64 ='''\
R0lGODlhFgAWAPUAAIcoJIkpJpUxLKA4NMQ8NcU9NsY/OKxBOsdAOclCO8lDO7dIQclJQstMRs1P
SMRSSs5STMhVTs9WT9BTTtFVT9FWT8pZUs1eVtFZU9RdVtBiW9VhWtdjXtJmX9hmYNpnYdRqY9dp
ZNZsZtpoYtduaNp0cN5/euOIhOWSjuialuqhnuymogAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAACwALAAAAAAWABYAAAZ5QJZw
SCwaj8ikcslsOp/QqPT4iFgumg5IRCKJQB3NxRJ5EBehkumESqlWK1UKdTKVQgviQYLJbDgeHyMj
Hx4cGxkYEgdEAwwMDQ4QExQVFRQTEA4NjwNEAgShBQYICQoKCQgGBaEEAkQAAbKztLUBAFO5uru8
vb69QQA7
'''




icon_remove_all_b64 ='''\
R0lGODlhFgAWAPYAABISEh4eHiIiIiMjIyUlJSYmJiwsLDAwMDMzMzQ0NDU1NTY2Njs7Ozw8PD09
PT8/P0BAQEFBQUREREVFRUdHR0hISEpKSkxMTE5OTk9PT1BQUFFRUVRUVFVVVVhYWFlZWVtbW11d
XV9fX2BgYGFhYWJiYmNjY2VlZWZmZmdnZ2hoaGlpaWpqamxsbG1tbW9vb3BwcHFxcXNzc3R0dHV1
dXZ2dnd3d3h4eHt7e3x8fH19fX5+fn9/f4CAgIGBgYKCgoODg4SEhIWFhYqKiouLi4yMjI2NjY6O
jo+Pj5CQkJGRkZKSkpOTk5SUlJWVlZaWlpeXl5iYmJmZmZubm56enp+fn6CgoKKioqOjo6Wlpaam
pqenp6mpqaqqqqurq6ysrK2tra6urq+vr7CwsLGxsba2tr29vcDAwMHBwcPDw8bGxsfHx8jIyMrK
ysvLy8zMzM3Nzc7Ozs/Pz9TU1NbW1tfX19jY2N3d3eHh4eLi4gAAAAAAAAAAAAAAAAAAAAAAACH5
BAEAAHoALAAAAAAWABYAAAf+gHqCg4SFhodOSkZCNTVBR0lQh4IcOmBymHBoaG+YcmA6HIUROXNn
XUkoEAUEDylKXWdzORGEEms5LTo6IxYIBxQlPDstO2sShA5AdHBtZVAwGxwyT2VucXQ/DYUkUmx5
d3Z1mHR2d3hqTyKGCThWbm1mYVRUYGZtblU5CYYAGT5exlAhcuPGECpjwPzQAOBQBRhIuEzZIQhI
Ey5RaFSYFCHGEi1RfAjqIeWLExkTJjHwiKUJEEE7pnxR8mLboQMujGSRQlFPDydblsQ4MGlACyNa
oOAAMUIHkyxJXgiYFEAFEzFXjtyYUSQLGSUpph4yEGKJDxMbIlhYEeSJkxBFBjiGOBEDxAQEDTqk
uLHCQ61DC2xkCTOEBYYLLIaEuTJDwSQ9H5CkQTOmSpUxaNIg+fBY0AIUOHoU7IEDxYLOqFOrJhQI
ADs=
'''


icon_remove_all_b64 ='''\
R0lGODlhFgAWAPcAABwdGyYnJSInKCMoKSYrLSguLyowMiswMisxMy0yNC0zNS40NjQ1MzE2Nzc4
NjU4OTo7OTs8Ojo9Ozw9Oz0+PD4/PT9APkBBPz5DREFCQENEQkRFQ0NFREdKSUlKSEpLSEtMSkxN
S01PS0pNTUhOT1FTT01RUU9SUVFWV1ZXVVRXV1ZYVFlbV1NYWFtcWV5gXF9gXl5hYGFiYGVnY2Bk
ZWZnZGZoZWdpZWhpZmhqZmdqaWttaWtsam5wbGxwbm1wbnBybnBxcHN1cXR1c3V3c3Z4dHd5dXd4
dnh6dnp8eHt8en1/e3x/f36AfH+AfoCBf4CCfoGDgIKDgIKDgYKEgoSFgoWGg4WHg4WHhIaHhIeJ
hoiJhomKiIqLiIqMiIuMi42Oi42Pi42OjI6QjI6QjY+RjZCRjpCSjpGSj5KUkJSWkpWXk5WXlJiZ
lpmamJqcmZudmZqcmpyemp2fm56gnZ+hnZ+gn6CinqGjo6OloaOkoqSmoqKkpqSnpaeppaiqpqiq
p6mrp6qsqKutqa2vq66vrK6wra+xr7Gyr7GysbO1sbO0srS2s7a3tLe4trm6t7m6uLq8ubu8ury9
u72+vL/AvsDBv8HCv8HCwMPEwsXGxMfIxsjJx8jJyMjKyMrLycvMyszMy83OzM7Pzc/PztTV09bX
1dXW1tfX1tfY1djY19jZ19rb2d3e3d/f3d/g3uHh4OHi4OLj4uPj4+Pl4+jo6Ojp6Onp6evs6+3t
7PDw8PT09Pj4+Pn5+QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAL4ALAAAAAAWABYA
AAj+AH0JHDhwgcEFBBMq9GWwSKYzHgwuJHhwAa1YumpJKhHi4MIFiTql8jTLiIUdlgLN8APnCkKK
l1BpAhWozIYAAETcGQNpDyI6LwUukIVJ1KpNgcJoeNEDyaI/gUgVCsoQ1y5TpV59GkUoz5pBkT6F
MiSH6gI+qnj12pXrFi5brmCJ6hOHChiqvmi0YtVoEydNjxQpApQGCxceDSQkXGACz6lKkg55svPF
DRknJjg8ULgAzYcKJlCIRmFiRAcNDE7gZchmRRMbUmq4iMCiCgQZF6asXvCGhZclfooUoZCjiwMY
GarsfrNiDxRHdaBQACJmghAQQ5avmAOFkqAxIohimKFw/Yh2NVAmCVIjIsn4KCCC7G4tJ/369uOF
pPixW88KOUuox14SVpCHgwqrDYBBFm2wwQgcA96ghBUxLEDAQgIc0AITW2ShxRNO+KADCQhcOJEv
BSCgQEUKJGDAiTCeGBAAOw==
'''


RECYCLEicon_pdbqt_lig_opt_b64 ='''\
R0lGODlhFgAWAPcAAAEBAQICAQQEBAYGBgkJCQ0ODRERERcXFxcYFxgaFBgYFxsbGxscGR0fGR0f
Gh0dHR4eHSImGyEiHyMmHSMnHSYqHiAgICMkIiQkIiUmIyQkJCYpICcqICkrIygsISgpJSstJSgo
KC8yJjM5JjQ5JzAzKTA0KTk+LTAwMDQ0NDg4ODk5OTw8PD09PT4+PjpBLj1DLTxBLzxCMT9COEBF
NUJHNkNKM0RLM0VNNEZNNkBDOURIPEZKP0tPP0pTNkpTN0tVN0pQO01WOFBZN1BdNVJbPEJCQkND
QkZGRkhLQkpNQ0hLREpNRktORkxPRUlJSUtLS0tMSk1OSUxMTE9TR05QSVBXQlFWR1VcQVZfQ1JZ
RFBTSlBQTVBQT1JVTFNWTlRXTlRWT1dcTFleTlBQUFJSUlNTU1ZXVFdXV1ZZUFdYU1daUlhbUVhb
UlhbU1xeVlxfVl5fXV9fX1ljRFxlRFxiSl1mSV1lT19hWV9gX2VvTWZ1RWt3TXB/TGFnVmVuUGZu
VGJkXWNmXWNmXmRmX2dtWWNoXGdtXWh0UGlxVmJiYmpsZXh4eHWDT3SBU3qEYX+MYZClWpCmX5Kq
XpSrX5OoYZmvZZmuaJ2zap2za6S9aa/LbbHMabDOabDMarPQbLXSbLTSbbTRbrXTbrXUbrHNcbXS
cLfTdbjWcLjVcrnWdLrXd73Xe7/hccXlfouLi46Ojo+Pj5KSkpOTk5aWlpiYmJubm52dnZ+fn6Oj
o6Wlpampqaurq6+vr7GxsbS0tLa2tre3t7q6uru7u7y8vL29vb6+vr+/v8DAwMHBwcLCwsPDw8TE
xMbGxsjIyMnJycrKysvLy83Nzc7Pzc/Pz9HR0dPT09XV1dnZ2dvb29/f3+Hh4eLi4uXl5ejo6Onp
6erq6uzs7O3t7e7u7u/v7/Dw8PHx8QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAOcALAAAAAAWABYA
AAj+AM8JHEiwoMFzxYQJG0asmLFjyJJJTIbsmLFixIYpLBaMm7dv4MKJG0eunDlz5ciNExcO3Ddv
3IL96sYCRYoVLo4ggUKGDBQkRlysSIGCRbdfvraFQPKlyxlDcfIsUiSHEBozbX6G2OarlzYNTbak
8fPokKBBgwLhebMmzJYmGrT14pXNQgsmUhKxKqQGjpkybqY8qWKkhYVsvHZhW6AiyZVLriCBYcMl
ihegS1ioWIBtl65rCHT00LMKU6Y7YwCJoeJECY8dMxBc05WrWoMadCRVclSqDqJTf+xosZIlCI0G
1XLhmhbBE6hQWOZs4mNJlaZUpkSR+sQpwjRct6DCJbjxA4eMHJMooWo0qk8RIUB83EgA7ZatZwUw
lMBw4cSeVpHYEMMLH2RgQgYYFPCMLbU0Q8ADHTwAgQgwdDJEBxKAAAGEDzxAQDO10MLMABuUuIEH
IxBBggccmGjiAMzQMosyAhwwwQEHUMCAAxUoYCOONx4ggDKzyIKMAQAkqWQASjaZpAHIyBKLMcks
04wz0UhDTTXWWFMNNdJE40wzyyRjTCywADPMmmy26SabwMDCyCt01mnnnXcyctCefPbZZ0AAOw==
'''

icon_pdbqt_lig_opt_b64 ='''\
R0lGODlhFgAWAPcAACEnJywxMy40Ni81Ni80Ny41Ny81NzA1NzE2NzA2ODA3ODE3ODE2OTA3OTE3
OTI4OjM4OjM5OjM4OzM5OzM6OzU6OzU6PDU7PDU7PTU8PTY8PDc8PDc8PTY8Pjc8Pjc9Pjs/Pzg+
QDo/QTlAQDtAQj1BQzxCQz1DRD5ERj9ERktOSlBTT1VXU1ZYVFhbVlhbV1xeWmlranp9e3t+f32A
gX+CgIaJhYqMiIuNiZCTkZCTkpOVkZWYlZaYlZmcl5mamJqcmpyempuenZ6enZ6gnJ+gnaChnqCi
np+ioKKkoaGko6Kko6eppaqrqKmrqqyvqq2uq62vq66uq6uurKyvra6vrK6vra+wra6wrrO3sLO2
sbO0s7O2tLa5tLi6tre5uLm7uL2+vrzAvL/BvsLGv8DCwcHCwcLCwcLEwcLGwMPGwMXFxMbHxcXK
w8bIxMfIxsfJx8zMy8zNzM3OzM/PzsvQyc/SzdDSztHUz9DR0NLT0dLU0dPU0tXV09bX1dfX1tbY
1NfZ1NfZ1tjc1tnc19na2Nvb2drc2Nvc2Nvd2tzc297e3d/f3t7g3N7i3N/h3uHh3+Hh4OLi4OPl
4ufo5+jp5+nr6e3t7O7u7O7u7vf39/j4+Pv7+/z8+wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAJ4ALAAAAAAWABYA
AAj+AD0J9NSCxQtPL1i0GMiwoUAWdCRdeXNFEh0WDjOyiLSpk6ZOmyJhzNjQhRRORWAU4STFBUmH
azRhZKHpjCcTAiK89GQSpUpOPwSEkTNhYAOHGzt+3MTIQiFMKR4koKHkQkOIEtkkgeQEwpxLnDKV
MWNIiIKGBQ8KwNBB0Z8jN4zoWQRmxksSX+DIyYMjSJMoR/hwWfAywZY+lI4wASJiCRotgh4wTIsQ
xIMQlXyMOeEJRaIsjz4wkOAJ68SKcSb4eeJmSgkujdIggmIlQWmOHkFG0oDlTpdDlia1CSSGB5IN
PE+mXFnDA5E9eNSQqUPITgYHAgbGnKlphA4mPag/AHI0yEuFksp/DqGQ40IAAxx22DhwFffSSCsK
ABBIQEaM7AxhVQUbVVg0kkADCIBARgWp4IkKCu0k4YQUShgQADs=
'''

icon_lig_filters_b64 ='''\
R0lGODlhFgAWAPcAAHdTHXdUHnlVHn9aHVw1ZmI9YGE7ZHdUWXZTfXhVf49aA4hYDJJcBZJcBpRf
CJRfCZZfCIBXFoJYE4JZF5ZkEZ1rF6hyHbB0EpBmJKt6LKx+Mq5/NItuUINib4draJd4f6qRDKyY
DbOWDLSWDLaXDbaXDreYD7ebDrmZDbiaDbmbDbiZDrudDbqeDb+HGr6iDb2jE76INcWrDcasDsat
DsqwC8+3D9W/D8ygF8etF8etGsmxFs62FtC0FtK7E8eJJs+UOdCYPceuJMiwINe+INm+IMKpNtK7
NNfCD97FC97ED9jDE9zDEdnDFNnEFNnEFdnFFd7FFd/GF97HF9zCGNrFGtrGG9vAHOXPFuTOG+DJ
HdfAKtfDK9nEMdzEM9fDONfEP+POJ+TOJeXPJuDIKOPMKubQIOnUJ+HNPePOPOTRNefRNOTQN+zY
MujWPevYPu7cPJ2ARb6OQqyLVrupQbqnTrmYZM2aSNGZQdCkX8atYdirad6xa9zHVOLSQuTTQu3Z
R+/dRuDQT+rXTOjWTubUVOvXUO3aUOfZXuvZW+vbXe3dXvLdWfDfXfHgSPLhTPPjUfTjUPLgV/Pj
V/XkVfblWPbmW/blXM3BYdfBZO3fafDfcO/havXlYvTmdPjqcvLmepV3mKKGheW+gsq3pfPlhvfr
h/rvjffulvjulP7zlgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAKsALAAAAAAWABYA
AAjvAFcJHEiw4AMGCgoqXOhgg51RDRZKFFhhToQ9CyYuhJAnwwU5EzQqpMAnyJ0BIhVqwAMEA4CU
BCXE+GEhAEyBSJbswOFCwM1VoUSRylSIB4yfcTogSPBBzxcZMKEk6lOHgwECB2BaQVXqEyA/dDwU
SFkllapOlgLBcYMJhMgmpk4xuhRpTZsxml5odOIJ1CBJlN6UOTNFEYuJTzghSnOokiMyYrIwIaRC
IpI/gnwYmvSIyBUzSqKgSTHxBpdNjSDN6EEFSw0tW0RotNFlEZghRaQkQRFGR8oQNHII8cLmiBE1
K36eaKGihAkSI37eDAgAOw==
'''

open_small_folder_icon_b64 ='''\
R0lGODlhEAAQAPYAAJBZHp1iIaNoKKluLa5zM7V6Obp/P9ODKdSDKdWDKdeINdeJNdiKN9mPP8CF
RMaLS9uSQtyTRN2VRt2VR9qUStuWS92YTsySUt+bUtybVNOYWN+eWeGcVOKeVuKeV+GiXNqgYtyj
ZN+naeCiYuCjYuSkYOWnYuOnZeaoZeapZuaqaeOqbuOrbuetbeWuc+aucumwceqxc+uzc+myduiy
d+azeuq1e+u1e+i1fu24fr+/v+y5gO66gey5gu+7g+m7huq7h+69hvDAivLCju3BlO7BlPPEkPDI
nvHInvPPqPbVsvjausDAwMPDw8XFxcbGxsjIyPrfwvX19fj4+AAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5
BAEAAFQALAAAAAAQABAAAAfIgFSCg4SFg1BPiU9QhoNOUFORU1BNlZZOgkxSm5ydmzpUICEiKy40
Njs7NjQuKyIhIBpARUhJSktRUUtKSUdEPxoXNTg9QUJDRkZDQkE9ODUXDywvMzc5PD4+PDk3My8s
Dw4kJyotMDEyMjEwLSonIw4GGRsfJSYoKSkoJiUfGxkGClCoYAEDhw4ePHTggMFCBQoFCDSYCCGC
hAkTJESAMLEBgQEKQipYwKAkgwUiFQwQgCCBy5cwESA4IABAgJs4c+YE0KgnlUAAOw==
'''

ok_icon_b64 ='''\
R0lGODlhEAAQAPYAACc+JzBOMjpbN0ZySE55SFB3RlWASV2GSVqLTl6KTVWTT2KMS2GLTmaRTmyU
TGmSUW+eV3ObVHWdWF+iVWGpWGmrWWyrW3qhVX2iWXmnXWywXW2xXnSwXXmwXXezYXa2YX2zYXi2
Ynm4Y3+7ZIKoV4OqV4CmXISqWIGrXomuXJG1WYOyYI+3Z4C4ZYO/aZS3Y5G4YpvAV6HGV6/QX4zB
bI3EbZrAZZTDbZjKc5/NdZ/PdaDDZ6jLZ6XGbLHRbKbId6XOdbPQcq3WgLvXhrbahbrZhrrbjcLh
ksrjmQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5
BAEAAEkALAAAAAAQABAAAAdpgEmCg4SFhoYzh4c+SEEyioM8Q0dFMZCCPUZEO5dJNj9CQCqdLzk6
MIckJ4IpLDg3JYcXKxhJJjQ1KIcOHSMgEhkuLRGHCw0cHx4hIhAPigcJFRobFgydBhMUCAWdAgQK
BJ2CAAMB4p2BADs=
'''

edit_icon_b64 ='''\
R0lGODlhEAAQAPUAAF1PMlRPOmVTKHJpPllXVmtqZoNdC4dfCoFdEYFeFYBfFYtkDoJgFaV6G6Vf
Uq9sY7Rxa6yCI7GeKrOdLLWgLrikOMebO8GrNcauOKqXVayMdbaqcbCmeMyjQtCoSta/U+O/X9Gx
YdrDVd3FV/zVXufGZ/TQYf3YZPfVaf3abOrPee7VdO3XduvVePfadvnacpuHhKenprOxr728ucms
qdmoqMC9veO8u+PUoQAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAADkALAAAAAAQABAAAAZQwJxw
SMxBasWkUEO7PZREjswGc0CHm1mMcBVKWqoCoJv7pDwI8sVVWpAnLFSEnBOdOgoy5gU6kCkrJg10
IyQWCWQVOCEGdAMZDHQ5AQKSlkEAOw==
'''


default_setting_icon_b64 ='''\
R0lGODlhEAAQAPYAAIlyDotyDqCDEKGEEKSHFaSIFqiKFquNFbyaFLCSG7SVHrSXJ7aZJ72gMcin
Ht+5HuK7HcaqPebBK+bBLOfBLefBLubEOebEOurHPOrIPcuvRM+zSs+1TdG2Tda7VNm+U9u+VNzB
WNzCWd7CXN7CXevKSe3MS+7NTOrNUuzOXPDRV/HSWfHTWvHTW+HIZ+LJZuXMaubNbefPbebOb/HU
YfPVZfTXZ/XXaPXYaejPcujQdurSefbcdffcdvjddvfdfPPchPHdkfjhgvrihPfhj/jjjPbimPfj
m/LioAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5
BAEAAEkALAAAAAAQABAAAAeLgEmCg4I5hIeHMjsyiI06RDqNhy9ARUAukh8hIzNCQ0IzJCIggxwe
MEFHPz0+PTxGSDEeHYIbKTQ1Njc4NzY1NCkbhBooKissLSwrKigaiBElJifTJiURjQ0WGBncGBcN
jQwSExQVFBMSC40JEA8OCg4PEAmNBwgGBEkFBggHjQIADgUYIKmgQUmBAAA7
'''

preview_icon_b64 ='''\
R0lGODlhEAAQAMZLAC40NkZKSk1RUFJWVWJmY2JmZD9rokBrokNupGZqZ0RvpUhvoUlwokVxqEdz
qkhzqkhzq0l1rEp2q052p0x3rU14rVF4qU55r3J1cXJ1ck56r1B7sFB7slB8sXR4dXV4dFJ9slN+
s1WCtlqDsliEt1mFuV6FtFmGuVuGul+HuF6KvV+KvYOGgl+LvmGNwGWNvYiKhWOQwmaQwGiQvmSR
w2eTxWqTwGeUxmiUxmiVxmqWx2yZyXCczZmblo6frI+frpamtKOmn5eotZiotpmqt5+xxq2wqZ+y
x7e6s9XX09rc2P//////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////yH+
EUNyZWF0ZWQgd2l0aCBHSU1QACH5BAEKAH8ALAAAAAAQABAAAAeagH+CMISFgoeIMD1GSEhGPRiI
hzBBQzM1ODZEQZGJPUAoMTs8NytCPTCJRiMnLjk6NComRhmJSBoiMrotJSBIH7YSKS+6JCEVv6oT
ERccHRsUFkapkyw/CA0PEA4KR6iSBEE+CwYHDEVBAgCSfwQ9SUpKST0BHgD3kjAFCQkFMPcD/q1j
hwgAjID4CAq6d/CfwkMMHT5ceA9AIAA7
'''



single_receptor_icon_b64 ='''\
R0lGODlhMAAwAOf/AEQHAkoIAFMHAGcGAVkLBk8ODGAKBGMNAHQKAHANAYYHAWYQC1kUCn4KA04Y
E2EUCVgXEm8RCmoUB2IWEYoNAEsfG30WDWIdGHgYEZcRAIYVC5kUB2giF5kVD4McEYoaFHYgGGUm
HYUfGX4hHGcoI2ArJJocEZIfE30mGnEqHpEhGXEqI2ssLHYqIJQkG5kjF3AvJIgpImoxLnYvJ6oj
E4MtJ34vKoYuI7AkEGU4NKEpHXk0MG04LZQwJHU6MYA3Lz5KQKAwJLIsGoc3LJM0K4c3MaIyK6Qz
IaMzJ4E8N5o2L2hEP3BCPrQyIp45LH5COIhBNo5CNHZIRIlEPYNHQplBPYBJQq89L5xCOXtMR5hF
OZBIPY1JQsk9KXtSS39RUatIN4lQTJFOS6VKQaBNRptPRblHQoNWUIpVUqlOSa9NRsBLL6pRQ4Nc
VJJYUX1dXpVYWN5HL6RWTKlVUINgXMtOPJNcWdhLN45eWZFfVYphX5tfWMZVQopnY5FmX6dhW6Rk
XtJaPZloY5RqaL9gT99YQo5vaopwb65nYZluZ6BuaaptZpdzb5J1b71sYJ50cqpxbpZ7eqV4cZ56
dchwZrh2bax5dKF8eOlrULR4cNB0YKl+fMt4bJ+Dgsp4cqWEfsN/c7KEfcKBf6WJiKGLiKqJg4yW
i7aKiKqOjcSIf6+RiqiTj82Kg76QiLiSjsaPirKWlJudma6YlaqbltCSibuYk+yNd9GVkqufn7uf
nreinsKinM2gnbSoqL6opcqmp62vrNall82notykmbCyr8WvrNato7S2ssS0r7e5tsW4uM63tNS2
tbu9usu8t+C5tNm7usHDwNW+u83AwcrEw+u8utHExMbIxdfDxc/JyMnLyNXIydjJw9/Ixc7QzNDS
z9bR0OvOydPV0tzW1efX0tnb2N/a2OPd3N3f3N7g3eXf3uDi3+/f2eji4eLk4evl5OXn5Ojq5+/p
6Ozu6/Tu7e7w7fDy7/Hz8PP18vn08vT38/b49fj69/n7+Pr9+f///yH+EUNyZWF0ZWQgd2l0aCBH
SU1QACH5BAEKAP8ALAAAAAAwADAAAAj+AP8JHEiwoMGDCBMqXMiwocOHECNKnIjQm8WLFr99E8ex
o8eP4jRixLjQWzl79/Dh07ev5T5+/WL280ezpsx+/Fzu06fynr1y3hRqq3cv5UqX/GDKrGlTZlKX
PPEVradNaNGU+li2TLqUaVOcOVtmlVq0akJtV41mRXqT6c2wO6OmNYsQ7VWVa7e2/YoTqtyrdA9e
S4tX60ulM78+Ffu36DWF11ASXmmY602wfnumtfc4YeS0ag0ffgs3ruarnCHbk3yXss6ksEuPJYs6
ted69VaDLpxPns6W8s6do3e66GrcnRFew617Nz52w2hVg8ZM2bJnkGzYsMQNtE97yCH+z8PNvF67
d/fIDbOF6U4XHRoWRNDhQgSGEVCWvYPW7d143PMkJ9h/uI1TyxaLSFPJCZUY80w4oUwwAwm7MLNL
Lp+UAMMYdWCiSTDhACigQdHMM5483ZDxwQEEhJDFFFuMMAcrolDhBxOP7LGCG6MckkMBHDjCRyGE
OGNiNAqVOM87t/DRhBySzAABGrJY8wsiDXSgAAITkIDHGcWsNgkBATzxRBRQlFLMPEgmpOQ2qVDC
SyJD/ABIAofMY485fpSChx25jGNOH+as1kgAJdhwyjSRGDKIOW0iVCI4qEwzji4gYCBIFQi0IIw9
yMAij4m5zSOLL/Uw8wQBeMBRwzL+8SgjyzuRHhRNPPGsQkcfdsSwQy4nENGDE9igQg155IEzijVU
kCDABYyMsIg8uMZTq0HN4PqOcH/EkEsoNNzyCgqutEIgbu2008kSTPgyCQOo/IGENNU2o1C21ebi
QRWTBIGDE2CgMIUPuGzzDm6+MNKHFBX0Mg81JIjxihCKTIOrvQnhiysqAxCQQiBsIMIJKCEQQMIl
qrSjTjHgbCPGBJKccsoUIjyChQQ8OBMPxghpHI8sDMjAxhpEzOEGLHQUAAEpumQzDSzSeLJBBhQg
MIABB2C9Qh/n7HxvtfGcM8oSHnhQhhoaqDCCAFbQYcghh0gRgxlKNJDAAEwAIID+ARf4Ys7FCiUD
D9juZMPFAnvs4YIQDaABzjnTqFKKMlb4kQskN7yQhtUG6PF3PPAkEzg8g4N9CAA7yGfCGNvEo8ol
vmxjTRlGNHFHHF10MIIBaHxOuugJJeMO6cTDgwsLerzhwAtXFGPNJ59vs0kxoWhxxAt5PLGAHcW7
AzxCwg9f/DhfHLDDAxZEMMo0naijzjKALGINONNsokESXiRhh/jueB94//0rnjIEMQIanMASgjoD
HQTRgw3oQBG+KEYmjhCGLMygDQDs3/cOcox1rCODGYRFEVLACEa0wQEV4IAEGNACWMADGbXYBTh0
NQsAevAYCumgB0EIQGpYIxuspPACKagBCyrIAA+X6AUIs2HDG+YwHVCEogenmMFzmOMc7ljHOEgR
iUgoMYtTXEcUoYjDhBxjjFEMIxV5CEY1opGMT3xjGtVIxzDKMYplRAgx7sjHPvKRGArZox8HOUhA
JkSQhEykHA2pR3Q48pGQjKQkJ0lJRh6EGOWgpCY3OclyAEMhsYhGJjlJSkqWIxqmWEgsgMHKVrry
lbCMJSxNAQSK2PKWuMylLh0SEAA7
'''

multi_receptor_icon_b64 ='''\
R0lGODlhMAAwAOf/AFUHAmUDAFALB0kNC18IA00QB2ILAHEHAWoKBGMNB1URDYUFAF4RDVoVC3AQ
AlcaEnMVDlsdGn0WE5cRAHcZEWQeGWAhGGseF2YgFogYDYEaEJEXCmMkIHAiG5MaDJsYEFEsJ34g
G1wqJWwmIGMqI2IqJ4ghFWkpJJ8cDIMkGTc5NnwnInIrJG4uI4coHJwjEoEqIGkwLJQlHHssI3cv
KJoqIJIsKJQsI300J4kxJogxKo8wJ3I4NLQoGWk8OG07OaYtIIA3L3I+N4g4Mn48NrEvJno+NbIw
IXFDP3lCN4c+Opo6MH1CPps7NotBOItBPaw6J6U8MKQ8Nbs4J7Y7JqFANYpGP7A+MKRCMpJHQ5lG
OoJMRY9LQ5NNQZ9LP35VTqVMTa9MQJZST41WTr9LNY5XVZVWS5RWUJtVTaNWUJhZVNdKM6VXTZJc
WYlfWI9eWcNUOqhbVYxjYY5jXKVeVpVkX4RpaKJiXZ1kXJFnZatjWpBtaI1wasliVL5nXqJwa7lq
ZLZsXZN1b8doXJl1caR3cJ97d750a6p5eax5dN9tVutqVJp+fbl3cZx/eM9zX6h9e7V7d8t4bJ+D
gsZ6a6yBf6eDf6SGf6qHiKyHg7OHhaiLiryIgpSWk6eRjruPjZeZlraRjMqNhLCUk7aXkbKdmsCa
lrGeoOSTfr2dl7ChnLagncChmrmjoL+iobKmpramodmdmb+ppq2vrNWmnrCyr9+nm8Suq8utrLO1
ss2vrtWuqra4tcq0sLi6t7m7uMW4udK1tNS2tb2/vMu8t9G7t9u7tMDCv8y/wOK6tcfCwdu9vMPF
ws/Cw+C/uMXHxM3HxsfJxuHDwtTHx8nLyN7HxNjJw9bJysvNydHMys7QzNTPzc/RztvOz+bOy9HU
0NnT0tPV0t3X1tnb2OXY2dze2+Ld293f3Nvg497g3eHj3+Pl4unk4uXn5Ozm5efp5unr6PDq6evu
6u3v7PPu7O/x7vbw7/Dy7/Hz8PL08fT28/b49Pf59vn7+Pr9+f///yH+EUNyZWF0ZWQgd2l0aCBH
SU1QACH5BAEKAP8ALAAAAAAwADAAAAj+AP8JHEiwoMGDCBMa1MawobZvECNKnPjNYUOFB7WVu6dP
376P/Pj1G9nPn0l/JPuF/Liv471y2jAWxFYvX0eQIUmePEkyJL+PHfPVwyaTIDV8+fApXcq0qdOm
SakVHRjtqdWrTqNNFVgVq1erWrdGu/e17NJ7YaeONWsW7dZ/z+qRZYv1Xr1nb+PWwwrTIsW/ES0y
LPhs3l6r2MZx9Igz5c6UK4HqexlzILN585qyY2fPGU2bjH3q3IlypE/JQolaxrzUnSknVkJpOZqU
7tWoBI/Jk6dUmqQaWTA8kNPVtte0/3TzZidqECczOM7QKG78KvJj8ODFW4VM3B8HdZr+HFhb3arb
gcPewcMHjZGhLEpcfWBDvrzT8wLTv1tazEYlOj0cEtdcbBHYlF14offOfkpZEsAIcIQBiF5W0ZMM
Ld5UA401wqhhhSnuOFXPXQT9suBSmyjQBRlLpFHYYUpt1hkqi6wxRQYJQACECRSEgAc5y1QTjz34
1DNPggKZyCA+8XgShAR0SHFZZvi4BptsWnCyizFMEPEDLqaQMokIM0ChyCO2sIMZMyW2005TowjA
xQpT4uMbcMLJkckdYEhxgw4cMGFEIdCswkEBaGARBSnizMPmQL6ss05TypSQhw/KMeccdNJtE08x
Y5yhBCbNOLINPuCQEMEQqVzChyH+8RxDEC/qqOOUHAGwoBs73HkHnniJ0HNLL0wB04o9oTBQhhpo
uJPNKfLIOhCttjYljiY3YAdPe+/FN98NuozCDlP0eLIKDzE0YIgOwuCTnbQCUWtVL+mth09//wWY
Ax5/oEMPPvcQ08oeILyyzQmI+AGIOfC8MwxBudR6lX4NPhghIJS0wIAbpLjjTi/ZtGEBK7iIsUMk
LiRxjcMQp5POxCfik+KKLWayxwBCrJJNM7LEgsIECyBAgAEJXOAGOywPlIvLVympVJNPRrmBBhUY
MokgfGxRRRwpOECEAgAQsAk9C/7S8stWOb1UnHO+IMMt8dyySi+uOOFHH1QUoYH+AWWYg0/ZBNXC
dNpuMlXppRpccQ0xvbhDjzCfNBLFEV5YQQApSrlp9kC1nHPOVZFOyhSuLEBwQCnATPM4HbiY00wa
MHzxRChKSeoLQbOM87lV8jJ17Q0eJAJOKUiMkcEGaRTTSyB6zEFEKUrVygtBoBwzzlW9N9ULJK0I
goQdb3RwQiHgiNNNPOCo4jc+0hfUySzwxy9/9k3VQ4854MTjDjKEEAILUzBq31YiVi37LKVWuXjL
0tBmQKW4LIEDHFwD8fFABUqwgRXciuAYiMF01OItndvdBD33wa3kznMoTKEKV8jCc4xjFm+pnu5a
SMMWjuMYoHiLCt4nvx768IcRPeyECt5CxCIa8YhITGJRAgIAOw==
'''


split_icon_b64 ='''\
R0lGODlhEAAQAMZ3AKQAAKUAAKQBAaUBAaYBAacBAaUCAqMDA6cCAqgCAqkCAqoCAqcDA6QEBKUE
BKoDA6QFBacFBagFBaYHB6wMDK0MDLEPD7IQELkVFboXF70ZGb4cHMAiIsghIcMkJMokJNQwMN0/
P98/P95AQOBAQOZDQ+ZFRedGRuhGRuhHR+pLS+xNTe5PT+5QUPBRUfJRUfBSUvFSUvFTU/JUVI54
co6Be4iKhYmLhYmLhomMhYqMiIuNiIyOiIyOiY6PioyQio6Qi+V7e5SWkpWXkJyVkZWXkpWXk5eZ
k6uXk+6FhZucmZydmZ+fm5+hnqCinaGinqSloKmppqmqpqmrqaurp62vq7GxrbKzsLK0sLS2s7W2
sra2s83NydHQzdLRzdPSztva1t3b2ODf2+Th3eTi3uXi3uXj3+jm4unn4+np5+rq6O7u6+/u7PDw
7/Hw7/Dx8Pf39vj39vn5+Pr6+fr6+vv7+vv7+////////////////////////////////////yH+
EUNyZWF0ZWQgd2l0aCBHSU1QACH5BAEKAH8ALAAAAAAQABAAAAe9gH9/CQMLgoeIgggZKC5JFolA
PUc4NggqGgwfJgiHS19sdVg6ADECfxIsBIJOYmhzV4ILJBwOEzCrRWFlclaIFSMrMiAQP11mcFWJ
fw8FAQBIO1FtU8uINFBqb0bWiDVPaVJN3Q8IAgdEO1RuWMsUIcJBDUBcZHGxhwsiHg4OMwB/hoAZ
I0fLoQEtDPyJ8ALgHyZiztDZIihBig0MOqQocEiJlzV2stxAgOGEixIXEvngIQRHDkEKBiTodigQ
ADs=
'''


root = Tk()
# Custom font setting:
root.option_add( "*font", "Helvetica 9 bold")
root.option_add( "*font", "Helvetica 9")
#root.option_add( "*font", "Helvetica 8 bold")
root.title('Raccoon | AutoDock VS')
Pmw.initialise()

nb = Pmw.NoteBook(root)
p1 = nb.add('Ligand(s)')
p2 = nb.add('Receptor(s)')
p3 = nb.add('Maps')
p4 = nb.add('Docking')
p5 = nb.add('VS Generation')
#p6 = nb.add('Experimental')
nb.pack(padx=3, pady=5, fill=BOTH, expand=1)

# TODO check
# list of windows that can be created and managed
Mol2OptionsWin, LigandOptionsWin = None, None

# Font settings
## Courier-related settings
if system == "Windows":
    courier = "Courier New"
    courier_size = "6"
    cygwin = BooleanVar()
    cygwin.set(False)
    import ctypes # used by CheckDiskSpace on Windows
else:
    courier = "Courier"
    courier_size = "9"

courier_style = "roman"



# For the hand-breake function
StopImmediately = BooleanVar()
StopImmediately.set(False)

receptorFileList = []
DirJournal = []




# Mol2 Splitting facilities
mol2_naming_scheme = StringVar()
mol2_naming_scheme.set("ZINC id")

# Ligand preparation options

# AutoDock atom type list
#     this dictionary is updated with the atom types found
#     in the selected ligands, and used to evaluate dir's
#    of cached maps
## Warning: atomic weights are inaccurate and there
#           is no account for merged non-polar H's
#
#
# TODO check for more accurate atomic weights

AtypeList = {   # count  MW
        'H'      : [ 0,  1    ],
        'HD'     : [ 0,  1    ],
        'HS'     : [ 0,  1    ],
        'C'      : [ 0,  12   ],
        'A'      : [ 0,  12   ],
        'N'      : [ 0,  14   ],
        'NA'     : [ 0,  14   ],
        'NS'     : [ 0,  14   ],
        'OA'     : [ 0,  16   ],
        'OS'     : [ 0,  16   ],
        'F'      : [ 0,  19   ],
        'Mg'     : [ 0,  24   ],
        'MG'     : [ 0,  24   ],
        'P'      : [ 0,  31   ],
        'SA'     : [ 0,  32   ],
        'S'      : [ 0,  32   ],
        'Cl'     : [ 0,  35.4 ],
        'CL'     : [ 0,  35.4 ],
        'Ca'     : [ 0,  40   ],
        'CA'     : [ 0,  40   ],
        'Mn'     : [ 0,  55   ],
        'MN'     : [ 0,  55   ],
        'Fe'     : [ 0,  56   ],
        'FE'     : [ 0,  56   ],
        'Zn'     : [ 0,  65.4 ],
        'ZN'     : [ 0,  65.4 ],
        'Br'     : [ 0,  80   ],
        'BR'     : [ 0,  80   ],
        'I'      : [ 0, 126   ],
        'e'      : [ 1,   0   ], # always 1 by default
        'd'      : [ 1,   0   ]  # always 1 by default
        }


AtypeList_special = {} # list of non-recognized atom types
DEFAULT_ATOM_WEIGHT = 12 # default aweight to be used for unrecognized atypes


# The Great Book of Ligands
LigandDictionary = {}
# its general structure is:
# {'filename' : {
#        "Atypes"    : list
#        "TORSDOF"    : int
#        "HbD"        : int
#        "HbA"        : int
#        "MW"        : float
#        "Nat"        : int
#        "NotStdAT"    : bool
#        "accepted"    : bool }
#        }

ResidueRotatableBondTable = {
        'GLY'    : [ 0, [""] ],
        'ALA'    : [ 0, [""] ],
        'PRO'    : [ 0, [""] ],
        'VAL'    : [ 1, ["C"] ],
        'LEU'    : [ 2, ["C"] ],
        'SER'    : [ 2, ["C", "OA", "HD"] ],
        'THR'    : [ 2, ["C", "OA", "HD"] ],
        'CYS'    : [ 2, ["C", "SA", "HD"] ],
        'ASN'    : [ 2, ["", "", ""] ],
        'PHE'    : [ 2, ["A", "C"] ],
        'TRP'    : [ 2, ["C", "A", "N", "HD"] ],
        'HIE'    : [ 2, ["C", "A", "NA", "N", "HD"] ],
        'HIS'    : [ 2, ["C", "A", "NA", "N", "HD"] ],
        'ASP'    : [ 2, ["C", "OA"] ],
        'ILE'    : [ 2, ["C"] ],
        'GLN'    : [ 3, ["C", "OA","N","HD"] ],
        'TYR'    : [ 3, ["C", "A", "OA", "HD"] ],
        'GLU'    : [ 3, ["C", "OA"] ],
        'MET'    : [ 3, ["C", "S"] ],
        'ARG'    : [ 4, ["C", "N", "HD"] ],
        'LYS'    : [ 5, ["C", "N", "HD"] ] }

# Filtering preview labels
TotalNumberLigandsMsg = StringVar()
TotAcceptedLigandsMsg = StringVar()
TotRejectedLigandsMsg = StringVar()
TotalAcceptedLigands = IntVar()


AutoDockMaxTORSDOF = IntVar()
AutoDockMaxTORSDOF.set(32)

FlexResTORSDOF = IntVar()
FlexResTORSDOF.set(0)
FlexResTypes = []

seriously = BooleanVar() # filtering or just previewing
DoRejectATypes = BooleanVar()
DoRejectATypes.set(True)
HbDmin = IntVar() # HydBond DONOR 
HbDmin.set(0)   
HbDmax = IntVar()
HbDmax.set(99)
HbAmin = IntVar() # HydBond ACCEPTOR
HbAmin.set(0)   
HbAmax = IntVar()
HbAmax.set(99)
MWmin = IntVar()   # Molecular weight
MWmin.set(0)
MWmax = IntVar()
MWmax.set(9999)
NatMin = IntVar() # Number of heavy atoms
NatMin.set(0) 
NatMax = IntVar()
NatMax.set(999)
TORSDOFmin = IntVar()
TORSDOFmin.set(0)
TORSDOFmax = IntVar()
TORSDOFmax.set(32)
FilterSet = StringVar()
FilterSet.set("Default")


# mol2 splitting
sub_splitting = StringVar()
sub_splitting.set("every 1000 molecules")

# Grid settings
AutoGridBin = StringVar()
AutoGridBin.set("")
GPFkeywords = [
        'npts',  
        'parameter_file',
        'gridfld',
        'spacing',
        'receptor_types',
        'ligand_types',
        'receptor',
        'gridcenter',
        'smooth',
        'map',
        'elecmap',
        'dsolvmap',
        'dielectric'
        ]

mapDir = None # The path of the cached maps

GPFParameterFile = StringVar(value = "")
DPFParameterFile = StringVar(value = "")

DPFkeywords = [
        'autodock_parameter_version',
        'outlev',
        'parameter_file',
        'intelec',
        'seed',
        'ligand_types',
        'fld',
        'map',
        'elecmap',
        'desolvmap',
        'move',
        'about',
        'axisangle0',
        'tran0',
        'quat0',
        'dihe0',
        'ndihe',
        'tstep',
        'qstep',
        'dstep',
        'torsdof',
        'unbound',
        'rmstol',
        'rmsmode',
        'extnrg',
        'e0max',
        'intnbp_r_eps',
        'ga_pop_size',
        'ga_num_evals',
        'ga_num_generations',
        'ga_elitism',
        'ga_mutation_rate',
        'ga_crossover_rate',
        'ga_window_size',
        'ga_cauchy_alpha',
        'ga_cauchy_beta',
        'output_pop_file',
        'set_ga',
        'sw_max_its',
        'sw_max_succ',
        'sw_max_fail',
        'sw_rho',
        'sw_lb_rho',
        'ls_search_freq',
        'set_sw1',
        'set_psw1',
        'rmsmode',
        'ga_run',
        'analysis'
        ]


# Default DPF
default_docking_parameter_file = """# Raccoon v.%s DPF template 
autodock_parameter_version 4.2       # used by autodock to validate parameter set
outlev 2                             # diagnostic output level
intelec                              # calculate internal electrostatics
seed pid time                        # seeds for random generator
tran0 random                         # initial coordinates/A or random
axisangle0 random                    # initial orientation
dihe0 random                         # initial dihedrals (relative) or random
tstep 2.0                            # translation step/A
qstep 50.0                           # quaternion step/deg
dstep 50.0                           # torsion step/deg
torsdof 0                            # torsional degrees of freedom
rmstol 2.0                           # cluster_tolerance/A
extnrg 1000.0                        # external grid energy
e0max 0.0 10000                      # max initial energy; max number of retries
ga_pop_size 150                      # number of individuals in population
ga_num_evals 2500000                 # maximum number of energy evaluations
ga_num_generations 27000             # maximum number of generations
ga_elitism 1                         # number of top individuals to survive to next generation
ga_mutation_rate 0.02                # rate of gene mutation
ga_crossover_rate 0.8                # rate of crossover
ga_window_size 10                    # 
ga_cauchy_alpha 0.0                  # Alpha parameter of Cauchy distribution
ga_cauchy_beta 1.0                   # Beta parameter Cauchy distribution
set_ga                               # set the above parameters for GA or LGA
sw_max_its 300                       # iterations of Solis & Wets local search
sw_max_succ 4                        # consecutive successes before changing rho
sw_max_fail 4                        # consecutive failures before changing rho
sw_rho 1.0                           # size of local search space to sample
sw_lb_rho 0.01                       # lower bound on rho
ls_search_freq 0.06                  # probability of performing local search on individual
set_psw1                             # set the above pseudo-Solis & Wets parameters
unbound_model bound                  # state of unbound ligand
ga_run 100                           # do this many hybrid GA-LS runs
analysis                             # perform a ranked cluster analysis""" % version


# Ligand Import default options
LigandListLabel = StringVar()
LigandListLabel.set('Import ligands...')

# PrepareLigand options defaults
ChargeSet = StringVar()
ChargeSet.set("gasteiger")
Repair = StringVar()
Repair.set("")
Cleanup = StringVar()
Cleanup.set("nphs_lps")
BackboneRotatable = BooleanVar()
BackboneRotatable.set(True)
AmideRotatable = BooleanVar()
AmideRotatable.set(True) # Raccoon default (ADT=False)
GuanidiniumRotatable = BooleanVar()
GuanidiniumRotatable.set(False)
LargestFrag = BooleanVar()
LargestFrag.set(True) # Raccoon default (ADT=False)
AttachFrag = BooleanVar()
AttachFrag.set(False)
LockTors = BooleanVar()
LockTors.set(False)

LIGAND_SET = False # define if ligand filenames have been set

#### Receptor options

# default receptor structure multiplicity (one/many)
TargetPDBQT = StringVar()
RCstatus = IntVar()
RCstatus.set(0) # Initial option is "single conformation
RecFilename = StringVar()
RecFilename.set("[ none ]")

# Variables defining if either the single or the multiple receptor
# conformations have been defined
SingleReceptorSet = BooleanVar()
SingleReceptorSet.set(False)
MultiReceptorSet = BooleanVar()
MultiReceptorSet.set(False)

RecChargeSet = StringVar()
RecChargeSet.set('gasteiger')

RecCleanNPH = StringVar()
RecCleanNPH.set("_nphs")
RecCleanLP = StringVar()
RecCleanLP.set("_lps")
RecCleanWAT = StringVar()
RecCleanWAT.set("_waters")
RecCleanStdRes = BooleanVar()
RecCleanStdRes.set(False) 
RecDelAlternate = StringVar()
RecDelAlternate.set("")
RecRepairOptionsSet = StringVar()
RecRepairOptionsSet.set("add H (if missing)")

# default flexible residues (y/n)
FlexResDefined = BooleanVar()
DoFlex = IntVar()
DoFlex.set(0)
DoFlexFromWhat = IntVar()
DoFlexFromWhat.set(-1) # values are 1 for "from file" and 2 "from selection"
FlexResFileName = StringVar()
FlexResFileName.set("")
ResidueStatusLoaded = StringVar()
ResidueStatusSelected = StringVar()
ResidueStatusLoaded.set("")
ResidueStatusSelected.set("")
ResidueStatus = StringVar()
ListFlexResiduesNames = StringVar()
FlexResSelected = StringVar()


### AutoGrid options
AutoGridWhen1, AutoGridWhen2, AutoGridWhen3 = None, None, None
GPFfilename = StringVar()
GPFfilename.set("[ no GPF loaded ]")
CacheMapDirName = StringVar()
CacheMapDirName.set("[ none ]")
mapFileList = []
MapSource = IntVar()
MapSource.set(0)
CacheMapPolicy = StringVar()

CacheMapFrame, GPFframe, CacheMapHandleNow, CacheMapHandle = None, None, None, None

# values for DoCachedMaps
# 0 : no maps defined
# 1 : maps defined and checked
DoCachedMaps = BooleanVar()


# Docking menu params
dockMenuSettings = None
DPFfilename = StringVar()
DPFfilename.set("[ no DPF loaded ]")
DPFedit, DPFcontent = None, None


# Docking/DPF default settings 
DPFgroupTemplate, DPFgroupSimple, DPFgroupSmart, DPFgroupTemplate, DPFgroupComplex = None, None, None, None, None

DPF_group = None
DPF_INFO = None
InfoFrame = None
DockMenuSetting = None
DPFSpeed = IntVar()

Info = None
numGen = None
EnEval = None
simple_settings = None
simple_settings_info = None
EnEval = None
OpenDPF = None
docking_set = None
CheckTDOF = None
CheckVOL = None
complex_gen_info = None
complex_eval_info = None

# Final destination directory
JobDirectory = StringVar()
JobDirectory.set("")
JobDirectoryInfo = StringVar()
JobDirectoryInfo.set("")

# System options
TargetOS = StringVar()
TargetOS.set("lin")
LinuxScriptLevel = StringVar()
LinuxScriptLevel.set("master script for starting the VS")
PBStime = StringVar()
PBStime.set("24:00:00")
PBShowmanyruns = IntVar()
PBShowmanyruns.set(1)
TarFile = StringVar()
TarFile.set('[disabled]')
RemoveMapsAfter = BooleanVar(value = True) # Default to delete map files after the calculation

# Load session defaults
LoadLig = BooleanVar()
LoadLig.set(True)
LoadFilter = BooleanVar()
LoadFilter.set(True)
LoadRec = BooleanVar()
LoadRec.set(True)
LoadFlex = BooleanVar()
LoadFlex.set(True)
LoadMap = BooleanVar()
LoadMap.set(True)
LoadDock = BooleanVar()
LoadDock.set(True)
LoadGen = BooleanVar()
LoadGen.set(True)


# Save session defaults
SaveLig = BooleanVar()
SaveLig.set(True)
SaveFilter = BooleanVar()
SaveFilter.set(True)
SaveRec = BooleanVar()
SaveRec.set(True)
SaveFlex = BooleanVar()
SaveFlex.set(True)
SaveMap = BooleanVar()
SaveMap.set(True)
SaveDock = BooleanVar()
SaveDock.set(True)
SaveGen = BooleanVar()
SaveGen.set(True)


RecStatus = "[ not yet selected ]"

# Summary page variables
LigandSummary = StringVar()
ReceptorSummary = StringVar()
MapsSummary = StringVar()
DockingSummary = StringVar()
JobsSummary = StringVar()

LigandSummary.set(( " [ none ] "))
ReceptorSummary.set( " [ none ] " )
MapsSummary.set((" [ none ] "))
DockingSummary.set(" [ none ] ")
JobsSummary.set(" ")



# filename variables
jobs_list='jobs_list'



def get_lines(filename):
    # open a file return lines
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    return lines

def writeLines(filename, list, do_strip = True):
    # get lines, write them to a file
    output = open(filename, 'w')
    if do_strip:
        for i in list:
            output.write(i.strip())
    else:
        for i in list:
            output.write(i)
    output.close()


def InfoInit():
    global InfoMessage, InfoBar, InfoText
    # Initialize the info-bar at the bottom of the root
    InfoMessage = StringVar()
    InfoText = Label(root, textvariable = InfoMessage, font=("Helvetica", 10))
    InfoText.pack(padx = 2, pady = 2, expand='no', fill='x')
    InfoMessage.set('Welcome to Raccoon | AutoDock VS')

def raccoon():
    data = [
        "UilvYnVzdCBBKXV0b0RvY2sgQyloZW1pY2FsIEMpb21wb3VuZCBPKXJnYW5pemF0aW9uIGFuZCBPKXB0aW1pemF0aW9uIE4pb3RlYm9vaw==",
        "Uil1bm5pbmcgQSlmdGVyIEMpaGVtaWNhbCBDKWhpbWVyYXMgTyl2ZXIgTylic2N1cmUgTilpbWJp",
        "UilvbWFudGljbHkgQSlkZGljdGVkIEMpYWxjdWxhdGlvbnMgQylhcmVmdWxseSBPKWZmZXJpbmcgTylwZW5pbmcgTilvdmVsdGllcw==",
        "UilhcGlkIEEpdXRvbWF0aWMgQylyZWF0aW9uIG9mIEMpbHVzdGVycyBPKWNjYXNpb25hbGx5IE8pYnNlcnZlZCBpbiBOKWF0dXJl",
        "UilldHVybmluZyBBKWJyb3VwdGx5IGEgQyktc2hlbGwgQylvbW1hbmQgTyl1dHB1dCBPKXBlcmF0aXZlbHkgTil1bGxpZmllZA==",
        "UillZnJhaW4gQSlic3RydXNlIEMpb21tb24gQylvbXB1dGF0aW9ucyBPKWZ0ZW4gTylwZXJhdGlvbmFsbHkgTilveGlvdXM=",
        "UillbGVhc2luZyBBKWxsZWdlZGx5IEMpcml0aWNhbCBDKW9tcHJlc3Npb25zIE8pdmVya2lsbHMgTylic3RydWN0ZWQgTillZWRz",
        "Uillc3RsZXNzIEEpbmltYWwgQylyYXZpbmcgQyloZW1pY2FscyBPKXV0IE8pZiBOKW93aGVyZQ==",
        "UilldHJpZXZpbmcgQSltYXppbmcgQylvbXBvdW5kcyBPKXZlcndoZWxtcyBPKXV0Y3J5aW5nIE4pdW1iZXJz",
        "Uil1biBBKXV0b2RvY2ssIEMpaGVjayBDKWx1c3RlcnMsIE8pYnNlcnZlLCBPKXJkZXIgYW5kIE4pb2Q=",
        "UilldmVhbGluZyBBKW5vdGhlciBDKW9tcG91bmQgQylhbiBPKWNjdXIgTyliZWRpZW50bHkgTilvdw==",
        "UilhY2Nvb24gQSl1dG9tYXRlIEMpb21wdXRhdGlvbmFsIEMpaGVtaXN0cnkgTylwZXJhdGlvbnMgTyluIE4pb2Rlcw==",
        "UillbWFyY2FibGUgQSljdGlvbnMgQylvbnN0YW50bHkgQyl1dCBPKWZmIE8pYm5veGlvdXMgTillZ290aWF0aW9ucw==",
        "UillZHVuZGFudCBBKWN0aW9ucyBDKWxlYXJseSBDKWF1c2UgTyl2ZXItcHJvZHVjdGlvbiBPKWYgTilvaXNl",
        "UilldmlldyBBKWxsIEMpb25zdGFudHMsIEMpaGVjayBPKXV0IE8pcHByZXNzZWQgTil1bWJlcnM=",
        "UillbWVtYmVyOiBBKW55IEMpb25jZXB0IEMpb3VsZCBPKXV0c3RhbmQuLi4gTylyIE4pb3Q="
        ]
    return "\n"+b64decode(data[choice(range(0, len(data)))])+"\n"



def about():  

    #global LOGO_BASE64
    GNU="""       This program is free software: you can redistribute it and/or modify
       it under the terms of the GNU General Public License as published by
       the Free Software Foundation, either version 3 of the License, or
       (at your option) any later version."""


    ICON_LICENSE = """Some of the icons are from the following icon packs:
            - Candy icons http://launchpad.net/candyproject 
            - default Gnome icons http://www.gnome.org/"""



    logo = StringVar()
    logo.set("""          ________________________________________________________________ 

    __________//___________________________/////___________________/____________  
    _________/__/__________________________/____/__________________/____________  
    ________/____/___________/_____________/_____/_________________/____________  
    ________/____/__/_____/_/////___/////__/_____/__/////___/////__/___/________  
    _______/______/_/_____/__/_____/_____/_/_____/_/_____/_/_____/_/_//_________  
    _______////////_/_____/__/_____/_____/_/_____/_/_____/_/_______//_/_________  
    _______/______/_/____//__/___/_/_____/_/____/__/_____/_/_____/_/___/________  
    _______/______/__////_/___///___/////__/////____/////___/////__/____/_______  
 
          ________________________________________________________________
                                        ______ 
                                       /      \\ 
                                      /        \\ 
                                     /          \\  
                                     \\    /\\    / 
                                      \\  /  \\  / 
                                       \\/ /\\ \\/ 
                                        /\\  \\ 
                                      /\\  \\__\\ 
                                     /  \\__\\ 
                                    /____\\

                        ______________________________________ 
                       |                                      |
                       |         Raccoon | AutoDock VS        |
                       |            version %4s             |
                       |              (c) 2011                |
                       |    The Scripps Research Institute    |
                       |                                      |
                       |          Stefano Forli, TSRI         |
                       |            Ruth Huey, TSRI           |
                       |          Arthur Olson, TSRI          |
                       |______________________________________|
                       """ % (version) )
                       


    AboutWin = Toplevel(root)
    AboutWin.transient(root)
    #print type(LOGO_BASE64)

    AboutWin.bind("<Button-3>", lambda x : help("help"))
    AboutWin.title("About Raccoon | AutoDockVS")
    AboutWin.winfo_toplevel().resizable(NO,NO)
    Label(AboutWin, textvar = logo, font = (courier, courier_size, ), justify = LEFT ).pack()
    Label(AboutWin, text = " "+raccoon()+" ", justify = LEFT, font = ('Courier', 10, 'bold')).pack()
    Frame(AboutWin, height = 2, bd = 1, relief = SUNKEN).pack(fill = X, padx = 5 , pady = 3)
    Label(AboutWin, text = GNU, font = ('Helvetica', 9, 'roman')).pack()
    Frame(AboutWin, height = 2, bd = 1, relief = SUNKEN).pack(fill = X, padx = 5 , pady = 3)
#    Label(AboutWin, text = "Manual pages and version updates could be *potentially* found at this address:", font = ('Helvetica', 9, 'roman')).pack()
#    Label(AboutWin, text = "http://www.scripps.edu/~forli/").pack(padx = 5)
    #Label(AboutWin, text = "LICENCE").pack(padx = 5)
    Label(AboutWin, text = ICON_LICENSE, font = ('Helvetica', 9, 'roman'),justify = LEFT).pack()
    Button(AboutWin, height = 2, text = "Close", command = lambda: AboutWin.destroy()).pack(fill = X,
            padx = 15, pady = 3, anchor = S, side = BOTTOM )

    Logo = Canvas(AboutWin, width =360, height=73)
    logo_img = Tkinter.PhotoImage(master=root, data=LOGO_BASE64)
    Logo.create_image(170,35, image=logo_img, anchor=CENTER)
    Logo.pack(anchor=S, side = BOTTOM) 

    return


def help(topic):
    global HelpWin
    
    help_database = { 
    # ligands tab
        'loadlig' : ["Add ligands...", 
"Allows to import ligands by manually selecting them.\n\n\
A single ligand can be selected by clicking on the file browser.\n\n\
Multiple ligands can be selected by Ctrl-clicking. \
Ranges can be specified by Shift-clicking.\n\n\
Non-PDBQT files are converted automatically to PDBQT\n\
Multi-structure MOL2 files can be splitted automatically.\n\n\
Imported ligands are filtered with the current filter set.\n\n\
Supported file types : PDB, PDBQT, MOL2.\n"],

        'loadligdir' : ["Add a directory...",
"Allows to import ligands by scanning a directory.\n\n\
Multi-structure MOL2 files can be splitted automatically.\n\n\
Non-PDBQT files are converted automatically to PDBQT\n\
Imported ligands are filtered with the current filter set.\n\n\
A report window will show all supported files found (PDB, PDBQT, MOL2) and user can specify which types can be imported."],


        'loadligrecursive' : ["Add recursively..",
"Allows to import ligands by scanning a directory and all its sub-directories.\n\n\
Multi-structure MOL2 files can be splitted automatically.\n\n\
Non-PDBQT files are converted automatically to PDBQT\n\
Imported ligands are filtered with the current filter set.\n\n\
A report window will show all supported files found (PDB, PDBQT, MOL2) and user can specify which types can be imported."],

        'delsellig' : ["Remove selected",
"Remove selected ligands from the ligand list.\n\
It can be used to pick which ligands will be removed from the list. Multiple ligands can be selected by Ctrl-clicking. \
Ranges can be specified by Shift-clicking.\n\n "],

        'delalllig' : ["Remove all",
"Remove all the ligands and empty the ligand list."],

        'filterlig' : ["Filter ligands...",
"Ligand filtering options management.\nAllows to set the ligand property filters that are applied to the ligand set."],

        'ligpdbqtopt' : ["PDBQT generation options",
"Allows to set the parameters and the options used in the generation of the PDBQT files.\n\n\
NOTE: changes will be applied only to newly imported files."],

        'ligscroll' : [ "Ligand list", 
"Contains all the ligands loaded in the current session.\n\n\
Ligands that do not pass the filtering procedure are marked in red.\n\
Items can be selected and deleted by using the [Remove selected] button on the toobar.\n\
Multiple ligands can be selected by Ctrl-clicking. \
Ranges can be specified by Shift-clicking.\
        "],

        'keyword'      : ["title", "text"],
        'help'      : ["About?", #"...seriously?\n\nRequesting help about the \"about\"?\nWell, find yourself a towel.\n\
"    __ __       ___     \n   /\\ \\\\ \\    /'___`\\  \n   \\ \\ \\\\ \\  /\\_\\ /\\ \\  \n    \\ \\ \\\\ \\_\\/_/// /__ \n     \\ \\__ ,__\\ // /_\\ \\   \n      \\/_/\\_\\_//\\______/ \n         \\/_/  \\/_____/  \n\
       "],
#
#
#"       :::     ::::::::  \n      :+:     :+:    :+: \n     +:+ +:+        +:+  \n    +#+  +:+      +#+    \n   +#+#+#+#+#+  +#+      \n         #+#   #+#      \n         ###  ##########  \n\n\"



    # receptor tab
        'recmode' : ["Single target/Multiple targets", 
"Set the target mode to a single structure or to multiple targets.\n\
Multiple targets can be several conformations of the receptor or different variant/mutants, but also completely \
unrelated targets could be used.\n\n\
NOTE: In any case, all target structures *MUST* be aligned and covered by the grid box specified.\n\
Supported file types : PDB, PDBQT, MOL2.\n"],

        'flexres'      : ["Flexible residues panel", "Activate flexible residues during docking.\n\n\
Flexible residues can be specified in two ways:\n\
    -from file     \t: a pre-generated PDBQT file is used (single-rec only)\n\
    -from selection\t: specified flexible residue(s) will be generated on the fly from the receptor structure.\n\
\nResidue selections can be specified with the syntax \"CHAIN:RESnn\":\n\n\
  THR276 \t\t\t threonine 276 in all chains will be made flexible.\n\
  B:THR276 \t\t threonine 276 in chain B will be made flexible.\n\
  B:THR276,B:HIS229 \t multiple residues can be specified by separating them with commas.\n\n\
If the selected residues are not present in the currently defined receptor(s), mismatching residues are prompted.\
  "],

        'recpdbqtopt' : ["PDBQT generation options", "Allows to set the parameters and the options used in the generation of the PDBQT files.\n\n\
NOTE: changes will be applied only to newly imported files."] ,




        'loadsinglerec' : ["Add receptor file...",
"Set the receptor file on which dockings will be performed.\n\
Non-PDBQT files are converted automatically to PDBQT\n\n\
Supported file types : PDB, PDBQT, MOL2.\n"],
    

        'loadrec'      : ["Add a structure...", 
"Import a receptor structure file in the list of targets.\n\n\
Multiple files can be selected by Ctrl-clicking. \
Ranges can be specified by Shift-clicking.\n\n\
Non-PDBQT files are converted automatically to PDBQT\n\
Supported file types : PDB, PDBQT, MOL2.\n"],

        'loadrecdir' : ["Add a directory...",
"Allows to import ligands by scanning a directory.\n\n\
Multi-structure MOL2 files can be splitted automatically.\n\n\
Non-PDBQT files are converted automatically to PDBQT\n\
Imported ligands are filtered with the current filter set.\n\n\
A report window will show all supported files found (PDB, PDBQT, MOL2) and user can specify which types can be imported."],


        'delselrec' : ["Remove selected",
"It can be used to pick which structures will be removed from the list. Multiple items can be selected by Ctrl-clicking. \
Ranges can be specified by Shift-clicking.\n\n "],

        'delallrec' : ["Remove all",
"Remove all the structures and empty the target list."],



}

    #tkMessageBox.showinfo("Help", help_database[topic])

    try:
        #content.config(text =help_database[topic] ) 
        HelpWin.lift()
    except:
        HelpWin = Toplevel(root)
        HelpWin.transient(root)
        
        HelpWin.title("HELP => "+help_database[topic][0])
        HelpWin.winfo_toplevel().resizable(NO,NO)
        if not topic == 'help':
            content = Message(master = HelpWin, relief = GROOVE, bg = 'white', text = help_database[topic][1], width = 500)
        else:
            content = Message(master = HelpWin, relief = GROOVE, bg = 'white', font = ('Courier', 10, 'bold'), 
            text = help_database[topic][1], width = 500)
            
        content.pack(padx=10, pady=10)
        Button(master = HelpWin, text = "OK", command = lambda : HelpWin.destroy(), width = 20 ).pack(pady = 5)


def makemenu(win):
    top = Menu(win)       
    win.config(menu=top)
    
    file = Menu(top, tearoff=0)
    file.add_command(label='Load VS configuration...',command=LoadLogWindow, underline=0)
    file.add_command(label='Save VS configuration...',command=SaveLogWindow, underline=0)
    file.add_separator()
    file.add_command(label='Import ligand list file...',command=ImportLigList, underline=0)
    file.add_command(label='Export ligand list file...',command=ExportLigList, underline=0)
    file.add_separator()
    file.add_command(label='Quit', command=confirm, underline=0)
    top.add_cascade(label='File', menu=file, underline=0)

    setup = Menu(top, tearoff=0)
    #setup.add_command(label='Split multi-MOL2', command=SplitMol2, underline=0)
    setup.add_command(label='Split multi-MOL2', command=SplitMol2Interface, underline=0)

    top.add_cascade(label='Utilities', menu=setup, underline=0)

    help = Menu(top, tearoff=0)
    help.add_command(label='About Raccoon', command=about, underline=0)
    top.add_cascade(label='Help', menu=help, underline=0)

def LoadLogWindow(logname = None):
    def Done():
        LoadOptWin.destroy()
        ext = os.path.splitext(logname)[1]
        if ext == "log":
            LoadLog(logname)
        else:
            LoadSession(logname)

    DisableInterface()
    if not logname:
        logname = askopenfilename(parent = root, title = "Select a Raccoon session file to load...", filetypes=[("Raccoon Session File", "*.rsf"), ("old Raccoon 1.0 Log file", "*.log"), ("Any file...", ("*"))])
    if not logname:
        EnableInterface()
        return False
    DisableInterface()
    LoadOptWin = Toplevel(root)
    LoadOptWin.transient(root)
    LoadOptWin.title("Load session")
    LoadOptWin.winfo_toplevel().resizable(NO,NO)
    Label(LoadOptWin, text = "Select data to import:", justify = LEFT).grid(row = 1, column = 0, columnspan = 3, sticky = N, padx = 5, pady = 15)
    l_frame = Pmw.Group(LoadOptWin, tag_text = "Ligands")
    Label(l_frame.interior(), text = "                                        ").grid(row = 2, column = 0, sticky = W) # Tk sucks: workaround...
    Checkbutton(l_frame.interior(), text = "Ligands list", variable = LoadLig).grid(row = 2, column = 0, columnspan = 1, sticky = W)
    Checkbutton(l_frame.interior(), text = "Filter set", variable = LoadFilter).grid(row = 3, column = 0, columnspan = 1, sticky = W)
    l_frame.grid(row = 3, column = 0, columnspan = 3, sticky = W+E, padx = 5, pady = 5)

    r_frame = Pmw.Group(LoadOptWin, tag_text = "Target")
    Label(r_frame.interior(), text = "                                        ").grid(row = 4, column = 0, sticky = W) # Tk sucks: workaround...
    Checkbutton(r_frame.interior(), text = "Receptors list", variable = LoadRec).grid(row = 4, column = 0, columnspan = 1, sticky = W)
    Checkbutton(r_frame.interior(), text = "Flexible residues", variable = LoadFlex).grid(row = 5, column = 0, columnspan = 1, sticky = W)
    r_frame.grid(row = 4, column = 0, columnspan = 3, sticky = W+E, padx = 5, pady = 5)
    
    p_frame = Pmw.Group(LoadOptWin, tag_text = "Parameters")
    Label(p_frame.interior(), text = "                                        ").grid(row = 6, column = 0, sticky = W) # Tk sucks: workaround...
    Checkbutton(p_frame.interior(), text = "Map parameters", variable = LoadMap).grid(row = 6, column = 0, columnspan = 1, sticky = W)
    Checkbutton(p_frame.interior(), text = "Docking parameters", variable = LoadDock).grid(row = 7, column = 0, columnspan = 1, sticky = W)
    p_frame.grid(row = 5, column = 0, columnspan = 3, sticky = W+E, padx = 5, pady = 5)
    Button(LoadOptWin, text = "OK", command = Done).grid(row = 10, column = 1, columnspan = 1, sticky = W, padx = 10, pady= 10)
    Button(LoadOptWin, text = "Cancel", command = lambda: LoadOptWin.destroy()).grid(row = 10, column = 2, sticky = W, padx = 10, pady= 10)
    EnableInterface()

def LoadSession(file):
    pass

def LoadLog(logname):
    # DEBUG = True
    if LoadLig.get() + LoadRec.get() + LoadFlex.get() + LoadMap.get() + LoadDock.get() + LoadGen.get() + LoadFilter.get() == 0:
            return
    logfile = get_lines(logname)
    # Check that is an original Raccoon(TM) LogFile(TM)
    # with an advanced and sofisticated text scanning...
    raccoon, virtual, screening = False, False, False
    for line in logfile:
        if "Raccoon" in line:
            raccoon = True
        if "Virtual" in line:
            virtual = True
        if "Screening" in line:
            screning = True
    if raccoon:
        if virtual:
            if screening:
                pass
    else:
        tkMessageBox.showerror("Error!", ("The loaded file is not a Raccoon VS file"))
        return False
    if DEBUG: print logfile[-1]

    ################################
    # Start importing all the params
    ################################

    # Load the filters
    if LoadFilter.get():
        try:
            for index in range(38, 44):
                logfile[index] = logfile[index].rsplit() # clean up the line from space and \n's
                if DEBUG: print "LOAD_SESSION: filter params => ", logfile[index]
            # Hb donor max-min
            HbDmin.set(int(logfile[38][-3])), HbDmax.set(int(logfile[38][-1]))
            # Hb acceptor max-min
            HbAmin.set(int(logfile[39][-3])), HbAmax.set(int(logfile[39][-1]))
            # MW max-min
            MWmin.set(int(logfile[40][-3])), MWmax.set(int(logfile[40][-1]))
            # Nat max-min
            NatMin.set(int(logfile[41][-3])), NatMax.set(int(logfile[41][-1]))
            # TORSDOF max-min
            TORSDOFmin.set(int(logfile[42][-3])), TORSDOFmax.set(int(logfile[42][-1]))
            # Filter non-AD atom types
            if logfile[43][-1] == "True":
                DoRejectATypes.set(True)
            else:
                DoRejectATypes.set(False)
        except:
            tkMessageBox.showerror("Error!", ("Problems loading the filter settings."))
            if (tkMessageBox.askokcancel("Warning", ("Error while loading the filter settings.\nSkip loading filters and continue loading the log file?") == 0 )):
                return False
    
    if LoadRec.get():
        # Load the target structure
        receptor_list = []
        try:
            for line in logfile:
                if line[0:7] == "TARGET>":
                    filename = line.split("TARGET>")[-1]
                    filename = filename.strip()
                    receptor_list.append(filename)
                    if DEBUG: print "LOAD_SESSION> found receptor: |%s|" % receptor_list[0]
        except:
            tkMessageBox.showerror("Error!", ("Unable to load the receptor structure(s)."))
            return False
        if len(receptor_list) > 1:
            RCstatus.set(1)
            ReceptorOptions()
            try:
                openReceptor(receptor_list)
            except:
                if (tkMessageBox.askokcancel("Warning", ("Error while loading the receptor structures.\nSkip receptor loading and continue loading the log file?") == 0 )):
                    return False

        elif len(receptor_list) == 1:
            RCstatus.set(0)
            ReceptorOptions()
            try:
                openSingleReceptor(receptor_list[0]) 
            except:
                if (tkMessageBox.askokcancel("Warning", (("Error while loading the receptor structure:\n %s\n\nSkip receptor loading and continue loading the log file?") % receptor_list[0]))) == 0:
                    return False

    # Load flexible residues info        
    if LoadFlex.get():
        try:
            for line in logfile:
                if line[0:5] == "FLEX>":
                    DoFlex.set(1)
                    SetFlexibleMode() 
                    # loaded from file
                    if "file" in line:
                        if DEBUG: print "LOAD_SESSION: got flex from file", line.split(":", 1)[1][:-1].split("\t")[1]
                        DoFlexFromWhat.set(1)
                        SetFlexibleResidueFile(line.split(":", 1)[1][:-1].split("\t")[1])
                        break

                    # generated from selection
                    if "selection" in line:
                        if DEBUG: print "LOAD_SESSION: got flex from selection", line.split(":", 1)[1][:-1]
                        DoFlexFromWhat.set(2)
                        ListFlexResiduesNames.set(line.split(":", 1)[1][:-1])
                        ParseFlexSelection()
                        break
        except:
            tkMessageBox.showwarning("Flexible residues", ("There is a problem in reading the flexible residues information."))

    # Load the GPF setup
    defer_map_check = False
    if LoadMap.get():
        # identify the grid mode
        mode = ""
        for line in logfile:
            if "Grid mode :" in line:
                mode = line.split(":")[1]
            #if "Grid param file template :" in line:
            #    GPFParameterFile.set(line.split(":")[1].strip())

        if DEBUG: print "LOAD_SESSION> the grid mode is |%s|"% mode
        if "calculated in each job" in mode:
            if DEBUG :print "    applying map mode 0"
            MapMenu()
            AutoGridWhen1.invoke() 
        if "calculated now" in mode:
            if DEBUG: print "    applying map mode 1"
            MapMenu()
            if not system == "Windows":
                AutoGridWhen2.invoke() 
            else:
                AutoGridWhen1.invoke()
        if "use pre-calculated" in mode:
            if DEBUG: print "    applying map mode 2 ( deferring map check)"
            defer_map_check = True
    
        # Cached maps policy
        if MapSource.get() >= 1 or defer_map_check:
            if ">copied<" in mode:
                CacheMapPolicy.set("Make copies [ use more disk space ]")
                if DEBUG: print "    set map policy to COPIES"
            if ">linked<" in mode:
                CacheMapPolicy.set("Make symbolic links [ save disk space ]")
                if DEBUG: print "    set map policy to LINKS"
    
        # load GPF if needed
        if MapSource.get() <= 1:
            GPFcontent.config(state = NORMAL)
            GPFcontent.delete(1.0, END) 
            for line in logfile:
                if line[0:4] == "GPF>":
                    line = line.split('GPF>\t')[1]
                    GPFcontent.insert(END, line)
                    GPFfilename.set((" Grid parms from %s " % logname))
            GPFcontent.config(state = DISABLED)
            GPFedit.config(state = ACTIVE)
            setGPFtags()

        # get the autogrid binary specified if needed
        if MapSource.get() == 1:
            for line in logfile:
                if "AutoGrid binary file" in line:
                    line = line.split("|")
                    if not line[1] == "":
                        if not GetAutoGrid(line[1]):
                            if not (tkMessageBox.askokcancel("Warning", ("Unable to find the AutoGrid binary file specified\
in the log:\n\n%s\n\nSkip the binary specification and continue or cancel log loading?" % line[1]) == 0 )):
                                return False
    if LoadDock.get():
        # Load the DPF setup
    
        # identify the docking mode
        for line in logfile:
            if "Docking mode :" in line:
                line = line.split(">")[1]
                mode = line.split("<")[0]
                break
    
        if mode == "generated from template" in mode:
            docking_set.set("From template...")
            docking_setup_interface(None)
            DPFcontent.config(state = NORMAL)
            DPFcontent.delete(1.0, END) 
            for line in logfile:
                if line[0:4] == "DPF>":
                    line = line.split('DPF>\t')[1]
                    DPFcontent.insert(END, line)
                    DPFfilename.set((" Docking parms from %s " % logname))
            DPFcontent.config(state = DISABLED)
            DPFedit.config(state = ACTIVE)
            setDPFtags()

                    # Add a check for parameter files specified here...
    
    if LoadLig.get():
        # Load the ligands
        ligand_list = []
        for line in logfile:
            if line[0:7] == "LIGAND>":
                line = line.rsplit("\n", 1)[0]
                ligand_list.append(line.split("LIGAND> ")[1])
        if len(ligand_list) >= 1:
            openLigand(ligand_list)

        # define the cached maps dir and test them (it needs to be done *after* ligands
        # have been imported to check if maps are missing)
        if defer_map_check:
            MapMenu()
            for line in logfile:
                if "Grid cache dir" in line:
                    cache_dir = line.split("   Grid cache dir : ")[1][:-1]
                    if DEBUG :
                        print "    (Deferred map checking)    found cache dir : |%s|"% cache_dir
                        print "    List of map files:"
                        print glob.glob(os.path.join(cache_dir, "*map*"))
                    opendirMaps(cache_dir)
            AutoGridWhen3.invoke() 
    JobDirectory.set("")
    JobDirectoryInfo.set("")
    InfoMessage.set("Log file loaded successfully")
    TheCheck()


def SaveLogWindow():
    DisableInterface()

    def Done():
        SaveOptWin.destroy()
        print "SUCKS"
        SaveLog(logname)
        return True

    keepasking = True
    while keepasking:
        logname = asksaveasfilename(parent = root, title = "Select the Raccoon log filename to save...", filetypes = [('Raccoon log file', '*.log'), ("Any file...", "*")] ,  defaultextension=".log") 
        if logname:
            if DEBUG: print "here I should save the file log..."
            InitializeLog(None, logname)
            EnableInterface()
            break
            #return True
        else:
            EnableInterface()
            return False

    DisableInterface()
    SaveOptWin = Toplevel(root)
    SaveOptWin.transient(root)
    SaveOptWin.title("SAVE session")
    SaveOptWin.winfo_toplevel().resizable(NO,NO)
    Label(SaveOptWin, text = "Select data to be saved in the file:", justify = LEFT).grid(row = 1, column = 0, columnspan = 3, sticky = N, padx = 5, pady = 5)
    Checkbutton(SaveOptWin, text = "Ligands list", variable = SaveLig).grid(row = 2, column = 1, columnspan = 2, sticky = W)
    Checkbutton(SaveOptWin, text = "Ligand filters", variable = SaveFilter).grid(row = 3, column = 1, columnspan = 2, sticky = W)
    Checkbutton(SaveOptWin, text = "Receptors list", variable = SaveRec).grid(row = 4, column = 1, columnspan = 2, sticky = W)
    Checkbutton(SaveOptWin, text = "Flexible residues", variable = SaveFlex).grid(row = 5, column = 1, columnspan = 2, sticky = W, padx = 15)
    Checkbutton(SaveOptWin, text = "Map parameters", variable = SaveMap).grid(row = 6, column = 1, columnspan = 2, sticky = W)
    Checkbutton(SaveOptWin, text = "Docking parameters", variable = SaveDock).grid(row = 7, column = 1, columnspan = 2, sticky = W)
    Checkbutton(SaveOptWin, text = "Generation options", variable = SaveGen).grid(row = 8, column = 1, columnspan = 2, sticky = W)
    Button(SaveOptWin, text = "OK", command = Done).grid(row = 9, column = 1, columnspan = 1, sticky = W, padx = 10, pady= 10)
    Button(SaveOptWin, text = "Cancel", command = lambda: SaveOptWin.destroy()).grid(row = 9, column = 2, sticky = W, padx = 10, pady= 10)
    EnableInterface()



def SaveLog(file):
    # TODO incomplete
    # initialize the log
    # line = date()
    buffer = []
    buffer.append("# Raccoon VS generator v.%s log file " % version)

    if SaveFilter.get():
        # hbd
        buffer.append( "FILTER_HBD> %d,%d" % (HbDmin.get(), HbDmax.get() ) )
        # hba
        buffer.append( "FILTER_HBA> %d,%d" % (HbAmin.get(), HbAmax.get() ) )
        # mol weight
        buffer.append( "FILTER_MW> %d,%d" % ( MWmin.get(), MWmax.get() ) )
        # N.atoms
        buffer.append( "FILTER_NAT> %d,%d" % ( NatMin.get(), NatMax.get()) )
        # TORSDOF
        buffer.append( "FILTER_TOR> %d,%d" % ( TORSDOFmin.get(), TORSDOFmax.get()) )
        # filter AD types
        buffer.append( "FILTER_ATYPE> %d" % ( int(DoRejectATypes.get()) ) )

    if SaveRec.get():
        if RCstatus.get() == 0:
            receptor_list = [ RecFilename.get() ]
        else:
            receptor_list = receptorScrolledListBox.get('0', END)
        for r in receptor_list:
            buffer.append( "TARGET> %s" % (r) ) 

    if SaveFlex.get():
        pass

    if SaveMap.get():
        pass

    if SaveDock.get():
        pass

    if SaveGen.get():
        pass

    if SaveLig.get():
        pass # ligand


    try:
        fp = open(file, 'w')
        fp.writelines(buffer)
        fp.close()
        return True

    except:
        if DEBUG: print "SaveLog> problems saving session file %s [ %s ] " % (file, err.getwhatever)
        return False



def SetJobDirectory(dir = None): 
    """General opendir function useful for setting 
    the finaloutput dir
    """
    dir_accepted = False
    if dir:
        DirName = dir
    else:
        while not dir_accepted:
            DirName = askdirectory()
            if DirName:
                try:
                    if os.path.exists(DirName):
                        if len(glob.glob(os.path.join(DirName, "*"))):
                            #if tkMessageBox.askyesno('Output directory','The selected directory is not empty.\nAre you sure you want to use it?'):
                            #    dir_accepted = True
                            tkMessageBox.showerror("Output directory", 'The selected directory contains some files but an empty directory is required to generate the VS jobs:\n\n - specify another directory\n - type a new name to create one.' )
                        else:
                            dir_accepted = True
                    else:
                        if tkMessageBox.askokcancel('Output directory','The selected directory doesn\'t exist.\nDo you want to create it?'):
                            os.makedirs(DirName, 0755)
                            dir_accepted = True
                    if dir_accepted:
                        JobDirectory.set(DirName)
                        JobDirectoryInfo.set(CheckDiskSpace(DirName))
                        TheCheck()
                        return
                except:
                    tkMessageBox.showerror("Error!", ("The directory:\n%s\n is not accessible" % DirName))
                    JobDirectory.set("")
                    JobDirectoryInfo.set("")
                    TheCheck()
                    return
            else:
                TheCheck()
                return


def CheckDiskSpace(path):
    print "\n\n\n\n\n\n#########################\n WARNING EXPERIMENTAL FEATURE ON WINDOWS \n\n################################\n\n\n"
    #DEBUG = True
    # TODO fix the win issue 

    # TODO TO BE TESTED!!!
    """
    import ctypes

    if free_bytes.value == 0:
       print 'dont panic'
    """



    if system == "Windows": # Warning: cover your eyes 'cause this workaround is extremely ugly (...but it works)
        # TODO  this is a buggy version! TO BE FIXED
        if DEBUG: print "CHECKDISKSPACE> this is path", path
        free_bytes = ctypes.c_ulonglong(0)
        ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(u'c:\\'), None, None, ctypes.pointer(free_bytes))
        """
        dir_list = "dir \"%s\"" % path
        command = os.popen2(dir_list)
        output = command[1].readlines()
        if DEBUG: print "CHECKDISKSPACE> output", output
        diskspace = output[-1].split()[-3]
        if DEBUG: print "CHECKDISKSPACE> diskspace", diskspace
        #available = str(diskspace.replace(".", "")) # total bytes (for EU support)
        #available = str(diskspace.replace(",", "")) # total bytes (for USA support)
        available = ""
        for c in diskspace:
            if c.isdigit():
                available += c
        """
        available = free_bytes.value
        try:
            available = float(available)
        except:
            if DEBUG:
                print "CHECKDISKSPACE [%s] > there was an issue with the disk space" % system
                print "CHECKDISKSPACE [%s] > available = %s" % (system, available)
            return "[ WARNING: disk space not available ]"

    elif system == "Linux" or system == "Darwin":
        disk = os.statvfs(path)
        capacity = disk.f_bsize * disk.f_blocks
        available = disk.f_bsize * disk.f_bavail
        used = disk.f_bsize * (disk.f_blocks - disk.f_bavail)
    else:
        return "[ Warning: disk space not available ]"

    if DEBUG: print "CHECKDISKSPACE> System = %s, Diskspace = %12.3f " % ( system, available)

    if available > 1073741824:
        unit = " Gb"
        factor = 1073741824
    else:
        unit = " Mb"
        factor = 1048576

    calculated_space = "%5.2f" % (float(available)/float(factor))
    if DEBUG: print "Calculated disk space: ", calculated_space
    available_space = "[ "+str(calculated_space)+unit+" available disk space ]" 
    return available_space

#########################################################################################################
#########################################################################################################
#########################################################################################################
#########################################################################################################
#########################################################################################################
#### Ligand (p1) functions #####

def countLigands(): 
    verbose = False
    if verbose or DEBUG: print "countLigands> this would be the dictionary lenght:", len(LigandDictionary)

    # If there are no ligands just return
    if len(LigandDictionary) < 1:
        LigandListLabel.set('Import ligands...')
        AutoGridWhen3.config(state = DISABLED)
        AutoGridWhen1.invoke()
        TotalAcceptedLigands.set(0)
        return

    # start counting...
    ligand_conscription = 0
    for item in LigandDictionary.keys():
        if LigandDictionary[item]["accepted"]:
            ligand_conscription += 1

    # choices
    if ligand_conscription < 1:
        tag = " Ligands accepted : %s / %s " % ( str(ligand_conscription), str(len(LigandDictionary)))
        LigandListLabel.set(tag)
        # Color the label by red...
        AutoGridWhen3.config(state = DISABLED)
        AutoGridWhen1.invoke()
    else:
        tag = " Ligands accepted : %s / %s " % ( str(ligand_conscription), str(len(LigandDictionary)))
        LigandListLabel.set(tag)
        if RCstatus.get() == 0:
            if SingleReceptorSet.get():
                AutoGridWhen3.config(state = NORMAL)
        if RCstatus.get() == 1:
            AutoGridWhen3.config(state = NORMAL)

    if ligand_conscription > 1500:
        sub_splitting.set("find 1000 molecules")
        if DEBUG: print "countLigands> sub-splitting set to :", sub_splitting.get()
    return

def makeDir(path, name = "out_dir"):
    out_dir = path+os.sep+name
    try:
        if not os.path.exists(out_dir):
            os.makedirs(out_dir, 0755)
            if DEBUG: print "makeDir> the directory \"%s\" doesn't exist, creating" % out_dir
        else:
            if DEBUG: print "makeDir> the directory \"%s\" exist, passing..." % out_dir
        return out_dir
    except:
        if DEBUG: print "makeDir> Error in creating the directory : ", out_dir
        return False

def openLigand(ligFile = None, quiet = False): # Now unified loader for all the supported formats
    # The input is a list

    # by default it creates a directory called "pdbqt" where the PDBQt file is generated (new)

    got_some = False
    problematic_list = []
    if not ligFile:
        ligFile = askopenfilename(parent = root, title = "Select one or more PDBQT, PDB or (multi)MOL2", filetypes=[("Supported ligand formats", ("*.pdbqt", "*.mol2", "*.pdb" )), ("PDBQT", "*.pdbqt"), ("PDB", "*.pdb"), ("Mol2", "*.mol2"), ("Any file type...", "*")], multiple = 1)
    if ligFile:
        # now any filter can be applied in the openfilename interface ("*" included)
        pdb_list, pdbqt_list, mol2_list = [], [], []
        for file in ligFile:
            basename, ext = os.path.splitext(file) #.split(".")[-1]
            if ext == ".pdb": pdb_list.append(file)
            if ext == ".pdbqt": pdbqt_list.append(file)
            if ext == ".mol2": mol2_list.append(file)
            if DEBUG:
                print "openLigand> found files:"
                print "\t %d pdb" % len(pdb_list)
                print "\t %d pdbqt" % len(pdb_list)
                print "\t %d mol2" % len(pdb_list)
                
        # PDBQT
        if pdbqt_list:
            list_of_accepted, problematic = checkPDBQTligList(pdbqt_list)
            if list_of_accepted:
                got_some = True
                gc.disable()
                for ligand in list_of_accepted:
                    LigandRegistration(ligand)        
                gc.enable()
            if problematic:
                problematic_list += problematic
        # PDB
        for filename in pdb_list:
            dirname = os.path.dirname(filename)
            name, ext = os.path.splitext( os.path.basename(filename) )
            pdbqt_dir = makeDir(dirname, "pdbqt")
            if pdbqt_dir:
                output_file = pdbqt_dir + os.sep + name + ".pdbqt" # path/filename.pdbqt
                if genPDBQT(filename, output_file):
                    got_some = True
                    LigandRegistration(output_file)
                else:
                    problematic_list.append([filename, "problem in generating PDBQT"])
                    #tkMessageBox.showwarning("PDB Error", ("There is a problem in the input, please check the ligand:\n%s" % filename ))
                    #break
            else:
                problematic_list.append([filename, ("problem in generating PDBQT (dir creation: %s)" % dirname+os.sep+"pdbqt" )])
                
        # MOL2
        for filename in mol2_list:
            openMultiMol2(filename)


    # Ligands will be filtered every time (at least because of the TDOF)
    if got_some:
        InfoMessage.set( "Ligands imported successfully.")
    if problematic_list:
        pass
        # HIC SUNT LEONES FOR THE PAPER
        # TODO TODO
        
    FilterLigands(True)
    countLigands()
    # Re-check map cache folder if is defined
    if mapDir and MapSource.get() == 2:
        openDirMaps(mapDir)
    TheCheck()

def importPDBQT():
    pass
def importPDB():
    pass
def importMol2():
    pass


def openMultiMol2(ligFile = None, quiet = False):
    # -import both single- and multi-MOL2
    # -accept both input file or none
    # -check for the number of molecules in the MOL2
    # -find a suitable place for splitting the molecules
    # -convert them
    # -add them to the list
    #
    # TODO WARNING! quiet mode disabled!!

    if not ligFile: 
        ligFile = askopenfilename(parent = root, title = "Select a Mol2...", filetypes=[("Mol2", "*.mol2", "MOL2")])
    if ligFile:
        problematic_list = []
        count_mols = CheckMultiMol2(ligFile)
        if not count_mols and not quiet:
            tkMessageBox.showwarning("Mol2 Error", ("%s doesn't contain any Mol2 structures." % ligFile))
        if count_mols == 1: # it's a single Mol2
            dirname = os.path.dirname(ligFile)
            name, ext = os.path.splitext( os.path.basename(ligFile) )
            pdbqt_dir = makeDir(dirname, "pdbqt")
            if pdbqt_dir:
                output_file = pdbqt_dir + os.sep + name + ".pdbqt" # path/filename.pdbqt
                if genPDBQT(ligFile, output_file):
                    LigandRegistration(output_file)
                else:
                    #tkMessageBox.showerror("Error!", ("Problems converting the MOL2: %s" % ligFile))
                    return [ligFile]
            else:
                return [ligFile]

        elif count_mols > 1: # it's a multiMol2
            if count_mols >= 100:
                WARNING = "\n\n[ Warning: this may take some time ]"
            else:
                WARNING = ""
            if not quiet:
               if not tkMessageBox.askokcancel('Multi-structure MOL2 file',('A multi-structure file MOL2 containing %d ligands was found.\
Proceed to split and convert it to PDBQT?%s' % (count_mols, WARNING))):
                    return

            # here we should call the interface...
            # TODO TODO WARNING!  TODO TODO EXPERIMENTAL!! TODO TODO EXPERIMENTAL!!!!
            SplitMol2Interface ( import_result = True, input_filename = ligFile)
            if mapDir and MapSource.get() == 2:
                openDirMaps(mapDir)
            """
                output_dir = askdirectory(parent = root, title = ("MOL2: Split and convert %d molecules in the following dir..."% count_mols) , initialdir = os.path.dirname(ligFile))
                if not output_dir:
                    tkMessageBox.showinfo(title="MOL2 splitting", message =( "The splitting process of %s has been cancelled by the user" % ligFile))
                    return
            else:
                output_dir = os.path.dirname(ligFile)
            
            name = os.path.basename(ligFile)[:-5] # get rid of path and extension ".mol2" (stem)
            
            if os.path.isfile(output_dir+os.sep+name):
                tkMessageBox.showwarning(title = ("Mol2 conversion error"), message = ("The directory\n%s\n is a file!\n Please specify another output directory." % output_dir+os.sep+name  )  )
                return False
                    
            outputDirMOL2 = output_dir+os.sep+name+os.sep+"mol2"
            outputDirPDBQT = output_dir+os.sep+name+os.sep+"pdbqt"
            # attempt to create the Mol2 output dir
            try:
                if not os.path.exists(outputDirMOL2):
                    os.makedirs(outputDirMOL2, 0755)
            except:
                if not quiet:
                    tkMessageBox.showerror("Error!", ("I can't create the output dir:\n%s.\nTry to specify a different output directory..." % outputDirMOL2))
                else:
                    error_msg = "Error in creating the output directory: %s" % outputDirMOL2
                    problematic_list.append([ligFile, error_msg])
                if DEBUG: print "ERROR> mol2 import process died when creating the output directory"

            # split the mol2 files
            DisableInterface()
            to_be_imported = SplitMol2(ligFile, outputDirMOL2)
            # def SplitMol2 (filename = None, rootdir = None, naming = "ZINC id", sub_splitting = 1000):
            processed = 0
            if to_be_imported:
                if DEBUG: print "OpenMultiMol2> i'm gong to import", to_be_imported
                # attempt to create the PDBQT output dir
                try:
                    if not os.path.exists(outputDirPDBQT):
                        os.makedirs(outputDirPDBQT, 0755)
                except:
                    if not quiet:
                        tkMessageBox.showerror("Error!", ("I can't create the output dir:\n%s" % outputDirPDBQT))
                    else:
                        error_msg = "Error in creating the output directory: %s" % outputDirPDBQT
                        problematic_list.append([ligFile, error_msg])

                    if DEBUG: print "ERROR> pdbqt import process died on dir" % outputDirPDBQT
                message = Message(text = "I'm going to convert"+str(count_mols)+"molecules")
                for ligand in to_be_imported:
                    name = os.path.basename(ligand)[:-5]
                    output_file = outputDirPDBQT+os.sep+name+".pdbqt" # path/filename.pdbqt
                    InfoMessage.set(("Generating PDBQT for %s ...") % name)
                    root.update()
                    if genPDBQT( ligand, output_file ):
                        LigandRegistration(output_file)
                        processed += 1
                        InfoMessage.set(("Ligand generation: %d/%d ...") % (processed,count_mols))
                    else:
                        if not quiet:
                            tkMessageBox.showerror("Error!", ("Some problem occurred in converting the file:\n%s\n Import process aborted." % ligand))
                        else:
                            error_msg = "Error in generating the PDBQT"
                            problematic_list.append([ligand, error_msg])
                            
            EnableInterface()
            if processed == count_mols:
                # Re-check map cache folder if is defined
                if mapDir and MapSource.get() == 2:
                    openDirMaps(mapDir)
                if not quiet:
                    tkMessageBox.showinfo(title = "MultiMol2-to-PDBQT", message = ("%d ligands successfully imported from\n%s" % (count_mols, ligFile)))
                    return True
            else:
                if not quiet:
                    tkMessageBox.showwarning(title = ligFile, message = ("Some problem occurred.\n %d out of %d structures accepted." % (processed, count_mols) )  )
                else:
                    return problematic_list
            """

def CheckMultiMol2(filename, quiet = False):
    # simple function for checking the number oou
    # multiple structures in the mol2
    count = 0
    try:
        mol2_file = open(filename, 'r')
        for line in mol2_file:
            if "@<TRIPOS>MOLECULE" in line:
                count += 1
        if count == 0:
            return False
        else:
            return count
        mol2_file.close()
    except:
        if not quiet:
            tkMessageBox.showwarning("Mol2 Error", "The file doesn't contain any Mol2 structures.")
        return False


def SplitMol2Interface (reset = False, import_result = False, input_filename = None) :
    global Mol2OptionsWin
    # TODO import_results variable will be used by the "Advanced options" button
    # when importing from the multiple ligands


    # TODO there should be a unique database of ligands stored for the lifespan of the function
    # to keep track of the ligand names ever if they end up in different directories.


    print "\n\n\n==================================\n\n remember to close the interface before strting !!!! \n\n==============================="


    # support multiple files?
    molfilename = StringVar()
    molfilename.set("[ none ]")
    
    molfilenameLabel = StringVar()
    molfilenameLabel.set("")
    molcount = StringVar()
    molcount.set("")
    output_dir = StringVar()
    output_dir.set("[ none ]")
    output_dirLabel = StringVar()
    output_dirLabel.set("[ none ]")
    newdir_tag = StringVar()
    newdir_tag.set("")
    
    ImportSplitted = BooleanVar()
    ImportSplitted.set(False)

    OptionsButtonText = StringVar()
    OptionsButtonText.set("More >>")

    ImportSplitted.set(import_result)
   
    def open_a_mol2(filename = None):
        if not filename:
            filename = askopenfilename(parent = Mol2OptionsWin, 
                title = "Select a Mol2...", filetypes=[("Mol2", "*.mol2", "MOL2")])
        if filename:
            total = CheckMultiMol2(filename)
            #if DEBUG: print "GOT THIS FILENAME", filename
            if not total:
                tkMessageBox.showwarning("Warning!", 
                    ("The selected file doesn't seems to contain any structures or there's a problem in reading the file"))
                molfilename.set("[ none ]")
                output_dir.set("[ none ]")
                molcount.set("")
                SplitButton.configure(state = "disabled")
                return False
            else:
                if total == 1:
                    tkMessageBox.showwarning("Warning!", ("The selected file contains only a structure, therefore will not be splitted"))
                    #SplitButton.configure(state = "normal")
                    return False
                #print "GOT THIS FILENAME", filename

                molfilename.set(filename)
                molname_label = shortname(filename)
                molfilenameLabel.set(molname_label)
                text = "%d structures" % total
                molcount.set(text)
                SplitButton.configure(state = "normal")
                #default_dir = os.path.dirname(filename)
                default_dir = filename.rsplit(".", 1)[0]+os.sep
                if DEBUG: print "SplitMol2Interface> open_a_mol2> Default dir = ", default_dir
                set_dir(default_dir)
            
    def set_dir(dir = None):
        create = False
        if not dir:
            try:
                filename = molfilename.get()
                default_dir = os.path.dirname(filename)
            except:
                default_dir = ""
            dir = askdirectory(parent = Mol2OptionsWin, title = ("MOL2: Split and convert in the following dir...") , initialdir = default_dir)
        if not dir:
            return False
        dir_label = shortname(dir)
        output_dirLabel.set(dir_label)
        output_dir.set(dir)
        if not os.path.exists(dir):
            newdir_tag.set("(new)")

    def OptionsButtonCommand():
        if OptionsButtonText.get() == "More >>":
            Label(OptionsFrame.interior(), text = "ligand filename", justify = LEFT).grid(row=3, column = 0, padx = 5, sticky = W)
            OptionMenu(OptionsFrame.interior(), mol2_naming_scheme, "try ligand name", "ZINC id",\
            "progressive numbering").grid(row = 3, column = 1, padx = 5, stick = W)
            Label(OptionsFrame.interior(), text = "create sub-directories").grid(row=4, column = 0, padx = 5, sticky = W)
            OptionMenu(OptionsFrame.interior(), sub_splitting, "[ off ]",  "every 10 molecules",\
            "every 100 molecules", "every 1000 molecules", "every 10K molecules", "every\
            100K molecules").grid(row = 4, column = 1, padx = 5, stick = W)
            Checkbutton(OptionsFrame.interior(), text = "Import splitted molecules",\
            variable = ImportSplitted).grid(row = 6, column = 0, columnspan = 2, sticky= W, padx = 5)
            OptionsFrame.grid(row = 4, column = 0, sticky = W+E+N+S, padx = 10, columnspan = 2, ipady = 2, pady = 5)
            OptionsButtonText.set("<< Less")
        else:
            OptionsButtonText.set("More >>")
            OptionsFrame.grid_forget()



    def start_split():

        #sub_splitting, "never", "every 10 molecules", "every 100 molecules", "every 1000 molecules", "every 10K molecules", "every 100K molecules")
        split = sub_splitting.get()
        chunk = { "[ off ]" : None,  "every 10 molecules" : 10, "every 100 molecules" : 100,
        "every 1000 molecules" : 1000, "every 10K molecules" : 10000, "every 100K molecules": 100000 }
        if DEBUG:
            print "Mol2Options> Triggering mol2 splitting with the following params:"
            print molfilename.get(), output_dir.get(), chunk[split]
            
        if SplitMol2(filename = molfilename.get(), rootdir = output_dir.get(), naming = mol2_naming_scheme.get(), sub_splitting = chunk[split]):
            print "SplitMol2Interface> start_split> ImportedSplitted.get()",ImportSplitted.get() 
            print "                                 output_dir.get()",output_dir.get()
            if ImportSplitted.get():
                nb.tab('Ligand(s)').focus_set()
                nb.tab('Ligand(s)').invoke()
                openLigandDir(output_dir.get(), do_confirm = False, recursive = True)
                print "I'l import!"
                Mol2OptionsWin.destroy()    
                return True
            else:
                tkMessageBox.showinfo(parent = Mol2OptionsWin, title = "Mol2 split", message = ("File splitted successfully"))
                Mol2OptionsWin.destroy()    
                return True


    def shortname(name):
        if len(name) > 50:
            name = "..."+name[-48:]
        return name

    def set_split_size():
        pass
        # is going to change the label next to the pulldown menu

    ##########################################
    # The window is created here
    try:
        Mol2OptionsWin.lift()
    except:
        Mol2OptionsWin = Toplevel(root)
        Mol2OptionsWin.transient(root)
        
        Mol2OptionsWin.title("Multi-Mol2 splitting")
        Mol2OptionsWin.winfo_toplevel().resizable(NO,NO)
        #Mol2OptionsWin.winfo_toplevel().resizable(NO,NO)
        Mol2OptionsWin.grid_columnconfigure(0, weight = 1, minsize = 500)
        #Mol2OptionsWin.grid_columnconfigure(2, weight = 1)# , minsize = 200)
        Mol2OptionsWin.grid_rowconfigure(1, weight = 0, pad = 0)
        Mol2OptionsWin.grid_rowconfigure(2, weight = 0, pad = 0)
        Mol2OptionsWin.grid_rowconfigure(5, weight = 0, pad = 0)
        #Mol2OptionsWin.grid_columnconfigure(2, weight = 1)

        
        InputFrame = Pmw.Group(Mol2OptionsWin, tag_text = "Input file")

        InputFrame.grid_rowconfigure(0, weight = 0)
        InputFrame.grid_rowconfigure(1, weight = 0)
        #InputFrame.grid_columnconfigure(0, weight = 0)
        #InputFrame.grid_columnconfigure(1, weight = 1)
        #InputFrame.grid_columnconfigure(1, weight = 1)
        InputFrame.grid_rowconfigure(2, weight = 0)
        #InputFrame.grid_columnconfigure(2, weight = 1)
        InputFrame.grid_rowconfigure(3, weight = 0)
        #InputFrame.grid_columnconfigure(3, weight = 1)
        #InputFrame.grid_rowconfigure(1, weight = 1)


        Button(InputFrame.interior(), compound = LEFT, text = "Open...", image = open_smfolder_icon, command = open_a_mol2).grid(row=0, column = 0, padx = 5, sticky = W)
        input_label = Label(InputFrame.interior(), textvar = molfilenameLabel)
        input_label.grid(row=0, column = 1, padx = 5, sticky = W+E)
        # separator
        #Frame(InputFrame.interior(), height=2, bd=1, relief=SUNKEN).grid(row = 1, sticky = E+W, columnspan = 4, padx = 2, pady = 5)
        filenamelabel = Label(InputFrame.interior(), textvar = molcount)
        filenamelabel.grid(row=2, column = 1, columnspan = 1, padx = 5, sticky = N)
        filenamelabel.configure(state="disabled")
        
        InputFrame.grid(row = 1, column = 0, sticky = N+W+E+S, padx = 10, pady = 10, columnspan = 2)
        
        #print InputFrame.grid_info()


        OutputFrame = Pmw.Group(Mol2OptionsWin, tag_text = "Output directory")

        OutputFrame.grid_rowconfigure(0, weight = 0)
        #OutputFrame.grid_rowconfigure(1, weight = 0)
        #OutputFrame.grid_rowconfigure(3, weight = 0)
        #OutputFrame.grid_rowconfigure(4, weight = 0)
        #OutputFrame.grid_columnconfigure(1, weight = 1)
        Button(OutputFrame.interior(), compound = LEFT, text = "Set...", image = open_smfolder_icon, command = set_dir).grid(row=0, column = 0, padx = 5, sticky = W, pady = 3)
        Label(OutputFrame.interior(), textvar = output_dirLabel, justify = RIGHT).grid(row=0, column = 1, padx = 5, sticky = E)
        Label(OutputFrame.interior(), textvar = newdir_tag, fg = 'red').grid(row=0, column = 2, ipadx = 5, sticky = W)
        # separator
        #Frame(OutputFrame.interior(), height=2, bd=1, relief=SUNKEN).grid(row = 1, sticky = E+W, columnspan = 4, padx = 2, pady = 5)

        OutputFrame.grid(row = 2, column = 0, sticky = W+E, padx = 10, pady = 10, columnspan = 2) #, ipady = 2, pady = 5)

        OptionsButton = Button(Mol2OptionsWin, textvar = OptionsButtonText, command = OptionsButtonCommand)
        OptionsButton.grid(row = 3, column = 0, sticky = W, padx = 10, pady = 10)
        OptionsFrame = Pmw.Group(Mol2OptionsWin, tag_text = "Options")

    
        # buttons
        #buttons_frame = Frame(Mol2OptionsWin)
        #buttons_frame.grid(row = 5, column = 0, sticky = W+E+S)
        SplitButton = Button(Mol2OptionsWin, compound = LEFT, text = "Split", image = split_icon, command = lambda : start_split(), state = "disabled", width = 120)
        #SplitButton.configure(status = "disabled")
        SplitButton.grid(row=0, column = 0, padx = 10, sticky = E+W+S, pady = 10)
        Button(Mol2OptionsWin, compound = LEFT, text = "Exit", command = lambda : Mol2OptionsWin.destroy() ).grid(row= 5, column = 0, padx = 10, pady = 10, sticky = E+S)
        #Button(Mol2OptionsWin, text = "Cancel", command = lambda: Mol2OptionsWin.destroy()).grid(row = 5, column = 1, sticky = W, padx = 10, pady = 10)
        if input_filename:
            open_a_mol2(input_filename)



def valid_filename(file):
    pass


def SplitMol2 (filename = None, rootdir = None, naming = "ZINC id", sub_splitting = 1000):
    DEBUG = True
    # TODO: see if there's a zinc molname, if the name is allowed by the os...
    if DEBUG: print "SplitMol2> called with the following parameters:", filename, rootdir, naming, sub_splitting

    # split a multi-mol2 in the specified directory
    utility_mode = False
    # This is for using the splitting function as an utility:
    if not filename:
        filename = askopenfilename(parent = root, title = "Select a Mol2...", filetypes=[("Mol2", "*.mol2", "MOL2")])
        utility_mode = True
    if not filename:
        return
    # end of utility mode

    buffer = []
    count = 0
    zinc_found = False
    merge_remainder = False

    splitted_mols = []
    total = CheckMultiMol2(filename)
    name_register = {}

    # if sub_splitting is requested, define the directory size
    if sub_splitting:
        if sub_splitting >= total:
            sub_splitting = None
            if DEBUG: print "SplitMol2> no splitting is actually required"
        else:
            merge_remainder = False
            # if remainder is =< 10% of sub_splitting value, the last dir is not created
            remainder_pc = (float(total % sub_splitting)/float(sub_splitting))*100.0 
            if DEBUG: print "SplitMol2> last dir would contain %d files =  %2.3f percent " % ((total % sub_splitting), remainder_pc  )
            if remainder_pc < 10.0 :
                merge_remainder = True
            if DEBUG: print "SplitMol2> merge_remainder = ", merge_remainder
            size = len(str( total / sub_splitting ))+1 # count how many zeroes will be necessary and add one to be sure
            #if DEBUG: print "SplitMol2> cypher lenght:", size
            dir_format = "%0*d"
            if DEBUG: print "SplitMol2> dir_format is ", dir_format

    # Also this is for using the splitting function as an utility
    if not rootdir:
        rootdir = askdirectory(parent = root, title = ("MOL2: Split the molecules in the following dir..."))
    if not rootdir:
        tkMessageBox.showinfo(title="MOL2 splitting", message =( "The splitting process of %s has been cancelled by the user" % filename))
        return
    # end of utility mode

    multimol2 = open(filename, 'r')  #get_lines(filename)
    name = os.path.basename(filename)[:-5] # needed for the stem of the output files

    try:
        if not os.path.exists(rootdir):
            if DEBUG: print "SplitMol2> the rootdir %s doesn't exists, therefore will be created" % rootdir
            os.makedirs(rootdir, 0755)
        InfoMessage.set(("Splitting %s ") % os.path.basename(filename) )
        root.update()
        if sub_splitting:    
            dir_count = 0
            dir_name = dir_format % (size, dir_count)
            outdir = rootdir+os.sep+dir_name
            if DEBUG: print "SplitMol2> initialized the first sub-directory : ", outdir
            if DEBUG: print "SplitMol2> (dir_count = %s ) ", dir_count
            
            if not os.path.exists(outdir):
                try:
                    if DEBUG: print "SplitMol2> creating the new directory : ", outdir
                    os.makedirs(outdir, 0755)
                except:
                    tkMessageBox.showerror("Error!", ("Impossible to create the following directory:\n%s\nThe splitting process is aborted."% outdir))
                    return False
        else:
            outdir = rootdir
        
        split_count = -1

        gc.disable()

        for line in multimol2: # mol2 optimization should happen here...

            if "@<TRIPOS>MOLECULE" in line:
                split_count +=1
                if len(buffer) > 0: # INCREASED FROM 0
                    if count == 0: # the first molecule found
                        buffer.append(line)
                    count += 1
                    number = "%06d" % count # TODO to adapt to the number of molecules like the directories

                    if zinc_found and naming == "ZINC id":
                        name_register.setdefault(zinc_id, -1)
                        name_register[zinc_id] += 1
                        if name_register[zinc_id] == 0:
                            mol_name = zinc_id+".mol2"
                        else:
                            mol_name = zinc_id+"_"+str(name_register[zinc_id])+".mol2"
                        filename = outdir+os.sep+mol_name
                    else:
                        filename = outdir+os.sep+name+"_"+str(number)+".mol2"
         
                    writeLines(filename, buffer, do_strip = False)

                    del buffer[:]
                    splitted_mols.append(filename)
                    zinc_found = False

                    if sub_splitting: # 
                        if (split_count % sub_splitting) == 0 : # or split_count < 1:
                            print "%d == %d : %d" % (split_count, sub_splitting, (split_count % sub_splitting))
                            dir_count += 1
                            dir_name = dir_format % (size, dir_count)
                            outdir = rootdir+os.sep+dir_name
                            if DEBUG: print "SplitMol2> the current directory is : ", outdir, "##########################################"
                            if not os.path.exists(outdir):
                                try:
                                    if DEBUG: print "SplitMol2> creating the new directory : ", outdir
                                    os.makedirs(outdir, 0755)
                                except:
                                    tkMessageBox.showerror("Error!", ("Impossible to create the following directory:\n%s\nThe splitting process is aborted."% outdir))
                                    return False
                    buffer.append(line)
            else:
                buffer.append(line)
            if "ZINC" in line[0:5]:
                zinc_id = line.split()[0]
                zinc_found = True
        gc.enable()
        multimol2.close()

        if len(buffer) > 0: # Flush the remaining buffer...
            count += 1
            number = "%06d" % count
            if zinc_found:
                if not zinc_id in name_register.keys():
                    name_register[zinc_id] = 0
                    mol_name = zinc_id+".mol2"
                else:
                    name_register[zinc_id] += 1
                    mol_name = zinc_id+"_"+str(name_register[zinc_id])+".mol2"
                    filename = outdir+os.sep+mol_name
                filename = outdir+os.sep+mol_name
            else:
                filename = outdir+os.sep+name+"_"+str(number)+".mol2"

            writeLines(filename, buffer, do_strip = False)
            zinc_found = False
            splitted_mols.append(filename)
            del buffer[:]
        if utility_mode:
            tkMessageBox.showinfo(title="MOL2 splitting", message =( "%d molecules have been successfully created in:\n %s" % (count, rootdir)))
        InfoMessage.set(("Splitting %s : DONE ") % os.path.basename(filename) )
        root.update()
        return splitted_mols
    except:
        tkMessageBox.showerror("Error!", ("The selected directory is not accessible: %s\nThe splitting process is aborted."% rootdir))
        return False
    if DEBUG : print count, "molecules processed"
        
def genPDBQT(infile, outfile):
    DisableInterface()
    # any resemblance with the prepare_ligand script is accidental
    #
    # generate a pdbqt from a directory containing the splitted mol2 
    #
    # optional parameters

    # PrepareLigand options defaults
    verbose = None
    add_bonds = False
    #-A: repairs to make: add bonds and/or hydrogens
    repairs = Repair.get()
    #-C  default: add gasteiger charges 
    charges_to_add = ChargeSet.get()
    #-p preserve charges on specific atom types
    preserve_charge_types=''
    #-U: cleanup by merging nphs_lps, nphs, lps
    cleanup  = Cleanup.get()
    #-B named rotatable bond type(s) to allow to rotate
    
    SELECTED_ALLOWED_BONDS = ""
    if BackboneRotatable.get():
        SELECTED_ALLOWED_BONDS += "_backbone"
    if AmideRotatable.get():
        SELECTED_ALLOWED_BONDS += "_amide"
    if GuanidiniumRotatable.get():
        SELECTED_ALLOWED_BONDS += "_guanidinium"
    allowed_bonds = SELECTED_ALLOWED_BONDS
    if DEBUG: print "genPDBQT> allowed bonds:", allowed_bonds
    #-r  root
    root = 'auto'
    #-o outputfilename
    outputfilename = outfile # GOOD
    #-F check_for_fragments
    check_for_fragments = LargestFrag.get()
    #-I bonds_to_inactivate
    bonds_to_inactivate = ""
    #-Z inactivate_all_torsions
    inactivate_all_torsions = LockTors.get()
    #-g attach_nonbonded_fragments
    attach_nonbonded_fragments = AttachFrag.get()
    #-m mode 
    mode = 'automatic'
    #-d dictionary
    dict = None

    if DEBUG: print "genPDBQT> Selected allowed bonds", SELECTED_ALLOWED_BONDS

    try:
        mols = Read(infile)
        mol = mols[0]
    except:
        return False
    if len(mols) > 1:
        # put here the filtering
        ctr +=1
        if len(m.allAtoms) > len(mol.allAtoms):
            mol = m

    coord_dict = {}
    for atom in mol.allAtoms: coord_dict[atom] = atom.coords
    mol.buildBondsByDistance()
    if charges_to_add is not None:
        preserved = {}
        preserved_types = preserve_charge_types.split(',')
        for type in preserved_types:
            if not len(type): continue
            ats = mol.allAtoms.get(lambda x: x.autodock_element == type)
            for a in ats:
                if a.chageSet is not None:
                    preserved[a] = [a.chargeSet, a.charge]
    LPO = AD4LigandPreparation(mol, mode, repairs, charges_to_add, 
                          cleanup, allowed_bonds, root, 
                          outputfilename=outputfilename,
                          dict=dict, check_for_fragments=check_for_fragments,
                          bonds_to_inactivate=bonds_to_inactivate, 
                          inactivate_all_torsions=inactivate_all_torsions,
                          attach_nonbonded_fragments=attach_nonbonded_fragments)
    if charges_to_add is not None:
        # restore the previous charges
        for atom, chargeList in preserved.items():
            atom._charges[chargeList[0]] = chargeList[1]
            atom.chargeSet = chargeList[0]
    bad_list = []
    for a in mol.allAtoms:
        if a.coords!=coord_dict[a]: bad_list.append(a)
    if len(bad_list):
        if DEBUG:
            print len(bad_list), ' atom coordinates changed!'    
            for a in bad_list:
                print a.name, ":", coord_dict[a], ' -> ', a.coords
    if mol.returnCode is not 0:
        InfoMessage.set("ERROR generating PDBQT for %s" % os.path.basename(infile))
        if DEBUG: print "ERROR IN THE EXITCODE!"
        LPO = None # TODO TEST TEST TEST!!!!
        mols = None 
        EnableInterface()
        return False
    else:
        InfoMessage.set("%s converted to PDBQT" % os.path.basename(infile))
        nb.update() # TODO Update the window with the message... but not the ROOT!
        LPO = None
        mols = None
        EnableInterface()
        return True

def LigandRegistration(filename):
    # INPUT        : pdbqt file
    # OUTPUT    : nothing
    # EXTRA        : append the ligand properties to the Great Book of Ligands
    #               update the list of total atom types considered (for caching map)

    ligand = get_lines(filename)
    current_atypes = []
    bad_atom_types = []
    MW  = 0
    HbD = 0
    HbA = 0
    Nat = 0
    torsdof = 0
    status = True
    
    hbd_h = []
    hbd_candidate = []

    # Calculate all the properties
    for line in ligand:
        if 'TORSDOF' in line:
            torsdof = int(line.split()[1])
        if line[0:6] == 'HETATM' or line[0:4] == 'ATOM':
            # Nat += 1 # Consider to remove Hydrogens? (search on PubMed)
            atype = line.split()[-1]
            if atype in AtypeList.keys():
                if atype not in current_atypes:
                    current_atypes.append(atype)
                # Hb acceptor
                if atype == "OA" or atype == "NA" or atype == "SA":
                    HbA += 1
                # Hb donor preparation
                if atype == "HD":
                    #capture the hydrogens that could be bond to the Hb donor...
                    hbd_h.append(line)
                else:
                    # count heavy atoms
                    Nat += 1

                if atype == "N" or atype == "O" or atype == "OA" or atype == "NA":
                    hbd_candidate.append(line)
                    MW += AtypeList[atype][1] # add the atomic weight to the total MW
            else:
                #MW += 10000 # check this if it's reasonable
                MW += 0 # check this if it's reasonable
                if not atype in bad_atom_types:
                    bad_atom_types.append(atype)
                status = False # non-standard atom types are rejected by default
    # identify HBD by checking if N/O's are bound to H's
    for atom in hbd_candidate:
        for hydrogen in hbd_h:
            #print atom,hydrogen
            if dist(atom, hydrogen) <= 1.1:
                HbD += 1
                break
    if DEBUG: print "I've found %s HBD"% HbD

    # Insert the ligand in the Great Book of Ligands
    if not LigandDictionary.has_key(filename):
        # ligand is registered with properties
        LigandDictionary[filename] = {
        "Atypes"    : current_atypes,
        "TORSDOF"    : torsdof,
        "HbD"        : HbD,
        "HbA"        : HbA,
        "MW"        : MW,
        "Nat"        : Nat,
        "NotStdAT"    : bad_atom_types,
        "accepted"    : status }
        
        LigandScrolledListBox.insert('end', filename)
        for atype in current_atypes:
            AtypeList[atype][0] += 1  # increment the count for this atom type
            # Add a list of the non std atomt types and count it (for cached maps purposes)???
        for atype in bad_atom_types:
            if atype in AtypeList_special.keys():
                AtypeList_special[atype][0] += 1
            else:
                AtypeList_special[atype] = [0, DEFAULT_ATOM_WEIGHT]


    if DEBUG:
        # Debug function for atom types...
        print "#### Atom type-DICTIONARY ####"
        for item in AtypeList.keys():
            print item, AtypeList[item][0]
        print "#### Atom type-DICTIONARY ####"


# TODO USE N3PUTILITY!!!!
#def dist(firstline, secondline):  
#    # INFO   : calculate the atomic distance between two PDB atom lines
#    # INPUT  : two pdb lines
#    # OUTPUT : a pdb line
#    coord1=[]
#    coord2=[]
#    temp=firstline[28:56] # TODO WARNING! fragile! use the single coord spacing...
#    coord1=temp.split()
#    temp=secondline[28:56]
#    coord2=temp.split()
#    # floating the strings
#    print coord1, coord2
#    for index in range(len(coord1)):
#        coord1[index]=float(coord1[index])
#        coord2[index]=float(coord2[index])
#    measure=sqrt((coord1[0]-coord2[0])**2+(coord1[1]-coord2[1])**2+(coord1[2]-coord2[2])**2)
#    return measure



def dist(f, s, sq=True):  
    """ works with PDB(QT) lines"""
    if sq: 
        return sqrt((float(f[30:38])-float(s[30:38]))**2 +\
                    (float(f[38:46])-float(s[38:46]))**2 +\
                    (float(f[46:54])-float(s[46:54]))**2  )
    else:  return (float(f[30:38])-float(s[30:38]))**2 +\
                  (float(f[38:46])-float(s[38:46]))**2 +\
                  (float(f[46:54])-float(s[46:54]))**2






# TODO USE N3P UTILITY!

def UpdateATDict(file_list):
    """
    input:        list of PDBQT filenames to be excluded
    output:     (nothing)
    operation:    update the dictionary of atom types currently
                loaded
    """
    for ligand in file_list:
        # standard atypes
        atypes_to_be_removed = LigandDictionary[ligand]["Atypes"]
        for atype in atypes_to_be_removed:
            if atype in AtypeList:
                AtypeList[atype][0] -= 1
        # extra atypes
        atypes_to_be_removed = LigandDictionary[ligand]["NotStdAT"]
        for atype in atypes_to_be_removed:
            if atype in AtypeList_special:
                AtypeList_special[atype][0]-= 1
                

def clearATDict():
    # set all atom type counts to 0 (except for d and e)
    for atom in AtypeList:
        AtypeList[atom][0] = 0
    AtypeList["e"][0] = 1
    AtypeList["d"][0] = 1
    if DEBUG:
        for atom in AtypeList:
            print atom, AtypeList[atom]


def openLigandDir(ligDir = None, recursive = False, do_confirm = True):

    # print "=== openLigandDir ==================================ligDir", ligDir
    importPDBQTcheck = BooleanVar(value = False)
    importPDBcheck= BooleanVar(value = False)
    importMol2check = BooleanVar(value = False)

    def ligsummary():
        global root
        sumwin = Toplevel(master = root)
        sumwin.transient(root)
        sumwin.title("Import ligands")
        def doimport():
            #print "3333333333333 doimport"
            sumwin.destroy()
            startimport()
        def closeimport():
            #print "closeimpot"
            sumwin.destroy()

        Label(sumwin, text = ("%d total ligands found." % (total) )).grid(row = 0, column = 0, padx = 10, pady = 10)
        if count_pdbqt:
            importPDBQTcheck.set(True)
            #print importPDBQTcheck.get()
            i = Checkbutton(sumwin, text = ("PDBQT\t[ %d ]" % count_pdbqt), variable = importPDBQTcheck)
            i.grid(row = 1 , column = 0, sticky = W, padx = 10, pady = 0)
            #print importPDBQTcheck.get()
        if count_pdb:
            importPDBcheck.set(True)
            Checkbutton(sumwin, text = ("PDB\t [ %d ]" % count_pdb), variable = importPDBcheck, onvalue = True, offvalue = False).grid(row = 2 , column = 0, sticky = W, padx = 10, pady = 0)
        if count_mol2:
            importMol2check.set(True)
            Checkbutton(sumwin, text = ("Mol2\t [ %d ]" % count_mol2 ), variable = importMol2check).grid(row = 3 , column = 0, sticky = W, padx = 10, pady = 0)
        Button(sumwin, text = "Import", command = doimport).grid(row = 10, column = 0, sticky = W, padx = 10, pady = 10)
        Button(sumwin, text = "Close", command = closeimport).grid(row = 10, column = 2, sticky = E, padx = 10, pady = 10)

    def startimport():
        list = []
        # PDBQT 
        if importPDBQTcheck.get():
            #openLigand(pdbqt_ligandlist, quiet = True)
            list += pdbqt_ligandlist
        #    for item in checkPDBQTligList(pdbqt_ligandlist):
        #        LigandRegistration(item)
        # PDB
        if importPDBcheck.get():
             #openLigand(pdb_ligandlist)
            list += pdb_ligandlist
        # MOL2
        if importMol2check.get():
             #openLigand(mol2_ligandlist)          
             list += mol2_ligandlist
        # print "=########################## got this list", list
        if list:
            openLigand(list, quiet = True)
        # Re-check map cache folder if is defined
        if mapDir and MapSource.get() == 2:
            openDirMaps(mapDir)
        # Ligands will be filtered every time (at least because of the TDOF)
        FilterLigands(True)
        countLigands()
        TheCheck()

    pdbqt_ligandlist = []
    mol2_ligandlist = []
    pdb_ligandlist = []
    count_pdbqt = 0
    count_mol2 = 0
    count_pdb = 0
    if recursive:
        message = "Searching ligands recursively"
    else:
        message = "Searching ligands in directory"
    if not ligDir:
        ligDir = askdirectory(title = message)
    if ligDir:
        if recursive:
            for root, subFolders, files in os.walk(ligDir):
                for file in files:
                    fname, ext = os.path.splitext(file)
                    if ext == ".pdbqt":
                        pdbqt_ligandlist.append(os.path.join(root,file))
                    elif ext == ".mol2":
                        mol2_ligandlist.append(os.path.join(root,file))
                    elif ext == ".pdb":
                        pdb_ligandlist.append(os.path.join(root,file))
        else:
            pdbqt_ligandlist = glob.glob(os.path.join(ligDir, "*.pdbqt"))            
            pdb_ligandlist = glob.glob(os.path.join(ligDir, "*.pdb"))
            mol2_ligandlist = glob.glob(os.path.join(ligDir, "*.mol2"))

        if DEBUG:
            print "This would be the ligand file list"
            print "pdbqt", pdbqt_ligandlist
            print "mol2", mol2_ligandlist
            print "pdb", pdb_ligandlist

        count_pdbqt = len(pdbqt_ligandlist)
        count_mol2 = len(mol2_ligandlist)
        count_pdb = len(pdb_ligandlist)
        total = count_pdbqt + count_mol2 + count_pdb
        if total >= 1 and do_confirm:
           ligsummary()
        else:
            openLigand( (pdbqt_ligandlist + mol2_ligandlist + pdb_ligandlist), quiet = True)
            # Re-check map cache folder if is defined
            if mapDir and MapSource.get() == 2:
                openDirMaps(mapDir)
            # Ligands will be filtered every time (at least because of the TDOF)
            FilterLigands(True)
            countLigands()
            TheCheck()

def removeLigand(): 
    ligand_index = LigandScrolledListBox.curselection() # position of ligands in the list...
    ligand_list = []

    # update the list of ligands to be removed from the Great Book of Ligands
    for item in ligand_index:
        ligand_list.append(LigandScrolledListBox.get(item))
    # remove the ligands...
    UpdateATDict(ligand_list)
    for ligand in ligand_list:
        del LigandDictionary[ligand]
    countLigands()

    # remove the ligands from the visualized list
    ligand_index = list(ligand_index)
    ligand_index.reverse()    
    for item in ligand_index:
        LigandScrolledListBox.delete(item)
    FilterLigands(True)
    TheCheck()

def removeReceptor():
    items = receptorScrolledListBox.getcurselection()
    # update the atom type list decrementing the atoms of each ligand
    for ligand in items:
        receptorFileList.remove(ligand)
    receptorScrolledListBox.setlist(receptorFileList) # NOT CLEAR!!!
    if len(receptorFileList) == 0:
        MultiReceptorSet.set(False)
    countReceptors()
    TheCheck()
        
def removeAllLigands():
    if len(LigandDictionary) > 1 and not tkMessageBox.askokcancel(title = 'Delete all the ligands', 
        message= 'Do you really want to\nremove all the ligands\nfrom the list?'):
        return
    LigandScrolledListBox.delete(0, END) 
    # Buy a new Great Book of Ligands
    for item in LigandDictionary.keys():
        del LigandDictionary[item]
    countLigands()
    clearATDict()
    TheCheck()

def checkPDBQTligList(filenamelist, quiet = False): 
    AcceptedFiles = []
    problematic_list = []
    CountAccepted = 0
    CountRejected = 0
    for file in filenamelist:
        found_ligand = 0
        found_residue = 0
        try:
            for line in get_lines(file):
                if line[0:4] == "ROOT":
                    found_ligand = 1
                if line[0:9] == "BEGIN_RES":
                    found_residue = 1
                if DEBUG: print "found res"
            if found_ligand == 1 and found_residue == 0:
                AcceptedFiles.append(file)
                CountAccepted += 1
            else:
                CountRejected += 1
                problematic_list.append([file, "invalid PDBQT file"])
        except:
            CountRejected += 1
            problematic_list.append([file, "error in opening the file"])
    if CountAccepted == 0:
       if CountRejected == 1:
           tkMessageBox.showerror("Error!", "The ligand is not valid.")
       else:
           tkMessageBox.showerror("Ligands error!", "None of %d PDBQT have been accepted.\nPlease check the inputs." % CountRejected)
    if not quiet:
        if CountAccepted > 0 and CountRejected > 0:
            if tkMessageBox.askokcancel("Ligands imported", "%d\taccepted.\n%d\trejected.\n\nDo you want to inspect the list of rejected ligands?" % (CountAccepted, CountRejected)):
                issueInspectorWindow("List of rejected PDBQT's", problematic_list)
    return AcceptedFiles, problematic_list


def checkPDBQTreclist(filenamelist, quiet = False): 
    AcceptedFiles = []
    problematic_list = []
    CountAccepted = 0
    CountRejected = 0
    for file in filenamelist:
        found_ligand = 0
        found_residue = 0
        try:
            for line in get_lines(file):
                if line[0:4] == "ROOT":
                    found_ligand = 1
            if found_ligand == 1:
                CountRejected += 1
                problematic_list.append([file,"improper PDBQT (possible ligand)"])
                if DEBUG: print file, "is bad receptor.."
            else:
                AcceptedFiles.append(file)
                CountAccepted += 1
                if DEBUG: print file, "a good receptor.."
        except:
            CountRejected += 1
            problematic_list.append([file, "error in opening the file"])
    if not quiet:
        if CountRejected == 0:
            if CountAccepted > 1: # To suppress messages for a single ligand import
                notification = "%d receptors\nhave been accepted." % CountAccepted
                tkMessageBox.showinfo(title="PDBQT receptor imported", message=notification)
        if CountAccepted == 0:
            if CountRejected == 1:
                tkMessageBox.showwarning("Error!", "The receptor is not valid.")
            else:
                tkMessageBox.showwarning("Receptors error!", "None of %d receptors have been accepted.\nPlease check the inputs." % CountRejected)
        if CountAccepted > 0 and CountRejected > 0:
            if tkMessageBox.askokcancel("Receptors imported", "%d\taccepted.\n%d\trejected.\n\nDo you want to inspect the list of rejected structures?" % (CountAccepted, CountRejected)):
                issueInspectorWindow("List of rejected PDBQT's", problematic_list)
    return AcceptedFiles, problematic_list



def issueInspectorWindow(title, issue_list):
    """
    helper function for issue inspection.

    issue_list must be a list of lists in the format [ [filename, error], ...]

    """
    def saveList():
        file = askopenfilename(title = "Select error list log filename...", filetypes=[("CSV error file", "*.csv"), ("Any file...", "*")])
        if not file:
            return
        try:
            fp = open(file, 'wb')
            for i in issue_list:
                line = '%s,"%s"' % (i[0], i[1]) 
                fp.write(line)
            fp.close()
        except:
            tkMessageBox.showerror("Error!", "Impossible to save the file:\n%s" % file)
            
    def close():
        RejectedWindow.destroy()

    RejectedWindow = Toplevel(root)
    RejectedWindow.transient(root)
    RejectedWindow.title(title)
    scrollbar = Scrollbar(RejectedWindow)
    ListOfRejected = Listbox(RejectedWindow)
    #CloseButton = Button(RejectedWindow, text = "Close", command = RejectedWindow.destroy)
    ListOfRejected.grid(column = 0, sticky = W+N+S+E)
    RejectedWindow.grid_rowconfigure(0, minsize = 300, weight = 1)
    RejectedWindow.grid_columnconfigure(0, minsize = 330, weight = 1)
    scrollbar.grid(row = 0, column = 1, sticky = S+N)
    scrollbar.config(command = ListOfRejected.yview)
    ListOfRejected.config(yscrollcommand=scrollbar.set)
    for item in issue_list:
        ListOfRejected.insert(END, (item[0]+" => > "+item[1]))
    CloseButton = Button(RejectedWindow, text = "Close", command = close).grid(row = 2, columnspan = 2, sticky = W+E)
    SaveButton = Button(RejectedWindow, text = "Save", command = saveList).grid(row = 2, column = 3, columnspan = 2, sticky = W+E)

def CheckLigFilterOptions():
    for value in HbDmin, HbDmax, HbAmin, HbAmax, MWmin, MWmax, NatMin, NatMax, TORSDOFmin, TORSDOFmax:
        try:
            value.get()
        except:
            tkMessageBox.showwarning("Error", "Only numerical values\nare allowed ...\n Try again!\n(resetting to default)")
            FilteringDefaults(FilterSet.get())
            return False
            break
        if value.get() < 0:
            tkMessageBox.showwarning("Uhmmmm...", "In the current implementation of\nthe Universe negative values\nfor these params are not allowed...\n\nTry one of the following options:\n   - recompile the Universe\n   - use positive value\n\n[resetting to default]")
            FilteringDefaults(FilterSet.get())
            return False
            break
    if TORSDOFmax.get() + FlexResTORSDOF.get() > AutoDockMaxTORSDOF.get():
        if DEBUG: print TORSDOFmax.get(), FlexResTORSDOF.get(), AutoDockMaxTORSDOF.get()
        if FlexResTORSDOF.get() > 0:    
            tkMessageBox.showwarning("Torsion Limit", "WARNING: AutoDock can handle up to %s rotatable bonds.\n\nThere are %s rotatable bonds already allotted for the flex residues, therefore the maximum number of rotatable bonds per ligand should be %s.\n\nUse this value carefully." % ( AutoDockMaxTORSDOF.get(), FlexResTORSDOF.get(), AutoDockMaxTORSDOF.get() - FlexResTORSDOF.get() ))
        else:
            tkMessageBox.showwarning("Torsion Limit", "WARNING: AutoDock can handle up to %s rotatable bonds. Use this value carefully..." % ( AutoDockMaxTORSDOF.get() ))
        #FilteringDefaults("TORSDOF")

    MinMax = False
    if HbDmin.get() <= HbDmax.get():
        if HbAmin.get() <= HbAmax.get():
            if MWmin.get() <= MWmax.get():
                if NatMin.get() <= NatMax.get():
                    if TORSDOFmin.get() <= TORSDOFmax.get():
                        MinMax = True
    if not MinMax:
        FilteringDefaults(FilterSet.get())
        tkMessageBox.showwarning("Uhmmmm...", "Guess what?\nMAX must be bigger than or equal to MIN.\n\n[resetting to default]")
        return False
    else:
        return True

def DefaultLigOptions():
    ChargeSet.set("gasteiger")
    Repair.set("")
    Cleanup.set("nphs_lps")
    BackboneRotatable.set(True)
    AmideRotatable.set(False) # Raccoon default (ADT=False)
    GuanidiniumRotatable.set(False) 
    LockTors.set(False) 
    LargestFrag.set(True) # Raccoon default (ADT=False)
    AttachFrag.set(False)

def LigandImportOptions(): # Options for non-PDBQT files only
    global LigandOptionsWin
    try:
        LigandOptionsWin.lift()
    except:
        LigandOptionsWin = Toplevel(root)
        LigandOptionsWin.title("Ligand PDBQT generation")
        LigandOptionsWin.winfo_toplevel().resizable(NO,NO)
        LigandOptionsWin.transient(root)

        ChargeFrame = Pmw.Group(LigandOptionsWin, tag_text = "Partial charges")
        Radiobutton(ChargeFrame.interior(), text="add Gasteiger", variable = ChargeSet, value = "gasteiger",
            highlightbackground = 'black', indicatoron = 0, selectcolor = 'lightblue', width = 23, height = 2).grid(row = 0, column = 0, sticky = W,
            padx = 2, pady = 3) # Default
        Radiobutton(ChargeFrame.interior(), text="keep original", variable = ChargeSet, value = "",
            highlightbackground = 'black', indicatoron = 0, selectcolor = 'lightblue', width = 23, height = 2).grid(row = 0, column = 2, sticky = E,
            padx = 2, pady = 3)
        #Label(ChargeFrame.interior(), text = "       ").grid(row=0, column = 1, sticky = E+W)
        ChargeFrame.grid(row = 2, column = 0, padx = 10, pady = 2, ipady = 5, sticky = W+E, columnspan = 2)

        RepairFrame = Pmw.Group(LigandOptionsWin, tag_text = "Structure repair ")
        Radiobutton(RepairFrame.interior(), text = "[ off ]", variable = Repair, value = "",
            highlightbackground = 'black', indicatoron = 0, selectcolor = 'lightblue', width = 11).grid(row = 1 , column = 0, sticky = N,
            padx = 1, pady = 5) # Default
        Radiobutton(RepairFrame.interior(), text = "bonds", variable = Repair, value = "bonds",
            highlightbackground = 'black', indicatoron = 0, selectcolor = 'lightblue', width = 11).grid(row = 1 , column = 1, sticky = N,
            padx = 1, pady = 5)
        Radiobutton(RepairFrame.interior(), text = "hydrogens", variable = Repair, value = "hydrogens",
            highlightbackground = 'black', indicatoron = 0, selectcolor = 'lightblue', width = 11).grid(row = 1 , column = 2 , sticky = N,
            padx = 1, pady = 5)
        Radiobutton(RepairFrame.interior(), text = "both", variable = Repair, value = "bond_hydrogens",
            highlightbackground = 'black', indicatoron = 0, selectcolor = 'lightblue', width = 11).grid(row = 1 , column = 3, sticky = N,
            padx = 1, pady = 5)
        RepairFrame.grid(row = 3, column = 0, padx = 10, pady = 2, ipady = 5, sticky = W+E, columnspan = 2)

        CleanupFrame = Pmw.Group(LigandOptionsWin, tag_text = "Structure clean-up ")
        Radiobutton(CleanupFrame.interior(), text = "[ off ]", variable = Cleanup, value = "",
            highlightbackground = 'black', indicatoron = 0, selectcolor = 'lightblue', width = 11,height = 2).grid(row = 1 , column = 0, sticky = N,
            padx = 1, pady = 5) 
        Radiobutton(CleanupFrame.interior(), text = "both", variable = Cleanup, value = "nphs_lps", 
            highlightbackground = 'black', indicatoron = 0, selectcolor = 'lightblue', width = 11,height = 2).grid(row = 1 , column = 3, sticky = N,
            padx = 1, pady = 5) 
        Radiobutton(CleanupFrame.interior(), text = "merge\nnon-polar H", variable = Cleanup, value = "nphs",
            highlightbackground = 'black', indicatoron = 0, selectcolor = 'lightblue', width = 11,height = 2).grid(row = 1 , column = 1, sticky = N,
            padx = 1, pady = 5)
        Radiobutton(CleanupFrame.interior(), text = "delete\nlone pairs", variable = Cleanup, value = "lps",
          highlightbackground = 'black', indicatoron = 0, selectcolor = 'lightblue', width = 11,height = 2).grid(row = 1 , column = 2 , sticky = N,
            padx = 1, pady = 5)
        #Label(CleanupFrame.interior(), text = "       ").grid(row=2, column = 1, sticky = E+W)

        CleanupFrame.grid(row = 4, column = 0, padx = 10, pady = 2, ipady = 5, sticky = W+E, columnspan = 2)

        RotatableFrame = Pmw.Group(LigandOptionsWin, tag_text = "Activate special\nrotatable bonds")
        Label(RotatableFrame.interior(), text = "yes").grid(row = 0, column = 1, sticky = W)
        Label(RotatableFrame.interior(), text = "no").grid(row = 0, column = 2, sticky = W)
        Label(RotatableFrame.interior(), text = "     backbone   ").grid(row = 1, column = 0, sticky = W)
        Radiobutton(RotatableFrame.interior(), variable = BackboneRotatable, value = True, selectcolor = 'green' ).grid(row = 1 , column = 1, sticky = W ) # Default
        Radiobutton(RotatableFrame.interior(), variable = BackboneRotatable, value = False , selectcolor = 'red').grid(row = 1 , column = 2, sticky = W )
        Label(RotatableFrame.interior(), text = "     amide   ").grid(row = 2, column = 0, sticky = W)
        Radiobutton(RotatableFrame.interior(), variable = AmideRotatable, value = True, selectcolor = 'green' ).grid(row = 2 , column = 1, sticky = W ) # Raccoon default
        Radiobutton(RotatableFrame.interior(), variable = AmideRotatable, value = False, selectcolor = 'red' ).grid(row = 2 , column = 2, sticky = W ) # ADT default
        Label(RotatableFrame.interior(), text = " guanidinium   ").grid(row = 3, column = 0, sticky = W)
        Radiobutton(RotatableFrame.interior(), variable = GuanidiniumRotatable, value = True, selectcolor = 'green' ).grid(row = 3 , column = 1, sticky = W )
        Radiobutton(RotatableFrame.interior(), variable = GuanidiniumRotatable, value = False, selectcolor = 'red' ).grid(row = 3 , column = 2, sticky = W ) # Default
        #Label(RotatableFrame.interior(), text = "       ").grid(row=4, column = 1, sticky = E+W)
        RotatableFrame.grid(row = 5, column = 0, padx = 10, pady = 2, ipady = 5, sticky = W+E)

        Checkbutton(LigandOptionsWin, text = "Inactivate ALL active\ntorsions", variable = LockTors,
            indicatoron = False, highlightbackground = 'black', selectcolor = 'lightblue' ).grid(row = 5 , column = 1, sticky = W, rowspan = 1, padx = 5, pady = 5, ipadx = 3, ipady = 3)

        FragmentFrame = Pmw.Group(LigandOptionsWin, tag_text = "Fragmented structures")
        Radiobutton(FragmentFrame.interior(), text = "keep largest fragment", variable = LargestFrag, 
            value = True, selectcolor = 'lightblue' ).grid(row = 0 , column = 0, sticky = W )
        Label(FragmentFrame.interior(), text = "           ").grid(row=0, column = 1, sticky = E+W)
        Radiobutton(FragmentFrame.interior(), text = "keep all", variable = LargestFrag, value = False, selectcolor = 'lightblue' ).grid(row = 0 , column = 2, sticky = W, ) # Default
        Checkbutton(FragmentFrame.interior(), text = "Attach non-bonded fragments", variable = AttachFrag, 
            highlightcolor = 'black', selectcolor = 'lightblue', indicatoron = False).grid(row = 1 , column = 0, sticky = W+E, columnspan = 4, ipadx = 2, ipady = 2) 
        FragmentFrame.grid(row = 6, column = 0,  padx = 10, pady = 2, ipady = 5, sticky = W+E, columnspan = 2)

        Tkinter.Button(LigandOptionsWin, compound = LEFT, text="OK", image = ok_icon, command = LigandOptionsWin.destroy,
            highlightbackground = 'black').grid(row = 9, column = 0, sticky = S+W+E, columnspan = 2, pady = 10, padx = 10)
        Tkinter.Button(LigandOptionsWin, compound = LEFT, text="Set defaults", image = default_setting_icon, command = DefaultLigOptions,
            highlightbackground = 'black').grid(row = 1, column = 0, columnspan = 2, sticky = S+W+E, pady = 10, padx = 10)

    
def LigandFilterOptions(): # Filtering files
    global LigandFilterWin, FilterSet, root
    try:
        LigandFilterWin.lift()
    except:
        LigandFilterWin = Toplevel()
        LigandFilterWin.transient(root)
        LigandFilterWin.title("Ligand filters")
        LigandFilterWin.winfo_toplevel().resizable(NO,NO)
        rejected = 0
        total = len(LigandDictionary.keys())
        for item in LigandDictionary.keys():
            if not LigandDictionary[item]["accepted"]:
                rejected += 1
        accepted = total - rejected
        msg = "Total number of ligands: %12s" % str(total)
        TotalNumberLigandsMsg.set(msg)
        msg = "Accepted ligands: %12s" % str(accepted)
        TotAcceptedLigandsMsg.set(msg)
        msg = "Rejected ligands: %12s" % str(rejected)
        TotRejectedLigandsMsg.set(msg)

        # Preset menu
        PresetFrame = Frame(LigandFilterWin)
        Label(PresetFrame, text = "Filter presets :").grid(row = 0, column = 0, columnspan = 1, sticky = E, padx = 10 ) #, padx = 30)
        PrecannedFilters = OptionMenu(PresetFrame, FilterSet, "Default", "Lipinski-like", "DrugLikeness", "DrugLikeness (frag)",
                command = lambda event : FilteringDefaults())
        PrecannedFilters.grid(row = 0, column = 1, columnspan = 1, sticky = W, pady = 10)
        PrecannedFilters.configure(highlightbackground = 'black', width = 25)
        PresetFrame.grid(row = 0, column = 0, columnspan = 4, sticky = N, pady = 10)

        FiltersFrame = Pmw.Group(LigandFilterWin, tag_text = "Molecular properties")
        Label(FiltersFrame.interior(), text = "MIN").grid(row = 1, column = 1, sticky = N)
        Label(FiltersFrame.interior(), text = "MAX").grid(row = 1, column = 2, sticky = N)

        Label(FiltersFrame.interior(), text = "H-bond donors").grid(row = 2, column = 0, sticky = W, padx = 10)
        HbDonors1 = Entry(FiltersFrame.interior(), width = 4, textvariable=HbDmin).grid(row=2, column = 1, sticky = W, columnspan = 1)
        HbDonors2 = Entry(FiltersFrame.interior(), width = 4, textvariable=HbDmax).grid(row=2, column = 2, sticky = W, columnspan = 1)
        Button(FiltersFrame.interior(), text = "Default", image = default_setting_icon, highlightbackground = 'black',
                    command = lambda : FilteringDefaults("HbD")).grid(row = 2, column = 3, padx = 10, pady = 3)

        Label(FiltersFrame.interior(), text = "H-bond acceptors").grid(row = 3, column = 0, sticky = W, padx = 10)
        HbAcceptors1 = Entry(FiltersFrame.interior(), width = 4, textvariable=HbAmin).grid(row=3, column = 1, sticky = W, columnspan = 1)
        HbAcceptors2 = Entry(FiltersFrame.interior(), width = 4, textvariable=HbAmax).grid(row=3, column = 2, sticky = W, columnspan = 1)
        Button(FiltersFrame.interior(), text = "Default", image = default_setting_icon, highlightbackground = 'black',
                    command = lambda : FilteringDefaults("HbA")).grid(row = 3, column = 3, padx = 10, pady = 3)

        Label(FiltersFrame.interior(), text = "Molecular weight").grid(row = 4, column = 0, sticky = W, padx = 10)
        HbAcceptors1 = Entry(FiltersFrame.interior(), width = 4, textvariable=MWmin).grid(row=4, column = 1, sticky = W, columnspan = 1)
        HbAcceptors2 = Entry(FiltersFrame.interior(), width = 4, textvariable=MWmax).grid(row=4, column = 2, sticky = W, columnspan = 1)
        Button(FiltersFrame.interior(), text = "Default", image = default_setting_icon, highlightbackground = 'black',
                    command = lambda : FilteringDefaults("MW")).grid(row = 4, column = 3, padx = 10, pady = 3)

        Label(FiltersFrame.interior(), text = "Number of atoms").grid(row = 5, column = 0, sticky = W, padx = 10)
        HbAcceptors1 = Entry(FiltersFrame.interior(), width = 4, textvariable=NatMin).grid(row=5, column = 1, sticky = W, columnspan = 1)
        HbAcceptors2 = Entry(FiltersFrame.interior(), width = 4, textvariable=NatMax).grid(row=5, column = 2, sticky = W, columnspan = 1)
        Button(FiltersFrame.interior(), text = "Default", image = default_setting_icon, highlightbackground = 'black',
                    command = lambda : FilteringDefaults("Nat")).grid(row = 5, column = 3, padx = 10, pady = 3)

        Label(FiltersFrame.interior(), text = "Rotatable bonds").grid(row = 6, column = 0, sticky = W, padx = 10)
        HbAcceptors1 = Entry(FiltersFrame.interior(), width = 4, textvariable=TORSDOFmin).grid(row=6, column = 1, sticky = W, columnspan = 1)
        HbAcceptors2 = Entry(FiltersFrame.interior(), width = 4, textvariable=TORSDOFmax).grid(row=6, column = 2, sticky = W, columnspan = 1)
        Button(FiltersFrame.interior(), text = "Default", image = default_setting_icon, highlightbackground = 'black',
                    command = lambda : FilteringDefaults("TORSDOF")).grid(row = 6, column = 3, padx = 10, pady = 3)

        FiltersFrame.grid(row = 1 , column = 0, columnspan = 2, padx = 10)
    
        # Preview info frame
        PreviewFrame = Frame(LigandFilterWin, relief=GROOVE, padx = 10, pady = 10, border = 2)
        TotalLabel = Label(PreviewFrame, textvariable = TotalNumberLigandsMsg).grid(row = 1, column = 0, sticky = E)
        AcceptedLabel = Label(PreviewFrame, textvariable = TotAcceptedLigandsMsg)
        AcceptedLabel.grid(row = 2, column = 0, sticky = E)
        RejectedLabel = Label(PreviewFrame, textvariable = TotRejectedLigandsMsg)
        RejectedLabel.grid(row = 3, column = 0, sticky = E)
        
        PreviewFrame.grid(row = 1, column = 2, padx = 10, sticky = N+S)
        Checkbutton(FiltersFrame.interior(), text = "Filter ligands with non-AD atom types", variable = DoRejectATypes,
                onvalue = True, offvalue = False).grid(row = 7, column = 0, columnspan = 4, pady = 2)

        Button(LigandFilterWin, compound = LEFT, text = "Preview", image = preview_icon, highlightbackground = 'black',
                command = lambda : FilterLigands(False)).grid(row = 1, column = 2, sticky = N, pady = 10) #, columnspan = 3)
        Button(LigandFilterWin, compound = LEFT, text = "Apply", height = 32,  image = ok_icon, highlightbackground = 'black',
                command = lambda : FilterLigands(True)).grid(row = 5, column = 0, columnspan = 4, padx = 10, pady = 10, sticky = W+E)



def FilteringDefaults(param = None):
    # The function set the default values for all the single parameters
     # as well as for the entire sets.
    #
    verbose = False
    if not param:
        param = FilterSet.get()
    # calculate how many torsions are left counting the flex residues, if present
    max_tors = AutoDockMaxTORSDOF.get() - FlexResTORSDOF.get() # Include the FlexResidues into the count of max TORSDOF
    if verbose or DEBUG: print "FILTERING DEFAULTS> setting the max TORSDOF to ", max_tors

    if param == "HbD":
        if FilterSet.get() == "Default":
            HbDmin.set(0), HbDmax.set(99)
        if FilterSet.get() == "Lipinski-like":
            HbDmin.set(0), HbDmax.set(5)
        if FilterSet.get() == "DrugLikeness":
            HbDmin.set(0), HbDmax.set(5)
        if FilterSet.get() == "DrugLikeness (frag)":
            HbDmin.set(0), HbDmax.set(3)

    if param == "HbA":
        if FilterSet.get() == "Default":
            HbAmin.set(0), HbAmax.set(99)
        if FilterSet.get() == "Lipinski-like":
            HbAmin.set(0), HbAmax.set(10)
        if FilterSet.get() == "DrugLikeness":
            HbAmin.set(0), HbAmax.set(10)
        if FilterSet.get() == "DrugLikeness (frag)":
            HbAmin.set(0), HbAmax.set(6) 

    if param == "MW":
        if FilterSet.get() == "Default":
            MWmin.set(0), MWmax.set(9999)
        if FilterSet.get() == "Lipinski-like":
            MWmin.set(0), MWmax.set(500)
        if FilterSet.get() == "DrugLikeness":
            MWmin.set(160), MWmax.set(480)
        if FilterSet.get() == "DrugLikeness (frag)":
            MWmin.set(160), MWmax.set(300)

    if param == "Nat":
        if FilterSet.get() == "Default":
            NatMin.set(0), NatMax.set(999) # TODO use the right value for unix (2048) or cygwin (128) max atoms ?
        if FilterSet.get() == "Lipinski-like":
            NatMin.set(0), NatMax.set(999)
        if FilterSet.get() == "DrugLikeness":
            NatMin.set(20), NatMax.set(70)
        if FilterSet.get() == "DrugLikeness (frag)":
            NatMin.set(6), NatMax.set(45)

    if param == "TORSDOF":
        if FilterSet.get() == "Default":
            TORSDOFmin.set(0), TORSDOFmax.set(max_tors)
        if FilterSet.get() == "Lipinski-like":
            TORSDOFmin.set(0), TORSDOFmax.set(max_tors)
        if FilterSet.get() == "DrugLikeness":
            TORSDOFmin.set(0), TORSDOFmax.set(max_tors)
        if FilterSet.get() == "DrugLikeness (frag)":
            TORSDOFmin.set(0), TORSDOFmax.set(max_tors)

    # set the Raccoon defaults
    if not param or param == "Default":
        HbDmin.set(0), HbDmax.set(99)
        HbAmin.set(0), HbAmax.set(99)
        MWmin.set(0), MWmax.set(9999)
        NatMin.set(0), NatMax.set(999)
        TORSDOFmin.set(0), TORSDOFmax.set(max_tors)
        DoRejectATypes.set(True)
    
    # http://en.wikipedia.org/wiki/Lipinski%27s_Rule_of_Five
    if param == "Lipinski-like":
        HbDmin.set(0), HbDmax.set(5)
        HbAmin.set(0), HbAmax.set(10)
        MWmin.set(0), MWmax.set(500)
        NatMin.set(0), NatMax.set(999)
        TORSDOFmin.set(0), TORSDOFmax.set(max_tors)
        DoRejectATypes.set(True)

    # http://en.wikipedia.org/wiki/Lipinski%27s_Rule_of_Five#cite_note-2
    if param == "DrugLikeness":
        HbDmin.set(0), HbDmax.set(5)
        HbAmin.set(0), HbAmax.set(10)
        MWmin.set(160), MWmax.set(480)
        NatMin.set(20), NatMax.set(70)
        TORSDOFmin.set(0), TORSDOFmax.set(max_tors)
        DoRejectATypes.set(True)

    # Values from Fattori's paper
    #Drugs R D. 2008;9(4):217-27.
    # Fragment-based approach to drug lead discovery: overview and advances in various techniques.
    # Fattori D, Squarcia A, Bartoli S.
    if param == "DrugLikeness (frag)":
        HbDmin.set(0), HbDmax.set(3)
        HbAmin.set(0), HbAmax.set(6)
        MWmin.set(160), MWmax.set(300)
        NatMin.set(6), NatMax.set(45)
        TORSDOFmin.set(0), TORSDOFmax.set(max_tors)
        DoRejectATypes.set(True)


def FilterLigands(seriously):
    accepted_ligands = []
    rejected_ligands = []

    verbose = False
    
    # VALIDATE INPUT
    if CheckLigFilterOptions():
        for lig in LigandDictionary.keys():
            lig_hba = LigandDictionary[lig]["HbA"]
            lig_hbd = LigandDictionary[lig]["HbD"]
            lig_tors = LigandDictionary[lig]["TORSDOF"]
            lig_mw = LigandDictionary[lig]["MW"]
            lig_nat = LigandDictionary[lig]["Nat"]
            lig_notstdat = LigandDictionary[lig]["NotStdAT"]
            if lig_notstdat and DoRejectATypes.get():
                #print lig_notstdat
                #print DoRejectATypes.get()
                rejected_ligands.append(lig)
                if verbose or DEBUG: print lig, "rejected by NonSTDatom type", LigandDictionary[lig]["NotStdAT"]
            else:
                # TODO try to implement all the filters at once then reporting the missing ones?
                if lig_hba >= HbAmin.get() and lig_hba <= HbAmax.get():
                    if lig_hbd >= HbDmin.get() and lig_hbd <= HbDmax.get():
                        if lig_tors >= TORSDOFmin.get() and lig_tors <= TORSDOFmax.get():
                            if lig_mw >= MWmin.get() and lig_mw <= MWmax.get():
                                if lig_nat >= NatMin.get() and lig_nat <= NatMax.get():
                                    accepted_ligands.append(lig)
                                    if verbose or DEBUG: print "ACCEPTED", lig
                                else:
                                    rejected_ligands.append(lig)
                                    if verbose or DEBUG: print lig, "rejected number of atoms", lig_nat
                            else:
                                rejected_ligands.append(lig)
                                if verbose or DEBUG: print lig, "rejected molecular weight", lig_mw
                        else:
                            rejected_ligands.append(lig)
                            if verbose or DEBUG: print lig, "rejected torsions", lig_tors
                    else:
                        rejected_ligands.append(lig)
                        if verbose or DEBUG: print lig, "rejected HBD", lig_hbd
                else:
                    rejected_ligands.append(lig)
                    if verbose or DEBUG: print lig, "rejected HBA", lig_hba
        # summarize the filtering process
        total = len(LigandDictionary.keys())
        rejected = len(rejected_ligands)
        accepted = total - rejected
        msg = "Total number of ligands: %12s" % str(total)
        TotalNumberLigandsMsg.set(msg)
        msg = "Accepted ligands: %12s" % str(accepted)
        TotAcceptedLigandsMsg.set(msg)
        msg = "Rejected ligands: %12s" % str(rejected)
        TotRejectedLigandsMsg.set(msg)
        # this variable is set for make TheCheck function quicker
        TotalAcceptedLigands.set(accepted)
        if seriously:
            for lig in rejected_ligands:
                LigandDictionary[lig]["accepted"] = False
            for lig in accepted_ligands:
                LigandDictionary[lig]["accepted"] = True
            LigandsTag()
            try:
                TheCheck()
            except:
                pass
            countLigands()
            try:
                LigandFilterWin.destroy()
            except:
                return

def LigandsTag(): 
    # Color ligands basing on their status ACCEPTED/REJECTED
    acc_col = 'black'
    rej_col = 'red'
    if DEBUG:
        print "Lenght of the LigandScrolledListBox.size(): ", LigandScrolledListBox.size() 
    for item in range(0, LigandScrolledListBox.size()):
        if DEBUG: print "Tagging item ",item, LigandScrolledListBox.get(item)
        if not LigandDictionary[LigandScrolledListBox.get(item)]["accepted"]:
            LigandScrolledListBox.itemconfig(item, fg = 'red') #white', bg = '#aa2200')
        else:
            LigandScrolledListBox.itemconfig(item, fg = 'black') #white', bg = '#22aa00') 
    return

#########################################################################################################
#########################################################################################################
#########################################################################################################
#########################################################################################################
#########################################################################################################
############################### RECEPTOR STUFF

def countReceptors():
    # it works for RC's only
    if len(receptorFileList) > 0:
        message = "Receptor conformations ("+str(len(receptorFileList))+")"
        TargetPDBQT.set(message)
    else:
        TargetPDBQT.set("Import receptor conformations...")

def openReceptorDir(recDir = None):
    problematic_list = []
    if not recDir:
        recDir = askdirectory()
    if recDir:
        queue_in = []
        queue_out = []
        # PDBQT
        recFiles = glob.glob(os.path.join(recDir, "*.pdbqt"))            
        for item in recFiles:
            queue_out.append(item)
        # PDB/MOL2
        recFiles = glob.glob(os.path.join(recDir, "*.pdb"))
        for item in recFiles:
            queue_in.append(item)
        recFiles = glob.glob(os.path.join(recDir, "*.mol2"))
        for item in recFiles:
            queue_in.append(item)

        if len(queue_in) and not tkMessageBox.askokcancel('Non-PDBQT files found',('The directory contains %d structures\
        to be converted in PDBQT.\nDo you want to proceed?' % len(queue_in))):
            tkMessageBox.showwarning("Import skipped", "No structures have been imported")
            return

        DisableInterface()
        for file in queue_in:
            output_file = file.rsplit(".", 1)[:-1][0]+".pdbqt" # 'Efficient' way to get the stem
            InfoMessage.set( (  "=> Generating PDBQT structure for  %s" % (os.path.basename(file)[-5:]) ))
            root.update()
            genPDBQTrec(file, output_file)
            queue_out.append(output_file)
        #if queue_out:
        queue_out, problematic = checkPDBQTreclist(queue_out)
        for item in queue_out:
            if item not in receptorFileList:
                receptorFileList.append(item)
                receptorScrolledListBox.insert('end', item)                
                MultiReceptorSet.set(True)
        countReceptors()
        InfoMessage.set("Receptor structures imported successfully")
        EnableInterface()
        if DoFlex.get() == 1:
            ParseFlexSelection()
        TheCheck()

def openReceptor(filename = None):
    # the input is a list
    if filename:
        recFile = filename
    else:
        recFile = askopenfilename(title = "Select one or more target structures...", filetypes=[("Protein/DNA PDBQT", "*.pdbqt"), ("PDB", "*.pdb"), ("Mol2", "*.mol2")], multiple = 1)
    if recFile:
        queue_in = []
        queue_out = []
        for file in recFile:
            if file[-3:] == "pdb" or file[-4:] == "mol2":
                queue_in.append(file)
            if file[-5:] == "pdbqt":
                queue_out.append(file)
        DisableInterface()
        for file in queue_in:
            output_file = file.rsplit(".", 1)[:-1][0]+".pdbqt" # 'Efficient' way to get the stem
            InfoMessage.set( (  "=> Generating PDBQT structure for  %s" % (os.path.basename(file) )))
            root.update()
            genPDBQTrec(file, output_file)
            queue_out.append(output_file)
        queue_out, problematic =checkPDBQTreclist(queue_out)
        for item in queue_out:
            if item not in receptorFileList:
                receptorFileList.append(item)
                print "ITEM", item
                receptorScrolledListBox.insert('end', item)                
            MultiReceptorSet.set(True)
        InfoMessage.set(   "Receptor structure imported successfully")
        EnableInterface()
        countReceptors()
        if DoFlex.get() == 1:
            ParseFlexSelection()
        TheCheck()



def removeAllReceptors():
    global receptorFileList
    if len(receptorFileList) > 1 and not tkMessageBox.askokcancel('Delete all the receptors.','Do you really want to\nremove all the receptors\nfrom the list?'):
         return
    del receptorFileList[:]
    receptorScrolledListBox.clear()
    MultiReceptorSet.set(False)
    countReceptors()
    TheCheck()


def openSingleReceptor(filename = None): 
    if filename:
        SingleRecFileAsk = filename
    else:
        SingleRecFileAsk = askopenfilename(filetypes=[("Supported formats", ("*.pdbqt", "*.mol2", "*.pdb")), ("PDBQT", "*.pdbqt"), ("PDB", "*.pdb"), ("Mol2", "*.mol2")])
        #ligFile = askopenfilename(parent = root, title = "Select one or more PDBQT, PDB or (multi)MOL2", filetypes=[("Supported ligand formats", ("*.pdbqt", "*.mol2", "*.pdb" )), ("PDBQT", "*.pdbqt"), ("PDB", "*.pdb"), ("Mol2", "*.mol2"), ("Any file type...", "*")], multiple = 1)
    if SingleRecFileAsk:
        # PDBQT structure
        if SingleRecFileAsk[-5:] == "pdbqt":
            if checkPDBQTrec(SingleRecFileAsk):
                singleRecFile = SingleRecFileAsk
                RecFilename.set(SingleRecFileAsk)
                SingleRecFilenameLabel.config(font = ("Helvetica", 10, "bold") ) 
                SingleReceptorSet.set(True)
                ReceptorOptions()
        # PDB/Mol2 receptor
        elif SingleRecFileAsk[-3:] == "pdb" or SingleRecFileAsk[-4:] == "mol2":
            print "PDB/MOL2 receptor"
            output_file = SingleRecFileAsk.rsplit(".", 1)[:-1][0]+".pdbqt" # Efficient way to get the stem
            if genPDBQTrec(SingleRecFileAsk, output_file):
                if checkPDBQTrec(output_file):
                    singleRecFile = output_file
                    RecFilename.set(output_file)
                    SingleRecFilenameLabel.config(font = ("Helvetica", 10, "bold") ) 
                    SingleReceptorSet.set(True)
                    ReceptorOptions()
    else:
        RecFilename.set('')
        SingleReceptorSet.set(False)
        AutoGridWhen3.config(state = DISABLED)
    TheCheck()    

def genPDBQTrec(infile, outfile):
    # If this file closely resemble the Prepare_receptor4.py, it's normal.
    receptor_filename = infile
    outputfilename = outfile

    repair_set = RecRepairOptionsSet.get()
    if repair_set == 'none':
        repairs = None
    if repair_set == 'rebuild bonds':
        repairs = 'bonds'
    if repair_set == 'add H':
        repairs = 'hydrogens'
    if repair_set == 'add H (if missing)':
        repairs = 'checkhydrogens'
    if repair_set == 'rebuild bonds + add H':
        repairs = 'bonds_hydrogens'
    
    charges_to_add = RecChargeSet.get()

    # preserve_charge_types = a             # NEGLECTED AS IN THE LIGANDS
    cleanup = RecCleanNPH.get()+RecCleanLP.get()+RecCleanWAT.get()+RecDelAlternate.get()
    delete_single_nonstd_residues  = RecCleanStdRes.get()
    
    verbose = None
    mode = 'automatic'
    preserve_charge_types = None

    mols = Read(receptor_filename)
    if verbose: print 'read ', receptor_filename
    try:
        mol = mols[0]
    except:
        return False
    preserved = {}
    if charges_to_add is not None and preserve_charge_types is not None:
        preserved_types = preserve_charge_types.split(',') 
        if verbose: print "preserved_types=", preserved_types
        for t in preserved_types:
            if verbose: print 'preserving charges on type->', t
            if not len(t): continue
            ats = mol.allAtoms.get(lambda x: x.autodock_element==t)
            if verbose: print "preserving charges on ", ats.name
            for a in ats:
                if a.chargeSet is not None:
                    preserved[a] = [a.chargeSet, a.charge]

    if len(mols)>1:
        if verbose: print "more than one molecule in file"
        #use the molecule with the most atoms
        ctr = 1
        for m in mols[1:]:
            ctr += 1
            if len(m.allAtoms)>len(mol.allAtoms):
                mol = m
                if verbose: print "mol set to ", ctr, "th molecule with", len(mol.allAtoms), "atoms"
    mol.buildBondsByDistance()

    try:
        RPO = AD4ReceptorPreparation(mol, mode, repairs, charges_to_add, 
                            cleanup, outputfilename=outputfilename,
                            preserved=preserved, 
                            delete_single_nonstd_residues=delete_single_nonstd_residues)    
        if charges_to_add is not None:
            #restore any previous charges
            for atom, chargeList in preserved.items():
                atom._charges[chargeList[0]] = chargeList[1]
                atom.chargeSet = chargeList[0]
        return True
    except:
        if DEBUG: print "genPDBQTrec> problems in generating receptor PDBQT", receptor_filename
        return False


def checkPDBQTrec(filename, quiet = False):
    found_ligand = 0
    found_some_atom = 0
    for line in get_lines(filename):
        if line[0:4] == "ROOT":
            found_ligand = 1
        #if line[0:4] == "ATOM":
        if line.startswith("ATOM"): # or line.startswith("HETATM"):
            found_some_atom = 1
    if found_ligand == 0:
        if found_some_atom == 1:
            return True
        else:
            if not quiet:
                tkMessageBox.showerror("Receptor Error", "The file is not a valid PDBQT.")
            return False
    else:
        if not quiet:
            tkMessageBox.showerror("Receptor Error", "The selected PDBQT file is a ligand file...")
        return False

def SetFlexibleResidueFile(get_name = None):
    global FlexResFileName, FLEX_SET, ResidueStatus, ResidueStatusLoaded, flex_types
    if not get_name:
        get_name = askopenfilename(filetypes=[("Flex residue PDBQT", "*.pdbqt")])
    S = ""
    if get_name:
        FlexResFileName.set("")
        ResidueCount = 0
        try:
            
            lines = get_lines(get_name)
        except:
            tkMessageBox.showerror("Flexibile Residue Error", "Error while opening the flexible residue file:\n"+get_name)
            return False

        for line in lines: 
            if line[0:9] == "BEGIN_RES":
                ResidueCount += 1

        if ResidueCount:
            # Chech that torsions are OK in the flex res file
            # update the message bar
            if ResidueCount >1: S = "s"
            FlexResFileName.set(get_name)
            FlexResDefined.set(True)
            FlexTorsionCount()
###            fp = open(get_name, 'r')
###            resAtms = fp.readlines()
###            fp.close()
###            for ra in resAtms:
###                if ra.startswith('ATOM') or ra.startswith('HETATM'):
###                    flex_types.append(ra.split()[-1])
###            
            ResidueStatusLoaded.set(str(ResidueCount)+" residue"+S+" loaded [ "+str(FlexResTORSDOF.get())+" rotatable bonds ]")
            ResidueStatus.set(ResidueStatusLoaded.get())
        else:
            tkMessageBox.showerror("Flexibile Residue Error", "The loaded PDBQT file is not a flexible residue.")
            ResidueStatus.set("")
    else:
        FlexResTORSDOF.set(0)
        FlexResFileName.set("")
        ResidueStatus.set("")
        FlexTorsionCount()
    TheCheck()

def FlexTorsionCount(force = False):
    """-checks the number of rotatable bonds of selected/loaded flexible residues """
    verbose = False

    if force:
        FlexResTORSDOF.set(0)
        TORSDOFmax.set(AutoDockMaxTORSDOF.get())
        FilteringDefaults("TORSDOF")
        return

    found_flex_tors = 0

    if FlexResFileName.get() == "" and ListFlexResiduesNames.get() == "":
        return

    # File mode
    if DoFlexFromWhat.get() == 1 and not FlexResFileName.get() == "":
        try:
            lines = get_lines(FlexResFileName.get())
        except:
            if DEBUG: print "FlexTorsionCount> problems in reading the flex file:", FlexResFileName.get()
            tkMessageBox.showerror( ("FlexTorsionCount> problems in reading the flex file:", FlexResFileName.get()) )
            return False

        for line in lines:
            if "active torsions" in line:
                found_flex_tors +=  int(line.split()[1])
    # Selection mode
    if DoFlexFromWhat.get() == 2 and not ListFlexResiduesNames.get() == "":
        list_of_residues = []
        list_of_flex_res_atypes = []
        selection = ListFlexResiduesNames.get()
        selection = selection.replace(' ', '')
        selection = selection.split(',')
        for res in set(selection):
            res = res.split(':')
            res_nam = res[-1][0:3]
            list_of_residues.append(res_nam)
        for res in list_of_residues:
            found_flex_tors += ResidueRotatableBondTable[res][0]
        if verbose or DEBUG: print " adding %s rot's for %s" % ( ResidueRotatableBondTable[res_nam][0], res_nam)
        if verbose or DEBUG: print "FLEX> this is the final count of rotatable bonds included for the flex res count:", found_flex_tors

    # Too many rotatable bonds reached
    if found_flex_tors > AutoDockMaxTORSDOF.get():
        tkMessageBox.showerror("Too many rotatable bonds", ("The imported flex residues have %s rotatable bonds.\n\
The maximum number of rotatable bonds allowed by AutoDock is %s." % (found_flex_tors, AutoDockMaxTORSDOF.get() )))
        FlexResTORSDOF.set(0)
        # Remove the flex res settings
        if DoFlexFromWhat.get() == 1:
                FlexResFileName.set("")
                FlexResDefined.set(False)
                ResidueStatus.set("")
                FlexResTORSDOF.set(0)
                TORSDOFmax.set(AutoDockMaxTORSDOF.get())
                FilteringDefaults("TORSDOF")
                TheCheck()
                return False
        if DoFlexFromWhat.get() == 2:
                ResidueStatus.set("[ none ]") 
                FlexResDefined.set(False)
                FlexResTORSDOF.set(0)
                TORSDOFmax.set(AutoDockMaxTORSDOF.get())
                FilteringDefaults("TORSDOF")
                TheCheck()
                return False

    # Maximum rotatable bonds limit reached
    if found_flex_tors == AutoDockMaxTORSDOF.get():
        tkMessageBox.showwarning("Rotatable bonds limit", ("The imported flex residues have the maximum number of allowed rotatable \
bonds (%s).\n\nOnly rigid ligands will be accepted for the docking!" % (AutoDockMaxTORSDOF.get() )))
    FlexResTORSDOF.set( found_flex_tors )

    if len(LigandDictionary):
        tkMessageBox.showinfo("AutoDock rotatable bonds", ("The imported flex residues have %s rotatable bonds.\n\nThe maximum \
number of rotatable bonds for ligands will be set set to %s and the ligand set will be filtered with this \
value." % (found_flex_tors, AutoDockMaxTORSDOF.get()-found_flex_tors )  ))
    FilteringDefaults("TORSDOF")
    FilterLigands(True)
    if DEBUG:
        print "FLEX> found a total of %s rotatable bonds in the flexible residue" % found_flex_tors
    return True 
        


def EnableFlexFromFile():
    global Single_target_radio, Multi_target_radio, SingleTargetPanel, MultiTargetPanel, group_receptor1
    global group_receptor2, ResidueOrigin, receptorScrolledListBox 
    global SingleRecStatus,  FlexResFile, ImportFlexResPDBQT, FlexResFileNameLabel, FlexResListEntry
    global FlexResStatus, FlexResListSet,  DoFlex, ResidueStatus, ResidueStatusLoaded
    # Activate all buttons to load and display flex res filename
    ImportFlexResPDBQT.config(state=NORMAL)
    FlexResFileNameLabel.config(state=NORMAL)
    # Deactivate all buttons to select flex res filename
    FlexResListEntry.config(state = DISABLED)
    FlexResListSet.config(state = DISABLED)
    # Check if there was a previous filename defined 
    # and test the file again, else undefine 
    # the FlexResDefined (maybe activated from a selection of residues)
    if FlexResFileName.get() == '':
        FlexResDefined.set(False)

    ResidueStatus.set(ResidueStatusLoaded.get())
    try:
        FlexTorsionCount()
    except:
        pass
    try:
        TheCheck()
    except:
        return


def EnableFlexFromSel():
    global Single_target_radio, Multi_target_radio, SingleTargetPanel, MultiTargetPanel, group_receptor1
    global group_receptor2, ResidueOrigin, receptorScrolledListBox, SingleRecStatus,  FlexResFile, ImportFlexResPDBQT
    global FlexResFileNameLabel, FlexResListEntry, FlexResStatus,FlexResListSet,  DoFlex, ResidueStatus
    # Activate all buttons to load and display flex res filename
    ImportFlexResPDBQT.config(state=DISABLED)
    FlexResFileNameLabel.config(state=DISABLED)
    # Deactivate all buttons to select flex res filename
    FlexResListEntry.config(state = NORMAL)
    FlexResListSet.config(state = NORMAL)
    # Check if there was a previous selection defined and
    # test it again, else undefine the FlexResDefined (maybe activated from a filename)
    if not ListFlexResiduesNames.get() == '':
        FlexResDefined.set(False)
    ResidueStatus.set(ResidueStatusSelected.get())
    try:
        ParseFlexSelection()
    except:
        pass
    try:
        TheCheck()
    except:
        return


def ParseFlexSelection():
    verbose = False
    if not DoFlexFromWhat.get() == 2:
        return
    # figure out if the receptor is the single conformation or a multi_snapshot
    if RCstatus.get() == 0 and SingleReceptorSet.get():
        receptor_list = [RecFilename.get()]
    elif RCstatus.get() == 1 and MultiReceptorSet.get():
        receptor_list = receptorScrolledListBox.get('0', END)
    else:
        if RCstatus.get() == 0:
            SingleRecButton.flash()
        if RCstatus.get() == 1:
            AddAReceptorButton.flash()
        return

    found = []
    missing = []
    chain_list = []

    found_flex_tors = 0

    selection = ListFlexResiduesNames.get()
    selection = selection.replace(' ', '')
    selection = selection.split(',')
    # ARG9, B:THR276

    if not selection == ['']: #    empty residue list... don't waste my time, please...
        for receptor in receptor_list:
            # File opening
            if verbose or DEBUG: print "============> Checking receptor", receptor
            # TODO add a try/except
            file = open(receptor, 'r')
            protein = file.readlines()
            file.close
            del found[:]

            for res in set(selection): # changed from "selection" to "set(selection)" to avoid duplicates
                FOUND = False
                residue = res
                if verbose or DEBUG: print "\nThis would be the residue", res
                res = res.split(':')
                if verbose or DEBUG: print res
                res_nam = res[-1][0:3]
                if verbose or DEBUG: print "residue name  =>", res_nam
                res_num = res[-1][3:]
                if verbose or DEBUG: print "residue numb  =>", res_num
                if res_num == '':
                    if verbose or DEBUG: print "NO NUMBER SPECIFIED!"
                    tkMessageBox.showwarning("Wrong residue(s) specification", "Residues must be specified using\
the following syntax.\nFor example, 'threonine 276' can be either:\n\n\tTHR276\n\t\
( any )\n\n\tB:THR276\n\t       ( chain B only )\n\nMultiple residues can be specified\
by separating them with a comma (',') as:\n\n\tTHR276, HIS229\n\n\tB:THR276, B:HIS229")
                    FlexResDefined.set(False)
                    TheCheck()
                    return False
                if len(res) > 1: # there is a chain specification
                    chain = res[-2]
                    if verbose or DEBUG: print "chain         =>", chain
                else:
                    chain = ''
                for line in protein:
                    if line[0:4] == 'ATOM' or line[0:6] == 'HETATM':
                        if res_nam == line[17:20].split()[0]:
                            if res_num == line[22:26].split()[0]:
                                if chain in line[21]:
                                    FOUND = True
                                    if verbose or DEBUG: print line # useful for debugging, do not remove!
                                    if line[21] not in chain_list:
                                        chain_list.append(line[21])
                if FOUND:
                    if verbose or DEBUG: print "FOUND THE RESIDUE %s in %s" % (res, receptor)
                    found.append([residue, ( len(chain_list) )])
                    del chain_list[:]
                else:
                    missing.append(residue)
                    if verbose or DEBUG: print "XXXX this res is missing: ", res
                    if verbose or DEBUG:    print "this is a window with an error of residue"
            if len(missing) > 0:
                if verbose or DEBUG: print "XXXX some residues are missing"
                if verbose or DEBUG: print "this is a window with an error of residue"
                if verbose or DEBUG: print missing
                msg_missing = '\n'
                for item in missing:
                    msg_missing = msg_missing+"\t-> "+item+"\n"
                tkMessageBox.showwarning("Unable to find residue(s)", ("The following residue(s) \
are missing:\n"+msg_missing+"\n\n - Check the syntax (i.e. \'THR276', 'B:THR276' or 'B:THR276,B:HIS229')\n\n - Specify different residues.\n"))
                ResidueStatus.set("[ none ]") 
                FlexResDefined.set(False)
                TheCheck()
                return False
        if len(selection) == len(found):
            total = 0
            for i in range(len(found)):
                total = total + found[i][1]
            # The selection is copied into the variable used at the end
            FlexResSelected.set(ListFlexResiduesNames.get())
            # here goes the check torsions
            if not FlexTorsionCount():
                return False
            ResidueStatusSelected.set(( str(total)+" residue(s) selected [ "+ str(FlexResTORSDOF.get())+" rotatable bonds ]"))

            ResidueStatus.set(ResidueStatusSelected.get())
            FlexResDefined.set(True)

            TheCheck()
            return True
        else:
            FlexResDefined.set(False)
            ResidueStatusSelected.set("[ none ]")
            TheCheck()
            return False
    else: # empty the residue definition if no argument is present in the entry    
        if DEBUG: print "no residues"
        ResidueStatusSelected.set("[ none ]")
        ResidueStatus.set("[ none ]") 
        FlexResDefined.set(False)
        TheCheck()
        if DEBUG: print "again, no residues"
        return False



def MakeReceptorMenu():
    global Single_target_radio, Multi_target_radio, SingleTargetPanel, MultiTargetPanel, group_receptor1, group_receptor2, ResidueOrigin, receptorScrolledListBox,  FlexResFile, ImportFlexResPDBQT, FlexResFileName, FlexResFileNameLabel, FlexResList, FlexResListEntry, FlexResStatus, FlexResListSet, DoFlex, ResidueStatus, SingleRecFilenameLabel, SingleRecButton, AddAReceptorButton

    ReceptorRadioChoice = Pmw.Group( p2, tag_pyclass = None)
    ReceptorRadioChoice = Frame( p2, bd = 0)
    ReceptorRadioChoice.pack()
    Single_target_radio = Radiobutton(ReceptorRadioChoice, compound = RIGHT, text='Single\ntarget', width = 120,
            image = single_rec_icon, value=0, variable=RCstatus, state=ACTIVE, command=ReceptorOptions, 
            indicatoron = False, selectcolor = 'lightblue', disabledforeground = 'gray', highlightbackground = 'black')
    Single_target_radio.bind("<Button-3>", lambda x : help("recmode"))
    Multi_target_radio = Radiobutton(ReceptorRadioChoice, compound = LEFT, text='Multiple\ntargets', width = 120,
            image = multi_rec_icon, value=1, variable=RCstatus, command=ReceptorOptions, indicatoron = False,
            selectcolor = 'lightblue', disabledforeground = 'gray', highlightbackground = 'black')
    Single_target_radio.pack(anchor=NW, side = LEFT, expand = 0, padx = 5, pady = 5)
    Multi_target_radio.pack(anchor=NW, side = LEFT, expand = 0, padx = 5, pady = 5)
    Multi_target_radio.bind("<Button-3>", lambda x : help("recmode"))

    # Group containing the structure(s) choices ###################################
    group_receptor1 = Pmw.Group(p2, tag_textvariable = TargetPDBQT)

    # Single receptor menu
    SingleTargetPanel = Frame(group_receptor1.interior(), relief=FLAT ) 
    SingleRecFilenameLabel = Label(SingleTargetPanel, textvariable = RecFilename)
    SingleRecFilenameLabel.pack()



    #add_single_icon = Tkinter.PhotoImage(data=icon_open_b64)
    SingleRecButton = Button(SingleTargetPanel, compound = LEFT, text="Add receptor file...", image = add_single_icon, command = openSingleReceptor)
    SingleRecButton.pack(expand=YES, anchor=CENTER, side=LEFT)
    SingleRecButton.configure(highlightbackground = 'black')
    SingleRecButton.bind("<Button-3>", lambda x : help("loadsinglerec"))
    
    # Multi-receptor menu
    MultiTargetPanel = Frame(group_receptor1.interior(), relief=FLAT)
    MultiTargetPanel.bind("<Button-3>", lambda x : help("recmultimode"))
    MultiTargetPanel.configure(highlightbackground = 'black')
    MultiTargetPanel.grid_columnconfigure(0, weight = 1)
    MultiTargetPanel.grid_columnconfigure(1, weight = 1)
    MultiTargetPanel.grid_columnconfigure(2, weight = 1)
    MultiTargetPanel.grid_columnconfigure(3, weight = 1)
    MultiTargetPanel.grid_rowconfigure(0, weight = 1)
    #MultiTargetPanel.grid_rowconfigure(1, weight = 1)
    #MultiTargetPanel.grid_rowconfigure(2, weight = 1)
    #MultiTargetPanel.grid_rowconfigure(3, weight = 1)
    receptorScrolledListBox = Pmw.ScrolledListBox(MultiTargetPanel)
    receptorScrolledListBox.grid(row = 0, column = 0, sticky = N+W+E+S, columnspan = 4)
    AddAReceptorButton = Button(MultiTargetPanel, compound = LEFT, text='Add a structure...', image = add_single_icon, command=openReceptor)
    AddAReceptorButton.grid(row = 1, column = 0, padx = 3, sticky = W)
    AddAReceptorButton.bind("<Button-3>", lambda x : help("loadrec"))
    AddAReceptorButton.configure(highlightbackground = 'black')
    AddDirRecButton = Button(MultiTargetPanel, compound = LEFT, text='Add a directory...', image = add_dir_icon, command=openReceptorDir)
    AddDirRecButton.grid(row = 1, column = 1, padx = 3, sticky = W)
    AddDirRecButton.bind("<Button-3>", lambda x : help("loadrecdir"))
    AddDirRecButton.configure(highlightbackground = 'black')
    DelSelRec = Button(MultiTargetPanel, compound = LEFT, text='Remove selected', image = remove_selected_icon, command=removeReceptor)
    DelSelRec.grid(row = 1, column = 2, padx = 3, sticky = W)
    DelSelRec.bind("<Button-3>", lambda x : help("delselrec"))
    DelSelRec.configure(highlightbackground = 'black')

    DelAllRec = Button(MultiTargetPanel, compound = LEFT, text='Remove all', image = remove_all_icon, command=removeAllReceptors)
    DelAllRec.grid(row = 1, column = 3, padx = 3, sticky = W)
    DelAllRec.bind("<Button-3>", lambda x : help("delallrec"))
    DelAllRec.configure(highlightbackground = 'black')

    group_receptor1.pack(fill = BOTH, expand = 1, padx = 10, pady = 10, anchor = S, side = TOP)


    # Group containing the flexible residues choice #######################################
    group_receptor2 = Pmw.Group(p2, tag_text = 'Flexible residues', tag_pyclass = Tkinter.Checkbutton, tag_variable = DoFlex, tag_command = SetFlexibleMode)
    group_receptor2.pack( expand = 0, padx = 5, pady = 3, anchor = N, side = TOP)    
    group_receptor2.bind("<Button-3>", lambda x : help("flexres"))
    FlexResFile = Radiobutton(group_receptor2.interior(), text='From file', value=1, variable=DoFlexFromWhat, command = EnableFlexFromFile)
    FlexResFile.grid(row = 0, column = 0, sticky = W)
    FlexResFile.bind("<Button-3>", lambda x : help("flexres"))
    ImportFlexResPDBQT = Button(group_receptor2.interior(), image = open_smfolder_icon,  command=SetFlexibleResidueFile)
    ImportFlexResPDBQT.grid(row = 0, column = 1, sticky = W)
    ImportFlexResPDBQT.bind("<Button-3>", lambda x : help("flexres"))
    ImportFlexResPDBQT.configure(highlightbackground = 'black')
    FlexResFileNameLabel = Label(group_receptor2.interior(), textvariable=FlexResFileName)
    FlexResFileNameLabel.grid(row = 0, column = 2, sticky = W)

    FlexResList = Radiobutton(group_receptor2.interior(), text='From selection', value=2, variable=DoFlexFromWhat, command = EnableFlexFromSel)
    #FlexResList.config(fg = 'red')
    FlexResList.grid(row = 1, column = 0, sticky = W)
    FlexResList.bind("<Button-3>", lambda x : help("flexres"))
    FlexResListEntry = Tkinter.Entry(group_receptor2.interior(), textvariable=ListFlexResiduesNames)
    FlexResListEntry.grid(row = 1, column = 1, sticky = W)
    FlexResListEntry.bind("<Button-3>", lambda x : help("flexres"))
    FlexResListSet = Button(group_receptor2.interior(), image = ok_icon, command = ParseFlexSelection)
    FlexResListSet.configure(highlightbackground = 'black')
    FlexResListSet.grid(row = 1, column = 2, sticky = W, padx = 3)
    FlexResListSet.bind("<Button-3>", lambda x : help("flexres"))
    FlexResStatus = Label(group_receptor2.interior(), textvariable = ResidueStatus) 
    FlexResStatus.grid(row = 2, column = 1, sticky = W, columnspan = 3)
    FlexResStatus.bind("<Button-3>", lambda x : help("flexres"))

    DefaultRec = Tkinter.Button(p2, compound = LEFT, text="Target PDBQT generation", image = pdbqt_lig_opt_icon, command = ReceptorImportOptions)
    DefaultRec.pack(anchor = S, side = TOP)
    DefaultRec.bind("<Button-3>", lambda x : help("recpdbqtopt"))
    DefaultRec.configure(highlightbackground = 'black')



def ReceptorImportOptions():

    global RecRepairOptions
    try:
        ReceptorOptionsWin.lift()
    except:
        ReceptorOptionsWin = Toplevel(root)
        ReceptorOptionsWin.transient(root)
        ReceptorOptionsWin.title("Receptor PDBQT generation options")
        ReceptorOptionsWin.winfo_toplevel().resizable(NO,NO)
        ChargeFrame = Pmw.Group(ReceptorOptionsWin, tag_text = "Partial charges")
        Radiobutton(ChargeFrame.interior(), text="Add Gasteiger", variable = RecChargeSet, value = "gasteiger", indicatoron = 0, width = 15,
            highlightbackground = 'black', selectcolor = 'lightblue').grid(row = 0, column = 0, sticky = W, padx = 5, pady = 5) # Default
        Radiobutton(ChargeFrame.interior(), text="Keep original", variable = RecChargeSet, value = "", indicatoron = 0, width = 15,
            highlightbackground = 'black', selectcolor = 'lightblue').grid(row = 0, column = 1, sticky = W, padx = 5, pady = 5)
        ChargeFrame.grid(row = 2, column = 0, padx = 10, pady = 5, sticky = N)

        CleanupFrame = Pmw.Group(ReceptorOptionsWin, tag_text = "Remove")
        Label(CleanupFrame.interior(), text = "yes").grid(row = 0, column = 1, sticky = W, pady = 2)
        Label(CleanupFrame.interior(), text = "no").grid(row = 0, column = 2, sticky = W, pady = 2)
        Label(CleanupFrame.interior(), text = "Non-polar hydrogens").grid(row = 1, column = 0, sticky = E, pady = 3)
        Radiobutton(CleanupFrame.interior(), variable = RecCleanNPH, value = "_nphs", selectcolor = "green").grid(row = 1 , column = 1, sticky = N, pady = 3) 
        Radiobutton(CleanupFrame.interior(), variable = RecCleanNPH, value = "" , selectcolor = "red").grid(row = 1 , column = 2, sticky = N, pady = 3)
        Label(CleanupFrame.interior(), text = "Lone pairs").grid(row = 2, column = 0, sticky = E, pady = 3)
        Radiobutton(CleanupFrame.interior(), variable = RecCleanLP, value = "_lps", selectcolor = 'green' ).grid(row = 2 , column = 1, sticky = N , pady = 3) 
        Radiobutton(CleanupFrame.interior(), variable = RecCleanLP, value = "", selectcolor = 'red' ).grid(row = 2 , column = 2, sticky = N , pady = 3) 
        Label(CleanupFrame.interior(), text = "Water molecules").grid(row = 3, column = 0, sticky = E, pady = 3)
        Radiobutton(CleanupFrame.interior(), variable = RecCleanWAT, value = "_waters" , selectcolor = 'green').grid(row = 3 , column = 1, sticky = N , pady = 3)
        Radiobutton(CleanupFrame.interior(), variable = RecCleanWAT, value = "", selectcolor = 'red' ).grid(row = 3 , column = 2, sticky = N , pady = 3)
        Label(CleanupFrame.interior(), text = "Non-standard residues").grid(row = 4, column = 0, sticky = E, pady = 3)
        Radiobutton(CleanupFrame.interior(), variable = RecCleanStdRes, value = True , selectcolor = 'green').grid(row = 4 , column = 1, sticky = N , pady = 3)
        Radiobutton(CleanupFrame.interior(), variable = RecCleanStdRes, value = False, selectcolor = 'red' ).grid(row = 4 , column = 2, sticky = N , pady = 3)
        Label(CleanupFrame.interior(), text = "Alternate conformations").grid(row = 5, column = 0, sticky = E, pady = 3)
        Radiobutton(CleanupFrame.interior(), variable = RecDelAlternate, value = "deleteAltB" , selectcolor = 'green').grid(row = 5 , column = 1, sticky = N , pady = 3)
        Radiobutton(CleanupFrame.interior(), variable = RecDelAlternate, value = "", selectcolor = 'red' ).grid(row = 5 , column = 2, sticky = N , pady = 3)
        CleanupFrame.grid(row = 3, column = 0, padx = 10, pady = 5, sticky = N+W+E)

        RepairFrame = Pmw.Group(ReceptorOptionsWin, tag_text = "Structure repair")
        # label
        RecRepairOptions = OptionMenu(RepairFrame.interior(), RecRepairOptionsSet, "none", "rebuild bonds", "add H", "add H (if missing)",
            "rebuild bonds + add H")
        RecRepairOptions.config(width = 30, highlightbackground = 'black')
        RecRepairOptions.grid(row = 4, padx = 10, sticky = N, pady = 5)
        RepairFrame.grid(row = 5, column = 0, padx = 10, pady = 5, sticky = N+W+E)

        Tkinter.Button(ReceptorOptionsWin, compound = LEFT, text="OK", image = ok_icon, command = ReceptorOptionsWin.destroy,
            highlightbackground = 'black').grid(row = 9, column = 0, sticky = W+E, columnspan = 2, pady = 10, padx = 10)
        Tkinter.Button(ReceptorOptionsWin, compound = LEFT, text="Set defaults", image = default_setting_icon,command = ReceptorOptionsDefault,
            highlightbackground = 'black').grid(row = 0, column = 0, columnspan = 3, sticky = W+E, pady = 10, padx = 10)


def ReceptorOptionsDefault():
    RecChargeSet.set('gasteiger')
    RecCleanNPH.set('_nphs')
    RecCleanLP.set('_lps')
    RecCleanWAT.set('_waters')
    RecCleanStdRes.set(False)
    RecDelAlternate.set('')
    RecRepairOptionsSet.set('add H (if missing)')




def ReceptorOptions():
    verbose = False
    global SingleTargetPanel, MultiTargetPanel, group_receptor1, group_receptor2, RCstatus, FlexResFile, ImportFlexResPDBQT, FlexResFileNameLabel, FlexResList, FlexResListEntry, AutoGridWhen1, AutoGridWhen2, AutoGridWhen3 #, TargetPDBQT

    if RCstatus.get() == 0: # Single Target
        if verbose: print "I'm running the RCstatus with this value:", RCstatus.get()
        MultiTargetPanel.forget()
        SingleTargetPanel.pack(expand = YES, fill = 'x')
        TargetPDBQT.set("Receptor structure")
        if DoFlex.get() == 1:
            FlexResFile.config(state=NORMAL)
            ImportFlexResPDBQT.config(state=NORMAL)
            FlexResFileNameLabel.config(state=NORMAL)
            ParseFlexSelection()
        if AutoGridWhen2:
            if not system == "Windows":
                AutoGridWhen2.config(state = NORMAL)

        if AutoGridWhen3 and TotalAcceptedLigands.get():
            AutoGridWhen3.config(state = NORMAL)
        
    if RCstatus.get() == 1: # Multiple Targets 
        if verbose: print "I'm running the RCstatus with this value:", RCstatus.get()
        SingleTargetPanel.forget()
        FlexResFile.config(state=DISABLED)
        FlexResFileNameLabel.config(state=DISABLED)
        ImportFlexResPDBQT.config(state=DISABLED)
        countReceptors()
        if DoFlex.get() == 1:
            ParseFlexSelection()

        MultiTargetPanel.pack(expand = YES, fill = BOTH)
        if AutoGridWhen3:
            AutoGridWhen3.config(state = DISABLED)
    try:
        TheCheck()
    except:
        return

def SetFlexibleMode():
    global Single_target_radio, Multi_target_radio, SingleTargetPanel, MultiTargetPanel, group_receptor1, group_receptor2, ResidueOrigin, receptorScrolledListBox, SingleRecStatus,  FlexResFile, ImportFlexResPDBQT, FlexResFileNameLabel, FlexResListEntry, FlexResStatus,FlexResListSet,  DoFlex

    # To initialize the default flexible option as "from file"
    if DoFlexFromWhat.get() == -1:
        FlexResFile.invoke()

    if DoFlex.get() == 0:
        FlexResFile.config(state = DISABLED)
        ImportFlexResPDBQT.config(state=DISABLED)
        FlexResFileNameLabel.config(state=DISABLED)
        FlexResList.config(state = DISABLED)
        FlexResListEntry.config(state = DISABLED)
        FlexResListSet.config(state = DISABLED)
        FlexResStatus.config(state = DISABLED)
        FlexResListSet.config(state = DISABLED)
        FlexTorsionCount(force = True)
        try:
            TheCheck()
        except:
            pass
    if DoFlex.get() == 1:
        if RCstatus.get() == 0: # Single receptor mode enable the "From file button"
            FlexResFile.config(state = NORMAL)
            ImportFlexResPDBQT.config(state=NORMAL)
            FlexResFileNameLabel.config(state=NORMAL)
            FlexResListSet.config(state = NORMAL)
        FlexResList.config(state = NORMAL)
        FlexResListEntry.config(state = NORMAL)
        FlexResStatus.config(state = NORMAL)
        FlexResListSet.config(state = NORMAL)
        FlexResListSet.config(state = NORMAL)
        FlexTorsionCount()
        try:
            TheCheck()
        except:
            pass


###### Estetical tricks

def FontSizeInc():
    pass
    # TODO

def FontSizeDec():
    pass
    # TODO

#########################
### GPF RELATED FUNCTIONS

def MakeGPFMenu():
    global CacheMapFrame, GPFframe, CacheMapHandleNow, CacheMapHandle, GPFcontent, GPFedit, GPFsave, GPFFilenameLabel, GPFload, CacheMapDir, CacheMapDirLabel, MapFolderList

    # The GPF management facility is contained here in GPFframe
    # GPF edit group  
    GPFframe = Pmw.Group(p3, tag_text = 'Grid Parameter File')
    GPFframe.interior().grid_columnconfigure(1, weight = 1) # make the grid items flexible
    GPFframe.interior().grid_rowconfigure(1,weight = 1)     # make the grid items flexible   

    GPFload = Button(GPFframe.interior(), compound = LEFT, text='Load template...', image = open_smfolder_icon, 
        highlightbackground = 'black', command=opengpf)
    GPFload.grid(row = 0, column = 0, sticky = W, columnspan = 1)
    GPFedit = Button(GPFframe.interior(), compound = LEFT, text='Edit', image = edit_icon, 
        highlightbackground = 'black', command=editGPF, state = ACTIVE)
    GPFedit.grid(row = 2, column = 0, sticky = W)
    GPFsave = Button(GPFframe.interior(), compound = LEFT, text='Save', image = ok_icon, 
        highlightbackground = 'black', command=saveGPFchanges)#, state = DISABLED)
    GPFFilenameLabel = Label(GPFframe.interior(), textvariable=GPFfilename, state = DISABLED)
    GPFFilenameLabel.grid(row = 0, column = 1, sticky = E)
    # GPF Text editor
    GPFcontent = Text(GPFframe.interior(), bg = 'white') #, height=22, width = 100)
    GPFscroll = Scrollbar(GPFframe.interior(), command=GPFcontent.yview)
    GPFscroll.grid(row = 1, column = 3, sticky = N+S)
    GPFcontent.grid_columnconfigure(1, weight = 1)
    GPFcontent.grid_rowconfigure(1,weight = 1)
    GPFcontent.configure(yscrollcommand=GPFscroll.set)
    GPFcontent.grid(row = 1, column = 0, columnspan = 3, sticky = N+S+W+E)
    GPFcontent.config(fg = 'black', font = ("Courier", 10, "normal"))

    CacheMapHandleNow = Pmw.Group(GPFframe.interior(), tag_text="Cached maps")
    CacheMapOptionsNow = OptionMenu(CacheMapHandleNow.interior(), CacheMapPolicy, "Make copies [ use more disk space ]", "Make symbolic links [ save disk space ]")
    CacheMapPolicy.set('Make copies [ use more disk space ]')
    CacheMapOptionsNow.grid(row = 1, column = 3, columnspan = 2)


    # The cached maps management facility is contained here in CacheMapFrame
    # Cached maps group    
    CacheMapFrame = Pmw.Group(p3, tag_text = 'Pre-calculated maps')
    CacheMapDir = Button(CacheMapFrame.interior(), compound = LEFT, text='Select cached maps directory', image = open_smfolder_icon, command=opendirMaps) #, state = DISABLED)
    CacheMapDir.grid(row = 0, column = 0)
    CacheMapDirLabel = Label(CacheMapFrame.interior(), textvariable = CacheMapDirName, state = DISABLED)
    CacheMapDirLabel.grid(row = 0, column = 1)
    # Maps folder browser
    MapFolderScroll = Scrollbar(CacheMapFrame.interior())
    MapFolderList = Listbox(CacheMapFrame.interior(), yscrollcommand = MapFolderScroll.set, width = 90, bg = 'white')
    MapFolderScroll.config(command = MapFolderList.yview )
    # TODO Add an orizontal scroll list?
    MapFolderScroll.grid(row = 1, column = 3, sticky = N+S)
    MapFolderList.grid(row = 1, column = 0, sticky = W+E, columnspan = 3)
    MapFolderList.insert(END, "[no map directory defined yet... ]")
    MapFolderScroll = Scrollbar(CacheMapFrame.interior(), command = MapFolderList.yview)

    CacheMapHandle = Pmw.Group(CacheMapFrame.interior(), tag_text="Cached maps")
    CacheMapOptions = OptionMenu(CacheMapHandle.interior(), CacheMapPolicy, "Make copies [ use more disk space ]", "Make symbolic links [ save disk space ]")
    CacheMapPolicy.set('Make copies [ use more disk space ]')
    CacheMapOptions.grid(row = 5, column = 1, columnspan = 2)
    CacheMapHandle.grid(row = 2, column = 0, columnspan = 2)

    if system == "Windows":
        CacheMapOptionsNow.config(state = DISABLED)
        CacheMapOptions.config(state = DISABLED)

def MapMenu():
    for item in CacheMapFrame, GPFframe, CacheMapHandle:
        if item:
                item.forget()
        try: 
            if AGoptions:
                AGoptions.forget()
        except:
            pass
        if CacheMapHandleNow:
            CacheMapHandleNow.grid_forget()
    state = MapSource.get()
    if state == 0: # Use the GPF to run AutoGrid in all the jobs
        GPFframe.pack(fill = BOTH, expand = 1, padx = 10, pady = 3, side = TOP, anchor = N)
    if state == 1: # Use the GPF to run AutoGrid now, then cache the maps
        AGoptions.pack()
        GPFframe.pack(fill = BOTH, expand = 1, padx = 10, pady = 3, anchor = N)
        CacheMapHandleNow.grid(row = 2, column = 1, sticky = W, columnspan = 1)
        if not AutoGridBin.get():
            WhichAutoGrid()
    if state == 2: # Use the maps in the cache folder
        CacheMapFrame.pack(fill = BOTH, expand = 1, padx = 10, pady = 10)
    try:
        TheCheck()
    except:
        pass


def setGPFtags(): # Inspired by:  http://effbot.org/tkinterbook/text.htm
    GPFcontent.tag_remove('keyword', '1.0', END)
    GPFcontent.tag_remove('comment', '1.0', END)
    for keyw in GPFkeywords:
        idx = '1.0'
        while 1:
            idx = GPFcontent.search(keyw, idx, stopindex=END)
            if not idx: break
            lastidx = '%s+%dc' % (idx, len(keyw))
            if idx.split('.')[1] == "0":
                GPFcontent.tag_add('keyword', idx, lastidx)
            idx = lastidx
        GPFcontent.tag_config('keyword', font = ("Courier", 10, "bold"), foreground = 'blue')
    idx = '1.0'
    while 1:
        idx = GPFcontent.search("#", idx, stopindex=END)
        if not idx: break
        lastidx = idx.split('.')[0]+".end"
        GPFcontent.tag_add('comment', idx, lastidx)
        idx = lastidx
        GPFcontent.tag_config('comment', foreground = 'gray')

def removeGPFtags(): # Inspired by:  http://effbot.org/tkinterbook/text.htm
    GPFcontent.tag_remove('keyword', '1.0', END)
    GPFcontent.tag_remove('comment', '1.0', END)


def opengpf():
    # Provides:
    #  GPFlines = list of lines contained in the GPF (=> prepare_x scripts)
    #  GPFParameterFile = filename of the parameter file required by the GPF (if found)
    #
    global GPFlines, GPFcontent, GPFedit, GPFsave, GPFFilenameLabel, GPFParameterFile

    GPFcontent.tag_config("npts", foreground="red")
    gpfFile = askopenfilename(filetypes=[("Grid Parameter File", "*.gpf"), ("Any file...", "*")])
    if DEBUG: print gpfFile
    
    if gpfFile:
        gpftemplate = gpfFile
        ask_for_param_file = 0
        GPFParameterFile.set("")
        GPFcontent.config(state = NORMAL)
        GPFcontent.delete(1.0, END) 
        for line in get_lines(gpfFile): # surprisingly, adding the text to the editor worked at the first attempt....
            if line[0:14] == "parameter_file":
                if DEBUG: print "I found a param file in %s!" % gpfFile
                ask_for_param_file = 1
                param_file_name = line.split()[1]
            GPFcontent.insert(END, line)
        GPFlines = GPFcontent.get(1.0, END)
        GPFfilename.set(gpfFile)
        GPFFilenameLabel.config(state = NORMAL)
        if ask_for_param_file == 1:
            tkMessageBox.showwarning("Parameter file required", "A parameter file is required by the GPF:\n => %s \n The filename location must be specified..." % param_file_name)
            askGPFParamFile(param_file_name)
        else:
            GPFcontent.config(state = DISABLED)
            GPFedit.config(state = ACTIVE)
    setGPFtags()
    TheCheck()

def askGPFParamFile(filename):
    # ask the user the location of the ADX.X_xxxx.dat file found in the GPF
    #
    # Provides:
    #  defines the GPFParameterFile
    keepasking = True
    while keepasking == True:
        parameter_filename = askopenfilename(filetypes=[("AutoDock Parameter File", filename)])
        if parameter_filename:
            GPFParameterFile.set(parameter_filename) 
            keepasking = False
            GPFcontent.config(state = DISABLED)
            GPFedit.config(state = ACTIVE)
            return True
        else:
            answer = tkMessageBox.askquestion('Warning', 'The file is required by the GPF.\nDo you want to define it?')
            if answer == "no":
                tkMessageBox.showwarning("Error", "The file is essential for this GPF.\nRe-import the GPF and set the correct parameter file.")
                # empty the GPF buffer and the entry in GPF the editor
                GPFlines = None
                GPFcontent.delete(1.0, END) 
                GPFfilename.set("[ no GPF loaded ]")
                keepasking = False
                GPFcontent.config(state = DISABLED)
                GPFedit.config(state = ACTIVE)
                return False

def editGPF():
    # TODO change this to use a single widget that's updated
    # basing on the function...
    GPFcontent.config(state = NORMAL)
    GPFedit.grid_forget()
    GPFload.config(state = DISABLED)
    GPFcontent.config(fg = 'red', font = ("Courier", 10, "bold"))
    GPFsave.config(fg = 'red')
    GPFsave.grid(row = 2, column = 0, sticky = W)
    removeGPFtags()

def saveGPFchanges():
    # TODO change this to use a single widget that's updated
    # basing on the function...
    GPFlines = GPFcontent.get(1.0, END)
    GPFload.config(state = NORMAL)
    GPFcontent.config(fg = 'black', font = ("Courier", 10, "normal"))
    GPFcontent.config(state = DISABLED)
    parseGPF()
    GPFsave.grid_forget()
    setGPFtags() 
    GPFedit.grid(row = 2, column = 0, sticky = W)
    #setGPFtags()

def disableGPF(): 
    GPFcontent.config(fg = 'gray', font = ("Courier", 10, "normal"))
    GPFcontent.config(state = DISABLED)
    GPFedit.config(state = ACTIVE)
    GPFload.config(state = DISABLED)
    GPFFilenameLabel.config(state = DISABLED)
    if not CacheMapDirName.get() == "[ none ]":
        CacheMapDir.config(state = NORMAL)
    else:
        CacheMapDir.config(state = NORMAL)
        CacheMapDir.flash()

def enableGPF():
    GPFcontent.config(fg = 'black', font = ("Courier", 10, "normal"))
    GPFcontent.config(state = NORMAL)
    GPFedit.config(state = NORMAL)
    GPFload.config(state = NORMAL)
    CacheMapDir.config(state = DISABLED)
    setGPFtags()

def opendirMaps(mapfolder = None): 
    # Check map integrity and presence of all maps for all atom types
    #
    #
    #
    global LIGAND_SET , mapDir 
    FldFound, XyzFound = False, False
    accepted_maps = []
    if not mapfolder:
        mapDir = askdirectory(title = "Select the dir containing the grid maps...")
    else:
        mapDir = mapfolder
    if mapDir:
        MapFolderList.delete(0, END)
        DoCachedMaps.set(False)
        # collect all the atomic maps
        mapFiles = glob.glob(os.path.join(mapDir, "*.map"))
        # add the *.fld and *.xyz maps
        for extra_map in glob.glob(os.path.join(mapDir, "*.maps.*")):
            mapFiles.append(extra_map)
        # Prune possible dirs matching "*map*" pattern
        for item in mapFiles:
            if os.path.isdir(item):
                del mapFiles[mapFiles.index(item)]

        if len(mapFiles):
            for map in mapFiles:
                # TODO ugly and potentially fragile, fix this
                if map[-8:] == "maps.fld":
                    FldFound = True
                if map[-8:] == "maps.xyz":
                    XyzFound = True
        if not FldFound: # manage possible errors
            tkMessageBox.showerror("Map file not found!", "The .fld map is missing.\nSelect another directory.")
        elif not XyzFound:
            tkMessageBox.showerror("Map file not found!", "The .xyz map is missing.\nSelect another directory.")
        # ...then check for necessary atom types if ligands have been set
        if XyzFound and FldFound:
            CheckFolderMap(mapFiles)
        TheCheck()

def CheckFolderMap(MapFileList):
    # Check for mapfiles for all the atom types (+e +d) that
    # are found in the ligands of the Great Book of Ligands
    # and assure that all the maps are consistent
    # (same parameters)
    MissingMaps = []
    FolderIsOk = True
    MapConsistency = True
    del MissingMaps[:]
    
    receptor_stem = (os.path.basename(RecFilename.get())).split(".")[0]
    if DEBUG: print "CheckFolderMap> RECEPTOR_STEM", receptor_stem
    # Check for all atom types maps
    name_consistency = True
    if DEBUG: 
        for x in AtypeList: print x, AtypeList[x][0]
    #print "AtypeList = ", AtypeList

    for atype in AtypeList.keys():
        if AtypeList[atype][0] > 0:
            missing = 1
            for map in MapFileList:
                if atype == map.split(".")[-2]: 
                    missing = 0
                    break
            if missing == 0:
                # name consistency check
                if not os.path.basename(map).split(".")[0] == receptor_stem:
                    name_consistency = False
                    if DEBUG : 
                        print "inconsistency",
                        print os.path.basename(map).split(".")[0],
                        print receptor_stem
            if missing == 1:   
                MissingMaps.append(atype)

    for atype in AtypeList_special.keys():
        if AtypeList_special[atype][0] > 0:
            missing = 1
            for map in MapFileList:
                if atype == map.split(".")[-2]: 
                    missing = 0
                # name consistency check
                if not os.path.basename(map).split(".")[0] == receptor_stem:
                    name_consistency = False
                    if DEBUG : 
                        print "inconsistency(special)",
                        print os.path.basename(map).split(".")[0],
                        print receptor_stem
            if missing == 1:   
                MissingMaps.append(atype)

    # manage possible name errors
    if not name_consistency:
        if not tkMessageBox.askokcancel('Warning', ("One or more map filenames doesn't match with the receptor \
name.\n\n\t'%s'\n\n Are you sure you want to continue?" % (receptor_stem+".pdbqt"))):
            MapFolderList.delete(0, END)
            DoCachedMaps.set(False)
            CacheMapDirName.set("[ none ]")
            CacheMapDirLabel.config(state = DISABLED)
            InfoMessage.set("Cached maps inconsistency: aborted by user.")
            return False

    #GetAtypes(selection = )
    # Selection mode
    if DoFlexFromWhat.get() == 2 and not ListFlexResiduesNames.get() == "":
        for res_type in ListFlexResiduesNames.get():
            flex_types += ResidueRotatableBondTable[res_type][0]
        for atype in AtypeList:
            if AtypeList[atype][0] > 0:
                missing = 1
                for map in MapFileList:
                    if atype == map.split(".")[-2]: 
                        missing = 0
                if missing == 1:   
                    MissingMaps.append(atype)

    # Check for number of points
    if len(MissingMaps) == 0:
        mapheader = []
        mapheader_checking = []
        try:
            for file in MapFileList:
                if file[-3:] == "map":
                    MAP = open(file, 'r')
                    # first map populates the map reference dictionary
                    # TODO Very ugly: use get_lines and slices to get the first 6 lines...
                    if len(mapheader) == 0:
                        line = MAP.next()
                        for count in '123456':
                            mapheader.append(line)
                            line = MAP.next()
                        MAP.close()
                    else:
                        line = MAP.next()
                        for count in '123456':
                            mapheader_checking.append(line)
                            line = MAP.next()
                        MAP.close()
                        if not mapheader == mapheader_checking:
                            MapConsistency == False
                        else:
                            MapConsistency == True
                            del mapheader_checking[:]
        except:
            if DEBUG: print "CheckFolderMap> Houston, we've got a problem in checking maps..."
            MapConsistency = False

        if MapConsistency:
            for item in MapFileList:
                MapFolderList.insert('end', item)
                CacheMapDirName.set(mapDir)
                CacheMapDirLabel.config(state = NORMAL)
            DoCachedMaps.set(True)
            return True
        else:
            tkMessageBox.showwarning("Map files are not coherent!", "The maps doesn't have the same properties\
                            (i.e npoints, resolution...). Please check them or select another folder")
            CacheMapDirName.set("[ none ]")
            CacheMapDirLabel.config(state = DISABLED)
            AutoGridWhen1.invoke() # Select the default as "Run AG in each job"
            return False
    else: # One or more maps are missing...
        MapFolderList.delete(0, END)
        DoCachedMaps.set(False)
        message_missing = ""
        for mmap in MissingMaps:
            message_missing = message_missing+"==> "+mmap+"\n"

        CacheMapDirName.set("[ none ]")
        CacheMapDirLabel.config(state = DISABLED)
        tkMessageBox.showwarning("Map file not found!",
        "The following maps are missing:\n\n%s\nRe-define the directory or use different ligands."% message_missing)
        AutoGridWhen1.invoke() # Select the default as "Run AG in each job"
        return False


def parseGPF():
    # parse the gpf to check if it's all ok.
    gpf_lines = GPFcontent.get(1.0, END)
    kw_list = { 'npts' : 0,
                'spacing' : 0,
                'gridcenter' : 0,
                'smooth' : 0,
                'dielectric': 0 }
    #parm_found = False
    for line in gpf_lines.split('\n'):
        if line.strip(): # get rid of empty lines
            line = line.split("#")[0] # get rid of comments
            line = line.split(" ", 1)
            kw = line[0]
            if kw == "npts":
                try:
                    argument = line[1].split()
                    if not len(argument) == 3:
                        raise
                    for i in argument:
                        float(i)
                    kw_list[kw] = 1
                except:
                    pass
            if kw == "spacing":
                try:
                    float(line[1].replace(" ", ""))
                    kw_list[kw] = 1
                except:
                    pass
            if kw == "gridcenter":
                argument = line[1].split()
                try:
                    if not len(argument) == 3:
                        raise
                    for i in argument:
                        float(i)
                    kw_list[kw] = 1
                except:
                    pass
            if kw == "smooth":
                try:
                    float(line[1].replace(" ", ""))
                    kw_list[kw] = 1
                except:
                    pass
            if kw == "dielectric":
                try:
                    float(line[1].replace(" ", ""))
                    kw_list[kw] = 1
                except:
                    pass
            if kw == "parameter_file":
                try:
                    parameter_argument = line[1].strip() # parameter_file xxxx.xx#comment
                    if not parameter_argument in GPFParameterFile.get():
                        askGPFParamFile(parameter_argument)
                except:
                    tkMessageBox.showerror("GPF template", ("An error occurred when reading the parameter file line" ))
    problems = False
    missing = ''
    for k in kw_list:
        if kw_list[k] == 0:
            problems = True
            missing += k+"\n"
    if problems:
        tkMessageBox.showerror("GPF template", ("There are errors in the GPF template.\n\nThe following keywords are missing or not correctly used:\n\n"+missing+"\nCorrect the template and try again"))
        return False
    else:
        return True
"""            
            if kw == "parameter_file":
                try:
                    parameter_argument = line[1].strip() # parameter_file xxxx.xx#comment
                    if not parameter_argument in GPFParameterFile.get():
                        askGPFParamFile(parameter_argument)
                except:
                    tkMessageBox.showerror("GPF template", ("An error occurred when reading the parameter file line:\n%s" (line[1]+line[2]) ) )
"""

def parseDPF():
    # to be expanded to read the keywords?
    dpf_lines = DPFcontent.get(1.0, END)

    for line in dpf_lines.split('\n'):
        if line.strip(): # get rid of empty lines
            line = line.split("#")[0] # get rid of comments
            line = line.split(" ", 1)
            kw = line[0]
            if kw == "parameter_file":
                try:
                    parameter_argument = line[1].strip() # parameter_file xxxx.xx#comment
                    if not parameter_argument in DPFParameterFile.get():
                        askDPFParamFile(parameter_argument)
                except:
                    tkMessageBox.showerror("DPF template", ("An error occurred when reading the parameter file line" ))


def docking_setup_interface(event):
    global Info, numGen, EnEval, simple_settings, simple_settings_info 
    global EnEval, OpenDPF, DPF_group, docking_set, CheckTDOF, CheckVOL 
    global complex_gen_info, complex_eval_info, DPF_INFO, InfoFrame, dockMenuSettings
    global DPFcontent, DPFscroll, DPFedit, DPFsave, DPFfilename, DPFFilenameLabel, simple_settings_info
    global DPFgroupTemplate, DPFgroupSimple, DPFgroupComplex, DPFgroupSmart

    if not DPFgroupTemplate:
        DPFgroupTemplate = Pmw.Group(p4, tag_text = 'Docking Parameter File')
    if not DPFgroupSimple:
        DPFgroupSimple = Pmw.Group(p4, tag_text = 'DPF simple settings')
    if not DPFgroupComplex:
        DPFgroupComplex = Pmw.Group(p4, tag_text = 'DPF manual settings')
    if not DPFgroupSmart:
        DPFgroupSmart = Pmw.Group(p4, tag_text = 'SmartDPF Settings')
    DPFgroupNone = Pmw.Group(p4, tag_pyclass = None) # UGLY, VERY UGLY WORKAROUND
    DPFgroupTemplate.forget()
    DPFgroupSimple.forget()
    DPFgroupComplex.forget()
    DPFgroupSmart.forget()

    if not dockMenuSettings:
        dockMenuSettings = OptionMenu(p4, docking_set, "From template...", command=docking_setup_interface)
        dockMenuSettings.pack()
    if not docking_set.get():
        docking_set.set("[ select docking setup ]") # default value
    if docking_set.get() == "From template...":
        OpenDPF = Button(DPFgroupTemplate.interior(), compound = LEFT, text='Load template...', image = open_smfolder_icon,  
            highlightbackground = 'black', command=opendpf)
        DPFedit = Button(DPFgroupTemplate.interior(), compound = LEFT, text='Edit', image = edit_icon, 
            highlightbackground = 'black', command=editDPF, state = ACTIVE)
        DPFsave = Button(DPFgroupTemplate.interior(), compound = LEFT, text='Save', image = ok_icon, 
            highlightbackground = 'black', command=saveDPFchanges)
        DPFFilenameLabel = Label(DPFgroupTemplate.interior(), textvariable=DPFfilename, state = DISABLED)
        DPFdefault = Button(DPFgroupTemplate.interior(), compound = LEFT, text='default', image = default_setting_icon, 
            highlightbackground = 'black', command = MkDefaultDPF)
        DPFgroupTemplate.interior().grid_columnconfigure(1, weight = 1) # make the grid items flexible
        DPFgroupTemplate.interior().grid_rowconfigure(1,weight = 1)     # make the grid items flexible   
        # DPF Text editor
        if not DPFcontent:
            DPFcontent = Text(DPFgroupTemplate.interior(), bg = 'white') #, height=22, width = 100)
        DPFscroll = Scrollbar(DPFgroupTemplate.interior(), command=DPFcontent.yview)
        DPFcontent.configure(yscrollcommand=DPFscroll.set)
        DPFcontent.config(fg = 'black', font = ("Courier", 10, "normal"))
        
        OpenDPF.grid(row = 0, column = 0, sticky = N+W)
        DPFedit.grid(row = 2, column = 0, sticky = S+W)
        DPFFilenameLabel.grid(row = 0, column = 1, sticky = N+E)
        DPFdefault.grid(row = 0, column = 2, sticky = N+E)

        DPFscroll.grid_columnconfigure(1, weight = 1)
        DPFscroll.grid_rowconfigure(1,weight = 1)

        DPFscroll.grid(row = 1, column = 3, sticky = N+S)
        DPFcontent.grid(row = 1, column = 0, columnspan = 4, rowspan = 1, sticky = N+S+W+E)
        DPFgroupTemplate.pack(expand = 1, fill = 'both', anchor = N)
    DPFgroupNone.pack_forget()


def MkDefaultDPF():
    # Substitute the current content of the DPF editor
    # with the canonical DPF with all default values
    # (as from ADT)
    if len(DPFcontent.get(1.0, END)) > 1:
        if not tkMessageBox.askokcancel("Default DPF", "The default set of parameters will overwrite the current DPF.\n\n\
Are you sure?"):
            return
    DPFcontent.config(state = NORMAL)
    DPFcontent.delete(1.0, END) 
    DPFfilename.set(" AutoDock default ")
    DPFFilenameLabel.config(state = DISABLED)
    DPFcontent.insert(END, default_docking_parameter_file)
    DPFedit.config(state = NORMAL)
    setDPFtags()
    TheCheck()
    return

    

def setDPFtags(): 
    # TODO the DPF validation should be made here...
    DPFcontent.tag_remove('keyword', '1.0', END)
    DPFcontent.tag_remove('comment', '1.0', END)
    for keyw in DPFkeywords:
        idx = '1.0'
        while 1:
            idx = DPFcontent.search(keyw, idx, stopindex=END)
            if not idx: break
            lastidx = '%s+%dc' % (idx, len(keyw))
            if idx.split('.')[1] == "0":
                DPFcontent.tag_add('keyword', idx, lastidx)
            idx = lastidx
        DPFcontent.tag_config('keyword', font = ("Courier", 10, "bold"), foreground = 'blue')
    idx = '1.0'
    while 1:
        idx = DPFcontent.search("#", idx, stopindex=END)
        if not idx: break
        lastidx = idx.split('.')[0]+".end"
        DPFcontent.tag_add('comment', idx, lastidx)
        idx = lastidx
        DPFcontent.tag_config('comment', foreground = 'gray')

def removeDPFtags(): 
    DPFcontent.tag_remove('keyword', '1.0', END)
    DPFcontent.tag_remove('comment', '1.0', END)


# TODO this part should be re-written to split different check functions and catch
#      users trying to sneak in parameter_file keywords, for example...

def opendpf():
    # Provides:
    #  DPFlines = list of lines contained in the DPF (=> prepare_x scripts)
    #  DPFParameterFile = filename of the parameter file required by the DPF (if found)
    #
    global DPFlines, DPFcontent, DPFedit, DPFsave, DPFFilenameLabel, DPFParameterFile

    #dpfFile = askopenfilename(filetypes=[("Docking Parameter File", "*.dpf")])
    dpfFile = askopenfilename(filetypes=[("Docking Parameter File", "*.dpf"), ("Any file...", "*")])
    if DEBUG: print dpfFile
    if dpfFile:
        dpftemplate = dpfFile
        ask_for_param_file = 0
        DPFParameterFile.set("")
        DPFcontent.config(state = NORMAL)
        DPFcontent.delete(1.0, END) 
        for line in get_lines(dpfFile):
            if line[0:14] == "parameter_file":
                if DEBUG: print "Found a param file!", line
                ask_for_param_file = 1 
                param_file_name = line.split("#")[0]
                param_file_name = param_file_name.split("parameter_file")[1].strip()
                param_file_name = os.path.basename(param_file_name)
            DPFcontent.insert(END, line)
        DPFlines = DPFcontent.get(1.0, END)
        DPFfilename.set(dpfFile)
        DPFFilenameLabel.config(state = NORMAL)
        if ask_for_param_file == 1:
            tkMessageBox.showwarning("Parameter file required", "A parameter file is required by the DPF:\n => %s \n The filename location must be specified..." % param_file_name)
            askDPFParamFile(param_file_name)
        else:
            DPFcontent.config(state = DISABLED)
            DPFedit.config(state = NORMAL)
    setDPFtags()
    TheCheck()

def editDPF():
    DPFcontent.config(state = NORMAL)
    DPFedit.grid_forget()
    DPFcontent.config(fg = 'red', font = ("Courier", 10, "bold"))
    OpenDPF.config(state = DISABLED)
    DPFsave.config(fg = 'red')
    DPFsave.grid(row = 3, column = 0, sticky = W)
    removeDPFtags()

def saveDPFchanges():
    DPFlines = DPFcontent.get(1.0, END)
    DPFcontent.config(fg = 'black', font = ("Courier", 10, "normal"))
    DPFcontent.config(state = DISABLED)
    parseDPF()
    OpenDPF.config(state = NORMAL)
    DPFsave.grid_forget()
    DPFedit.grid(row = 3, column = 0, sticky = W)
    setDPFtags()


def askDPFParamFile(filename):
    # ask the user the location of the ADX.X_xxxx.dat file found in the DPF
    #
    # Provides:
    #  defines the GPFParameterFile
    keepasking = True
    while keepasking == True:
        parameter_filename = askopenfilename(filetypes=[("AutoDock Parameter File", filename)])
        if parameter_filename:
            DPFParameterFile.set(parameter_filename)
            keepasking = False
            DPFcontent.config(state = DISABLED)
            DPFedit.config(state = NORMAL)
            break
        else:
            answer = tkMessageBox.askquestion('Warning', 'The file is required by the DPF.\nDo you want to define it?')
            if answer == "no":
                tkMessageBox.showwarning("Error", "The file is essential for this DPF.\nRe-import the DPF and set the correct parameter file.")
                # empty the GPF buffer and the entry in GPF the editor
                DPFlines = None
                DPFcontent.delete(1.0, END) 
                DPFfilename.set("[ no DPF loaded ]")
                DPFFilenameLabel.config(state = DISABLED)
                #DPFedit.config(state = DISABLED)
                DPFedit.config(state = ACTIVE)
                keepasking = False

##################################### DPF CLASS

def get_AD_atom_types(filename):
    atypes = []
    try:
        for line in get_lines(filename):
            if line[0:6] == 'HETATM' or line[0:4] == 'ATOM':
                atype = line.split()[-1]
                if atype not in atypes:
                    atypes.append(atype)
        return atypes
    except:
        if DEBUG: print "get_AD_atom_types> problems in reading the file: ", filename
        tkMessageBox.showerror("Error in reading the file", ("Impossible to read the file\n %s\n" % filename))
        return False


def prepareGPFfast(gpf_filename, receptor_filename, rec_types, lig_types):
    DEBUG=False
    if DEBUG:
        print "prepareGPFfast> "
        print "     GPF_FILENAME:",gpf_filename
        print "     RECEPTOR_FILENAME:",receptor_filename
        print "     REC_TYPES:",rec_types
        print "     LIG_TYPES:",lig_types
    if not rec_types:
        rec_types = get_AD_atom_types(receptor_filename)
    if not rec_types:
        tkMessageBox.showerror("Receptor properties error", ("Impossible to access to receptor properties, aborting..."))
        if DEBUG: print "prepareDPFfast> problems in reading the file: ", ligand_filename
        return False

    """
    if flex_res_filename:
        if not flex_res_types:
            flex_res_types = get_AD_atom_types(flex_res_filename)
    if not flex_res_types:
        tkMessageBox.showerror("Flexible residues properties error", ("Impossible to access to flexible residues properties, aborting..."))
        if DEBUG: print "prepareDPFfast> problems in reading the file: ", flex_res_filename
        return False

        IF THERE'S A RECEPTOR FILENAME, THE_FUNCTION SHOULD HAVE ALREADY PROVIDED THE RIGHT ATOM TYPES

    """
    
    rec_name = os.path.basename(receptor_filename)
    rec_name = os.path.splitext(rec_name)[0]

    parameter_file = None
    if not parseGPF:
        return False

    for line in GPFcontent.get(1.0, END).split('\n'):
        line = line.split("#")[0]
        if line.strip():
            line = line.split(" ", 1)
            kw = line[0]
            arg = line[1]
            if kw == 'npts':
                npts = arg# .split()
        
            # TODO handle here the param file!
            #

            if kw == 'spacing':
                spacing = arg
            if kw == 'gridcenter':
                gridcenter = arg
            if kw == 'smooth':
                smooth = arg
            if kw == 'dielectric':
                dielectric = arg
            if kw == 'parameter_file':
                parameter_file = arg.strip()

    text  = "npts %s\n" % npts
    if parameter_file:
        text += "parameter_file %s\n" % parameter_file
    text += "gridfld %s.maps.fld\n" % rec_name
    text += "spacing %s\n" % spacing
    text += "receptor_types "
    for a in rec_types:
        text += a+" "
    text += "\n"
    text += "ligand_types "
    for a in lig_types:
        text += a+" "
    text += "\n"
    text += "receptor %s.pdbqt\n" % rec_name
    text += "gridcenter %s\n" % gridcenter
    text += "smooth %s\n" % smooth
    for a in lig_types:
        text += "map %s.%s.map\n" % (rec_name, a)
    text += "elecmap %s.e.map\n" % rec_name
    text += "dsolvmap %s.d.map\n" % rec_name
    text += "dielectric %s\n" % dielectric

    try:

        file = open(gpf_filename, 'w')
        file.write(text)
        file.close()
        #writeLines(gpf_filename, text, do_strip=False)
        return True
    except:
        if DEBUG: print "prepareGPFfast> problems in saving the file: ", gpf_filename
        tkMessageBox.showerror("GPF generation error", ("Impossible to save the file\n"+gpf_filename+"\n\n"))
        return False

def prepareDPFfast(dpf_filename, receptor_filename, ligand_filename, lig_types, flex_res_filename = None, parameter_file = None):
    # TODO
    # -add the support for custom template file DONE
    # -handle command combinations?
    # flex_res?

    def get_mol_center(filename):
        x,y,z  = 0., 0., 0.
        counter = 0
        for l in get_lines(filename):
            if l[0:6] == 'HETATM' or l[0:4] == 'ATOM':
                counter += 1
                x += float(l[30:38])
                y += float(l[38:46])
                z += float(l[46:54])
        return [x/counter, y/counter, z/counter]

    # variables
    seed = "auto"
    ga_run = 100
    write_all = False
    # /variables
    # rec atom types

    # some defaults : keep them as strigs...
    rms_tol = "2.0" # TODO part of the autotune?
    ga_run = "100"
    local_search_mode = "set_psw1"
    energy_model = "unbound_model bound"


    # parameter parser
    dpf_lines = DPFcontent.get(1.0, END).split("\n")
    
    outlev = None
    intnbp_r_eps = []
    for i,l in enumerate(dpf_lines):
        l = l.split("#")[0]
        l = l.split()
        if DEBUG: print "prepareDPFfast> line parsing:", l
        if l:
            if "outlev" in l:
                outlev = l[1]
            if "ga_pop_size" in l:
                ga_pop_size = l[1]
            if "ga_num_evals" in l:
                ga_num_evals = l[1]
            if 'intnbp_r_eps' in l:
                intnbp_r_eps.append(dpf_lines[i])
            if "ga_num_generations" in l:
                ga_num_generations = l[1]
            if "ga_elitism" in l:
                ga_elitism = l[1]
            if "ga_mutation_rate" in l:
                ga_mutation_rate = l[1]
            if "ga_crossover_rate" in l:
                ga_crossover_rate = l[1]
            if "ga_window_size" in l:
                ga_window_size = l[1]
            if "ga_cauchy_alpha" in l:
                ga_cauchy_alpha = l[1]

            if "ga_cauchy_beta" in l:
                ga_cauchy_beta = l[1]
            if "sw_max_its" in l:
                sw_max_its = l[1]

            if "sw_max_succ" in l:
                sw_max_succ = l[1]
            if "sw_max_its" in l:
                sw_max_its = l[1]
            if "sw_max_fail" in l:
                sw_max_fail = l[1]
            if "sw_rho" in l:
                sw_rho = l[1]
            if "sw_lb_rho" in l:
                sw_lb_rho = l[1]

            if "ls_search_freq" in l:
                ls_search_freq = l[1]
            
            if ("set_psw1" in l) or ("set_sw1" in l):
                local_search_mode = l[0]

            if "rms_tol" in l:
                rms_tol = l[1]

            if "unbound_model" in l:
                energy_model = l[0]+" "+l[1]
                
            if "ga_run" in l:
                ga_run = l[1]

            if "write_all" in l:
                write_all = True

            if "analysis" in l:
                clustering = "analysis"


    # ligand data
    try:
        about = get_mol_center(ligand_filename)
        if DEBUG: print "prepareDPFfast> LIGAND: %s\t\t about : %3.2f  %3.3f %3.3f" % (ligand_filename, about[0], about[1], about[2])
        if not lig_types:
            lig_types = LigandDictionary[ligand_filename]['Atypes']
            # TODO deprecated! atypes should be provided in advance to include potential flex_res_atom types
    except:
        if DEBUG: print "prepareDPFfast> problems in getting ligand center: ", ligand_filename
        tkMessageBox.showerror("Receptor properties error", ("Impossible to access to receptor properties, aborting..."))

        return False

    # flex res handling #
    """
    if flex_res_filename:
        if not flex_res_types:
            flex_res_types = get_AD_atom_types(flex_res_filename)
    if not flex_res_types:
        tkMessageBox.showerror("Flexible residues properties error", ("Impossible to access to flexible residues properties, aborting..."))
        if DEBUG: print "prepareDPFfast> problems in reading the file: ", flex_res_filename
        return False
    for a in flex_res_types:
        if not a in lig_types:
            lig_types.append(a)
    """

    if DEBUG: print "prepareDPFfast> getting flex_res atom types"
    if flex_res_filename:
        for a in get_AD_atom_types(flex_res_filename):
            if not a in lig_types:
                lig_types.append(a)

    rec_name = os.path.basename(receptor_filename)
    rec_name = os.path.splitext(rec_name)[0]

    # TODO change this to an append?
    text = "# Generated with Raccoon v.%s\n" % version
    if not outlev == None:
        text += "outlev %s\n" % outlev
    if parameter_file:
        text += "parameter_file %s\n"% os.path.basename(parameter_file)
    text += "intelec\n"
    if seed == "auto":
        text += "seed time pid\n"

    text += "ligand_types "
    for a in lig_types:
        text += a+" "
    text += "\n"
    text += "fld %s.maps.fld\n" % rec_name
    for a in lig_types:    
        text += "map %s.%s.map\n" % (rec_name, a)
    text += "elecmap %s.e.map\n" % rec_name
    text += "desolvmap %s.d.map\n" % rec_name
    for l in intnbp_r_eps:
        text += "%s\n" % l
    text += "move %s\n" % os.path.basename(ligand_filename)
    if flex_res_filename:
        text += "flexres %s\n" % os.path.basename(flex_res_filename)
    text += "about %3.3f %3.3f %3.3f\n" % (about[0], about[1], about[2])
    text +="tran0 random\n"
    text +="quat0 random\n"
    text +="axisangle0 random\n"
    text +="dihe0 random\n"
    text +="rmstol %s\n" % rms_tol
    text +="ga_pop_size %s\n" % ga_pop_size
    text +="ga_num_evals %s\n" % ga_num_evals
    text +="ga_num_generations %s\n" % ga_num_generations
    text +="ga_elitism %s\n" % ga_elitism
    text +="ga_mutation_rate %s\n" % ga_mutation_rate
    text +="ga_crossover_rate %s\n" % ga_crossover_rate
    text +="ga_window_size %s\n" % ga_window_size
    text +="ga_cauchy_alpha %s\n" % ga_cauchy_alpha
    text +="ga_cauchy_beta %s\n" % ga_cauchy_beta
    text +="set_ga\n"
    text +="sw_max_its %s\n" % sw_max_its
    text +="sw_max_succ %s\n" % sw_max_succ
    text +="sw_max_fail %s\n" % sw_max_fail
    text +="sw_rho %s\n" % sw_rho
    text +="sw_lb_rho %s\n" % sw_lb_rho
    text +="ls_search_freq %s\n" % ls_search_freq
    text +="%s\n" % local_search_mode # set_psw1
    text +="%s\n" % energy_model # unbound_model bound...
    text +="ga_run %s\n" % ga_run
    if write_all:
        text += "write_all\n"

    if clustering:
        text += "%s\n" % clustering

    try:
        file = open(dpf_filename, 'w')
        file.write(text)
        file.close()
        #writeLines(dpf_filename, text, do_strip=False)
        return True
    except:
        if DEBUG: print "prepareDPFfast> problems in saving the file: ", dpf_filename
        tkMessageBox.showerror("DPF generation error", ("Impossible to save the file\n"+dpf_filename+"\n\n"))
        return False
        

########################## INFO ###################################


def RMBhelp(aboutwhat = None):
    # TODO 
    pass

def GetOSoption():
    global TargetOS, LinuxOptionsPanel, PBSOptionsPanel, WinOptionsPanel
    
    LinMasterBash, LinSingleBash, LinTarGz, LinRunAfter = BooleanVar(),BooleanVar(),BooleanVar(), BooleanVar()
    PBScputime = StringVar()

    for panel in LinuxOptionsPanel, PBSOptionsPanel, WinOptionsPanel:
        panel.grid_forget()
    if not TargetOS.get():
        # TODO clarify this
        if DEBUG: print "this is the first time the TargetOS is called"
        TargetOS.set('lin')

    if TargetOS.get() == "lin":
        # Linux/Mac
        panel = LinuxOptionsPanel
        if system == "Windows":
            CygwinOption = Tkinter.Checkbutton(panel.interior(), text = 'Use Cygwin', variable = cygwin)
            CygwinOption.grid(row = 0, column = 0, sticky = W)
        Label(panel.interior(), text="Script generation ").grid(row = 1, column = 0, sticky = E)
        LinuxScriptOption = OptionMenu(panel.interior(), LinuxScriptLevel, "master script for starting the VS",\
                        "single scripts for each ligand", "[disabled]")
        LinuxScriptOption.grid(row = 1, column = 1, sticky = W)
        LinuxScriptOption.config(highlightcolor = 'black', width = 30)
        CheckMakeTarGZ = Tkinter.Label(panel.interior(), text = 'Create a VS package file ').grid(row = 2,\
                        column = 0, columnspan = 1, sticky = E)
        TarCompressionOptions = OptionMenu(panel.interior(), TarFile, "Tar (Bz2 compression)", "Tar (Gzip compression)",\
                        "Tar (uncompressed)", "Zip compressed", "[disabled]")

        TarCompressionOptions.grid(row = 2, column = 1, sticky = W)
        TarCompressionOptions.config(highlightcolor = 'black', width = 30)

        Label(panel.interior(), text = "create job sub-folders").grid(row=3, column = 0, sticky = W)
        SplitJobsOpt = OptionMenu(panel.interior(), job_subsplitting, "[ off ]", "every 100 molecules", \
            "every 1000 molecules", "every 10K molecules", "every 100K molecules")
        SplitJobsOpt.grid(row = 3, column = 1, stick = W)
        SplitJobsOpt.config(highlightbackground = 'black', width = 30)

        Checkbutton(panel.interior(), text = "delete map files after docking", var = RemoveMapsAfter).grid(row = 5, column = 1, columnspan = 2, sticky = W)

    if TargetOS.get() == "pbs":
        # PBS
        panel = PBSOptionsPanel 
        Label(panel.interior(), text="Script generation ").grid(row = 1, column = 0, sticky = E)
        ClusterScriptOption = OptionMenu(panel.interior(), LinuxScriptLevel, "master script for starting the VS",\
                        "single scripts for each ligand", "[disabled]")
        ClusterScriptOption.config(highlightcolor = 'black', width = 30)
        ClusterScriptOption.grid(row = 1, column = 1, sticky = W, columnspan = 3)
        CheckMakeTarGZ = Tkinter.Label(panel.interior(), text = 'Create a VS package file ').grid(row = 2, column = 0, columnspan = 1, sticky = E)
        TarCompressionOptions = OptionMenu(panel.interior(), TarFile, "Tar (Bz2 compression)", "Tar (Gzip compression)",\
                        "Tar (uncompressed)", "[disabled]")
        TarCompressionOptions.grid(row = 2, column = 1, sticky = W)
        PBSOptionCPUTime = Label(panel.interior(), text='CPU time per job ')
        PBSOptionCPUTime.grid(row = 3, column = 0, sticky = E)
        PBSOptionCPUTimeEntry = Tkinter.Entry(panel.interior(), textvariable=PBStime, width = 8)
        PBSOptionCPUTimeEntry.grid(row = 3, column =1, sticky = W)
        PBSOptionCPUset = Button(panel.interior(), text ="Set", command = SetPBStime)
        PBSOptionCPUset.grid(row = 3, column =2, sticky = W, columnspan = 1)
        Label(panel.interior(), text = "Number of DLG's to run per ligand ").grid(row = 4, column = 0, sticky = E)
        Entry(panel.interior(), textvariable = PBShowmanyruns, width = 4).grid(row = 4, column = 1, sticky = W)
        PBSOptionCPUset = Button(panel.interior(), text ="Set", command = SetPBShowmanyruns).grid(row = 4, column = 2, sticky = W)
        SetPBStime
        SetPBShowmanyruns
        Label(panel.interior(), text = "create job sub-folders").grid(row=5, column = 0, sticky = W)
        SplitJobsOpt = OptionMenu(panel.interior(), job_subsplitting, "[ off ]", "every 100 molecules",\
            "every 1000 molecules", "every 10K molecules", "every 100K molecules")
        SplitJobsOpt.grid(row = 5, column = 1, stick = W, columnspan = 3)
        SplitJobsOpt.config(highlightcolor = 'black', width = 30)
        Checkbutton(panel.interior(), text = "delete map files after docking", var = RemoveMapsAfter).grid(row = 6, column = 1, columnspan = 2, sticky = W)
        
# TODO remove, obsolete
    if TargetOS.get() == "win":
        # Win (God bless you)
        CheckMasterScript = Tkinter.Checkbutton(panel.interior(), text = 'Generate a master batch script for the VS job')
        CheckMasterScript.grid(row = 3, column = 0, sticky = W, columnspan = 3)
        CheckMakeTarGZ = Tkinter.Checkbutton(panel.interior(), text = 'Create a compressed file of the VS (.zip)') 
        CheckMakeTarGZ.grid(row = 4, column = 0, sticky = W, columnspan = 3)
    panel.grid(row = 3, column = 0, columnspan = 2, pady = 15, padx = 10)
# TODO remove, obsolete

def SetPBShowmanyruns():
    wrong = False
    try:
        howmany = PBShowmanyruns.get()
        if howmany == "":
            wrong = True
        if howmany <= 0:
            wrong = True
    except:
        wrong = True
    if wrong:
        nb.tab('VS Generation').invoke()
        tkMessageBox.showerror("PBS runs error!", ("The value of runs must be a number bigger than 0 and smaller than infinite.\n\nReset to default."))
        PBShowmanyruns.set(1)
        return False
    else:
        if howmany > 255:
            tkMessageBox.showwarning("Warning", ("The number of runs is very high."))
            return True
    """
    count_ligands, count_receptors = 0, 0 
    try:
        if SingleReceptorSet.get():
            count_receptors = 1
        if MultiReceptorSet.get():
            count_receptors = len(receptorScrolledListBox.get('0' , END))
        count_ligands = TotalAcceptedLigands.get()
    except:
        if verbose or DEBUG: print "EXCEPTION IN SETPBS..."
        pass
    if count_receptors and count_ligands:
        JobsSummary.set(("\t"+str(count_receptors * count_ligands * PBShowmanyruns.get() )+" jobs will be generated" ))
    #print count_receptors, count_ligands"""
    return True


def SetPBStime():
    if DEBUG: print "CHECKING TIME FOR PBS", PBStime.get()
    time = PBStime.get()
    try:
        time = time.split(':')
    except:
        nb.tab('VS Generation').invoke()
        tkMessageBox.showerror("PBS time error!", ("The time format must be :\n\n   hh:mm:ss\n\n Reset to default."))
        PBStime.set("24:00:00")
        return False

    wrong = False
    if len(time) < 3 or len(time) > 3:
        nb.tab('VS Generation').focus_set()
        nb.tab('VS Generation').invoke()
        tkMessageBox.showerror("PBS time error!", ("The time format must be :\n\n   hh:mm:ss\n\n Reset to default."))
        PBStime.set("24:00:00")
        return False
    try:
        if int(time[0]) < 0:
            wrong = True
        if int(time[1]) > 59 or int(time[1]) < 0:
            wrong = True
        if int(time[2]) > 59 or int(time[2]) < 0:
            wrong = True
        if not int(time[0]) > 0:
            if not int(time[1]) > 0:
                if not int(time[2]) > 0:
                    wrong = True
    except:
        wrong = True
    if wrong:    
        nb.tab('VS Generation').focus_set()
        nb.tab('VS Generation').invoke()
        tkMessageBox.showerror("PBS time error!", ("The time format must be :\n\n   hh:mm:ss\n\n Reset to default."))
        PBStime.set("24:00:00")
        return False
    else:
        return True


### CORE FUNCTIONS

def TheCheck(parameter = None):
    # Perform the checking for all the
    # necessary settings for activating
    # the GENERATE button
    LIGANDS = False
    RECEPTORS = False
    MAPS = False
    DOCKING = False
    FLEXIBLE = False
    DESTINATION = False

    if DEBUG: print "======= PERFORMING THE CHECK ============"

    # Check for ligands
    if TotalAcceptedLigands.get() > 0:
        LIGANDS = True
        count_ligands = TotalAcceptedLigands.get()
        LigandSummary.set(( str(count_ligands)+" accepted" ))
        LigSummaryLabel.config(fg = '#11bb11')
    else:
        LigandSummary.set(( " [ none ] "))
        LigSummaryLabel.config(fg = "red")

    if DEBUG : print "- ligands", TotalAcceptedLigands.get()


    # Check for the receptors
    if RCstatus.get() == 0:
        if SingleReceptorSet.get():
            receptor_message = (RecFilename.get())
            RECEPTORS = True
            count_receptors = 1
    if RCstatus.get() == 1:
        if MultiReceptorSet.get():
            count_receptors = len(receptorScrolledListBox.get('0' , END))
            if count_receptors > 0:
                receptor_message = (  str(count_receptors)+" structures" )
                RECEPTORS = True
    # potential flexible residues
    #
    #
    if RECEPTORS:
        if DoFlex.get():
            if DoFlexFromWhat.get() == 1:
                if not FlexResFileName.get() == "":
                    FLEXIBLE = True
            if DoFlexFromWhat.get() == 2:
                if FlexResDefined.get():
                    FLEXIBLE = True
            if FLEXIBLE:
                if DEBUG: print "THE_CHECK> we're going flexible..."
                receptor_message = ("\n"+receptor_message+"\n[ flex: "+ResidueStatus.get()+" ]" )
        RecSummaryLabel.config(fg = '#11bb11')
        ReceptorSummary.set(receptor_message)
    else:
        ReceptorSummary.set( " [ none ] " )
        RecSummaryLabel.config(fg = 'red')


    # Check for maps
    if MapSource.get() <= 1:
        if len(GPFcontent.get('1.0', END)) > 3:
            if MapSource.get() == 0:
                MapsSummary.set(("\ncalculated in each job\n[ "+GPFfilename.get()+" ]"))
                MAPS = True
            if MapSource.get() == 1 and AutoGridBin.get():
                MAPS = True
                if CacheMapPolicy.get() == "Make copies [ use more disk space ]":
                    MapsSummary.set(("\n\ncalculated now and copied\n  [ Template: "+GPFfilename.get()+" ]\n  [ AutoGrid bin: "+AutoGridBin.get()+" ]"))
                if CacheMapPolicy.get() == "Make symbolic links [ save disk space ]":
                    MapsSummary.set(("\n\ncalculated now and linked\n  [ "+GPFfilename.get()+" ]\n  [ AutoGrid bin: "+AutoGridBin.get()+" ]"))
    if MapSource.get() == 2:
        if DoCachedMaps.get():
            MAPS = True
            if CacheMapPolicy.get() == "Make copies [ use more disk space ]":
                MapsSummary.set(("\nalready calculated and copied in each ligand directory from:\n[ "+CacheMapDirName.get()+" ]" ))
            if CacheMapPolicy.get() == "Make symbolic links [ save disk space ]":
                MapsSummary.set(("\nalready calculated and linked in each ligand directory from:\n[ "+CacheMapDirName.get()+" ]" ))
            if DEBUG: MapsSummary.set(("\nusing pre-calculated\n\t[ "+CacheMapDirName.get()+" ]"))
    


    if MAPS:
        MapsSummaryLabel.config(fg = '#11bb11')
    else:
        MapsSummary.set((" [ none ] "))
        MapsSummaryLabel.config(fg = 'red')

    # Check for DPF
    if docking_set.get() == "From template...":
        if len(DPFcontent.get('1.0', END)) > 3: # three lines arbitrary value
            docking_message = ("\nusing DPF template\n[ "+DPFfilename.get()+" ]" )
            DOCKING = True
    
    if DOCKING:
        DockingSummary.set(docking_message)
        DockSummaryLabel.config(fg = '#11bb11')
    else:
        DockingSummary.set(" [ none ] ")
        DockSummaryLabel.config(fg = "red")

    # implement with some feedback
    if TargetOS.get() == "pbs":
        if SetPBStime():
            if SetPBShowmanyruns():
                pass
        else:
            return False

    #Check for the output directory
    if not JobDirectory.get() == "":
        DESTINATION = True
        SetOutDirButton.config(fg = 'black')
        OutputDirLabel.config(fg = '#11bb11')
        OutputDirLabel.config(fg = '#11bb11')
    else:
        SetOutDirButton.config(fg = 'red')
        OutputDirLabel.config(fg = 'red')

    if LIGANDS and RECEPTORS and MAPS and DOCKING:
        # that's why we're here...
        if TargetOS.get() == "pbs":
            if SetPBStime():
                if SetPBShowmanyruns():
                    pass
                else:
                    return False
            else:
                return False
        #else:
            #JobsSummary.set(("\t"+str(count_receptors * count_ligands * PBShowmanyruns.get() )+" jobs will be generated" ))
        JobsSummary.set(("\t"+str(count_receptors * count_ligands )+" jobs will be generated" ))
        if DESTINATION:
            TheButton.config(state = NORMAL, text = "G E N E R A T E", command = TheFunction, bg = '#77ff00')
            TheButton.flash()
    else:
        TheButton.config(state = DISABLED)
        JobsSummary.set((""))
    


def DisableInterface(Tab = None):
    if Tab:
        nb.tab(Tab).configure(state = 'disabled')
    else:
        nb.tab('Ligand(s)').configure(state = 'disabled')
        nb.tab('Receptor(s)').configure(state = 'disabled')
        nb.tab('Maps').configure(state = 'disabled')
        nb.tab('Docking').configure(state = 'disabled')
        nb.tab('VS Generation').configure(state = 'disabled')
        AddLigandsButton.config(state = DISABLED)
        AddLigandsDirButton.config(state = DISABLED)
        AddLigandsDirRecursiveButton.config(state = DISABLED)
        RemoveLigandsButton.config(state = DISABLED)
        RemoveAllLigandsButton.config(state = DISABLED)
        FilterButton.config(state = DISABLED)
        LigandPDBQTOptButton.config(state = DISABLED)
        SetOutDirButton.config(state = DISABLED)

def EnableInterface(Tab = None):
    if Tab:
        nb.tab(Tab).configure(state = 'normal')
    else:
        nb.tab('Ligand(s)').configure(state = 'normal')
        nb.tab('Receptor(s)').configure(state = 'normal')
        nb.tab('Maps').configure(state = 'normal')
        nb.tab('Docking').configure(state = 'normal')
        nb.tab('VS Generation').configure(state = 'normal')
        AddLigandsButton.config(state = NORMAL)
        AddLigandsDirButton.config(state = NORMAL)
        AddLigandsDirRecursiveButton.config(state = NORMAL)
        RemoveLigandsButton.config(state = NORMAL)
        RemoveAllLigandsButton.config(state = NORMAL)
        FilterButton.config(state = NORMAL)
        LigandPDBQTOptButton.config(state = NORMAL)
        SetOutDirButton.config(state = NORMAL)

def HandBrake():
    TheButton.config(state = DISABLED, text = " [ Generation process is paused... ]")
    if tkMessageBox.askquestion('Warning', 'Do you really want to interrupt the generation process?') == "yes":
        StopImmediately.set(True)
        TheButton.config(state = NORMAL,text = "> STOPPED <")
        return
    else:
        TheButton.config(state = NORMAL,text = "[ Stop the generation... ]")
        return


def TheFunction():
    global flex_types
    path = JobDirectory.get()
    if DEBUG: print "TheFunction> starting the vs creation in ", path

    StopImmediately.set(False)

    DisableInterface()
    EnableInterface('VS Generation')

    TheButton.config(state = NORMAL, text = " [ Stop the generation... ]", command = HandBrake)
    if DEBUG:
        print "\n========================================\n"
        print "===== STARTING THE GENERATION ==========\n"
        print "========================================\n"

    # Initialize the log
    log_file = InitializeLog(path)
    if not log_file:
        if DEBUG: print "[gen+log] => we start very well... :S no logging available!"
        EnableInterface()
        return False

    
    header = "\n\n     ======================================================================================================\n"
    header += "     ======================================================================================================\n\n"
    header += "                              G E N E R A T I O N    S T A R T E D\n\n"

    #print >> log_file, header
    log_file.write(header)


    # Define the target(s)
    if RCstatus.get() == 0:
        if DEBUG: print "[gen] => single receptor NAME = ", 
        receptor_list = [ RecFilename.get() ]
        if DEBUG: print RecFilename.get()
    else:
        if DEBUG: print "[gen] => multiple receptors", 
        multi_receptor_paths_list = []
        receptor_list = receptorScrolledListBox.get('0', END)
    
    if DEBUG: print "[ I'm going to use %d receptors ]" % len(receptor_list)

    # Get the filtered ligands
    ligand_list = []
    atomtypes_set = [] #atom types present in the accepted ligands set
    for ligand in LigandDictionary.keys():
        if LigandDictionary[ligand]["accepted"]:
            ligand_list.append(ligand)
            for atom in LigandDictionary[ligand]["Atypes"]+LigandDictionary[ligand]["NotStdAT"]:
                if atom not in atomtypes_set: atomtypes_set.append(atom)
    
    # counters are initialized here
    rec_count = len(receptor_list)
    lig_count = len(ligand_list) 
    jobs_todo = rec_count * lig_count
    jobs_done = 1
    nb.tab('VS Generation').focus_set()

    splitting = job_subsplitting.get()
    print "splitting ==", splitting
    if splitting == "[ off ]":
        splitting = None
    if splitting == "every 100 molecules":
        splitting = 100
    
    if splitting == "every 1000 molecules":
        splitting = 1000

    if splitting == "every 10K molecules":
        splitting = 10000

    if splitting == "every 100K molecules":
        splitting = 100000

    if splitting > len(ligand_list):
        splitting = None
    
    print "Splitting is", splitting
    # the Main loop
    #raw_input("PRESS SOMETHING")
    for receptor in receptor_list:
        rec_name = os.path.basename(receptor).rsplit('.', 1)[:-1][0]
        if len(receptor_list) > 1:
            current_path = path+os.sep+rec_name
            multi_receptor_paths_list.append(current_path)
            if DEBUG: print "\n=====================\nTheFunction> Current multi_receptor path is ", current_path
        else:
            current_path = path
            if DEBUG: print "\n=====================\nTheFunction> Current single_receptor path is ", current_path

        rec_atypes = get_AD_atom_types(receptor) # used by prepareXPFfast()
        # Flush the list of dir per ligands (this is generated on a per-receptor base)
        del DirJournal[:]
        # create the directory RECEPTOR/[ligands]
        if not os.path.exists(current_path):
            try:
                os.makedirs(current_path, 0755)
            except:
                tkMessageBox.showerror("Receptor dir error!", ("Impossible to create the directory:\n%s\n GIVING UP...\n(Error:%s)" % (current_path, sys.exc_info()[1])))
                #print >> log_file, ("\n\n\n#### ERROR ###\n\nThere was a problem in creating the directory:\n%s\n\n VS generation aborted.\n\n####      ####" % current_path) # End of receptor loop
                log_file.write("\n\n\n#### ERROR ###\n\nThere was a problem in creating the directory:\n%s\n\n VS generation aborted.\n\n####      ####" % current_path) # End of receptor loop
                TheButton.config(state = DISABLED, text = "E R R O R")
                EnableInterface()
                return False

        ## Preliminary stuff to do before the ligands get involved
        #
        #
        ## 1. define or generate flexible residue files
        #
        flex_res = None
        if DoFlex.get(): # 
            if FlexResDefined.get(): # 
                if DEBUG: print "\tsoo.... we want flexible,right?\n\nPREPARING"
                if DoFlexFromWhat.get() == 1:
                    if FlexResFileName.get(): # TODO in theory it shouldn't be necessary
                        if DEBUG: print "\tcopying the flexible residue in the right place"
                        if DEBUG: print "\tcp flex.pdbqt working_dir"
                        flex_res = FlexResFileName.get()
                if DoFlexFromWhat.get() == 2:
                    if FlexResSelected.get(): # TODO in theory it shouldn't be necessary
                        if DEBUG: print "\tgenerate the flexible residue from the receptor"
                        if DEBUG: print "\tprepare_flex_receptor blablabla "
                        InfoMessage.set( (  "[ Generating flex residues for %s... ]" % rec_name )) 
                        receptor, flex_res = genFlex(receptor)
                        if not flex_res:
                            if DEBUG: print "TheFunction> generation aborted"
                            tkMessageBox.showerror("Error!", ("Problems generating the flexible residues:\n receptor: %s\n\n\nGeneration aborted." % (receptor)))
                            return False
                            
                flex_atypes = GetAtypes(flex_res)
                for atom in flex_atypes:
                    if atom not in atomtypes_set: atomtypes_set.append(atom)

        if DEBUG:
            print "\t[GEN] I've got the flex_res filename", flex_res
            print "\t[GEN] Now the receptor is", receptor
        #
        ## 2. calculate or copy maps now if necessary
        #
        #  create the cached maps folder (for "now" and "already")
        CachedMapsDir = None

        ### TODO WHAT'S THIS DOING HERE??? CacheMapOptions = OptionMenu(CacheMapHandle.interior(), CacheMapPolicy, "Make copies [ use more disk space ]", "Make symbolic links [ save disk space ]")

        if CacheMapPolicy.get() == "Make copies [ use more disk space ]":
            symlink = False
        if CacheMapPolicy.get() == "Make symbolic links [ save disk space ]":
            symlink = True

        if MapSource.get() >= 1: 
            CachedMapsDir = current_path+os.sep+"maps"
            if not os.path.exists(CachedMapsDir):
                try:
                    os.makedirs(CachedMapsDir, 0755)
                except:
                    tkMessageBox.showerror("Maps caching", ("Impossible to create the directory:\n%s\n GIVING UP...\n(ERROR: %s)" % (CachedMapsDir,sys.exc_info()[1])))
                    #print >> log_file, ("\n\n\n#### ERROR ###\n\nThere was a problem in creating the directory:\n%s\n\n VS generation aborted.\n\n####      ####" % CachedMapsDir) 
                    log_file.write("\n\n\n#### ERROR ###\n\nThere was a problem in creating the directory:\n%s\n\n VS generation aborted.\n\n####      ####" % CachedMapsDir) 
                    EnableInterface()
                    return False
        if MapSource.get() == 1: # populate the dir with AutoGrid
            InfoMessage.set( (  "[ Running AutoGrid on %s... ]" % rec_name )) 
            if not CalcCacheMaps(CachedMapsDir, receptor, flex_res): 
                tkMessageBox.showerror("Error!", ("Impossible to calculate the cached maps here:\n%s\n GIVING UP...\n(ERROR:%s)" % (CachedMapsDir, sys.exc_info()[1])))
                EnableInterface()
                return False
        #CacheMapDirName.set(mapDir)
        if MapSource.get() == 2: # populate the dir by copying the files from the cache
            InfoMessage.set( (  "[ Copying cached maps for %s... ]" % rec_name )) 
            # no matter if maps will be eventually copied or linked, now it must be false
            if not CopyMapDir(atomtypes_set, CacheMapDirName.get(), CachedMapsDir, symlink = False): 
                tkMessageBox.showerror("Error!", ("Problems in copying the maps in the VS job master directory \n%s\n GIVING UP...\n(ERROR: %s)" % (CachedMapsDir,sys.exc_info()[1])))
                EnableInterface()
                return False

        if splitting:
            dir_counter = -1
            counter =  1e50 # if you want to process more than these ligands, you deserve an error in your Raccoon session
            #zero_count = int(log10( len(ligand_list) / splitting) )
            zero_count = len(str( len(ligand_list) / splitting) )
            print "ZERO COUNTING is ", zero_count
            #dir_format = "%"+("0"*zero_count)+"d"
        

        #for l in ligand_list:
        #    print "LIGAND>",l
        # Ligands loop #############################################################################################
        gc.disable()
        for ligand in ligand_list:
            if DEBUG:
                print "============================"
                print LigandDictionary[ligand]
                print "============================"

            lig_atypes = LigandDictionary[ligand]['Atypes'] + LigandDictionary[ligand]['NotStdAT'] 
            #print "lig_atypes", lig_atypes
            

            if StopImmediately.get():
                InfoMessage.set( "Generation process aborted by the user...")
                #print >> log_file, ("\n\n\n#### ABORT ###\n\nThe generation process was interrupted by the user.\n\n") 
                log_file.write("\n\n\n#### ABORT ###\n\nThe generation process was interrupted by the user.\n\n") 
                TheButton.config(state = DISABLED, text = " [ Generation aborted ]")
                EnableInterface()
                return False

            InfoMessage.set( (  "=> Processing %s | %s \t[ %d | %d ]" % (os.path.basename(receptor), os.path.basename(ligand), jobs_done, jobs_todo )   ))
            root.update()
            
            ligand_name = os.path.basename(ligand).rsplit('.', 1)[:-1][0]
            if DEBUG: print "\tTheFunction> processing the ligand ",ligand_name
            # create ligand dir
            if not splitting:
                #print "No splitting allowed"
                ligand_dir = MkJobDir(ligand, rec_name, current_path)
            else:
                if DEBUG: print "\tTheFunction> splitting ligand dirs has been required"
                if counter == splitting or counter == 1e50:
                    #print "Counter is bigger than spliting", counter, splitting
                    dir_counter += 1
                    dir_name = "%0*d" % (zero_count, dir_counter)
                    output_dir = current_path+os.sep+dir_name
                    #print output_dir
                    try:
                        if not os.path.exists(output_dir):
                            os.makedirs(output_dir, 0755)
                    except:
                        tkMessageBox.showerror("Ligand directory splitting", ("Impossible to create the directory:\n%s\n GIVING UP...\n(ERROR: %s)" % (output_dir,sys.exc_info()[1])))
                        #print >> log_file, ("\n\n\n#### ERROR ###\n\nThere was a problem in creating the directory:\n%s\n\n VS generation aborted.\n\n####      ####" % output_dir) 
                        log_filewrite("\n\n\n#### ERROR ###\n\nThere was a problem in creating the directory:\n%s\n\n VS generation aborted.\n\n####      ####" % output_dir) 
                        TheButton.config(state = DISABLED, text = " [ Generation aborted ]")
                        EnableInterface()
                        return False
                    counter = 0
                ligand_dir = MkJobDir(ligand, rec_name, output_dir, sub_dir = dir_name)


            if not ligand_dir:
                tkMessageBox.showerror("Ligand directory", ("Impossible to create the directory:\n%s\n GIVING UP...\n(ERROR: %s)" % (ligand_dir,sys.exc_info()[1])))
                #print >> log_file, ("\n\n\n#### ERROR ###\n\nThere was a problem in creating the directory:\n%s\n\n VS generation aborted.\n\n####      ####" % ligand_dir) 
                log_file.write("\n\n\n#### ERROR ###\n\nThere was a problem in creating the directory:\n%s\n\n VS generation aborted.\n\n####      ####" % ligand_dir) 
                TheButton.config(state = DISABLED, text = " [ Generation aborted ]")
                EnableInterface()
                return False

            # copy the ligand in place
            if not os.path.dirname(ligand) == ligand_dir:
                try:
                    shutil.copy2(ligand, ligand_dir)
                except:
                    tkMessageBox.showerror("Error!", ("Impossible to copy the ligand:\n%s\n\tto\n%s\n\nGIVING UP...\n(ERROR: %s)" % (ligand, ligand_dir,sys.exc_info()[1])))
                    TheButton.config(state = DISABLED, text = " [ Generation aborted ]")
                    EnableInterface()
                    return False
            else:
                if DEBUG: print "TheFunction> skipped the source/dest ligand copy because they are identical..."
            
            # copy flexres if necessary
            if DoFlex.get(): # 
                if FlexResDefined.get():
                    if not os.path.dirname(flex_res) == ligand_dir:
                        try:
                            shutil.copy2( flex_res, ligand_dir)
                        except:
                            tkMessageBox.showerror("Error!", ("Impossible to copy the flex res file:\n%s\n\tto\n%s\n\nGIVING UP...\n(ERROR: %s)" % (flex_res, ligand_dir,sys.exc_info()[1])))
                            TheButton.config(state = DISABLED, text = " [ Generation aborted ]")
                            EnableInterface()
                            return False
                    else:
                        if DEBUG: print "TheFunction> skipped the source/dest flex_res copy because they are identical..."
                for a in flex_atypes:
                    if not a in lig_atypes:
                        lig_atypes.append(a)


            # maps management
            #
            # a. generate GPF
            gpf_file = None
            if MapSource.get() == 0 : # being in the for loop cached maps will be referred to the receptor
                # generate the gpf
                gpf_file = ligand_dir+os.sep+rec_name+".gpf"
                if not prepareGPFfast(gpf_file, receptor, rec_types = rec_atypes, lig_types = lig_atypes):
                #try:
                #    prepareGPF(gpf_file, receptor, ligand_filename = ligand, atom_types = None, flexres_filename = flex_res)
                #except:
                    tkMessageBox.showerror("PrepareGPF", ("Error!\n\nImpossible to create the GPF file:\n%s\n\n     GIVING UP...\n(ERROR:%s)" % (gpf_file,sys.exc_info()[1])))
                    TheButton.config(state = DISABLED, text = " [ Generation aborted ]")
                    EnableInterface()
                    return False
                    
                if not os.path.exists(gpf_file):
                    tkMessageBox.showerror("Error!", ("Impossible to create the GPF file:\n%s\n        GIVING UP...\n(ERROR: %s)" % (gpf_file,sys.exc_info()[1])))
                    #print >> log_file, ("\n\n\n#### ERROR ###\n\nThere was a problem in creating the GPF:\n%s\n\n VS generation aborted.\n\n####      ####" % gpf_file) 
                    log_file.write("\n\n\n#### ERROR ###\n\nThere was a problem in creating the GPF:\n%s\n\n VS generation aborted.\n\n####      ####" % gpf_file) 
                    TheButton.config(state = DISABLED, text = " [ Generation aborted ]")
                    EnableInterface()
                    # error message window
                    return False

                # copy potential parameter files # 
                #if not GPFParameterFile.get() == "" or not GPFParameterFile.get() == None:
                if GPFParameterFile.get():
                    if DEBUG:
                        print "|%s|<= This is the parameter file" %GPFParameterFile.get() 
                        print GPFParameterFile.get() == ""
                        print GPFParameterFile.get() == None

                    if not os.path.dirname(GPFParameterFile.get()) == ligand_dir:
                        try:
                            shutil.copy2( GPFParameterFile.get(), ligand_dir)
                        except:
                            tkMessageBox.showerror("Error!", ("Impossible to copy the parameter file required by the\
 GPF:\nparameter file: %s\n\ndestination: %s\n\nGeneration aborted." % (GPFParameterFile.get(), ligand_dir)))
                            TheButton.config(state = DISABLED, text = " [ Generation aborted ]")
                            EnableInterface()
                            return False
                    else:
                        if DEBUG: print "TheFunction> skipped the source/dest GPFparamfile copy because they are identical..."


                # copy the receptor
                if not os.path.dirname(receptor) == ligand_dir:
                    try:
                        shutil.copy2(receptor, ligand_dir)
                    except:
                        tkMessageBox.showerror("Error!", ("Impossible to copy the receptor\n%s\n\tto\n%s\n\nGIVING UP...\n(ERROR: %s)" % (receptor, ligand_dir,sys.exc_info()[1])))
                        TheButton.config(state = DISABLED, text = " [ Generation aborted ]")
                        EnableInterface()
                        return False
                else:
                    if DEBUG: print "TheFunction> skipped the source/dest receptor copy because they are identical..."



            # b. use cached maps
            elif MapSource.get() >= 1:
                #current_atom_types = GetAtypes(ligand)
                # include flex res atoms
                if FlexResDefined.get():
                    flex_types = []
                    fname = FlexResFileName.get() 
                    fp = open(fname, 'r')
                    resAtms = fp.readlines()
                    fp.close()
                    for ra in resAtms:
                        if ra.startswith('ATOM') or ra.startswith('HETATM'):
                            flex_types.append(ra.split()[-1])
                    for atom in flex_types:
                        if atom not in lig_atypes: lig_atypes.append(atom)
                if DEBUG: print "TheFunction> lig_atypes>", lig_atypes
                CopyMapDir(lig_atypes, CachedMapsDir, ligand_dir, symlink = symlink)

            # Prepare the DPF
            if docking_set.get() == "From template...":
                dpf_file = ligand_dir+os.sep+ligand_name+"_"+rec_name+".dpf"
                #prepareDPF(dpf_file, receptor, ligand, flex_res)
                #if not os.path.exists(dpf_file):
                if not prepareDPFfast(dpf_file, receptor_filename = receptor, ligand_filename = ligand,
                        lig_types = lig_atypes, flex_res_filename = flex_res, parameter_file = DPFParameterFile.get()):
                    tkMessageBox.showerror("Error!", ("Impossible to create the DPF file:\n%s\n GIVING UP...\n(ERROR: %s)" % (dpf_file,sys.exc_info()[1])))
                    #print >> log_file, ("\n\n\n#### ERROR ###\n\nThere was a problem in creating the DPF:\n%s\n\n VS generation aborted.\n\n####      ####" % dpf_file) 
                    log_file.write("\n\n\n#### ERROR ###\n\nThere was a problem in creating the DPF:\n%s\n\n VS generation aborted.\n\n####      ####" % dpf_file) 
                    TheButton.config(state = DISABLED, text = " [ Generation aborted ]")
                    EnableInterface()
                    return False    
                # copy potential parameter files
                if not DPFParameterFile.get() == "":
                    if not os.path.dirname(DPFParameterFile.get()) == ligand_dir:
                        try:
                            shutil.copy2( DPFParameterFile.get(), ligand_dir)
                        except:
                            tkMessageBox.showerror("Error!", ("Impossible to copy the parameter file required by the\
DPF:\n%s\n\tto\n%s\n\nGIVING UP...\n(ERROR: %s)" % (DPFParameterFile.get(), ligand_dir,sys.exc_info()[1] ) ) )  
                            EnableInterface()
                            TheButton.config(state = DISABLED, text = " [ Generation aborted ]")
                            return False
                    else:
                        if DEBUG: print "TheFunction> skipped the source/dest DPFparamfile copy because they are identical..."
            jobs_done += 1
            if splitting:
                counter += 1

            if not TargetOS.get() == "win":
                if not LinuxScriptLevel.get() == "[disabled]":
                    MakeJobScript(ligand_dir, dpf_file, gpf_file)
            log_file.flush()
            
    
        if TargetOS.get() == "pbs" or TargetOS.get() == "lin":
            if DEBUG: print "Making the master script"
            if LinuxScriptLevel.get() == "master script for starting the VS":
                MakeMasterJobScript(current_path)
    gc.enable()
    if LinuxScriptLevel.get() == "master script for starting the VS" and len(receptor_list) > 1:
        if not MakeMasterJobScript_multireceptor(path, multi_receptor_paths_list):
            EnableInterface()
            TheButton.config(state = DISABLED, text = " [ Generation aborted ]")
            return False

    if DEBUG: print "\n\n\n    [ GENERATION DONE ]"
    if not TarFile.get() == "[disabled]":
        InfoMessage.set( (  "[ writing the compressed file... ]")   ) 
        TheButton.config(state = DISABLED, text = "...creating the VS package...")
        root.update()
        # vs pack filename
        pack_filename = path+os.sep+"VSpack_"+os.path.basename(path)
        if DEBUG:
            print "TheFunction> creating the package file", pack_filename, "in ", path

        # Zip file format
        if TarFile.get() == "Zip compressed":
            if not MakeZip(path, pack_filename):
                root.update()
                return False
        # ...anything else
        else:
            if not MakeTar(path, pack_filename):
                root.update()
                return False

    InfoMessage.set( (  "[ generation completed successfully ]")   ) 
    tkMessageBox.showinfo(title="VS generation finished", message=("%d docking jobs have been successfully \
generated in:\n\n%s\n" % (len(receptor_list) * len(ligand_list), path ) ))
    EnableInterface()
    # Success! update the log with all the ligands, and close the file
    #print >> log_file, "\n\t\t\t process completed successfully.\n\n"
    #print >> log_file, "\n\n\n[DONE]" # End of receptor loop. This line is used in the load function to recognize a successfull VSgeneration when loading it back.
    log_file.write("\n\t\t\t process completed successfully.\n\n")
    log_file.write("\n\n\n[DONE]")
    # End of receptor loop. TODO OBSOLETE: This line is used in the load function to recognize a successfull VSgeneration when loading it back.
    log_file.close()
    TheButton.config(state = DISABLED, text = "D O N E", fg = '#000000')


def CopyMapDir(atomtypes_to_copy, source_dir, destination_dir, symlink = False):
    # copy or make symbolic links of map files
    #
    #
    DEBUG = 0

    if DEBUG: print "CopyMapDir> called with the following args", atomtypes_to_copy, source_dir, destination_dir, symlink
    if source_dir == destination_dir:
        if DEBUG: print "CopyMapDir> skipping copy/symlink because the directories are the same"
        return True
    if MapSource.get() == 2:
        map_files = MapFolderList.get('0', END)
    if MapSource.get() == 1:
        map_files = glob.glob(os.path.join(source_dir, "*.map"))
        map_files.append(glob.glob(os.path.join(source_dir, "*.xyz"))[0])
        map_files.append(glob.glob(os.path.join(source_dir, "*.fld"))[0])

    counter = 0
    atom_list = atomtypes_to_copy[:]
    atom_list.append('e')
    atom_list.append('d')
    atom_list.append('maps')
    #xxx = []
    for atype in atom_list:
        if DEBUG: print "CopyMapDir> processing ", atype
        for map in map_files:
            if DEBUG: print "\t\tfile ", map
            if atype == map.split(".")[-2]:
                try:
                #if True:
                    if DEBUG: print "CopyMapDir> going to process this file ==>", map
                    if symlink:
                        if DEBUG: print "     doing symlinking", map, destination_dir
                        map_filename = os.path.basename(map)
                        map_dir = os.path.basename(source_dir)
                        #print job_subsplitting.get()
                        #print job_subsplitting.get() == '[ off  ]'
                        if job_subsplitting.get() == "[ off ]":
                            #print "## DEBUG CopyMapDir> NOT ADDING extra padding..."
                            pre_path = ".."+os.sep
                        else:
                            #print "## DEBUG CopyMapDir>  *ADDING* extra padding..."
                            pre_path = ".."+os.sep+".."+os.sep
                        SRC = pre_path+map_dir+os.sep+map_filename
                        DEST = destination_dir+os.sep+map_filename
                        if DEBUG: 
                            print "  SRC", SRC
                            print "  DEST", DEST
                        os.symlink(SRC, DEST)
                    else:
                        if DEBUG :print "     source (%s) => dest (%s) " % (map, destination_dir)
                        shutil.copy2( map, destination_dir)
                    counter = counter + 1 # +1 to account for the two maps.* files
                    #xxx.append(map)
                except:
                    print "CopyMapDir> ERROR! ", exc_info()[1]
                    tkMessageBox.showerror(title="Cached maps error", message=(("Some problem occurred when copying or linking the file %s") % map ))
                    return False
    #print "copied maps"
    #for x in xxx:
    #    print x
    #print len(xxx), len(atomtypes_to_copy)+1, counter
    if len(atom_list)+1 == counter:
        return True
    else:
        return False

def GetAtypes(filename = None, selection = None):
    # TODO FIX THIS? Selection is empty!
    # The selection works with selected
    # flex residues only
    #
    if not filename and not selection:
        return

    atypes = []
    if filename:
        for line in get_lines(filename):
            if line[0:6] == 'HETATM' or line[0:4] == 'ATOM':
                atom = line.split()[-1]
                if atom not in atypes:
                    atypes.append(atom)
    if selection:
        pass
    
    return atypes

def CalcCacheMaps(output_dir, receptor, flexible_residues = None):
    DEBUG=True
    # get the atom types for the accepted ligands
    atom_types = []
    for ligand in LigandDictionary.keys():
        if LigandDictionary[ligand]["accepted"]:
            for atom in LigandDictionary[ligand]["Atypes"]:
                if atom not in atom_types:
                    atom_types.append(atom)
    if flexible_residues:
        for a in get_AD_atom_types(flexible_residues):
            if not a in atom_types:
                atom_types.append(a)
    if not os.path.dirname(receptor) == output_dir:
        try:
            shutil.copy2( receptor, output_dir)
        except:
            if DEBUG: print "CalcCacheMaps> error in copying the receptor %s in %s" % (receptor, output_dir)
            tkMessageBox.showerror(title="Error", message=(("Impossible to copy the receptor in the target directory for caching the maps.")))
        gpf_name = output_dir+os.sep+os.path.basename(receptor).rsplit('.', 1)[:-1][0]+"_all_maps.gpf"
    else:
        if DEBUG: print "CalcCacheMaps> skipping the receptor copy, because files are identical"

    # copy potential parameter files # 
    if not GPFParameterFile.get() == "":
        if not os.path.dirname(GPFParameterFile.get()) == output_dir:
                        try:
                            shutil.copy2( GPFParameterFile.get(), output_dir)
                        except:
                            tkMessageBox.showerror("Error!", ("Impossible to copy the parameter file required by the\
GPF:\n%s\n\tto\n%s\n\nGIVING UP...\n(ERROR: %s)" % (GPFParameterFile.get(), output_dir, sys.exc_info()[1])))
                            TheButton.config(state = DISABLED, text = " [ Generation aborted ]")
                            EnableInterface()
                            return False
        else:
           if DEBUG: print "TheFunction> skipped the source/dest GPFparamfile copy because they are identical..."
    #try:
    if True:
        rec_types = get_AD_atom_types(receptor)
        prepareGPFfast(gpf_name, receptor, rec_types = rec_types, lig_types = atom_types)
    else:
    #except:
        if DEBUG: print "CalcCacheMaps> error in creating the GPF with the following parameters:", gpf_name, receptor, atom_types , flexible_residues
        return False
    if RunAutoGrid(output_dir, gpf_name):
        return True
    else:
        if DEBUG: print "CalcCacheMaps> error in running AutoGrid"
        return False


def RunAutoGrid(working_dir, gpf):
    DEBUG = True
    if DEBUG: print "RunAutoGrid> THE FUNCTION HAS BEN CALLED WITH THE FOLLOWING PARAMS", working_dir, gpf
    # define AutoGrid
    #
    if not AutoGridBin.get():
        if DEBUG: print "RunAutoGrid> Error, AutoGrid binary not found"
        return False
    else:
        AutoGrid = AutoGridBin.get()

    # path cleanup
    working_dir = os.path.normpath(working_dir)
    gpf = os.path.basename(gpf)
    glg = working_dir + os.path.sep + os.path.splitext(gpf)[0]+".glg"

    if DEBUG:
        print "RunAutoGrid> files and paths report:"
        print "\tthe normalized path is |"+working_dir+"|"
        print "\t the gpf name is "+gpf+"|"
        print "\t the glg name is "+glg+"|"

    nb.tab('VS Generation').focus_set()
    root.update()
    #print "Look, mom! I'm running Autogrid from inside Python!!!!"
    try:
        if system == "Windows":
            drive, directory = os.path.splitdrive(working_dir)
            if DEBUG: print drive + " && cd " + directory + " && " + AutoGrid + " -p \"" + gpf + "\" -l \"" + glg + "\""
            os.system(drive + " && cd " + directory + " && " + AutoGrid + " -p \"" + gpf + "\" -l \"" + glg + "\"")
        else:
            if DEBUG: print "cd \"%s\"; %s -p \"%s\" -l \"%s\" " % (working_dir, AutoGrid, gpf, glg )
            os.system(("cd \"%s\"; %s -p \"%s\" -l \"%s\" " % (working_dir, AutoGrid, gpf, glg )))
    except:
        tkMessageBox.showerror("AutoGrid error!", ("An error occurred when running AutoGrid. The generation will be halted."))
        return False
    
    # Check if the calculation succeded
    try:
        log = get_lines(glg)
    except: 
        if DEBUG: print "RunAutoGrid> Impossible to open the file ", glg
        tkMessageBox.showerror("AutoGrid error!", ("Maps calculation failed. Impossible to open the file %s" % glg))
        return False

    if DEBUG: print log[-2]
    if "Successful Completion" in log[-2]:
        return True
    else:
        error = ""
        for line in log[-7:]:
            error += line
        tkMessageBox.showerror("AutoGrid error!", ("Maps calculation failed with the following message:\n %s" % error))
        return False

def WhichAutoGrid(program = 'autogrid4'):
    # Try to check the file path....
    def is_exe(fpath):
        return os.path.exists(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            if CheckExe(program):
                AutoGridBin.set(os.path.normpath(program))
                AutoGridExecButton.config(text = "Change AutoGrid executable", fg = 'black')
                TheCheck()
                return True
    else:
    # walks thru the path...
        for path in os.environ["PATH"].split(os.pathsep):
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                if CheckExe(exe_file):
                    AutoGridBin.set(os.path.normpath(exe_file))
                    AutoGridExecButton.config(text = "Change AutoGrid executable", fg = 'black')
                    TheCheck()
                    return True
    # If the function gets here, AG was not found...
    AutoGridExecButton.config(text = "Set AutoGrid executable", fg = 'red')
    
def GetAutoGrid(filename = None):
    keepasking = True
    while keepasking == True:
        if filename:
            AutoGrid = filename
        else:
            AutoGrid = askopenfilename(title = "Specify AutoGrid binary file...", filetypes =[("Any file...", '*')])
        if AutoGrid:
            if CheckExe(AutoGrid):
                keepasking = False
                AutoGridBin.set(os.path.normpath(AutoGrid))
                AutoGridExecButton.config(text = "Change AutoGrid executable", fg = 'black')
                TheCheck()
                return True
            else:
                tkMessageBox.showwarning("AutoGrid", "The specified file is not an executable.")
                AutoGridExecButton.config(text = "Set AutoGrid executable", fg = 'red')
                return False
        else:
            if not AutoGridBin.get():
                answer = tkMessageBox.askquestion('Warning', 'The AutoGrid binary file is required for pre-caching maps.\nDo you want to define it?')
                if answer == "no":
                    tkMessageBox.showwarning("Pre-caching aborted", "The calculations of maps has been aborted by the user.")
                    keepasking = False        
                    GPFframe.forget()
                    AutoGridWhen1.invoke() # Select the default as "Run AG in each job"
                    AutoGridExecButton.config(text = "Set AutoGrid executable", fg = 'red')
                    return False
            else:
                keepasking = False
                TheCheck()
                return True

def CheckExe(file):
    # not working 
    return True

def genFlex(receptor_filename):
    verbose = False
    verbose=True
    name = os.path.splitext(receptor_filename)[0]
    rigid_filename=name+"_rigid.pdbqt"
    flexres_filename=name+"_flex.pdbqt"
    if verbose or DEBUG: print "[genFlex] rigid will be   = ", rigid_filename
    if verbose or DEBUG: print "[genFlex] flexres will be = ", flexres_filename

    residue_selected = ListFlexResiduesNames.get()
    residue_selected = residue_selected.replace(" ","")
    if verbose or DEBUG: print "[genFlex] gen from ", residue_selected

    residue_to_move = residue_selected.replace(',','_')
    if verbose or DEBUG: print "These are residues to move", residue_to_move

    disallow = ""
    disallowed_pairs = ""
    r = Read(receptor_filename)[0]
    r.buildBondsByDistance()
    all_res = ResidueSet()
    res_names = residue_to_move.split('_')
    res_names = residue_selected.split(',')
    
    if verbose or DEBUG: print "res_names will be", res_names

    #try:
    if True:
        for n in res_names:
            res = r.chains.residues.get(lambda x: x.name==n)
            all_res += res
    
        d = {}
        for res in all_res: d[res] = 1
        all_res = d.keys()
        all_res = ResidueSet(all_res)
        all_bnds = BondSet()
        bnd_pairs = disallowed_pairs.split(':')
        if not bnd_pairs == ['']:
            print "in bnd_pairs", bnd_pairs
            for pair in bnd_pairs:
                print "=========> pair", pair
                names = pair.split('_')
                bnds = all_res.atoms.bonds[0].get(lambda x: x.atom1.name in names and x.atom2.name in names)
                all_bnds += bnds
        print "THIS IS GOING TO BE THE INPUT", all_res, rigid_filename,flexres_filename
        fdp = AD4FlexibleReceptorPreparation(r, residues=all_res, rigid_filename=rigid_filename, flexres_filename=flexres_filename, non_rotatable_bonds=all_bnds)
        return rigid_filename, flexres_filename
    #except:
    else:
        if DEBUG or verbose: print "genFlex> problems in generating the flex residues..."
        return False, False

def update_status(status_message):
    status = Label(p1, text=status_message, bd=1, relief=SUNKEN, anchor=S)
    status.pack(side=BOTTOM, fill=X)

def confirm():
    if DEBUG:
        root.destroy()
        exit()

    if tkMessageBox.askokcancel("Close Raccoon", "\nAre you sure you want to quit?\n\n(all unsaved data will be lost)\n"):
        root.destroy()

def MkJobDir(ligand_filename, receptor_stem, output_dir, sub_dir = None):
    global DirJournal
    LigNAME = os.path.basename(ligand_filename).rsplit('.', 1)[:-1][0]
    RecNAME = receptor_stem
    JobDir = output_dir+os.sep+LigNAME+"_"+RecNAME
    if JobDir in DirJournal: # to manage homonimy (same ligand filename from different directories)
        JobDir = JobDir+"_"+str(DirJournal.count(JobDir))
    DirJournal.append([JobDir, sub_dir])
    try:
        if not os.path.exists(JobDir):
            os.makedirs(JobDir, 0755)
        else:
            return
        return JobDir
    except:
        return False

def MakeJobScript(ligand_dir, dpf_file, gpf_file):
    # TODO to fix because it waits for user input between ligands!

    # generate run.sh in the ligand_dir
    # TODO to clean up to remove TargetOS = Linux
    #if TargetOS.get() == "lin":
        if system == "Windows" and not cygwin.get():
            script_file = ligand_dir+os.sep+"run.bat"
            line = "@echo off"
            line = "REM Generated by AutoDock Raccoon"
            if gpf_file:
                gpf = os.path.basename(gpf_file)
                glg = gpf[:-3]+"glg"
                line += ("\necho Running AutoGrid...\nautogrid4.exe -p \"%s\" -l \"%s\">NUL\n" % (gpf, glg) ) # TODO test the NUL option
            dpf = os.path.basename(dpf_file)
            dlg = dpf[:-3]+"dlg"
            line += ("\necho Running AutoDock...\nautodock4.exe -p \"%s\" -l \"%s\">NUL\n" % (dpf, dlg) ) # TODO test the NUL option
            if RemoveMapsAfter.get():
                line += ("\necho [Removing grid maps]\ndel *.map *.maps.fld *.maps.xyz\n")
        else:
            script_file = ligand_dir+os.sep+"run.sh"
            line = "#!/bin/bash\n# Generated by AutoDock Raccoon\n#\n#"
            line += "\n# Specify here the paths for the binaries, if necessary"
            if gpf_file:
                line += "\n"+"# autogrid = ''"
                line += "\n"+"# autodock = ''"
            else:
                line += "\n"+"# autodock = ''"
            if gpf_file:
                gpf = os.path.basename(gpf_file)
                glg = gpf[:-3]+"glg"
                line += ("\necho Running AutoGrid...\nautogrid4 -p \"%s\" -l \"%s\" 1>/dev/null 2>/dev/null\n" % (gpf, glg) ) # TODO test the /dev/nul opt
            dpf = os.path.basename(dpf_file)
            dlg = dpf[:-3]+"dlg"
            line += ("\necho Running AutoDock...\nautodock4 -p \"%s\" -l \"%s\" 1>/dev/null 2>/dev/null\n" % (dpf, dlg))  # TODO test the /dev/nul opt
            if RemoveMapsAfter.get():
                line += ("\necho [Removing grid maps]\nrm -fr *.map *.maps.fld *.maps.xyz\n")
        script = open( script_file, 'wb')
        script.writelines(line)
        script.close()
        if not system == "Windows": os.system("chmod +x \"%s\"" % (script_file))
        return True



def MakeMasterJobScript_multireceptor(path, list_of_receptor_dirs):
    # TODO IT'S NOT YET COMPLETE!!!!!!
    # TODO this function must adapt automatically
    # to the target mode, either workstation or PBS!!!
    # therefore the file name is going to be different

    # master_script_name = path+os.sep+"RunVS.bat"
    #Q = '"'
    if False: # TODO to work on it...

        line += "echo -e \"\\n\\n\\n          ________________________________________________________________\"\n"
        line += "echo \"    __________//___________________________/////___________________/____________\"\n"
        line += "echo \"    _________/__/__________________________/____/__________________/____________\"\n"
        line += "echo \"    ________/____/___________/_____________/_____/_________________/____________\"\n"
        line += "echo \"    ________/____/__/_____/_/////___/////__/_____/__/////___/////__/___/________\"\n"
        line += "echo \"    _______/______/_/_____/__/_____/_____/_/_____/_/_____/_/_____/_/_//_________\"\n"
        line += "echo \"    _______////////_/_____/__/_____/_____/_/_____/_/_____/_/_______//_/_________\"\n"
        line += "echo \"    _______/______/_/____//__/___/_/_____/_/____/__/_____/_/_____/_/___/________\"\n"
        line += "echo \"    _______/______/__////_/___///___/////__/////____/////___/////__/____/_______\"\n"
        line += "echo \"          ________________________________________________________________\"\n"
        line += "echo \"                                     ______ \"\n"
        line += "echo \"                                    /      \\ \"\n"
        line += "echo \"                                   /        \\ \"\n"
        line += "echo \"                                  /          \\   Raccoon\"\n"
        line += "echo \"                                  \\    /\\    /    Virtual \"\n"
        line += "echo \"                                   \\  /  \\  /      Screening \"\n"
        line += "echo \"                                    \\/ /\\ \\/        Generation      \"\n"
        line += "echo \"                                     /\\  \\ \"\n"
        line += "echo \"                                   /\\  \\__\\    version %s\"\n" % version
        line += "echo \"                                  /  \\__\\ \"\n"
        line += "echo \"                                 /____\\ \"\n" 
        line += "echo \"\"\n"
        line += "echo -e \"                   `cat %s | wc -l ` jobs are going to be submitted on `hostname`.\"\n" % jobs_list
        line += "if [ \"$1\" == \"-t\" ]; then\n"
        line += "echo \"                              => TSRI mode is ON <=\"\n"
        line += "fi\n"
        line += "echo -e \"\\n\\n\"\n"

    if system == "Windows" and not cygwin.get():
        multi_rec_script_name = "RunVS_multireceptor.bat"

        line = "@echo off\nREM Generated by AutoDock Raccoon v.%s\necho.\n" % version
        command = "call RunVS.bat"
        #Q = '"'
    else:
        multi_rec_script_name = "RunVS_multireceptor.sh"

        line = "#!/bin/bash\n### Generated by AutoDock Raccoon v.%s\n" % version
        #Q = "'"
        if TargetOS.get() == "pbs":
            command = "sh ./vs_cluster_submit.sh"
        else:
            command = "sh ./RunVS.sh"

        # TODO ADD SOMETHING EXPLICATIVE AND A timed read...

    line += "# move to the master directory\n"
    #line += "cd \"%s%s%s\"\n\n" % (Q, path, Q)
    line += "cd \"%s\"\n\n" % (path)
    
    for rec_dir in list_of_receptor_dirs:
        rec_dir = os.path.basename(rec_dir)
        #line += "cd \"%s%s%s\"\n" % (Q, rec_dir, Q)
        line += "cd \"%s\"\n" % (rec_dir)
        line += "%s\n" % command
        line += "cd ..\n"

    try:
        filename = path + os.sep + multi_rec_script_name
        fp = open(filename, 'wb')
        fp.write(line)
        fp.close()

        if not system == "Windows":
            os.system("chmod +x \"%s\"" % (filename))
        return True
    except:
        if DEBUG: print "MakeMasterJobScript_multireceptor> ERROR generating the script:  %s " % filename
        tkMessageBox.showerror("Multi-receptor script.", ("An error occurred when trying to generate the multi-receptor script file."))
        return False

        


def MakeMasterJobScript(path):
    header = """      ________________________________________________________________
__________//___________________________/////___________________/____________
_________/__/__________________________/____/__________________/____________
________/____/___________/_____________/_____/_________________/____________
________/____/__/_____/_/////___/////__/_____/__/////___/////__/___/________
_______/______/_/_____/__/_____/_____/_/_____/_/_____/_/_____/_/_//_________
_______////////_/_____/__/_____/_____/_/_____/_/_____/_/_______//_/_________
_______/______/_/____//__/___/_/_____/_/____/__/_____/_/_____/_/___/________
_______/______/__////_/___///___/////__/////____/////___/////__/____/_______
      ________________________________________________________________
                                 ______ 
                                /      \\ 
                               /        \\ 
                              /          \\   Raccoon
                              \\    /\\    /    Virtual 
                               \\  /  \\  /      Screening 
                                \\/ /\\ \\/        Generator
                                 /\\  \\ 
                               /\\  \\__\\    version %s
                              /  \\__\\ 
                             /____\\ """ % version
    


    if TargetOS.get() == "lin": # TODO useless!
        if system == "Windows" and not cygwin.get():
            line = "@echo off\nREM Generated by AutoDock Raccoon v.%s\necho.\n" % version
            command = "call run.bat"
            master_script_name = path+os.sep+"RunVS.bat"
            spacer = ""
            Q = ""
        else:
            line = "#!/bin/bash\n### Generated by AutoDock Raccoon v.%s\n" % version

            if MapSource.get() == 0:
                # AutoGrid binary specification # TODO add a check for win too? 
                line += "export AUTOGRID=autogrid4\n"
                line += "type $AUTOGRID &> /dev/null || {\n"
                line += "        echo -e \"\\nError: the file [$AUTOGRID] doesn't exist or is not executable\\n\";\n"
                line += "        echo -e \"Try to specify the full path to the executable of the AutoGrid binary in the $0 script\";\n"
                line += "        echo -e \"( i.e. AUTOGRID=/usr/bin/autogrid4 )\\n\\n\";\n"
                line += "        echo -e \" [ virtual screening aborted]\\n\"\n"
                line += "        exit 1; }\n\n"
                line += ""

            # AutoDock binary specification
            line += "export AUTODOCK=autodock4\n"
            line += "type $AUTODOCK &> /dev/null || {\n"
            line += "        echo -e \"\\nError: the file [$AUTODOCK] doesn't exist or is not executable\\n\";\n"
            line += "        echo -e \"Try to specify the full path to the executable of the AutoDock binary in the $0 script\";\n"
            line += "        echo -e \"( i.e. export AUTODOCK=/usr/bin/autodock4 )\\n\\n\";\n"
            line += "        echo -e \" [ virtual screening aborted]\\n\"\n"
            line += "        exit 1; }\n\n"
            line += ""

            command = "./run.sh"
            master_script_name = path+os.sep+"RunVS.sh"
            Q = "'"
            spacer = "  "

        for i in header.split("\n"): # acrobatic moves for making a unified generator...
            line += "echo %s%s%s%s\n" % (Q, spacer, i, Q)

        if system == "Windows" and not cygwin.get():
            line += "echo.\necho                  == Press ENTER to start the calculation ==\n"
            line += "pause > NUL\n"
        else:
            line += "\necho -e \"\\n                 == Press ENTER to start the calculation ==\"\n"
            line += "read X\n"
            

        for DIR in DirJournal:
            if DIR[1]:
                dir = DIR[1]+os.sep+os.path.basename(DIR[0])
            else:
                dir = os.path.basename(DIR[0])
            line += ("echo %sDocking %s%s ==================================\n"% (Q, dir, Q)  )
            line += ("cd \"%s\"\n%s\ncd ..\n\n" % (dir, command))


        line += "echo %sCalculation completed.%s\n" % (Q,Q)
        if system == "Windows" and not cygwin.get():
            line += "pause > NUL\n"
        else:
            line += "read X\n"

        try:
            master_script = open(master_script_name, 'wb')
            master_script.writelines(line)
            master_script.close()
        except:
            tkMessageBox.showerror("Master script generation.", ("An error occurred when trying to generate the jobs list file."))
            return False

        if not system == "Windows":
            os.system("chmod +x \"%s\"" % (master_script_name))
        return True

    if TargetOS.get() == "pbs":
        # create the list of job dirs in which to go
        # for submitting the calculation
        try:
            file = open(path+os.sep+jobs_list, 'wb')
            for DIR in DirJournal:
                if DIR[1]:
                    dir = DIR[1]+os.sep+os.path.basename(DIR[0])
                else:
                    dir = os.path.basename(DIR[0])
                #dir = os.path.basename(DIR)
                dir = dir.rstrip('\n') # TODO EXPERIMENTAL!!!!
                file.write(dir+"\n") 
            file.close()
        except:
            tkMessageBox.showerror("PBS script generation.", ("An error occurred when trying to generate the jobs list file."))
            return False
        if CreateSmuggler(path):
            return True
        else:
            return False

def CreateSmuggler(path):
    # this function is called only for PBS jobs
    # cluster_scratch_dir = "$PBSTMPDIR" 
    # cluster_scratch_dir = "$PBSTESTDIR" # update from Bill Young 03/22/2010
    # cluster_scratch_dir = "$PBSREMOTEDIR" # update from Bill Young 04/21/2010
    cluster_scratch_dir = "$PBSTMPDIR"  # update from Lisa Dong 6/xx/2011
    if DEBUG: print "Creating the smuggler..."
    #filename = "vs_submit.sh"
    filename = "vs_cluster_submit.sh"
    end = PBShowmanyruns.get()
    line = "#!/bin/bash\n"
    line += "#\n# Generated with Raccoon | AutoDockVS v.%s\n#\n" % version
    line += "# This script can be used to submit jobs to any PBS-compatible\n"
    line += "# queuing system.\n\n"

    # TODO Add a description of the system for which it has been designed.
    # PBS and so on...
    #
    line += "### PATHS FOR EXECUTABLES ON THE CLUSTER\n"
    line += "# modify them to specify executables to be used\n"
    line += "# otherwise the binaries present in the $PATH variable\n"
    line += "# will be used\n"
    line += "# PBS qsub binary:\n"
    line += "QSUB=\"qsub\"\n"
    line += "# AutoDock binary:\n"
    line += "AUTODOCK=\"autodock4\"\n"
    # Set Autogrid if necessary"
    if MapSource.get() == 0:
        line += "# AutoGrid binary:\n"
        line += "AUTOGRID=\"autogrid4\"\n\n"

    line += "### PBS JOBS PARAMETERS\n"
    if end > 0:
        line += "# number of jobs submitted per ligand ( = number of DLG calculated per ligand)\n"
        line += "JOBS_PER_LIGAND=%s\n" % end 
    line += "# maximum CPU time allowed per ligand job\n"
    line += "CPUT=\"%s\"\n" % PBStime.get()
    #line += "WALLT=\"%s\"\n" % PBStime.get()
    line += "\n"

    line += "### JOB WORKING PATH\n"
    line += "# special path to move into before running the screening\n"
    line += "# This is usually very system-specific, but usually doesn't need to be modified.\n"
    line += "# Therefore unless you know what you are doing, leave it as it is\n"
    line += "WORKING_PATH=`pwd`\n\n"

    line += "### CUSTOM QUEUING OPTIONS\n"
    line += "# use the following line to set special options (e.g. specific queues)\n"
    line += "#OPT=\"-q MyPriorQueue\"\n"
    line += "OPT=\"\"\n\n"

    line +="### NODES SCRATCH DIRECTORY\n"
    line +="# specify this parameter if you want the jobs to use the scratch\n"
    line +="# disk space of the nodes.\n"
    line +="#\n"
    line +="# In PBS schedulers is generally referred to as a variable (i.e. $PBSTMPDIR)\n"
    line +="# If you're not going to use this option, leave it empty.\n#\n"
    line +="# NOTE: do *not* change or remove the single quotes below\n"
    line +="SCRATCH_DIR=''\n"

    line +="### JOBS ID LOG FILE\n"
    line +="# specify log file where PBS job id's of\n" 
    line +="# submitted jobs will be stored\n"
    line +="SUBMITTED_LOG='pbs_jobs_id.log'\n"
    line +="\n\n\n"

    line += "\n\n\n\n##################################################################################################\n"
    line += "##################################################################################################\n"
    line += "####### There should be no need to modify anything below this line ###############################\n"
    line += "##################################################################################################\n"
    line += "##################################################################################################\n\n\n"
    line += "\n"

    line +="#########################################################\n"
    line +="#                  TSRI usage option                    #\n"
    line +="#########################################################\n"
    line +="#\n"
    #line +="#     De-comment the following lines if you're going to run the vs\n"
    #line +="#     on the Garibaldi cluster at La Jolla.\n"
    #line +="#\n"
    #line +="#AUTODOCK=\"/garibaldi/people-b/applications/autodock/autodock4.2.3\"\n"
    #line +="#AUTOGRID=\"/garibaldi/people-b/applications/autodock/autogrid4.2.3\"\n"
    #line +="#QSUB=\"/usr/pbs/bin/qsub\"\n"
    #line +="#SCRATCH_DIR='$PBSTMPDIR'\n"
    #line +="#\n"
    line +="if [ ! \"$1\" == \"\" ]\n"
    line +="  then\n"
    line +="    if [ \"$1\" == \"-t\" ]\n"
    line +="      then\n"
    line +="        if [ ! `hostname` == \"%s\" ]\n" % ('garibaldi00') # garibaldi master node hostname
    line +="          then\n"
    line +="            echo -e \"ERROR: The current host doesn't seems to be Garibaldi\\n\"\n"
    line +="            echo -e \" Try without the '-t' option.\\n\"\n"
    line += "           echo -e \" [ virtual screening submission aborted]\\n\"\n"
    line +="            exit 1\n"
    line +="          else\n"
    line +="            AUTODOCK=\"%s\"\n" % ('/gpfs/home/forli/bin/autodock4')
    line +="            AUTOGRID=\"%s\"\n" % ('/gpfs/home/forli/bin/autogrid4')
    line +="            QSUB=\"%s\"\n" % ('/usr/bin/qsub')
    line +="            SCRATCH_DIR='%s'\n" % cluster_scratch_dir
    line +="        fi\n"
    line +="      else\n"
    line +="        echo -e \"\\nERROR: option $1 not recognized! \\n\\n\"\n"
    line +="        echo -e \" Usage\\n\"\n"
    line +="        echo -e \"   Launch the script for running the virtual screening:\\n\"\n"
    line +="        echo -e \"       ./%s\\n\"\n" % filename
    line +="        echo -e \"   Add the option '-t' if the script is going to be run on\"\n"
    line +="        echo -e \"   the Garibaldi cluster at TSRI La Jolla:\\n\"\n"
    line +="        echo -e \"       ./%s -t\\n\"\n" % filename
    line +="        echo -e \" [ virtual screening submission aborted]\\n\"\n"
    line +="        exit 1\n"
    line +="    fi\n"
    line +="fi\n\n"

    line += "# Checking for the command binaries\n"
    line += "type $AUTODOCK &> /dev/null || {\n"
    line += "        echo -e \"\\nError: the file [$AUTODOCK] doesn't exist or is not executable\\n\";\n"
    line += "        echo -e \"Try to specify the full path to the executable of the AutoDock binary in the script\";\n"
    line += "        echo -e \"( i.e. AUTODOCK=/usr/bin/autodock4 )\\n\\n\";\n"
    line += "        echo -e \" [ virtual screening submission aborted]\\n\"\n"
    line += "        exit 1; }\n\n"
    line += ""

    if MapSource.get() == 0:
        line += "type $AUTOGRID &> /dev/null || {\n"
        line += "        echo -e \"\\nError: the file [$AUTOGRID] doesn't exist or is not executable\\n\";\n"
        line += "        echo -e \"Try to specify the full path to the executable of the AutoGrid binary in the script\";\n"
        line += "        echo -e \"( i.e. AUTOGRID=/usr/bin/autogrid4 )\\n\\n\";\n"
        line += "        echo -e \" [ virtual screening submission aborted]\\n\"\n"
        line += "        exit 1; }\n\n"

    line += "type $QSUB &> /dev/null || {\n"
    line += "        echo -e \"\\nError: the file [$QSUB] doesn't exist or is not executable\\n\";\n"
    line += "        echo -e \"Try to specify the full path to the executable of the Qsub command binary in the script\";\n"
    line += "        echo -e \"( i.e. QSUB=/usr/bin/qsub )\\n\\n\";\n"
    line += "        echo -e \" [ virtual screening submission aborted]\\n\"\n"
    line += "        exit 1; }\n\n"

    line += "if [ ! -f jobs_list ]; then\n"
    line += "        echo -e \"\\nError: the file [jobs_list] doesn't exist or is not readable.\n"
    line += "        echo -e \"Check that the file has been created correctly or generate it manually [RISKY!]:\\n\"\n"
    line += "        echo -e \"    ls -d */ | grep -v maps > jobs_list\\n\""
    line += "        echo -e \"then run the submission again.\\n"
    line += "        echo -e \" [ virtual screening submission aborted]\\n\"\n"
    line += "        exit 1; \n\n"
    line += "fi\n"

    line += "# PBS node resources\n# There should be no reason for changing the following values\n"
    line += "NODES=1\n"
    line += "PPN=1\n"
    line += "MEM=512mb\n"
    line += "WALLT=\"$CPUT\"\n\n"

    if RCstatus.get() == 0:

        line += "echo -e \"\\n\\n\\n          ________________________________________________________________\"\n"
        line += "echo \"    __________//___________________________/////___________________/____________\"\n"
        line += "echo \"    _________/__/__________________________/____/__________________/____________\"\n"
        line += "echo \"    ________/____/___________/_____________/_____/_________________/____________\"\n"
        line += "echo \"    ________/____/__/_____/_/////___/////__/_____/__/////___/////__/___/________\"\n"
        line += "echo \"    _______/______/_/_____/__/_____/_____/_/_____/_/_____/_/_____/_/_//_________\"\n"
        line += "echo \"    _______////////_/_____/__/_____/_____/_/_____/_/_____/_/_______//_/_________\"\n"
        line += "echo \"    _______/______/_/____//__/___/_/_____/_/____/__/_____/_/_____/_/___/________\"\n"
        line += "echo \"    _______/______/__////_/___///___/////__/////____/////___/////__/____/_______\"\n"
        line += "echo \"          ________________________________________________________________\"\n"
        line += "echo \"                                     ______ \"\n"
        line += "echo \"                                    /      \\ \"\n"
        line += "echo \"                                   /        \\ \"\n"
        line += "echo \"                                  /          \\   Raccoon\"\n"
        line += "echo \"                                  \\    /\\    /    Virtual \"\n"
        line += "echo \"                                   \\  /  \\  /      Screening \"\n"
        line += "echo \"                                    \\/ /\\ \\/        Generator       \"\n"
        line += "echo \"                                     /\\  \\ \"\n"
        line += "echo \"                                   /\\  \\__\\    version %s\"\n" % version
        line += "echo \"                                  /  \\__\\ \"\n"
        line += "echo \"                                 /____\\ \"\n" 
        line += "echo \"\"\n"
        line += "echo -e \"                   `cat %s | wc -l ` jobs are going to be submitted on `hostname`.\"\n" % jobs_list
        line += "if [ \"$1\" == \"-t\" ]; then\n"
        line += "echo \"                              => TSRI mode is ON <=\"\n"
        line += "fi\n"
        line += "echo -e \"\\n\\n\"\n"
    # TODO to be changed...
    """
    if RCstatus.get() == 0: # the confirmation is required only for single-receptor mode
        line += "echo \"                            Press <ENTER> to start...\"\n"
        line += "echo \"                              [ Ctrl-C to abort ]\"\n"
        line += "read X \n"
    """
    # automatic submission after 10 seconds...
    line += "echo \"                         The submission is going to start in 10 seconds...\"\n"
    # line += "echo \"                            Press <ENTER> to start ...\"\n"
    line += "echo \"                              [ Ctrl-C to abort ]\"\n"
    line += "read -st 10 \n"

    #line += "WD=`pwd`\n"
    line += "echo -ne \"\\n\\n==> Starting the virtual screening submission.\n    Working dir: $WORKING_PATH\\n\\n\"\n"
    #line += "\n"
    line +="SUBMITTED_LOG=$WORKING_PATH/$SUBMITTED_LOG\n"
    line += "while read DIR\n"
    line += "    do\n"
    line += "        # skip empty lines in the list of jobs\n"
    line += '        if [[ ! "$DIR" == "" && ! "$DIR" == "\\n" ]]; then\n'
    line += "        cd \"$WORKING_PATH/$DIR\"\n"
    line += "        NAME=`basename $DIR`\n"
    # Set the extra loop for multiple DLG per ligand
    # and specify the name ligand_protein.#.job
    if end > 1:
        line += "        # Set the loop for multiple DLG's per ligand\n"
        line += "        for i in `seq 1 $JOBS_PER_LIGAND`\n"
        line += "            do\n"
        job_name = "$NAME.$i.job"
        tab = "    "
    else:
        tab = ""
        job_name = "$NAME.job"
    line += "%s        # start populating the job content...\n" % (tab)
    line += "%s        echo \"#!/bin/bash\" > %s\n" % (tab, job_name) 
    line += "%s        echo cd \"$WORKING_PATH/$DIR\" >> %s \n" % (tab, job_name)
    line += "%s        if [ $SCRATCH_DIR ]; then\n" % tab
    #line += "%s            then\n" % tab
    line += "%s                echo cp * \"$SCRATCH_DIR\" >> %s\n"  % (tab, job_name)
    line += "%s                echo cd \"$SCRATCH_DIR\" >> %s\n" % (tab, job_name)
    line += "%s        fi\n" % tab
    if MapSource.get() == 0:
        line += "%s        echo \"$AUTOGRID -p *.gpf -l grid_out.glg\" >> %s\n" % (tab, job_name) # TODO fragile for the *.gpf?
    if end > 1:
        line += "%s        echo \"$AUTODOCK -p $NAME.dpf -l $NAME.$i.dlg\" >> %s\n" % (tab, job_name)
        line += "%s        if [ $SCRATCH_DIR ]; then \n" % tab
        # line += "%s            then\n" % tab
        line += "%s                echo cp $NAME.$i.dlg \"$WORKING_PATH/$DIR\" >> %s\n"  % (tab, job_name)
        line += "%s        fi\n" % tab
    else:
        line += "%s        echo \"$AUTODOCK -p $NAME.dpf -l $NAME.dlg\" >> %s\n" % (tab, job_name)
        line += "%s        if [ $SCRATCH_DIR ]; then \n" % tab
        # line += "%s            then\n" % tab
        line += "%s                echo cp $NAME.dlg grid_out.glg \"$WORKING_PATH/$DIR\" >> %s\n" % (tab, job_name)
        line += "%s        fi\n" % tab
    if RemoveMapsAfter.get():
        line += "%s        echo cd \"$WORKING_PATH/$DIR\" >> %s \n" % (tab, job_name) # TODO  test this! for what to cd in the path?
        line += "%s        echo \"rm -fr *.map *.maps.fld *.maps.xyz\" >> %s\n" % (tab, job_name)
    line += "%s        # submitting the job...\n" %(tab)
        
    line += "%s        chmod +x \"%s\"\n" % (tab, job_name)
    line += "%s        echo -n \"$NAME : \"| tee -a $SUBMITTED_LOG\n" % tab
    line += "%s        $QSUB $OPT -l cput=$CPUT -l nodes=1:ppn=1 -l walltime=$WALLT -l mem=$MEM %s | tee -a $SUBMITTED_LOG\n" % (tab, job_name)
    #line += "        fi\n" # TODO doublecheck this?
    if end > 1:
        line += "        done\n"
    #line += "        cd ..\n"
    line += "        fi\n"  # TODO doublecheck this?
    line += "done < %s\n" % jobs_list
    line += "echo -ne \"\\n     [ submission completed ]    \\n\\n\"\n"
    try:
        output = open(path+os.sep+filename, 'wb')
        output.writelines(line)
        output.close()
        if not system == "Windows":
            os.system("chmod +x \"%s\"" % (path+os.sep+filename))
        return True
    except:
        tkMessageBox.showerror("PBS script generation.", ("An error occurred when trying to generate the %s file." % filename))
        return False


def InitializeLog(outdir = None, filename = None):
    if not outdir and not filename:
        return False
    if not outdir:
        outdir = ""
    #global LogFile, first_time
    if system == "Windows":
        os.environ.get("USERNAME")
    else:
        user = os.environ["USER"]
    machine = system_info[1]
    operative_system = system_info[0]
    
    if TargetOS.get() == "lin":
        target_machine = "Workstation"
    if TargetOS.get() == "pbs":
        target_machine = "Linux clusters"
    if TargetOS.get() == "win":
        target_machine = "Windows"

    # take a look at the clock
    date = datetime.datetime.now()
    year = str(date.year)
    month = str(date.month)
    day = str(date.day)
    hour = str(date.hour)
    minute = str(date.minute)
    second = str(date.second)             # too much?
    microsecond = str(date.microsecond)    # waaay to much!

    # VSgen-2009.7.26.log
    if not filename:
        log_name = outdir+os.sep+os.path.basename(outdir)+"_raccoonVS-"+year+"."+month+"."+day+".log"
    else:
        log_name = filename
    
    full_date = date.strftime("%Y-%B-%d %H:%M")


    if RCstatus.get() == 0:
        receptor_count = 1    
    else:
        receptor_count = len(receptorScrolledListBox.get('0', END))

    ligand_count = str(TotalAcceptedLigands.get())

    tot_number_jobs = str( (TotalAcceptedLigands.get() * receptor_count  ) )

    header = """
           ________________________________________________________________
    
    __________//___________________________/////___________________/____________
    _________/__/__________________________/____/__________________/____________
    ________/____/___________/_____________/_____/_________________/____________
    ________/____/__/_____/_/////___/////__/_____/__/////___/////__/___/________
    _______/______/_/_____/__/_____/_____/_/_____/_/_____/_/_____/_/_//_________
    _______////////_/_____/__/_____/_____/_/_____/_/_____/_/_______//_/_________
    _______/______/_/____//__/___/_/_____/_/____/__/_____/_/_____/_/___/________
    _______/______/__////_/___///___/////__/////____/////___/////__/____/_______
    
          ________________________________________________________________
                                     ______ 
                                    /      \\ 
                                   /        \\ 
                                  /          \\   Raccoon
                                  \\    /\\    /    Virtual 
                                   \\  /  \\  /      Screening 
                                    \\/ /\\ \\/        Generator
                                     /\\  \\ 
                                   /\\  \\__\\    version %s
                                  /  \\__\\ 
                                 /____\\
        
        
                  date :\t%s
      output directory :\t%s
    total docking jobs :\t%s
      operative system :\t%s [ %s ]
   generating jobs for :\t%s


      ===================================== Ligand filters =========================================
    
                       Filtering criteria
                       ------------------
                                   MIN      MAX
                    Hb donors :   %4s  -  %4s
                 Hb acceptors :   %4s  -  %4s
             Molecular weight :   %4s  -  %4s
        Total number of atoms :   %4s  -  %4s
              Rotatable bonds :   %4s  -  %4s
        Reject non-AD atypes  :   %s
    
    
        Ligands accepted for the virtual-screening: %s


""" % ( version, full_date, outdir, tot_number_jobs, operative_system, machine, target_machine , str(HbDmin.get()), str(HbDmax.get()), str(HbAmin.get()), str(HbAmax.get()), str(MWmin.get()), str(MWmax.get()), str(NatMin.get()), str(NatMax.get()), str(TORSDOFmin.get()), str(TORSDOFmax.get()), str(DoRejectATypes.get()), ligand_count)   
    

    # receptor
    if RCstatus.get() == 0:
        receptor_log = "\n      ============================= Single target receptor ==========================================\n"
        receptor_log = receptor_log+"\n   Target structure:\nTARGET>\t"+ RecFilename.get()

    else:
        receptor_log = "\n      =========================== Multiple target receptors =========================================\n"
        receptor_log = receptor_log+"\n   Total target structures :" + str(receptor_count)+"\n"
        # append the list of receptor structures
        for rec in receptorScrolledListBox.get('0', END):
            receptor_log = receptor_log+"\nTARGET>\t"+rec
    header = header + receptor_log

    # flexible residues
    if DoFlex.get():
        if FlexResDefined.get():
            flex_log = "\n\n      ------------------------------- Flexible residues -----------------------------------\n\n"
            if DoFlexFromWhat.get() == 1:
                if FlexResFileName.get(): # TODO in theory it shouldn't be necessary
                    flex_log = flex_log + "FLEX> Flexible residues from the file :\t"+FlexResFileName.get()
                else:
                    if DEBUG : print "RETURNING A SHAMEFUL FALSE: problems in logging the flex residues [FlexResFileName.get() = ", FlexResFileName.get(), "]"
                    return False
            if DoFlexFromWhat.get() == 2:
                if FlexResSelected.get(): # TODO in theory it shouldn't be necessary
                    flex_log = flex_log + "FLEX> Flexible residues generated from the selection : "+ FlexResSelected.get()
                else:
                    if DEBUG :print "RETURNING A SHAMEFUL FALSE: problems in logging the flex residues [FlexResSelected.get() = ", FlexResSelected.get(), "]"
                    return False
            header = header + flex_log + "\n"


    
    # Maps
    maps_log = "\n\n      ===================================== Maps ====================================================\n"

    if MapSource.get() <= 1:
        if MapSource.get() == 0:
            maps_log = maps_log + "\n   Grid mode : calculated in each job.\n"
            maps_log = maps_log + "   Grid param file template :\n\n"
    
        if MapSource.get() == 1:
            if CacheMapPolicy.get() == "Make copies [ use more disk space ]":
                maps_log = maps_log + "\n   Grid mode : calculated now and >copied< in each ligand job directory.\n"
                maps_log = maps_log + "   Grid param file template :\n\n"
            if CacheMapPolicy.get() == "Make symbolic links [ save disk space ]":
                maps_log = maps_log + "\n   Grid mode : calculated now and >linked< in each ligand job directory.\n"
                maps_log = maps_log + "   Grid param file template :\n\n"
            maps_log = maps_log+("\t [ AutoGrid binary file used : |%s| ]" % AutoGridBin.get())

        # add the gpf lines to the log
        for line in GPFcontent.get('1.0', END).split('\n'):
            if not line.strip(): # get rid of empty lines
                continue
            else:
                maps_log = maps_log+"\nGPF>\t"+line#"\n"
        if GPFParameterFile.get():
            maps_log = maps_log+(" [ the parameter file |%s| has been copied ]\n\n" % GPFParameterFile.get())

    if MapSource.get() == 2:
        if CacheMapPolicy.get() == "Make copies [ use more disk space ]":
            cache_policy = " >copied< "
        if CacheMapPolicy.get() == "Make symbolic links [ save disk space ]":
            cache_policy = " >linked< "
        maps_log = maps_log + "\n   Grid mode : use pre-calculated"+cache_policy+"in each ligand job directory.\n"
        maps_log = maps_log + "   Grid cache dir : "+CacheMapDirName.get()

    header = header + maps_log


    docking_log = "\n\n     ==================================  Docking parameters ========================================\n"

    if docking_set.get() == "From template...":
        docking_log = docking_log+"\n   Docking mode : docking parameters will be >generated from template< for each ligand.\n"
        docking_log = docking_log+"   Docking param file template :\n\n"
        for line in DPFcontent.get(1.0, END).split('\n'):
            if not line.strip(): # get rid of empty lines
                continue
            else:
                docking_log = docking_log+"\nDPF>\t"+line
        if DPFParameterFile.get():
            docking_log = docking_log+("\n\n[ the parameter file %s has been copied ]" % DPFParameterFile.get())
    header = header + docking_log

    ligands_log = "\n\n     ======================================  Ligands list ============================================\n\n"
    for ligand in LigandDictionary.keys():
        if LigandDictionary[ligand]["accepted"]:
            ligands_log += "\nLIGAND> "+ligand
    header += ligands_log
    try:
        LOG = open(log_name, 'w')
    except:
        if DEBUG: print "problems in opening the log file"
        InfoMessage.set('Problems in opening the log file... generation aborted...')
        return False
    LOG.write(header) # DANGER
    return LOG

def MakeTar(source_dir, tarfilename):

    if DEBUG:
        print "MakeTar> creating the tar from the source =>", source_dir
        print "MakeTar> The filename is    =>", tarfilename

    if TarFile.get() == "[disabled]":
        return True
    if TarFile.get() == "Tar (uncompressed)":
        filemode = "w"
        ext = ".tar"
    if TarFile.get() == "Tar (Bz2 compression)":
        filemode = "w:bz2"
        ext = ".tar.bz2"
    if TarFile.get() == "Tar (Gzip compression)":
        filemode = "w:gz"
        ext = ".tar.gz"

    tarfilename += ext
    InfoMessage.set('Writing the VS package...(this could take a while)')
    root.update()
    short_name = os.path.basename(source_dir)
    try:
        if DEBUG: print "Trying to generate the tar file", tarfilename
        vs_tar = tarfile.open(name = tarfilename, mode = filemode)
        root.update()
        vs_tar.add(source_dir, arcname = short_name)
        root.update()
        vs_tar.close()
        return True
    except:
        InfoMessage.set('Error in writing the VS package...')
        tkMessageBox.showwarning("Tar file error", "Unable to perform the operation.") 
        if DEBUG: print "problems in creating the tar file"
        return False


def MakeZip(source_dir, zipfilename):
    # compression level
    compression = zipfile.ZIP_DEFLATED

    zipfilename += ".zip"
    prefix = os.path.basename(source_dir)
    file_list = []
    InfoMessage.set('Creating the zip file...')
    root.update()
    try:
        output = zipfile.ZipFile(zipfilename, mode = 'w')
    except:
        InfoMessage.set('Zip file creation error!')
        root.update()
        return False
    for ROOT, SUBFOLDERS, FILES in os.walk(source_dir):
        if DEBUG:
            print "=================\nMAKEZIP > "
            print "ROOT", ROOT
            print "\tSUBFOLDS", SUBFOLDERS
            print "\t\tFILES", FILES
        for item in FILES:
            file_list.append(os.path.join(ROOT,item))

    for item in file_list:
        if DEBUG: print "Adding |%s| to %s" % (item, zipfilename)
        if not zipfilename in item: # to avoid a nice infinite, disk-hungry loop
            try:
                tmp = item
                shortname = tmp.replace(source_dir, prefix)
                output.write(item, arcname = shortname, compress_type = compression)
                InfoMessage.set('Adding files to the Zip file...(this could take a while)')
                root.update()
            except:
                InfoMessage.set('Error adding files to the Zip archive!')
                root.update()
                return False
    return True


def ImportLigList(filename = None):
    if not filename:
        filename = askopenfilename(title = "Select a ligand list file......", filetypes =[("Ligands list", "*.lig"), ("Any file...", '*')])
        if not filename:
            return False
    try:
        list = get_lines(filename)
    except:
        tkMessageBox.showwarning("Ligand list", "Warning: unable to open the selected file.") 
        return False
    if len(list)>0:
        before = len(LigandDictionary) # this remove spurious counts if there are duplicates in the file
        missing = []
        found = []
        for item in list:
            item = item.strip()  # XXX TEST
            if not item[0] == "#":
                #item = item.rstrip() ORG
                #item = item.strip()  # XXX TEST
                if os.path.isfile(item):
                    found.append(item)
                else:
                    missing.append([item, "missing file"])
        if len(found) == 0:
            tkMessageBox.showwarning("Ligand list", "No ligands loaded!\nCheck the list content...\n(maybe it's not a list)")
            return False
        if len(missing) > 0 and tkMessageBox.askyesno("Ligands imported", "%d ligands have not been found.\n\nDo you want to inspect the list of rejected ligands?" % len(missing)):
            issueInspectorWindow("List of discarded ligands", missing)
            return
        else:
            openLigand(found)
            after = len(LigandDictionary) # this remove spurious counts if there are duplicates in the file
            tkMessageBox.showinfo("Ligand list", ("%d new ligands imported." % (after - before)))
            return True
    else:
        tkMessageBox.showwarning("Ligand list", "Empty file... apparently.") 
        return False

def ExportLigList():
    SaveLig = StringVar()
    SaveLig.set("all")
    header  = "# Ligand list saved by Raccoon"
    header += "# "

    def ExportDone(filename = None):
        ExportLigWin.destroy()

        list = []
        if SaveLig.get() == "all":
            for ligand in LigandDictionary:
                list.append(ligand)
        if SaveLig.get() == "accepted":
            for ligand in LigandDictionary:
                if LigandDictionary[ligand]["accepted"]: list.append(ligand)
        if SaveLig.get() == "rejected":
            for ligand in LigandDictionary:
                if not LigandDictionary[ligand]["accepted"]: list.append(ligand)
        if len(list):
            if not filename:
                filename = asksaveasfilename(title = "Select a ligand list file......", filetypes = [('Ligand list', '*.lig'), ("Any file...", "*")] )
            if not filename:
                EnableInterface()
                return

            #file = open(filename, 'w')
            #for item in list:
            #    print >> file, item
            #file.close()
            writeLines(file, list)

        EnableInterface()
        return

    def ExportAbort():
        ExportLigWin.destroy()
        EnableInterface()    

    if not len(LigandDictionary):
        return
    try:
        ExportLigWin.lift()
    except:
        DisableInterface()    

        rejected = 0
        total = len(LigandDictionary.keys())
        for item in LigandDictionary.keys():
            if not LigandDictionary[item]["accepted"]:
                rejected += 1
        accepted = total - rejected

        all_msg      = "All ligands    [ %d ]" % total
        accepted_msg = "Accepted [ %d ]" % accepted
        rejected_msg = "Rejected  [ %d ]" % rejected

        ExportLigWin = Toplevel(root)
        ExportLigandWin.transient(root)
        ExportLigWin.title("Export list")
        ExportLigWin.winfo_toplevel().resizable(NO,NO)
        SelectionLevel = Pmw.Group(ExportLigWin, tag_text = "Select a set...")
        SaveLigDefault = Radiobutton(SelectionLevel.interior(), text=all_msg, variable = SaveLig, value = "all" )
        SaveLigDefault.grid(row = 0, column = 0, sticky = W) # Default
        Radiobutton(SelectionLevel.interior(), text=accepted_msg, variable = SaveLig, value = "accepted").grid(row = 1, column = 0, sticky = W, padx = 15)
        Radiobutton(SelectionLevel.interior(), text=rejected_msg, variable = SaveLig, value = "rejected").grid(row = 2, column = 0, sticky = W, padx = 15)
        SelectionLevel.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = W, columnspan = 2)
        SaveLigDefault.invoke()

        Button(ExportLigWin, text = "Save", command = ExportDone).grid(row = 10, column = 0, columnspan = 1, padx = 3, pady= 10)
        Button(ExportLigWin, text = "Cancel", command = ExportAbort).grid(row = 10, column = 1, padx = 3, pady= 10)
        #EnableInterface()

# Ligand page ############### p1 ################################
add_single_icon = Tkinter.PhotoImage(data=icon_open_b64)
add_dir_icon = Tkinter.PhotoImage(data=icon_add_dir_b64)
add_dir_recursive_icon = Tkinter.PhotoImage(data=icon_add_dir_recursive_b64)
remove_selected_icon = Tkinter.PhotoImage(data=icon_remove_sel_b64)
remove_all_icon = Tkinter.PhotoImage(data=icon_remove_all_b64)
pdbqt_lig_opt_icon = Tkinter.PhotoImage(data=icon_pdbqt_lig_opt_b64)
lig_filters_icon = Tkinter.PhotoImage(data=icon_lig_filters_b64)
open_smfolder_icon = Tkinter.PhotoImage(data=open_small_folder_icon_b64)
ok_icon = Tkinter.PhotoImage(data=ok_icon_b64)
edit_icon = Tkinter.PhotoImage(data=edit_icon_b64)
default_setting_icon = Tkinter.PhotoImage(data= default_setting_icon_b64)
preview_icon = Tkinter.PhotoImage(data= preview_icon_b64)
single_rec_icon = Tkinter.PhotoImage(data= single_receptor_icon_b64 )
multi_rec_icon = Tkinter.PhotoImage(data= multi_receptor_icon_b64)
split_icon = Tkinter.PhotoImage(data= split_icon_b64)
  

LigandButtonsGroup = Frame(p1, relief = FLAT)
AddLigandsButton = Button(LigandButtonsGroup, compound = LEFT, text='Add ligands', image = add_single_icon, command = openLigand)
#AddLigandsButton = Button(LigandButtonsGroup, compound = LEFT, image = add_single_icon, command = openLigand)
AddLigandsButton.configure(highlightbackground = 'black') # , width = 80, height = 25)
#            indicatoron = False, selectcolor = 'lightblue', disabledforeground = 'gray', highlightbackground = 'black')
AddLigandsButton.bind("<Button-3>", lambda x : help("loadlig"))
AddLigandsButton.pack(expand=NO, anchor=W, side=LEFT)
AddLigandsDirButton = Button(LigandButtonsGroup, compound = LEFT, text='Add directory', image = add_dir_icon, command = openLigandDir)
#AddLigandsDirButton = Button(LigandButtonsGroup, compound = LEFT, image = add_dir_icon, command = openLigandDir)
AddLigandsDirButton.pack(expand=NO, anchor=W, side=LEFT)
AddLigandsDirButton.bind("<Button-3>", lambda x : help("loadligdir"))
AddLigandsDirButton.configure(highlightbackground = 'black') #, width = 80, height = 25)
AddLigandsDirRecursiveButton = Button(LigandButtonsGroup, compound = LEFT, text='Add recursively', image = add_dir_recursive_icon, command = lambda : openLigandDir(recursive = True))
#AddLigandsDirRecursiveButton = Button(LigandButtonsGroup, compound = LEFT, text='Scan\ndirectories', image = add_dir_recursive_icon,
#AddLigandsDirRecursiveButton = Button(LigandButtonsGroup, compound = LEFT, image = add_dir_recursive_icon,
#                command = lambda : openLigandDir(recursive = True))
AddLigandsDirRecursiveButton.bind("<Button-3>", lambda x : help("loadligrecursive"))
AddLigandsDirRecursiveButton.pack(expand=NO, anchor=W, side=LEFT)
AddLigandsDirRecursiveButton.configure(highlightbackground = 'black') #, width = 80, height = 25)

LigandButtonsGroup.pack(fill = 'both', expand = 0, padx = 7, pady = 7, anchor = S)
Ligand_group = Pmw.Group(p1, tag_textvariable = LigandListLabel)
LigandScrolledListBox = Listbox(Ligand_group.interior(), selectmode=EXTENDED, bg = 'white') # white bg
LigandScroll = Scrollbar(Ligand_group.interior(), command=LigandScrolledListBox.yview)
LigandScroll.pack(anchor = N, side = RIGHT, fill = 'y')
LigandScrolledListBox.configure(yscrollcommand=LigandScroll.set)
LigandScrolledListBox.grid(row = 1, column = 0, columnspan = 3, sticky = N+S+W+E)
LigandScrolledListBox.config(fg = 'black', font = ("Courier", 9, "normal"))
LigandScrolledListBox.pack(fill = BOTH, expand = 1)
LigandScrolledListBox.bind("<Button-3>", lambda x : help("ligscroll"))
Ligand_group.pack(fill = BOTH, expand = 1, padx = 10, pady = 10, side = TOP , anchor = N)

FilterButton = Button(p1, compound = LEFT, text = "Filter\nligands", image = lig_filters_icon, command = LigandFilterOptions)
FilterButton.pack(expand = NO, anchor = W, side = LEFT)
FilterButton.bind("<Button-3>", lambda x : help("filterlig"))
FilterButton.configure(highlightbackground = 'black', width = 90, height = 30)
def LigStats():
    print "Lig stats"
    for i in LigandDictionary:
        print LigandDictionary[i]


#LigStatisticsButton = Button(p1, compound = LEFT, text = "Ligand\nstats...", image = lig_filters_icon, command = LigStats)
#LigStatisticsButton.pack(expand = NO, anchor = W, side = LEFT)
#LigStatisticsButton.bind("<Button-3>", lambda x : help("filterlig"))
#LigStatisticsButton.configure(highlightbackground = 'black', width = 80, height = 25)


LigandPDBQTOptButton = Button(p1, compound = LEFT, text = "PDBQT generation options", image = pdbqt_lig_opt_icon, command = LigandImportOptions)
LigandPDBQTOptButton.pack(expand = NO, anchor = E, side = RIGHT)
LigandPDBQTOptButton.bind("<Button-3>", lambda x : help("ligpdbqtopt"))
LigandPDBQTOptButton.configure(highlightbackground = 'black')

RemoveLigandsButton = Button(LigandButtonsGroup, compound = LEFT, text='Remove selected', image = remove_selected_icon ,command=removeLigand)
#RemoveLigandsButton = Button(LigandButtonsGroup, compound = LEFT, image = remove_selected_icon ,command=removeLigand)
RemoveLigandsButton.pack(expand=NO, anchor=W, side=LEFT)
RemoveLigandsButton.bind("<Button-3>", lambda x : help("delsellig"))
RemoveLigandsButton.configure(highlightbackground = 'black') #, width = 80, height = 25)
RemoveAllLigandsButton = Button(LigandButtonsGroup, compound = LEFT, text='Remove all', image = remove_all_icon, command=removeAllLigands)
#RemoveAllLigandsButton = Button(LigandButtonsGroup, compound = LEFT, image = remove_all_icon, command=removeAllLigands)
RemoveAllLigandsButton.pack(expand=NO, anchor=W, side=LEFT)
RemoveAllLigandsButton.bind("<Button-3>", lambda x : help("delalllig"))
RemoveAllLigandsButton.configure(highlightbackground = 'black') #, width = 80, height = 25)

# Receptor page ############### p2 ##################################
DefaultLigOptions()

RCstatus.set(0)
MakeReceptorMenu()
# set defaults
Single_target_radio.invoke()
DoFlex.set(0)
SetFlexibleMode()

# Maps page ################### p3 ##################################
# AutoGrid options
AutoGridMenu = Pmw.Group(p3, tag_text="Affinity maps") 
#AutoGridWhen1 = Radiobutton(AutoGridMenu.interior(), text=' every \njob', value=0, variable=MapSource, 
AutoGridWhen1 = Radiobutton(AutoGridMenu.interior(), text='Run AutoGrid\nat every job', value=0, variable=MapSource, 
    highlightbackground = 'black', selectcolor = 'lightblue', command = MapMenu, indicatoron = False, height = 2, width = 10)
AutoGridWhen1.grid(row = 1, column = 0, ipadx = 5, ipady = 5)
AutoGridWhen2 = Radiobutton(AutoGridMenu.interior(), text='Calculate\nmaps now', value=1, variable=MapSource, 
    highlightbackground = 'black', selectcolor = 'lightblue', command = MapMenu, indicatoron = False, height = 2, width = 10)
AutoGridWhen2.grid(row = 1, column = 1, ipadx = 5, ipady = 5)
AutoGridWhen3 = Radiobutton(AutoGridMenu.interior(), text='Use pre-calculated\nmap files', value=2, variable=MapSource, 
    highlightbackground = 'black', selectcolor = 'lightblue', command = MapMenu, indicatoron = False, height = 2, width = 10)
AutoGridWhen1.config(width = 15)
AutoGridWhen2.config(width = 15)
AutoGridWhen3.config(width = 15)
AutoGridWhen3.grid(row = 1, column = 2, ipadx = 5, ipady = 5)
AutoGridMenu.pack(expand = 1, anchor = NW, padx = 10, ipadx = 3, ipady = 3)

AGoptions = Pmw.Group(p3, tag_pyclass = None)
AutoGridExecButton = Button(AGoptions.interior(), compound = LEFT, text ="Set the AutoGrid executable", image = open_smfolder_icon, command = GetAutoGrid)
AutoGridExecLabel = Label(AGoptions.interior(),textvariable = AutoGridBin)
AutoGridExecButton.pack(side = TOP, padx = 10)
AutoGridExecLabel.pack(side = TOP, padx = 10)
AGoptions.pack(side = LEFT, anchor = W, padx = 10)

MakeGPFMenu()

# set defaults
MapSource.set(0)
AutoGridWhen3.config(state = DISABLED)
AutoGridWhen1.invoke() # Select the default as "Run AG in each job"

# Docking page ########################## p4 ##############################

docking_set = StringVar()
docking_setup_interface("")

# Summary page  #################### p5 ###################################

# Create the "Toolbar" contents of the page.

Summary_group = Pmw.Group(p5, tag_text = 'Summary')
"""
Summary_group.grid_rowconfigure(1, weight = 1)
Summary_group.grid_rowconfigure(2, weight = 1)
Summary_group.grid_rowconfigure(3, weight = 1)
Summary_group.grid_rowconfigure(4, weight = 1)
Summary_group.grid_rowconfigure(5, weight = 1)
Summary_group.grid_columnconfigure(1, weight = 1)
Summary_group.grid_columnconfigure(2, weight = 1)
Summary_group.grid_columnconfigure(3, weight = 1)
"""



#Summary_group.grid_columnconfigure(1, weight = 1)
Label(Summary_group.interior(), text = "Ligands : ", font = ('Helvetica', 12, 'bold' )).grid(row = 1, column = 1, padx = 5, sticky = E)
Label(Summary_group.interior(), text = "Receptor(s) : ",font = ('Helvetica', 12, 'bold' ) ).grid(row = 2, column = 1, padx = 5, sticky = E)
Label(Summary_group.interior(), text = "Maps : ", font = ('Helvetica', 12, 'bold' )).grid(row = 3, column = 1, padx = 5, sticky = E)
Label(Summary_group.interior(), text = "Docking : ", font = ('Helvetica', 12, 'bold' )).grid(row = 4, column = 1, padx = 5, sticky = E)
SetOutDirButton = Button(Summary_group.interior(), text ="Set directory...", command = SetJobDirectory, image = open_smfolder_icon, 
compound=LEFT,fg = 'red', justify = LEFT)
SetOutDirButton.grid(row = 5, column = 1, padx = 5, sticky = E)



"""
def SetSessionFilename(filename = None):
    # TODO!!!
    if not filename:
        filename = asksaveasfilename(title = "Select a ligand list file......", filetypes = [('Ligand list', '*.lig'), ("Any file...", "*")] )
        if not filename:
            return
Label(Summary_group.interior(), text = "Session log file : ", font =('Helvetica', 11, 'bold') ).grid(row = 0, column = 1, padx = 5, sticky = E)
SetSessionButton = Button(Summary_group.interior(), text ="...", command = SetSessionFilename, justify = LEFT)
SetSessionButton.grid(row = 0, column = 2, padx = 5, sticky = E)

SessionFileLabel = Label(Summary_group.interior(), textvariable = JobDirectory, justify = LEFT)
SessionFileLabel.grid(row = 6, column = 2, padx = 5, sticky = W)
"""





LigSummaryLabel = Label(Summary_group.interior(), textvariable = LigandSummary, justify = LEFT)
LigSummaryLabel.grid(row = 1, column = 2, padx = 5, sticky = W)

RecSummaryLabel = Label(Summary_group.interior(), textvariable = ReceptorSummary, justify = LEFT)
RecSummaryLabel.grid(row = 2, column = 2, padx = 5, sticky = W)

MapsSummaryLabel = Label(Summary_group.interior(), textvariable = MapsSummary, justify = LEFT)
MapsSummaryLabel.grid(row = 3, column = 2, padx = 5, sticky = W)

DockSummaryLabel = Label(Summary_group.interior(), textvariable = DockingSummary, justify = LEFT)
DockSummaryLabel.grid(row = 4, column = 2, padx = 5, sticky = W)

OutputDirLabel = Label(Summary_group.interior(), textvariable = JobDirectory, justify = LEFT)
OutputDirLabel.grid(row = 5, column = 2, padx = 5, sticky = W)
OutputDirLabelInfo = Label(Summary_group.interior(), textvariable = JobDirectoryInfo)
OutputDirLabelInfo.grid(row = 6, column = 2, columnspan = 3, padx = 5, sticky = S)

JobsSummaryLabel = Label(Summary_group.interior(), textvariable = JobsSummary)
JobsSummaryLabel.grid(row = 7, column = 1, columnspan = 2, padx = 5, sticky = S)
Summary_group.pack(anchor = N, side = TOP, fill = 'both', expand = 1, padx = 10, pady = 10)#

LigSummaryLabel.config(fg = 'red')
RecSummaryLabel.config(fg = 'red')
MapsSummaryLabel.config(fg = 'red')
DockSummaryLabel.config(fg = 'red')

job_subsplitting = StringVar()
job_subsplitting.set("[ off ]")



# OS specific options
Summary_group2 = Pmw.Group(p5, tag_text = 'OS options')
LinuxOptionsPanel = Pmw.Group(Summary_group2.interior(), tag_pyclass = None)
PBSOptionsPanel = Pmw.Group(Summary_group2.interior(), tag_pyclass = None)
WinOptionsPanel = Pmw.Group(Summary_group2.interior(), tag_pyclass = None)
SystemButton1 = Radiobutton(Summary_group2.interior(), text='Workstation', value='lin', variable=TargetOS, command = GetOSoption)
SystemButton1.grid(row = 1, column = 0, sticky = W+N, padx = 5)
SystemButton2 = Radiobutton(Summary_group2.interior(), text='Linux cluster', value='pbs', variable=TargetOS, command = GetOSoption)
SystemButton2.grid(row = 1, column = 1, sticky = W+N, padx = 5)


# TODO useless?
if system == "Linux" or system == "Darwin":
    SystemButton1.invoke()
if system == "Windows":
    SystemButton1.invoke()

SystemButton1.invoke()

Summary_group2.pack(anchor = N, side = TOP, expand = 0, padx = 10, pady = 5)#

# AutoDock Logo
"""
Logo = Canvas(root, width =360, height=73)
logo = Tkinter.PhotoImage(master=root, data=LOGO_BASE64)
Logo.create_image(170,35, image=logo, anchor=CENTER)
Logo.pack(anchor=CENTER, side = BOTTOM)
"""

InfoInit() # Generate the info bar

# Line for avoiding the destruction of the window
root.protocol("WM_DELETE_WINDOW", confirm)

# FINAL GENERATE BUTTON
#TheButton = Button(p5, text='G E N E R A T E', fg='black', bg = 'red', state = DISABLED, command = TheFunction, height = 3 )
#TheButton = Button(p5, text='G E N E R A T E', fg='black', bg = '#000000', state = DISABLED, command = TheFunction, height = 3 )
TheButton = Button(p5, text='G E N E R A T E', fg='black', state = DISABLED, command = TheFunction, height = 3 )
TheButton.pack(pady=2, fill = 'y', padx = 10)
#nb.setnaturalsize() # Resize automatically the window ORIGINAL
makemenu(root)
if '-s' in opts:
    LoadLogWindow(logname = opts['-s'])
#root.geometry("800x600")


# CLI options should go here

#test = MultiListbox(p6, (("Name", 20), ("atypes",15), ('file', 99) ), hull_height = 100, hull_width = 600)
#test.pack()

#root.wm_iconbitmap('raccoon.ico')
#root.iconbitmap('./raccoon.ico')
root.mainloop()

if DEBUG: print "KTHXBY"
