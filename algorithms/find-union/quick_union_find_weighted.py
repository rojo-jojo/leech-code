'''
0 1 2 3 4 5
0 2 2 4 5 5
'''

import fileinput
import os
import logging
logging.basicConfig(level=logging.DEBUG)
import time

class QuickUnionFind:
    def __init__(self, N):
        self.N = N
        self.id = list(range(0, N))
        self.sz = list(range(0, N))
    
    def _root(self, i: int) -> int:
        while i != self.id[i]:
            i = self.id[i]
        return i
    
    def union(self, p:int, q:int) -> None:
        i: int = self._root(p)
        j: int = self._root(q)
        if i == j: return # if both have same root, do nothing
        if self.sz[i] < self.sz[j]:
            self.id[i] = j
            self.sz[j] += self.sz[i]
        else:
            self.id[j] = i
            self.sz[i] += self.sz[j]

    def connected(self, p:int, q:int) -> bool:
        return self._root(p) == self._root(q)
    
    def find(self, p:int) -> int:
        return 0

    def count(self) -> int:
        return 0

def main():
    file_input_iter = fileinput.input(os.path.join('algorithms','tinyUF.txt'))
    N: int = int(file_input_iter[0])
    logging.info(f'N is : {N}')
    file_input_iter = list(file_input_iter)
    logging.info(f'type of input iter: {file_input_iter[1]}')
    uf = QuickUnionFind(N)
    logging.info(f'(0,0), array: {uf.id}')
    start = time.time()
    for item in file_input_iter[0:]:
        p, q = item.split()
        p = int(p)
        q = int(q)
        if not uf.connected(p,q):
            uf.union(p,q)
        logging.info(f'({p},{q}), array: {uf.id}')
    logging.info(f'Algo time: {time.time()-start}')
    


if __name__ == '__main__':
    main()

