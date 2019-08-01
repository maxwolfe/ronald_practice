'''
Common Searching Algorithms for Trees and Graphs
'''

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
        if not self.ordering:
            raise StopIteration("The queue is empty")

        cur = self.ordering.popleft()
        self.ordering.extend(
                        cur.children
        )

        return cur


class DFS(Searcher):
    '''
    Implement Depth First Search
    '''

    def __next__(
            self
    ):

        if not self.ordering:
            raise StopIteration("The stack is empty")

        cur = self.ordering.popleft()
        self.ordering.extendleft(
                        reversed(cur.children)
        )

        return cur


def main():
    print(
            'Breadth First Search:\n',
            SearchSimulator(
                BFS,
            ).order(),
    )

    print(
            'Depth First Search:\n',
            SearchSimulator(
                DFS,
            ).order(),
    )


if __name__ == '__main__':
    main()
