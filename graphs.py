#%%
class Graph:
    
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}

        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)

            else:
                self.graph_dict[start] = [end]

        print("Graph Dictionary:", self.graph_dict)
    
    def get_paths(self, start, end, path = []):
        path = path + [start]
        if start == end:
            return [path]
        
        if start not in self.graph_dict:
            return []
        
        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)

        return paths

    def get_shortest_path(self, start, end, path=[]):
        path = path + [start]

        if start not in self.graph_dict:
            return None
        
        if start == end:
            return [path]
        
        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                current_path = self.get_shortest_path(node, end, path)

                if current_path:
                    if shortest_path is None or len(current_path) < len(shortest_path):
                        shortest_path = current_path

        return shortest_path          

#%%
## These are edges in graphs (one node to next)
routes = {
    ("Icecrown Citadel", "Dalaran"),
    ("Dalaran", "Stormwind City"),
    ("Dalaran", "Orgrimmar"),
    ("Dalaran", "Howling Fjord"),
    ("Dalaran", "Undercity"),
    ("Dalaran", "Darnassus"),
    ("Dalaran", "Thunder Bluff"),
    ("Stormwind City", "Ironforge"),
    ("Stormwind City", "Darnassus"),
    ("Stormwind City", "Undercity"),
    ("Stormwind City", "Dalaran"),
    ("Orgrimmar", "Thunder Bluff"),
    ("Orgrimmar", "Silvermoon City"),
    ("Orgrimmar", "Dalaran"),
    ("Ironforge", "Stormwind City"),
    ("Ironforge", "Dalaran"),
    ("Darnassus", "Undercity"),
    ("Undercity", "Dalaran"),
    ("Thunder Bluff", "Ogrimmar"),

}


#%%

wow_graph = Graph(routes)

# %%
wow_graph.get_paths("Ironforge", "Darnassus")
wow_graph.get_shortest_path("Ironforge", "Darnassus")

# %%
