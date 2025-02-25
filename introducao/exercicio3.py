v_produto = float(input("Digite o valor do produto: "))
v_desconto = float(input("Digite o valor do desconto: "))

v_com_desconto = float(v_produto * (1 - v_desconto / 100))

print(f"O valor do produto com desconto ficara: {v_com_desconto:.2f}")
