import fileinput
import os
import logging
logging.basicConfig(level=logging.DEBUG)

class UF:
    def __init__(self, N):
        self.N = N
        self.id = list(range(0, N))
    
    def union(self, p:int, q:int) -> None:
        id = self.id
        pid:int = id[p]
        qid:int = id[q]
        for i, x in enumerate(self.id):
            if id[i] == pid:
                self.id[i] = qid

        return None
    
    def connected(self, p:int, q:int) -> bool:
        return self.id[p] == self.id[q]
    
    def find(self, p:int) -> int:
        return 0

    def count(self) -> int:
        return 0

def main():
    file_input_iter = fileinput.input(os.path.join('algorithms','tinyUF.txt'))
    N: int = int(file_input_iter[0])
    logging.info(f'N is : {N}')
    uf = UF(N)
    logging.info(f'Initial array is: {uf.id}')
    for item in file_input_iter:
        p, q = item.split()
        p = int(p)
        q = int(q)
        if not uf.connected(p,q):
            uf.union(p,q)
            #print(p," ",q)
    logging.info(f'final array is: {uf.id}')


if __name__ == '__main__':
    main()

