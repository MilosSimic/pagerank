from model import A, B, C
from power import PageRank, AlgebricPageRank
import numpy as np

a = A()
b = B()
c = C()

a.in_links = [b, c]
a.out_links = [b]

b.in_links = [a]
b.out_links = [a, c]

c.in_links = [b]
c.out_links = [a]

nodes = [a, b, c]

pr = PageRank(nodes)
pr.run_pagerank(iters=1)
pr.print_pr()

for n in nodes:
	n.clear()

apr = AlgebricPageRank(np.array(nodes))
apr.pagerank(iters=1)
