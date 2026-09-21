idade = int(input("Idade: "))
estudante = input("Estudante (SIM/NÃO): ").strip().upper()

# O valor total é 30.00[cite: 1]
if idade < 12 or idade >= 60 or estudante == "SIM":
    valor = 15.00
else:
    valor = 30.00

print(f"Valor do ingresso: R$ {valor:.2f}")