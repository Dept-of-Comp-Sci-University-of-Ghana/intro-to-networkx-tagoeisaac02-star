from types import GenericAlias
from inspect import GEN_RUNNING
import networkx as n

# Define Directed Graph variable
G = n.DiGraph()

# list of Tuples, tuple of strings
edges = [
         ("Elton", "Asana"), ("Elton", "Harry"), ("Elton", "Isaac"),("Elton", "Samuel"),
         ("Asana", "Elton"), ("Asana", "Harry"), ("Asana", "Isaac"), ("Asana", "Samuel"),
         ("Harry", "Elton"),  ("Harry", "Isaac"), ("Harry", "Samuel"), ("Harry", "Asana"),
         ("Isaac", "Elton"),  ("Isaac", "Asana") ,  ("Isaac", "Harry"), ("Isaac", "Samuel"),
         ("Samuel", "Elton"),  ("Samuel", "Asana"),  ("Samuel", "Harry"),  ("Samuel", "Isaac")
        
 ]


# Add edges to Directed Graph
G.add_edges_from(edges)


# Drawing the 
n.draw(
    G,
    with_labels=True,
    node_size=2020,
    node_color="blue",
    font_color="white",
    font_size=12
    )


degree_of_connection=dict(G.degree())
print(f"Degree of connection: {degree_of_connection}\n")

number_of_nodes = G.number_of_nodes()
print(f"Number of Nodes: {number_of_nodes}\n")


number_of_edges = G.number_of_edges()
print(f"Number of Edges: {number_of_edges}\n")


degree_of_distribution = [value for key,value in G.degree()] # list comprehension


# In G.degree -> key, values -> values

print(f"Degree of Distribution: {degree_of_distribution}\n")



