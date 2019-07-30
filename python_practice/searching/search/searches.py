'''
Common Searching Algorithms for Trees and Graphs
'''

from collections import (
        deque,
)

from allowed.algorithms import (
        Searcher,
)
from allowed.printers import (
        SearchSimulator,
)


class BFS(Searcher):
    '''
    Implement Breadth First Search
    '''

    def __next__(
            self,
    ):
        if len(
                self.ordering,
        ):
            cur = self.ordering.popleft()
            self.ordering.extend(
                    cur.children,
            )

            return cur


class DFS(Searcher):
    '''
    Implement Depth First Search
    '''

    pass


def main():
    print (
            'Breadth First Search:\n',
            SearchSimulator(
                BFS,
            ),
    )
    print (
            'Depth First Search:\n',
            SearchSimulator(
                DFS,
            ),
    )

    
if __name__ == '__main__':
    main()
