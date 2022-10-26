import fileinput
import os
import logging
logging.basicConfig(level=logging.DEBUG)

class UF:
    def __init__(self, N):
        self.N = N
        self.graph_arr = list(range(0, N))
    
    def union(self, p:int, q:int) -> None:
        p_idx = self.graph_arr.index(p)
        q_idx = self.graph_arr.index(q)
        if p_idx < q_idx:
            self.graph_arr[q_idx] = p_idx
        else:
            self.graph_arr[p_idx] = q_idx

        return None
    
    def connected(self, p:int, q:int) -> bool:
        return False
    
    def find(self, p:int) -> int:
        return 0

    def count(self) -> int:
        return 0

def main():
    file_input_iter = fileinput.input('algorithms/tinyUF.txt')
    N: int = int(file_input_iter[0])
    logging.info(f'N is : {N}')
    uf = UF(N)
    logging.info(f'Initial array is: {uf.graph_arr}')
    for item in file_input_iter:
        p, q = item.split()
        p = int(p)
        q = int(q)
        if not uf.connected(p,q):
            uf.union(p,q)
            #print(p," ",q)
    logging.info(f'final array is: {uf.graph_arr}')


if __name__ == '__main__':
    main()

