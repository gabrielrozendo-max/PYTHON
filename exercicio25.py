preco = float(input("Preço: R$ "))
opcao = int(input("Opção (1 a 4): "))

if opcao == 1:
    valor_final = preco - (preco * 0.10) # 10% de desconto
elif opcao == 2:
    valor_final = preco - (preco * 0.05) # 5% de desconto
elif opcao == 3:
    valor_final = preco # Sem alteração
elif opcao == 4:
    valor_final = preco + (preco * 0.08) # 8% de acréscimo
else:
    print("Opção inválida.")
    valor_final = preco

print(f"Valor final: R$ {valor_final:.2f}")