from pyodm.utils.search.odm_dfs import ODMDfs



if __name__ == '__main__':
    dfs = ODMDfs(root)
    node = dfs.find(_lambda=lambda x: x.name == "node_1_child" and x.attributes.get("node_1") == "1-1")
    node.children.append(node_3)
    print(root)
