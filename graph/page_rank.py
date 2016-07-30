from graph_tool.all import *
import graph_tool as gt
import matplotlib
import uniout
import cPickle as pickle
import sys

#g = gt.collection.data["polblogs"]
#g = gt.GraphView(g, vfilt=gt.topology.label_largest_component(g))
#pr = gt.centrality.pagerank(g)
'''gt.draw.graph_draw(g, pos=g.vp["pos"], vertex_fill_color=pr,
	vertex_size=gt.draw.prop_to_size(pr, mi=5, ma=15),
	vorder=pr, vcmap=matplotlib.cm.gist_heat,
	output="polblogs_pr.pdf")'''


P_data_old = pickle.load( open( "../p_data/TITLE_TAGS.p", "rb" ) )
print "TOtal data loaded : %s" % len(P_data_old)
P_data = P_data_old
P_data = P_data_old[57000:]

g = Graph(directed=False)
#v1 = g.add_vertex()
#v2 = g.add_vertex()
#e = g.add_edge(v1, v2)

print "Creating Edges of Nodes"
runner = 0.00
edge = 0
vertex = -1
vprop_string = g.new_vertex_property("string")
g.vp.name = vprop_string
visited_tag = dict()

for image in P_data:
	title = image[0]
	tags = image[1]
	#connect all tags to title
	v_title = g.add_vertex()
	vertex += 1
	g.vp.name[v_title] = title
	#g.vertex_properties[title] = g.new_vertex_property("int")
	#g.vertex_properties[title] = 123
	for tag in tags:
		edge += 1
		if not (tag in visited_tag):
			v_tag = g.add_vertex()
			visited_tag[tag] = v_tag
		else:
			v_tag = visited_tag[tag]
		vertex += 1
		g.vp.name[v_tag] = tag
		#g.vertex_properties[tag] = vprop_string
		#g.vertex_properties[tag] = tag
		#g.add_vertex()
		g.add_edge(v_title,v_tag)
		
		#vprop_string[v_title] = title
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
print "Total Edges: %s " % edge
print "Total Vertexs: %s " % vertex

print g.list_properties()
print g.vp.name

#sys.exit()

print "Drawing graph"
#g.vp.name
pos = gt.draw.sfdp_layout(g)

#pos = gt.draw.random_layout(g,dim=4)
#pos = gt.draw.fruchterman_reingold_layout(g,n_iter=1000)
#graph_draw(g, pos=pos,vertex_text=g.vertex_index, vertex_font_size=8,output_size=(6000, 6000), output="two-nodes.pdf",bg_color=[1,1,1,1])
#graph_draw(g, pos=pos, output="two-nodes.pdf",bg_color=[1,1,1,1])

###hierarchy
state = minimize_nested_blockmodel_dl(g, deg_corr=True)
draw_hierarchy(state, output="celegansneural_nested_mdl.png",output_size=(6000,6000),bg_color=[1,1,1,1])

print "Done with graph"

'''print "Calculating Page Rank"
pr = gt.centrality.pagerank(g)
print "Done with Page Rank"
graph_draw(g, pos=pos, vertex_fill_color=pr,
	vertex_size=prop_to_size(pr, mi=5, ma=15),
	vorder=pr, vcmap=matplotlib.cm.gist_heat,output_size=(6000,6000),bg_color=[1,1,1,1],
	output="polblogs_pr.png")'''

#pickle.dump( pr, open( "page_rank_all.p", "wb" ) )
#pickle.dump( g, open( "graph.p", "wb" ) )