import numpy as np

class Cache:
	def __init__(self, nsets, bsize, assoc, politica):
		self.nsets = nsets
		self.nbize = bsize
		self.assoc = assoc
		self.politica = politica
		self.hits = 0
		self.misses = 0
		self.missesCompulsorios = 0
		self.missesCapacidade = 0
		self.missesConflito = 0
		
		self.cache = np.zeros(shape=(nsets, assoc), dtype=int)

cache = Cache(5, 1, 2, 1)
print(cache.cache)