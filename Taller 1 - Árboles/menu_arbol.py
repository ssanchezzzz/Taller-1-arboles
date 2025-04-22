# Proyecto: Estructura de Datos - Árboles
# Miembros:
# Joseph Emanuel Sanchez Sierra - 2240959
# Eduardo Hernandez Zambrano - 2241636

from estructura_arbol import LinkedListTree

def main():
    tree = LinkedListTree()
    
    while True:
        print("\n--- Menú ---")
        print("1. Agregar Nodo")
        print("2. Calcular Peso")
        print("3. Calcular Orden")
        print("4. Calcular Altura")
        print("5. Salir")
        
        choice = input("Elija una opción: ")
        
        if choice == '1':
            parent_value = input("Ingrese el valor del nodo padre (o presione Enter si es el nodo raíz): ")
            value = input("Ingrese el valor del nuevo nodo: ")
            if parent_value.strip() == "":
                tree.add_node(None, value)  # Nodo raíz
            else:
                tree.add_node(parent_value, value)
            print(f"Nodo con valor '{value}' agregado.")
        
        elif choice == '2':
            weight = tree.calculate_weight()
            print(f"El peso del árbol es: {weight}")
        
        elif choice == '3':
            order = tree.calculate_order()
            print(f"El orden del árbol es: {order}")
        
        elif choice == '4':
            height = tree.calculate_height()
            print(f"La altura del árbol es: {height}")
        
        elif choice == '5':
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()