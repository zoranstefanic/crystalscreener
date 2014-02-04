#!/usr/bin/env python
# Format to write to the sql database
#Num	ScreenName	Well	Buffer	Salt1	Salt2	Salt3	Salt4	Prec1	Prec2	Prec3	Ph
#
#	AnionsSuite		wln = num +TAB+ name +TAB+ list[2] +TAB+ list[3] +5*TAB+ list[4] +TAB+ list[5] +2*TAB+ '\n' 
#	AmSO4Suite		wln = num +TAB+ name +TAB+ list[2] +TAB+ list[4] +TAB+ list[3] +4*TAB+ list[5] +TAB+ list[6] +2*TAB+ '\n' 
#	pHclearSuite	wln = num +TAB+ name +TAB+ list[1] +TAB+ list[2] +TAB+ list[3] +4*TAB+ list[4] +3*TAB+ list[5] +TAB+ '\n' 
#	CationSuite		wln = num +TAB+ name +TAB+ list[2] +TAB+ list[3] +5*TAB+ list[4] +4*TAB+ '\n' 
#	pHClearIISuite	wln = num +TAB+ name +TAB+ list[2] +TAB+ list[4] +TAB+ list[3] +4*TAB+ list[5] +3*TAB+ list[6] +TAB+ '\n' 
#	PEGsIISuite		wln = num +TAB+ name +TAB+ list[2] +TAB+ list[5] +TAB+ list[3] +TAB+ list[4] +3*TAB+ list[6] +TAB+ list[7] +3*TAB+ '\n' 
#	PEGsSuite		wln = num +TAB+ name +TAB+ list[2] +TAB+ list[4] +TAB+ list[3] +4*TAB+ list[5] +4*TAB+ '\n' 
#	PACTSSuite		wln = num +TAB+ name +TAB+ list[2] +TAB+ list[4] +TAB+ list[3] +4*TAB+ list[5] +4*TAB+ '\n' 
#	JCSG+Suite		wln = num +TAB+ name +TAB+ list[2] +TAB+ list[7] +TAB+ list[3] +TAB+ list[4] +TAB+ list[5] +TAB+ list[6] +TAB+ list[8] +TAB+ list[9] +2*TAB+ '\n' 
#	MPDSuite		wln = num +TAB+ name +TAB+ list[2] +TAB+ list[4] +TAB+ list[3] +4*TAB+ list[5] +TAB+ list[6] +3*TAB+ '\n' 
import sys, os
from string import digits

TAB = '\t'

if not len(sys.argv) == 4:
	print "usage: txt2sql.py file.txt name first_num"
	sys.exit()
else:
	name = sys.argv[2]
	first_num = int(sys.argv[3])
	infile = sys.argv[1]
	outfile = name + '.sql'

input = open(infile,'r')
output = open(outfile,'w')

for line in input.readlines():
	list = line.split('\t')
	if list[0][0] not in digits:
		pass
	else:
		num = str(first_num)
		wln = num +TAB+ name +TAB+ list[1] +TAB+ list[2] +TAB+ list[3] +TAB+ list[4] +TAB+ list[5] +TAB+ list[6] +TAB+ list[7] +TAB+ list[8] +TAB+ list[9] + 2*TAB+ '\n' 
		output.write(wln)
		first_num += 1

input.close()
output.close()
