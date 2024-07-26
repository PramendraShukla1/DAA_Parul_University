import sys
import heapq
def dijkstra(graph, src, dest):
    inf = sys.maxsize
    node_data = {node: {'cost': inf, 'pred': []} for node in graph}
    node_data[src]['cost'] = 0
    visited = []
    temp = src

    for _ in range(len(graph)):
        if temp not in visited:
            visited.append(temp)
            min_heap = []
            for neighbor, weight in graph[temp].items():
                if neighbor not in visited:
                    cost = node_data[temp]['cost'] + int(weight)
                    if cost < node_data[neighbor]['cost']:
                        node_data[neighbor]['cost'] = cost
                        node_data[neighbor]['pred'] = node_data[temp]['pred'] + [temp]
                    heapq.heappush(min_heap, (node_data[neighbor]['cost'], neighbor))
        if min_heap:
            temp = min_heap[0][1]
        else:
            break

    if node_data[dest]['cost'] == inf:
        print("No path found from {} to {}".format(src, dest))
    else:
        print("Shortest Distance: " + str(node_data[dest]['cost']))
        print("Shortest Path: " + str(node_data[dest]['pred'] + [dest]))




if __name__ == "__main__":
    graph = {
        'A':{'B':2, 'C':4},
        'B':{'A':2, 'C':'3','D':8 },
        'C':{'A':4,'B':3,'E':5,'D':2},
        'D':{'B':8,'C':2,'E':11,'F':22},
        'E':{'C':5,'D':11,'F':1},
        'F':{'D':22, 'E':1}
    }

    source = 'A'
    destination = 'F'
    dijkstra(graph, source, destination)
