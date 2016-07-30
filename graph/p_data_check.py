import cPickle as pickle
import uniout

g = pickle.load( open( "graph.p", "rb" ) )
P_data = pickle.load( open( "page_rank_all.p", "rb" ) )

print P_data.key_type()
print P_data.value_type()

runner = 0
page_rank_info = dict()
print "Converting into dict"
for v in g.vertices():
	page_rank_info[g.vertex_index[v]] = [g.vp.name[v], P_data[v]]
	'''print(v)
	print g.vp.name[v]
	print P_data[v]
	runner += 1
	if runner > 20:
		break'''
print "fishined converting"

sorted_list = sorted(page_rank_info.items(), key=lambda x: x[1][1],reverse=True)

print type(sorted_list)
print sorted_list[:100]

pickle.dump( sorted_list, open( "page_rank_dict.p", "wb" ) )