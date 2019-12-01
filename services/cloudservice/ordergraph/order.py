import json

import matplotlib.pyplot as plt
import networkx as nx

from main import *


class ProductOptions:
    def __init__(self, product):
        self.product = product

    def to_json(self):
        required_features = dict()
        for f in self.product.required_features:
            required_features[f.name] = list({p.name: p.type} for p in f.properties)
        optional_features = dict()
        for f in self.product.optional_features:
            optional_features[f.name] = list({p.name: p.type} for p in f.properties)
        out = {'required_features': required_features, 'optional_features': optional_features}
        return json.dumps(out)


class Order:

    def __init__(self, product, selected_features):
        self.product = product
        self.selected_features = selected_features
        self.validate_required_features()

    def create_graph(self):
        all_features = self.product.required_features.all() + self.product.optional_features.all()
        graph = nx.DiGraph()
        for f in self.selected_features:
            f = next(x for x in all_features if x.name == f)
            self.add_subtree(graph, f)
        hanging_nodes = self.get_hanging_nodes(graph)
        self.print_graph(graph)
        for n in hanging_nodes:
            self.rebalance_node(graph, n)
        self.print_graph(graph)

    def add_subtree(self, graph, f):
        s = f.implemented_by[0]

        def add_children(root):
            for child in root.requires.all():
                add_children(child)
                graph.add_edge(child.name, root.name)

        add_children(s)

    def rebalance_node(self, graph, node):
        '''
        Rebalances the graph, pivoting the nodes without successor to their connected neighbour
        '''
        neighbours = graph.predecessors(node)
        # Find a node that is connected with the root
        for n in neighbours:
            if nx.has_path(graph, n, self.get_root_node()):
                break
        else:
            raise Exception("Pivot node not found for {}".format(node))
        # Pivot with connected node
        for successor in graph.successors(n):
            if nx.has_path(graph, successor, self.get_root_node()):
                break
        else:
            raise Exception("Pivot node not found for {}".format(node))
        graph.remove_edge(n, successor)
        graph.add_edge(n, node)
        graph.add_edge(node, successor)

    def validate_required_features(self):
        '''
        All required features must be present in order
        '''
        for f in self.product.required_features:
            if f.name not in self.selected_features:
                raise Exception('{} is a required feature'.format(f.name))

    def get_hanging_nodes(self, graph):
        '''
        Returns the nodes without successors and are not the root
        '''
        final_subassembly = self.get_root_node()
        return [x for x in nx.nodes(graph) if len(list(graph.neighbors(x))) == 0 and x != final_subassembly]

    def get_root_node(self):
        '''
        finds the root node
        :return: the root node
        '''
        return self.product.produced_by[0].name

    def print_graph(self, graph):
        nx.draw_networkx(graph)
        plt.draw()
        plt.show()


if __name__ == '__main__':
    # reset_db()
    # load_db('cell.yml')
    p = Product.nodes.get(name='cellphone')
    p = ProductOptions(p)
    print(p.to_json())
    order = Order(Product.nodes.get(name='cellphone'),
                  ['processor', 'display', 'microphone', 'speaker', 'battery', 'backcase', 'camera'])
    order.create_graph()
