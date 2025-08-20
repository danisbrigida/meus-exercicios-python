# 1. Pergunte ao usuário a distância da viagem em quilômetros.
distancia = input("Quantos km você vai viajar? ")

# 2. Pergunte quantos km o carro faz por litro de gasolina.
consumo = input("Quantos km por litro seu carro faz? ")

# 3. Pergunte o preço do litro da gasolina.
preco_gasolina = input("Qual o preço do litro da gasolina? ")

# 4. Converta as respostas de texto para números.
distancia_numero = float(distancia)
consumo_numero = float(consumo)
preco_gasolina_numero = float(preco_gasolina)

# 5. Calcule quantos litros de gasolina serão necessários.
litros_necessarios = distancia_numero / consumo_numero

# 6. Calcule o custo total da viagem.
custo_total = litros_necessarios * preco_gasolina_numero

# 7. Mostre o resultado para o usuário.
print("O custo total da sua viagem será de R$", custo_total)