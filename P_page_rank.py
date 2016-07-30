#get data from database
import uniout
import cPickle as pickle
import sys
P_data_old = pickle.load( open( "p_data/TITLE_TAGS.p", "rb" ) )

#P_data = P_data_old
P_data = P_data_old[:5000]
P_data += P_data_old[2000:8000]
P_data += P_data_old[55000:]

print "Total data len : %s" % len(P_data)
print P_data[:3]

#
###

import networkx as nx
G = nx.MultiGraph()

print "Creating Edges of Nodes"
runner = 0.00
edge = 0
for image in P_data:
	title = image[0]
	tags = image[1]
	#connect all tags to title
	for tag in tags:
		edge += 1
		G.add_edge(title,tag,weight=10)
	#connect all tags to each other only one time
	#for tag in tags:
	#	for tag2 in tags:
	#		edge += 1
	#		G.add_edge(tag,tag2,weight=5)
	#status
	sys.stdout.write('\r')
		# the exact output you're looking for:
	runner += 1
	i = int(float(float(runner) / float(len(P_data)))*20)
	sys.stdout.write("[%-20s] %d%%" % ('='*i, 5*i))
	sys.stdout.flush()
print "\r\nCompleted generated"
print "Total Edge: %s " % edge
#sys.exit()
#G.add_edge(1,2,weight=7)
#G.add_edge(1,2,weight=10)
#G.add_edge(2,3,weight=9)
#G.add_edge(3,3,weight=0)

# make new graph with sum of weights on each edge
H = nx.Graph()
for u,v,d in G.edges(data=True):
    w = d['weight']
    if H.has_edge(u,v):
        H[u][v]['weight'] += w
    else:
        H.add_edge(u,v,weight=w)

#print H.edges(data=True)
#[(1, 2, {'weight': 17}), (2, 3, {'weight': 9})]
print "Calcaulating page rank"
page_rank = nx.pagerank_numpy(H,alpha=0.85)
pickle.dump( page_rank, open( "page_rank_2.p", "wb" ) )
#{1: 0.32037465332634, 2: 0.4864858243244209, 3: 0.1931395223492388}



