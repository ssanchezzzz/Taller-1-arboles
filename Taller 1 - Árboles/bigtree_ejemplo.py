# Integrantes:
# Joseph Emanuel Sanchez Sierra - 2240959
# Eduardo Hernandez Zambrano - 2241636

from bigtree import Node

# Crear nodos del árbol
root = Node("A")
node_b = Node("B", parent=root)
node_c = Node("C", parent=root)
node_d = Node("D", parent=node_b)
node_e = Node("E", parent=node_b)
node_f = Node("F", parent=node_c)

# Mostrar el árbol
print(root.show())

# Calcular propiedades del árbol
print("Altura del árbol:", root.height)
print("Número de nodos:", root.size)