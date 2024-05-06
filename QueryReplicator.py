# def input_bancos_empresas():
#    bancos_empresas = {}
#    num_empresas = int(input("Quantas empresas deseja incluir? "))
#    for i in range(1, num_empresas + 1):
#        empresa = input(f"Digite o nome da Empresa {i}: ")
#        banco = input(f"Digite o nome do Banco para a Empresa {empresa}: ")
#        bancos_empresas[empresa] = banco
#    return bancos_empresas

def main():
    # Está hardcoded por praticidade eventual.
    # Para inserir os nomes das Empresas e Bancos,
    # descomente a função input_bancos_empresas() e
    # substitua o dicionário abaixo por sua chamada
    # input_bancos_empresas()

    bancos_empresas = {
        "Qualipol Louveira": "qualipol",
        "Qualipol Jundiai": "qualipol_j",
        "Qualipol Parana": "qualipol_p",
        "Alliance Louveira": "packhaus",
        "Alliance Jundiai": "packhaus_j",
        "Alliance Parana": "packhaus_p",
        "Quimipol Louveira": "quimipol",
        "Sense Louveira": "sense",
        "Embaquali Louveira": "embaquali"
    }

    with open(
            "C:/Users/andre/OneDrive/Documentos/CM Partners/Qualipol/Contas a Receber_Teste.txt",
            "r") as query:
        query = query.read()

    queries_atualizadas = []
    for empresa in bancos_empresas:
        query_atualizada = query.format(company=empresa, database=bancos_empresas[empresa])
        queries_atualizadas.append(query_atualizada)

    resultado = "\n\nUNION\n\n".join(queries_atualizadas)
    print(resultado)

if __name__ == "__main__":
    main()
