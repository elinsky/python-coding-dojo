import collections
import copy
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

WHITE, BLACK = range(2)

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))


def search_maze(maze: List[List[int]], s: Coordinate,
                e: Coordinate) -> List[Coordinate]:
    # so model the maze as a graph
    # then do a search. maybe DFS or BFS.
    # not sure if it matters which
    # how do you model the problem as a maze tho?
    # and i forget the logic for DFS vs BFS
    # you could build a tree, but that would take up a lot of space
    # also, the tree would have loops. so i guess its more of a graph than a tree
    # oh yeah, so i need to keep track of where we've been, so i need a hashmap maybe?
    visited = set()
    path = []

    def is_valid(coord: Coordinate) -> bool:
        if not (0 <= coord.x < len(maze)):  # if x not in bounds
            return False
        if not (0 <= coord.y < len(maze[0])): # if y not in bounds
            return False
        if maze[coord.x][coord.y] == BLACK:
            return False
        return True


    def helper(current: Coordinate):
        visited.add(current)
        path.append(current)
        if current == e:
            return True
        up = Coordinate(current.x, current.y + 1)
        down = Coordinate(current.x, current.y - 1)
        left = Coordinate(current.x - 1, current.y)
        right = Coordinate(current.x + 1, current.y)

        for neighbor in [up, down, left, right]:
            if is_valid(neighbor) and neighbor not in visited:
                if helper(neighbor):
                    return True
        path.pop()
        return False

    helper(s)
    return path


def path_element_is_feasible(maze, prev, cur):
    if not ((0 <= cur.x < len(maze)) and
            (0 <= cur.y < len(maze[cur.x])) and maze[cur.x][cur.y] == WHITE):
        return False
    return cur == (prev.x + 1, prev.y) or \
           cur == (prev.x - 1, prev.y) or \
           cur == (prev.x, prev.y + 1) or \
           cur == (prev.x, prev.y - 1)


@enable_executor_hook
def search_maze_wrapper(executor, maze, s, e):
    s = Coordinate(*s)
    e = Coordinate(*e)
    cp = copy.deepcopy(maze)

    path = executor.run(functools.partial(search_maze, cp, s, e))

    if not path:
        return s == e

    if path[0] != s or path[-1] != e:
        raise TestFailure('Path doesn\'t lay between start and end points')

    for i in range(1, len(path)):
        if not path_element_is_feasible(maze, path[i - 1], path[i]):
            raise TestFailure('Path contains invalid segments')

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_maze.py', 'search_maze.tsv',
                                       search_maze_wrapper))
