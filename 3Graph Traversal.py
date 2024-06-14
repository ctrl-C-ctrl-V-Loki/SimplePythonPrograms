class Vertex:
    def __init__(self, data):
        self.data = data
        self.nxtVertex = None
        self.AdjHead = None
        self.trvState = None

class AdjNode:
    def __init__(self):
        self.reference = None
        self.nxt = None

class Graph:
    def __init__(self):
        self.root = None
        self.vertexCtr = 0

    def create(self):
        print('Enter the Vertex List:')
        vertexLst = input().split()
        print(vertexLst)
        for i in range(len(vertexLst)):
            new_node = Vertex(vertexLst[i])
            if self.root is None:
                self.root = new_node
            else:
                temp = self.root
                while temp.nxtVertex is not None:
                    temp = temp.nxtVertex
                temp.nxtVertex = new_node
        # Creation of Adjacent List
        temp = self.root
        while temp is not None:
            print('Enter the Adjacency List of Vertex(', temp.data, ')')
            adjLst = input('Enter Here (In Ascending order): ').split()
            for i in range(len(adjLst)):
                refPtr = self.getReference(adjLst[i])
                new_node = AdjNode()
                new_node.reference = refPtr
                if temp.AdjHead is None:
                    temp.AdjHead = new_node
                else:
                    temp1 = temp.AdjHead
                    while temp1.nxt is not None:
                        temp1 = temp1.nxt
                    temp1.nxt = new_node
            temp = temp.nxtVertex

    def getReference(self, nodeData):
        temp = self.root
        while temp is not None:
            if temp.data == nodeData:
                return temp
            temp = temp.nxtVertex

    def LinearSearch(self, Lst, Key):
        for i in range(len(Lst)):
            if Lst[i] == Key:
                return True
        return False

    def DFT(self):
        Path = []
        S = []
        V = self.root
        S.append(V)
        while len(S) != 0:
            V = S.pop()
            if not self.LinearSearch(Path, V.data):
                Path.append(V.data)
                temp = V.AdjHead
                while temp is not None:
                    S.append(temp.reference)
                    temp = temp.nxt
        return Path

    def BFT(self):
        Path = []
        S = []
        V = self.root
        S.append(V)
        while len(S) != 0:
            V = S.pop(0)
            if not self.LinearSearch(Path, V.data):
                Path.append(V.data)
                temp = V.AdjHead
                while temp is not None:
                    S.append(temp.reference)
                    temp = temp.nxt
        return Path

# Driver Code
print("######---Graph---#####")
G = Graph()
G.create()

print('**************Graph Traversals :*************')
print('\t1. Depth First Traversal')
print('\t2. Breadth First Traversal')
while True:
    ch = int(input('Enter Choice: '))
    if ch == 1:
        print(G.DFT())
    elif ch == 2:
        print(G.BFT())
    else:
        print("Exit")
        break
