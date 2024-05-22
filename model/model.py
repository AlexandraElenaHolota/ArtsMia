import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._artObjectList = DAO.getAllObjects()
        self._grafo = nx.Graph()
        self._grafo.add_nodes_from(self._artObjectList)
        self._idMap = {}
        for v in self._artObjectList:
            self._idMap[v.object_id] = v

    def getConnessa(self, v0int):
        v0 = self._idMap[v0int]

        # Modo1: successori di v0 in DFS
        successors = nx.dfs_successors(self._grafo, v0) # dizionario
        allSucc = []
        for v in successors.values():
            allSucc.extend(v)

        print(f"Metodo 1 (succ): {len(allSucc)}")

        # Modo2: predecessori di v0 in DFS
        predecessors = nx.dfs_predecessors(self._grafo, v0)
        print(f"Metodo 2 (pred): {len(predecessors.values())}")

        # Modo3: conto i nodi dell'albero di visita
        tree = nx.dfs_tree(self._grafo, v0)
        print(f"Metodo 3 (tree): {len(tree.nodes)}")

        # Modo4: node_connected_component
        connComp = nx.node_connected_component(self._grafo, v0)
        print(f"Metodo 4 (connComp): {len(connComp)}")

        return len(connComp)



    def creaGrafo(self):
        self.addEdges()

    def addEdges(self):
        # self._grafo.edges.clear()
        #Soluzione1: Ciclare sui nodi SCONSIGLIATA!! UTILE SOLO SE PCOHE CONNESSIONI
            # questa soluzione è più facile, ma più lenta
        # for u in self._artObjectList:
        #    for v in self._artObjectList:
        #       peso = DAO.getPeso(u, v)
        #        self._grafo.add_edge(u, v, peso)

        #Soluzione2: una sola query
        allEdges = DAO.getAllConnessioni(self._idMap)
        for e in allEdges:
            self._grafo.add_edge(e.v1, e.v2, weight=e.peso)

    def checkExistece(self, idOggetto):
        return idOggetto in self._idMap


    def getNumNodes(self):
        return len(self._grafo.nodes)

    def getNumEdges(self):
        return len(self._grafo.edges)