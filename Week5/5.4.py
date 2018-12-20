class myqueue(list):
    def __init__(self, a=[]):
        list.__init__(self, a)

    def dequeue(self):
        return self.pop(0)

    def enqueue(self, x):
        self.append(x)


class Vertex:
    def __init__(self, data):
        self.data = data

    def __repr__(self):  # voor afdrukken
        return str(self.data)

    def __lt__(self, other):  # voor sorteren
        return self.data < other.data


import math

INFINITY = math.inf  # float("inf")


def vertices(G):
    return sorted(G)


def edges(G):
    return [(u, v) for u in vertices(G) for v in G[u]]


def BFS(G, s):
    V = vertices(G)
    s.predecessor = None
    s.distance = 0
    for v in V:
        if v != s:
            v.distance = INFINITY  # v krijgt het attribuut 'distance'
    q = myqueue()
    q.enqueue(s)
    while q:
        u = q.dequeue()
        for v in G[u]:
            if v.distance == INFINITY:  # v is nog niet bezocht
                v.distance = u.distance + 1
                v.predecessor = u  # v krijgt het attribuut 'predecessor'
                q.enqueue(v)


def clear(G):
    for v in vertices(G):
        k = [e for e in vars(v) if e != 'data']
        for e in k:
            delattr(v, e)

def is_connected(G, s):
    V = vertices(G)
    s.predecessor = None
    s.distance = 0
    for v in V:
        if v != s:
            v.distance = INFINITY

    q = myqueue()
    q.enqueue(s)

    found = set()

    while q:
        u = q.dequeue()
        found.add(u)
        for v in G[u]:
            if v.distance == INFINITY:
                v.distance = u.distance + 1
                v.predecessor = u
                q.enqueue(v)

    return len(found) == len(G)


def invert_graph(G):
    H = {}
    for u, v in edges(G):
        if v in H:
            H[v].append(u)
        else:
            H[v] = []
            H[v].append(u)
    return H


def strongly_connected(G):
    for node in G:
        if not is_connected(G, node):
            return False

    for node in invert_graph(G):
        if not is_connected(G, node):
            return False
    return True


v = [Vertex(i) for i in range(3)]

strongly_G = {  v[0]: [v[1]],
                v[1]: [v[2]],
                v[2]: [v[0]]}

non_strong_G = {v[0]: [v[1]],
                v[2]: [v[0], v[1]]}

print(strongly_connected(strongly_G))
print(strongly_connected(non_strong_G))


