from multiprocessing import Process, Manager,Queue

def bfs(graph,root, shared_list):
    visited=set()
    queue=Queue()

    visited.add(root)
    queue.put(root)

    while not queue.empty():
        node=queue.get()
        shared_list.append(node)
        for next in graph[node]:
            if next not in visited:
                visited.add(next)
                queue.put(next)

def para_bfs(graph,root,shared_list):
    print('Executing parallel bfs')
    bfs(graph,root,shared_list)



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

        search_process=Process(target=para_bfs,args=(graph,root,shared_list))
        search_process.start()
        process_list.append(search_process)

        for process in process_list:
            process.join()

        print(list(shared_list))
