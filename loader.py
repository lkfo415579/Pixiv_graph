import uniout
import operator
import cPickle as pickle

page_rank = pickle.load( open( "page_rank.p", "rb" ) )

from collections import OrderedDict
name_order = OrderedDict(sorted(page_rank.items(), key=lambda x: x[1],reverse=True))
#name_order = sorted(page_rank.values())
name_order = list(name_order)
print type(page_rank)
runner = 0
for name in name_order:
	runner += 1
	print name
	print page_rank[name]
	if runner > 40 :
		break
	
print len(page_rank)
	#print page_rank[runner]