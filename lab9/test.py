#  planarity nie chce sie zainstalować :l

import planarity

edgelist = [('a', 'b'), ('a', 'c'), ('a', 'd'), 
 ('a', 'e'), ('b', 'c'),('b', 'd'),
 ('b', 'e'), ('c', 'd'), ('c', 'e'), 
 ('d', 'e')]
print(planarity.is_planar(edgelist))
edgelist.remove(('a','b'))
print(planarity.is_planar(edgelist))
print(planarity.ascii(edgelist))
