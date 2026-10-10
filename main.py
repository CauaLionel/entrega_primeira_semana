import json

class Hotel:
    def __init__(self, id, nome, nota_geral, localizacao, preco_diaria, quantidade_quartos):
        self.id = id
        self.nome = nome
        self.nota_geral = nota_geral
        self.localizacao = localizacao
        self.preco_diaria = preco_diaria
        self.quantidade_quartos = quantidade_quartos

    def __repr__(self):
        return f"Hotel: {self.nome}, Nota: {self.nota_geral}, Localização: {self.localizacao}, Preço Diária: {self.preco_diaria}, Quantidade de Quartos: {self.quantidade_quartos}"

class quarto:
    def __init__(self, id, hotel_id, numero_quarto, preco, disponivel):
        self.id = id
        self.hotel_id = hotel_id
        self.numero_quarto = numero_quarto
        self.preco = preco
        self.disponivel = disponivel

    def __repr__(self):
        return f"Quarto: {self.numero_quarto}, Preço: {self.preco}, Disponivel: {self.disponivel}"

class hospede:
    def __init__(self, id, nome, cpf, email):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.email = email

    def __repr__(self):
        return f"Hospede: {self.nome}, CPF: {self.cpf}, Email: {self.email}"

class reserva:
    def __init__(self, id, hospede_id, quarto_id, data_reserva, quantidade_dias, valor_total):
        self.id = id
        self.hospede_id = hospede_id
        self.quarto_id = quarto_id
        self.data_reserva = data_reserva
        self.quantidade_dias = quantidade_dias
        self.valor_total = valor_total

    def __repr__(self):
        return f"Reserva: {self.hospede_id}, Quarto: {self.quarto_id}, Data Reserva: {self.data_reserva}, Valor Total: {self.valor_total}"

    def calcular_total(self, quarto_obj):
        # Converte a string "R$ 450,00" para número e multiplica pelos dias da reserva
        preco_num = float(quarto_obj.preco.replace("R$", "").replace(".", "").replace(",", ".").strip())
        return preco_num * self.quantidade_dias

    def exibir_resumo(self, lista_hospedes, lista_quartos, lista_hoteis):
        # Busca os objetos relacionados pelos IDs
        hospede_encontrado = next(h for h in lista_hospedes if h.id == self.hospede_id)
        quarto_encontrado = next(q for q in lista_quartos if q.id == self.quarto_id)
        hotel_encontrado = next(ht for ht in lista_hoteis if ht.id == quarto_encontrado.hotel_id)

        # Calcula a soma automaticamente
        total_calculado = self.calcular_total(quarto_encontrado)

        print(f"\n--- RESUMO DA RESERVA #{self.id} ---")
        print(f"Hóspede: {hospede_encontrado.nome}")
        print(f"Hotel: {hotel_encontrado.nome} ({hotel_encontrado.localizacao})")
        print(f"Quarto: {quarto_encontrado.numero_quarto}")
        print(f"Reserva: {self.quantidade_dias} diária(s)")
        print(f"Valor Total Calculado: R$ {total_calculado:,.2f}".replace(".", "X").replace(",", ".").replace("X", ","))


def carregar_dados(caminho_arquivo):
    with open(caminho_arquivo, "r", encoding="utf-8") as f:
        return json.load(f)


def executar_sistema():
    dados = carregar_dados("dados.json")
    
    lista_hoteis = []
    lista_quartos = []
    lista_hospedes = []
    lista_reservas = []

    for h in dados["hotel"]:
        lista_hoteis.append(Hotel(**h))

    for q in dados["quarto"]:
        lista_quartos.append(quarto(**q))

    for h in dados["hospede"]:
        lista_hospedes.append(hospede(**h))

    for r in dados["reserva"]:
        lista_reservas.append(reserva(**r))

    print(lista_hoteis)
    print(lista_quartos)
    print(lista_hospedes)
    print(lista_reservas)

    # Exibe o resumo com a soma calculada
    for r in lista_reservas:
        r.exibir_resumo(lista_hospedes, lista_quartos, lista_hoteis)

if __name__ == "__main__":
    executar_sistema()