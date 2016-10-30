class Node(object):
	def __init__(self, in_links=None, out_links=None, pr=1.0):
		self.in_links = in_links
		self.out_links = out_links
		self.pr = pr
		self.n_pr = pr
		
	#PR(Ta) = (1-d) + d*(PR(Tb)/C(Tb)+PR(Tc)/C(Tc)+...+PR(Tn)/C(Tn))
	def calculate_pr(self, d=0.85):
		val = 0
		
		for link in self.in_links:
			val += link.pr/float(len(link.out_links))
			
		self.n_pr = (1-d) + d*(val)
		
	def update(self):
		self.pr = self.n_pr

	def clear(self):
		self.pr = 1.0
		self.n_pr = 1.0
		
class A(Node):
	def __init__(self, in_links=None, out_links=None, pr=1.0):
		Node.__init__(self, in_links, out_links, pr)
	
class B(Node):
	def __init__(self, in_links=None, out_links=None, pr=1.0):
		Node.__init__(self, in_links, out_links, pr)
	
class C(Node):
	def __init__(self, in_links=None, out_links=None, pr=1.0):
		Node.__init__(self, in_links, out_links, pr)
