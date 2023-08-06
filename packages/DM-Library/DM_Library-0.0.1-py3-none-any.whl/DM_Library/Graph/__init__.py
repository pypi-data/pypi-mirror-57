class Graph:
    def __init__(self, graph_dict=None):
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict


    """To look for the change in dictonary Graph"""
    def getGraphDict(self):
        return self.__graph_dict

    """ returns the vertices of a graph """
    def get_nodes(self):
        return list(self.__graph_dict.keys())



    """ returns the edges of a graph """
    def get_links(self):
        return self.__generate_links()

    """ A static method generating the links of the 
       graph "graph". links are represented as sets 
       with one (a loop back to the node) or two nodes
       """

    def __generate_links(self):
        links = []
        for node in self.__graph_dict:
            for neighbour in self.__graph_dict[node]:
                if {node, neighbour} not in links:
                    links.append({node, neighbour})
        return links


    """returns a dictonary of a node and it's adjacent node if any exist"""
    def get_all_adjacencies(self):
        graph_dict = {}
        for node in self.__graph_dict:
            if len(self.__graph_dict[node]) == 0 or  (len(self.__graph_dict[node]) == 1 and (node in self.__graph_dict[node])):
                continue
            graph_dict.update({node : self.__graph_dict[node]})
        return  graph_dict


    """ Takes a node and return the list of adjacent node 
        to that node"""
    def get_node_adjacencies(self, node = None):
        if node is None:
            return []
        for node_itr in self.__graph_dict:
            if node == node_itr:
                return self.__graph_dict[node]



    def get_spanning_tree(self):
        edge_list = []
        node_list = []
        for (link0, link1) in self.get_links():
            if not ((link0 in node_list) and (link1 in node_list)):
                node_list.append(link0)
                node_list.append(link1)
                edge_list.append({link0, link1})
        return edge_list



    """ If the node "node" is not in 
    self.__graph_dict, a key "node" with an empty
    list as a value is added to the dictionary. 
    Otherwise nothing has to be done. 
    """
    def add_node(self, node):
        if node not in self.__graph_dict:
            self.__graph_dict[node] = []



    """ assumes that link is of type set, tuple or list; 
       between two vertices can be multiple links! 
    """
    def add_link(self, link):
        # link = set(link)
        # print(link)
        (node1, node2) = tuple(link)
        # print(node1, node2)
        if node1 in self.__graph_dict:
            if not node2 in self.__graph_dict[node1]:
                self.__graph_dict[node1].append(node2)
        else:
            self.__graph_dict[node1] = [node2]




    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nlinks: "
        for link in self.__generate_links():
            res += str(link) + " "
        return res



    """ find a path from start_node to end_node 
    in graph """
    def find_path(self, start_node, end_node, path=None):
        if path == None:
            path = []
        graph = self.__graph_dict
        path = path + [start_node]
        if start_node == end_node:
            return path
        if start_node not in graph:
            return None
        for node in graph[start_node]:
            if node not in path:
                extended_path = self.find_path(node,
                                               end_node,
                                               path)
                if extended_path:
                    return extended_path
        return None



    """ find all paths from start_node to
    end_node in graph """
    def find_all_paths(self, start_node, end_node, path=[]):
        graph = self.__graph_dict
        path = path + [start_node]
        if start_node == end_node:
            return [path]
        if start_node not in graph:
            return []
        paths = []
        for node in graph[start_node]:
            if node not in path:
                extended_paths = self.find_all_paths(node,
                                                     end_node,
                                                     path)
                for p in extended_paths:
                    paths.append(p)
        return paths



