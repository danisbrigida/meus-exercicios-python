inventario = []

def adicionar_item():
    """Adiciona um novo item ao inventário."""
    nome = input("Digite o nome do item: ")
    
    # Laço para garantir que a quantidade seja um número válido e positivo
    while True:
        quantidade_str = input("Digite a quantidade: ")
        # Verifica se a entrada é composta apenas por dígitos
        if quantidade_str.isdigit():
            quantidade = int(quantidade_str)
            if quantidade > 0:
                break  # Sai do laço se a quantidade for válida
            else:
                print("\nErro: A quantidade deve ser um número positivo.")
        else:
            print("\nErro: A quantidade deve ser um número inteiro.")

    item_existente = False
    for item in inventario:
        if item["nome"].lower() == nome.lower():
            item["quantidade"] += quantidade
            print(f"\nQuantidade de '{nome}' atualizada para {item['quantidade']}.")
            item_existente = True
            break
    
    if not item_existente:
        novo_item = {"nome": nome, "quantidade": quantidade}
        inventario.append(novo_item)
        print(f"\nItem '{nome}' com quantidade {quantidade} adicionado ao inventário.")

def remover_item():
    """Remove um item do inventário pelo nome."""
    nome = input("Digite o nome do item para remover: ")
    item_encontrado = False
    
    for item in inventario:
        if item["nome"].lower() == nome.lower():
            inventario.remove(item)
            item_encontrado = True
            print(f"\nItem '{nome}' removido com sucesso.")
            break
            
    if not item_encontrado:
        print(f"\nItem '{nome}' não encontrado no inventário.")

def listar_inventario():
    """Exibe todos os itens do inventário."""
    if not inventario:
        print("\nO inventário está vazio.")
    else:
        print("\n--- Inventário Atual ---")
        for item in inventario:
            print(f"Nome: {item['nome']}, Quantidade: {item['quantidade']}")
        print("-----------------------")

def main():
    """Função principal que exibe o menu e controla as opções."""
    while True:
        print("\n--- Menu de Controle de Inventário ---")
        print("1. Adicionar item")
        print("2. Remover item")
        print("3. Listar inventário")
        print("4. Sair")
        
        escolha = input("Digite sua escolha (1-4): ")
        
        if escolha == "1":
            adicionar_item()
        elif escolha == "2":
            remover_item()
        elif escolha == "3":
            listar_inventario()
        elif escolha == "4":
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Escolha inválida. Por favor, digite um número entre 1 e 4.")

if __name__ == "__main__":
    main()