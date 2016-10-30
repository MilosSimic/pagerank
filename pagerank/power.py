import numpy as np

class PageRank(object):
	def __init__(self, pages=None):
		self.pages = pages
	
	def update_pr(self):
		for page in self.pages:
			page.update()
	
	def calculate_pr(self):
		for page in self.pages:
			page.calculate_pr()
	
	def run_pagerank(self, iters=1):
		for i in range(iters):
			self.calculate_pr()
			self.update_pr()
			
			
	def print_pr(self):
		for page in self.pages:
			print (page.__class__.__name__, page.pr)
		
class AlgebricPageRank(object):
	def __init__(self, nodes=None):
		self.no_of_nodes = len(nodes)
		self.w = np.ones([self.no_of_nodes , 1])
		self.init_matrix(nodes)

	def init_matrix(self, nodes):
		self.M = np.zeros((nodes.size, nodes.size))
		for idx, inode in enumerate(nodes):
			for jdx, jnode in enumerate(nodes):
				if jnode in inode.in_links:
					self.M[idx, jdx] = jnode.pr/len(jnode.out_links)

	#PR(Ta) = (1-d) + d*(PR(Tb)/C(Tb)+PR(Tc)/C(Tc)+...+PR(Tn)/C(Tn))
	def pagerank(self, d=0.85, N=1, iters=1):
		for it in range(iters):
			rp = np.repeat((1-d)/N, self.no_of_nodes)[np.newaxis].T
			self.w = np.add(rp, d * self.M.dot(self.w))

		print self.w

	def print_stats(self):
		print "Matrix:\n", self.M
		print "First part:\n", self.rp
		print "Rank:\n", self.w
		print "Dumping factor {} number of elems {}".format(self.d, self.N)
