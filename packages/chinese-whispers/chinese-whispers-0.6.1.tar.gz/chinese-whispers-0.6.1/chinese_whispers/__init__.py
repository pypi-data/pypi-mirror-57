import random
from collections import Counter
from math import log2
from operator import itemgetter

__version__ = '0.6.1'


def top_weighting(G, node, neighbor):
    """ A weight is the edge weight. """
    return G[node][neighbor].get('weight', 1.)


def nolog_weighting(G, node, neighbor):
    """ A weight is the edge weight divided to the node degree. """
    return G[node][neighbor].get('weight', 1.) / G.degree(neighbor)


def log_weighting(G, node, neighbor):
    """ A weight is the edge weight divided to the log2 of node degree. """
    return G[node][neighbor].get('weight', 1.) / log2(G.degree(neighbor) + 1)


WEIGHTING = {
    'top': top_weighting,
    'nolog': nolog_weighting,
    'log': log_weighting
}


def chinese_whispers(G, weighting='top', iterations=20, seed=None):
    """ Performs clustering of nodes in a NetworkX graph G
    using the 'weighting' method. Three weighing schemas are available: 
    'top' relies on the original weights; 'nolog' normalizes an edge weight 
    by the degree of the related node; 'log' normalizes an edge weight by the 
    logarithm of the output degree. It is possible to specify the maximum number
    of iterations as well as the random seed to use. """

    weighting_func = WEIGHTING[weighting] if isinstance(weighting, str) else weighting

    rng = random.Random(seed) if seed else random
    shuffle_func = rng.shuffle
    choice_func = rng.choice

    for i, node in enumerate(G):
        G.nodes[node]['label'] = i + 1

    nodes = list(G)

    for i in range(iterations):
        changes = False

        shuffle_func(nodes)

        for node in nodes:
            previous = G.nodes[node]['label']

            if G[node]:
                scores = score(G, node, weighting_func)
                G.nodes[node]['label'] = random_argmax(scores.items(), choice_func=choice_func)

            changes = changes or previous != G.nodes[node]['label']

        if not changes:
            break

    return G


def score(G, node, weighting_func):
    """ Computes label scores in the given node neighborhood. """

    scores = Counter()

    if node not in G:
        return scores

    for neighbor in G[node]:
        scores[G.nodes[neighbor]['label']] += weighting_func(G, node, neighbor)

    return scores


def random_argmax(items, choice_func=random.choice):
    """An argmax function that breaks the ties randomly."""
    if not items:
        return

    _, maximum = max(items, key=itemgetter(1))

    keys = [k for k, v in items if v == maximum]

    return choice_func(keys)


def aggregate_clusters(G):
    """ Takes as input the labeled graph and outputs a dictionary with the keys
    being cluster IDs and the values being sets of cluster elements. """

    clusters = {}

    for node in G:
        label = G.nodes[node]['label']

        if label not in clusters:
            clusters[label] = {node}
        else:
            clusters[label].add(node)

    return clusters
