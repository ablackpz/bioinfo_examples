bioinfo_examples
================

random bioinformatics examples for other users

First example is a script to combine two tab-delimited data files.  Specifically, the first file contains a list of snps, chr/pos/ref/alt/meta, and is the master file.  The second file contains a subset of snps with just the chr/pos.  The script will use the second file info to pull the appropriate records from the master file.

Usage: python restoreMasterRecord.py masterfile.txt subsetfile.txt output.txt
