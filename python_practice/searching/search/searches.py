'''
Common Searching Algorithms for Trees and Graphs
'''

from allowed.algorithms import (
        Searcher,
)
from allowed.nodes import (
        BinaryTreeNode,
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
                [
                    item for item in cur.children
                    if item
                ],
        )

        return cur


class DFS(Searcher):
    '''
    Implement Depth First Search
    '''

    def __next__(
            self,
    ):

        if not self.ordering:
            raise StopIteration("The stack is empty")

        cur = self.ordering.popleft()
        self.ordering.extendleft(
                [
                    item for item in reversed(cur.children)
                    if item
                ],
        )

        return cur


class Preorder(DFS):
    '''
    Implement Preorder Traversal
    '''

    def __init__(
            self,
            start,
    ):
        super().__init__(
                start,
                node_type=BinaryTreeNode,
        )


class Postorder(Searcher):
    '''
    Implement Postorder Traversal
    '''


    def __init__(
            self,
            start,
    ):
        super().__init__(
                start,
                node_type=BinaryTreeNode,
        )

    def __iter__(
            self,
    ):
        self.seen = []

        return super().__iter__()

    def __next__(
            self,
    ):
        raise NotImplementedError(
                'Must be implemented',
        )


class Inorder(Searcher):
    '''
    Implement Inorder Traversal
    '''


    def __init__(
            self,
            start,
    ):
        super().__init__(
                start,
                node_type=BinaryTreeNode,
        )

    def __iter__(
            self,
    ):
        self.seen = []

        return super().__iter__()

    def __next__(
            self,
    ):
        raise NotImplementedError(
                'Must be implemented',
        )


def main():
    print(
            'Breadth First Search:\n',
            SearchSimulator(
                BFS,
            ).order(),
            sep='',
    )

    print(
            'Depth First Search:\n',
            SearchSimulator(
                DFS,
            ).order(),
            sep='',
    )

    print(
            'Preorder Traversal:\n',
            SearchSimulator(
                Preorder,
            ).order(),
            sep='',
    )

    print(
            'Postorder Traversal:\n',
            SearchSimulator(
                Postorder,
            ).order(),
            sep='',
    )

    print(
            'Inorder Traversal:\n',
            SearchSimulator(
                Inorder,
            ).order(),
            sep='',
    )


if __name__ == '__main__':
    main()
