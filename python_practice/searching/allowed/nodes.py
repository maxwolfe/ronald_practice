'''
Definitions for Node Object
'''

from collections import (
        deque,
        Iterable,
)


class Node:
    '''
    A Basic Node
    '''

    def __init__(
            self,
            value,
            type=None,
    ):
        '''
        Initialize a basic Node

        :param value: A nodes data
        :param type: The optional type of the data
        '''

        if type and not isinstance(
                value,
                type,
        ):
            raise TypeError(
                    '{value} is not of type {type}'.format(
                        value=value,
                        type=type,
                    ),
            )

        self.value = value

    def __repr__(
            self,
    ):
        return '{name} has value {value}'.format(
                name=self.__class__.__name__,
                value=self.value,
        )


class TreeNode(Node):
    '''
    A Node of a Tree
    '''

    def __init__(
            self,
            value,
            children=None,
            type=None,
    ):
        '''
        Initialize a tree Node

        :param children: A list of child nodes
        '''

        super().__init__(
                value,
                type,
        )

        if not children:
            children = deque()

        if not isinstance(
                children,
                Iterable,
        ):
            raise TypeError(
                    'Children must be a list of items',
            )

        if not all(
                map(
                    lambda x: isinstance(
                        x,
                        TreeNode,
                    ),
                    children,
                ),
        ):
            raise TypeError(
                    'All children of a Tree Node must also be Tree Nodes',
            )

        self.children = deque()
        self.children.extend(
                children,
        )

    def __repr__(
            self,
    ):
        return super().__repr__() +\
                ' has {number} children'.format(
                        number=len(self.children),
                )


class BinaryTreeNode(TreeNode):
    '''
    A Binary Tree Node
    '''

    def __init__(
            self,
            value,
            children=None,
            type=None,
    ):
        '''
        Initialize a binary tree node
        '''

        super().__init__(
                value,
                children,
                type,
        )

        while len(
                self.children,
        ) < 2:
            self.children.append(
                    None,
            )

        if len(
                self.children,
        ) > 2:
            raise TypeError(
                    'Binary Tree may only have 2 children',
            )

    @property
    def left(
            self,
    ):
        return self.children[0]

    @left.setter
    def left(
            self,
            value,
    ):
        self.children[0] = value

    @property
    def right(
            self,
    ):
        return self.children[-1]

    @right.setter
    def right(
            self,
            value,
    ):
        self.children[-1] = value
