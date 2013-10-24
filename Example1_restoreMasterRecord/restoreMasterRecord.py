# A script to take a file containing a master file containing all complete records indexed by chr and position and a subset file containing the chr and position of records of interest and output a file containing the master record info for each chr/pos in the subset file.
# Created: A. Black P.
# Date Created: 2013.10.23

# Usage: python restoreMasterRecord.py masterfile.txt subsetfile.txt output.txt

import sys

outfile = open(sys.argv[3],'w')

ids = {}

for newString in open(sys.argv[2]):
#    print newString
    parts = newString.rstrip().split('\t')
    ids[parts[0] + '_' + parts[1]] = ''

for newString in open(sys.argv[1]):
    parts = newString.rstrip().split('\t')
    if ids.has_key(parts[0] + '_' + parts[1]):
        ids[parts[0] + '_' + parts[1]] = newString

for record in sorted(ids):
    outfile.write(ids[record])

outfile.close()

print 'Finished!'
