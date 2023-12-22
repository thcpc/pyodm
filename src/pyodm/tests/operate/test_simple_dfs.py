import pytest

from pyodm.utils.search.dfs import DFS
from pyodm.tests.operate.node import Node


class SimpleDfs(DFS):

    def __init__(self, data, cached=False):
        super().__init__(data, cached)

    def pruning_strategy(self, node) -> bool:
        return True

    def neighbor_node(self, node) -> list:
        return node.children


@pytest.fixture
def data_tree():
    # level2
    node_1_1 = Node("node_1_child")
    node_1_1.attributes = {"node_1": "1-1"}
    node_1_2 = Node("node_1_child")
    node_1_2.attributes = {"node_1": "1-2"}

    node_2_1 = Node("node_2_child")
    node_2_1.attributes = {"node_2": "2-1"}
    node_2_2 = Node("node_1_child")
    node_2_2.attributes = {"node_2": "2-2"}

    # leve1
    node_1 = Node("root_child")
    node_1.attributes = {"root_1": "1"}
    node_1.children.append(node_1_1)
    node_1.children.append(node_1_2)

    node_2 = Node("root_child")
    node_2.attributes = {"root_2": "2"}
    node_2.children.append(node_2_1)
    node_2.children.append(node_2_2)

    # root
    root = Node("root")
    root.children.append(node_1)
    root.children.append(node_2)

    # level 3
    node_3 = Node("node_1_1_1")
    node_3.attributes["node_1_1_child"] = "1-1-1"
    return root


def test_dfs(data_tree):
    dfs = SimpleDfs(data_tree)
    node = dfs.find(_lambda=lambda x: x.name == "node_1_child" and x.attributes.get("node_1") == "1-1")
    assert node.name == "node_1_child"
    assert node.attributes.get("node_1") == "1-1"
    assert len(dfs._stack) == 0


def test_cached_dfs(data_tree):
    dfs = SimpleDfs(data_tree, cached=True)
    node = dfs.find(_lambda=lambda x: x.name == "node_1_child" and x.attributes.get("node_1") == "1-1")
    assert node.name == "node_1_child"
    assert node.attributes.get("node_1") == "1-1"
    assert len(dfs._stack) == 7
    node.name = "xxxx"
    # 因为增加了缓存，所以读取数据是从缓存栈读取，所以读取出来还是之前的值
    node = dfs.find(_lambda=lambda x: x.name == "node_1_child" and x.attributes.get("node_1") == "1-1")
    assert node.name == "node_1_child"
    assert node.attributes.get("node_1") == "1-1"
    assert len(dfs._stack) == 7

