from functools import TopologicalSorter

graph = {"A": {"D"}, "B": {"D"}, "C": {"E", "H"}, "D": {"F", "G", "H"}, "E": {"G"}}
ts = TopologicalSorter(graph)

print(list(ts.static_order()))