from multiprocessing import Process, Manager,Queue

def dfs(graph, node,visited):
    visited.add(node)

    for next in graph[node]:
        if next not in visited:
            dfs(graph,next,visited)


def para_dfs(graph, node, shared_list):
    print('Executing parallel dfs')
    visited=set()

    dfs(graph,node,visited)
    shared_list.extend(visited)






if __name__=='__main__':
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A', 'E'],
        'D': ['B'],
        'E': ['C']
    }

    root='A'

    with Manager() as manager:
        shared_list=manager.list()
        process_list=[]

        search_process=Process(target=para_dfs,args=(graph,root,shared_list))
        search_process.start()
        process_list.append(search_process)

        for process in process_list:
            process.join()

        print(list(shared_list))
