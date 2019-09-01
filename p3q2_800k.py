import sys
import numpy as np
import datetime


class Graph:
    def __init__(self, graph):
        self.nodes = {}
        for link in graph:
            nodeA = link[0]
            nodeB = link[1]

            if not nodeA in self.nodes:
                nodeA = Nodes(nodeA, {}, {}, False, 0, 0, 0)
                self.nodes[nodeA.id] = nodeA
            else:
                nodeA = self.nodes[nodeA]

            if not nodeB in self.nodes:
                nodeB = Nodes(nodeB, {}, {}, False, 0, 0, 0)
                self.nodes[nodeB.id] = nodeB
            else:
                nodeB = self.nodes[nodeB]

            nodeA.outbound[nodeB.id] = nodeB
            nodeA.outDegree = nodeA.outDegree + 1

            nodeB.inbound[nodeA.id] = nodeA
            nodeB.inDegree = nodeB.inDegree + 1

        

class Nodes:
    def __init__(self, id, inbound, outbound, deadEnd, inDegree, outDegree, pageRank):
        self.id = id
        self.inbound = inbound
        self.outbound = outbound
        self.deadEnd = deadEnd
        self.inDegree = inDegree
        self.outDegree = outDegree
        self.pageRank = pageRank

def writeToFile(graphNoDE):
    outputFile = open("PR_800k.tsv", "w")

    pageRankList = {}

    for id, node in graphNoDE.nodes.items():
        pageRankList[id] = node.pageRank

    pageRankList = sorted(pageRankList.items(), key=lambda kv: kv[1], reverse=True)

    outputFile.write("PageRank\tIds\n")
    for pr in pageRankList:
        outputFile.write(str(pr[1]) + "\t" + str(pr[0]) + "\n")
    outputFile.close()

    return

def findDeadEnds(graphNoDE):
    removedDeadEnd = True
    deadEndList = []
    while (1):
        if removedDeadEnd == True:
            removedDeadEnd = False
            for id, node in graphNoDE.nodes.items():
                if node.deadEnd == True:
                    continue
                if node.outDegree == 0:
                    for inNodeId, inNode in node.inbound.items():
                        del inNode.outbound[node.id]
                        inNode.outDegree = inNode.outDegree - 1
                    deadEndList.append(node.id)
                    node.deadEnd = True
                    removedDeadEnd = True
        else:
            break

    return deadEndList
                        

def findPageRanksNoDE(graphNoDE):
    noDeadEndSize = 0
    for id, node in graphNoDE.nodes.items():
        if node.deadEnd == False:
            noDeadEndSize = noDeadEndSize + 1

    nodeSize = len(graphNoDE.nodes)

    for id, node in graphNoDE.nodes.items():
        if node.deadEnd == True:
            continue
        node.pageRank = 1 / noDeadEndSize

    B = 0.85
    T = 10

    for t in range(T):
        for id, node in graphNoDE.nodes.items():
            if node.deadEnd == True:
                continue

            sum = 0
            for inNodeId, inNode in node.inbound.items():
                sum = sum + inNode.pageRank / inNode.outDegree

            node.pageRank = B * sum + ((1 - B) * (1 / noDeadEndSize))

    return graphNoDE

def findPageRanksDeadEnds(graph, graphNoDE, deadEndList):
    for deadId in reversed(deadEndList):
        node = graph.nodes[deadId]
        
        sum = 0
        for inNodeId, inNode in node.inbound.items():
            inNodeNoDE = graphNoDE.nodes[inNodeId]
            sum = sum + inNodeNoDE.pageRank / inNode.outDegree

        node.pageRank = sum
        graphNoDE.nodes[deadId].pageRank = sum
    
    return graphNoDE

    
def main (argv):
    files = open(argv[1], encoding="utf-8")
    file = [line.rstrip('\n') for line in files]

    lines = []
    linesKey = 0
    for line in file:
        if "#" in line:
            continue

        lines.append(line.split("\t"))

    files.close()

    graph = Graph(lines)
    graphNoDE = Graph(lines)
    deadEndList = findDeadEnds(graphNoDE)
    graphNoDE = findPageRanksNoDE(graphNoDE)
    graphNoDE = findPageRanksDeadEnds(graph, graphNoDE, deadEndList)
    writeToFile(graphNoDE)

    return


startTime = datetime.datetime.now()

main(sys.argv)

finishTime = datetime.datetime.now()
print("Start Time:")
print(startTime)
print("\nFinish Time:")
print(finishTime)
