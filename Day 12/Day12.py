import networkx

fname = "day12.txt"

with open(fname) as f:
    content = [x.strip("\n").split(" <-> ") for x in f.readlines()]

g = networkx.Graph()

for line in content:
    programs = line[1].split(", ")
    g.add_edges_from((line[0], p) for p in programs)

print(len(networkx.node_connected_component(g, "0")))
print(networkx.number_connected_components(g))
