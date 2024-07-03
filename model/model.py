import networkx as nx


from database.DAO import DAO
class Model:
    def __init__(self):
        self._listaNazioni=[]
        self._grafo=nx.Graph()
        self._dizionarioNodi={}
        self._bestSol=[]
        self._pesoMax=0
        pass
    def get_Nations(self):
        self._listaNazioni=[]
        for element in DAO.get_Nations():
            self._listaNazioni.append(element)
        return self._listaNazioni
    def creaGrafo(self,nazione, anno):
        self._grafo.clear()
        self._dizionarioNodi={}
        for element in DAO.getNodi(nazione):
            self._grafo.add_node(element)
            self._dizionarioNodi[element.code]=element
        for element in DAO.getArchi(nazione,anno):
            self._grafo.add_edge(self._dizionarioNodi[element[0]],self._dizionarioNodi[element[1]],weight=element[2])
    def numNodi(self):
        return len(self._grafo.nodes())
    def numArchi(self):
        return len(self._grafo.edges())
    def Volume(self):
        dizionario={}
        for nodo1 in self._grafo.nodes():
            peso=0
            for nodo2 in self._grafo.neighbors(nodo1):
                peso+=self._grafo[nodo1][nodo2]['weight']
            dizionario[nodo1]=peso
        dizionario_ordinato=dict(sorted(dizionario.items(), key=lambda item: item[1], reverse=True))
        return dizionario_ordinato
    def _ricorsione(self,parziale,nodo,pesoattuale,distanza,nodofinale):
        successori=list(self._grafo.neighbors(nodo))
        if len(parziale)==distanza:
            for element in successori.copy():
                if element!=nodofinale:
                    successori.remove(element)
        else:
            for element in successori.copy():
                if element in parziale:
                    successori.remove(element)
        if len(parziale)==distanza+1:
            print("r")
            if pesoattuale>self._pesoMax:
                self._pesoMax=pesoattuale
                self._bestSol=parziale
        elif len(successori)==0:
            return
        else:
            for item in successori:
                nuovo_nodo = item
                parziale_nuovo = list(parziale)
                parziale_nuovo.append(nuovo_nodo)
                pesoattuale_nuovo=pesoattuale+self._grafo[nodo][nuovo_nodo]['weight']
                self._ricorsione(parziale_nuovo,nuovo_nodo,pesoattuale_nuovo,distanza,nodofinale)
    def handle_ricorsione(self,distanza):
        self._pesoMax=0
        for nodo in self._grafo.nodes():
            self._ricorsione([nodo],nodo,0,distanza,nodo)
        lista=[]
        for i in range(len(self._bestSol)-1):
            lista.append(
                f"{self._bestSol[i].name}-->{self._bestSol[i+1].name}: {self._grafo[self._bestSol[i]][self._bestSol[i+1]]["weight"]}")
        return lista


