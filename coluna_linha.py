# Abra e leia o arquivo
with open('caminho\\packages.txt', 'r') as file:
    # Leia todas as linhas e remova quebras de linha
    lines = [line.strip() for line in file]

# Converta a lista para uma string única, separada por espaços
single_line = ' '.join(lines)

# Salve o resultado em um novo arquivo, se necessário
with open('caminho\\packages_single_line.txt', 'w') as output_file:
    output_file.write(single_line)

print("Transformação concluída! A linha única foi salva em 'packages_single_line.txt'.")