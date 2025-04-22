# Integrantes:
# Joseph Emanuel Sanchez Sierra - 2240959
# Eduardo Hernandez Zambrano - 2241636

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

class LinkedListTree:
    def __init__(self):
        self.root = None

    def add_node(self, parent_value, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            parent_node = self._find_node(self.root, parent_value)
            if parent_node:
                parent_node.children.append(TreeNode(value))
            else:
                print(f"Padre con valor {parent_value} no encontrado.")

    def _find_node(self, node, value):
        if node is None:
            return None
        if node.value == value:
            return node
        for child in node.children:
            found = self._find_node(child, value)
            if found:
                return found
        return None

    def calculate_weight(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return 0
        weight = 1  # Contar el nodo actual
        for child in node.children:
            weight += self.calculate_weight(child)
        return weight

    def calculate_order(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return 0
        max_order = len(node.children)
        for child in node.children:
            max_order = max(max_order, self.calculate_order(child))
        return max_order

    def calculate_height(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return 0
        if not node.children:
            return 1
        return 1 + max(self.calculate_height(child) for child in node.children)

# Ejemplo de uso
if __name__ == "__main__":
    tree = LinkedListTree()
    tree.add_node(None, "A")  # Nodo raíz
    tree.add_node("A", "B")
    tree.add_node("A", "C")
    tree.add_node("B", "D")
    tree.add_node("B", "E")
    tree.add_node("C", "F")

    print("Peso del árbol:", tree.calculate_weight())
    print("Orden del árbol:", tree.calculate_order())
    print("Altura del árbol:", tree.calculate_height())