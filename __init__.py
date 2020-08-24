import sys
sys.path.append("/Users/bolglo/Documents/VSC/python/KOL_Selection_Pack")

import importKOLCSV
import defineInfluencer
import optKOLs
import writeKOLCSV

# TODO LIST
#
# PRIORITY A
# Reach, eng, followers into a single csv
# Implement relevance metric to Program A and to SLSQP
# Stratify into 3 categories
#
# PRIORITY B
# Change response of empty input cell to: if(empty) [if(column=0)[break] else[set=0]]
#
#
# COMMIT-PUSH SEQUENCE
# git add *files to update*
# git commit -m "comment"
# git remote add origin "https://github.com/lorcanob/kol-optimization.git" # THIS PART MAY BE OPTIONAL
# git push -u origin master