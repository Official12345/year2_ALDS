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


def is_euler_graph(G):
    for nodes in G:
        if not len(G[nodes]) % 2 == 0:
            return False
    return True

def get_bridges(G):
    bridges = []
    for u in vertices(G):
        for v in G[u]:
            G[u].remove(v)
            clear(G)
            BFS(G, u)
            if v.distance is INFINITY:
                if (u, v) not in bridges:
                    bridges.append((u, v))

            G[u].append(v)
            G[u] = sorted(G[u])

    return bridges


def get_euler_circuit(G, s):
    if not is_euler_graph(G):
        return

    steps = [s]

    while (G[s]):
        for temp in G[s]:
            k = temp
            if (s, temp) not in get_bridges(G):
                break

        steps.append(k)
        G[s].remove(k)
        G[k].remove(s)
        s = k

    return steps

v = [Vertex(i) for i in range(8)]

G = {	v[0]: [v[1], v[2]],
		v[1]: [v[0], v[3]],
		v[2]: [v[0], v[3]],
		v[3]: [v[1], v[2], v[4], v[6]],
		v[4]: [v[3], v[5], v[6], v[7]],
		v[5]: [v[4], v[6]],
		v[6]: [v[3], v[4], v[5], v[7]],
		v[7]: [v[6], v[4]]
}
print("is Euler graph ", is_euler_graph(G))

G1 = {	v[0]: [v[1], v[2]],
		v[1]: [v[0], v[3],v[4]],
		v[2]: [v[0], v[3]],
		v[3]: [v[1], v[2], v[4], v[6]],
		v[4]: [v[3], v[5], v[6], v[7]],
		v[5]: [v[4], v[6]],
		v[6]: [v[3], v[4], v[5], v[7]],
		v[7]: [v[6], v[4]]
}
print("is not Euler graph ", is_euler_graph(G1))

#5b
G2 = {	v[0]: [v[1], v[2]],
		v[1]: [v[0], v[3]],
		v[2]: [v[0], v[3]],
		v[3]: [v[1], v[2], v[4], v[6]],
		v[4]: [v[3], v[5], v[6], v[7]],
		v[5]: [v[4], v[6]],
		v[6]: [v[3], v[4], v[5], v[7]],
		v[7]: [v[6], v[4]]
}
print("is Euler graph ", get_euler_circuit(G2, v[0]))
