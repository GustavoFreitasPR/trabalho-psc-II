import contextlib
import os


class ItemCatalogo:
    def __init__(self, nome, quantidade, preco):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def exibir(self):
        return f"{self.nome} - Quantidade: {self.quantidade} - Preço unitário: R${self.preco:.2f}"

class ItemOnline(ItemCatalogo):
  def __init__(self, nome, quantidade, preco, desconto):
      super().__init__(nome, quantidade, preco)
      self.desconto = desconto

  def calcular_preco_final(self):
      return self.preco * (1 - self.desconto / 100)

  def exibir(self):
      desconto_info = f" - Desconto: {self.desconto}%" if self.desconto else ""
      return f"{super().exibir()}{desconto_info} - Preço final: R${self.calcular_preco_final():.2f}"

class Catalogo:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo
        self.pecas_disponiveis = []
        self.lista_vendas = []

    def criar_catalogo(self):
        with contextlib.suppress(FileNotFoundError):
            os.remove(self.nome_arquivo)


        while True:
            nome = input("Digite o nome da peça (ou 'fim' para terminar): ")

            if nome.lower() == "fim":
                break

            quantidade = int(input("Digite a quantidade disponível: "))
            preco = float(input("Digite o preço unitário: "))
            desconto = float(input("Digite o desconto para a loja online (0 se não houver): "))

            if desconto > 0:
                item = ItemOnline(nome, quantidade, preco, desconto)
            else:
                item = ItemCatalogo(nome, quantidade, preco)

            self.pecas_disponiveis.append(item)

    def salvar_catalogo(self):
        with open(self.nome_arquivo, "w") as arquivo:
            for item in self.pecas_disponiveis:
                arquivo.write(f"{item.nome};{item.quantidade};{item.preco}\n")

    def carregar_catalogo(self):
        try:
            with open(self.nome_arquivo, "r") as arquivo:
                linhas = arquivo.readlines()

            for linha in linhas:
                nome, quantidade, preco = linha.strip().split(";")
                self.pecas_disponiveis.append(ItemCatalogo(nome, int(quantidade), float(preco)))
        except FileNotFoundError:
            print("Arquivo não encontrado.")

    def exibir_catalogo(self):
        print("\nCatálogo de Peças:")
        for indice, item in enumerate(self.pecas_disponiveis, start=1):
            print(f"{indice}. {item.exibir()}")

    def realizar_venda(self):
        self.exibir_catalogo()
        escolha = int(input("Digite o número da peça que deseja comprar (ou 0 para sair): "))

        if escolha == 0:
            return
        elif escolha < 1 or escolha > len(self.pecas_disponiveis):
            print("Escolha inválida. Tente novamente.")
        else:
            indice = escolha - 1
            item = self.pecas_disponiveis[indice]
            quantidade_disponivel = item.quantidade
            quantidade = int(input(f"Quantidade de '{item.nome}' disponível: {quantidade_disponivel}, informe a quantidade desejada: "))

            if quantidade > 0 and quantidade <= quantidade_disponivel:
                self.lista_vendas.append((item.nome, quantidade, item.preco))
                item.quantidade -= quantidade
                print(f"{quantidade} '{item.nome}'(s) adicionado(s) ao carrinho.")
            elif quantidade > quantidade_disponivel:
                print("Quantidade indisponível. Tente novamente.")
            else:
                print("Quantidade inválida. Tente novamente.")

    def calcular_total(self):
        total = sum(float(preco) * quantidade for _, quantidade, preco in self.lista_vendas)
        return total

    def concluir_venda(self):
        if not self.lista_vendas:
            print("Nenhum item no carrinho.")
            return

        print("\nItens no Carrinho:")
        for nome, quantidade, preco in self.lista_vendas:
            print(f"{nome} - Quantidade: {quantidade} - Preço unitário: R${preco:.2f}")

        total = self.calcular_total()
        print(f"Total da compra: R${total:.2f}")

        pagamento = float(input("Digite o valor pago pelo cliente: "))

        if pagamento < total:
            print("Valor insuficiente. Tente novamente.")
        else:
            troco = pagamento - total
            print(f"Troco: R${troco:.2f}")
            print("Venda concluída com sucesso!")
            self.lista_vendas.clear()

    def realizar_venda_online(self):
      self.exibir_catalogo()
      escolha = int(input("Digite o número da peça que deseja vender (ou 0 para sair): "))

      if escolha == 0:
          return
      elif escolha < 1 or escolha > len(self.pecas_disponiveis):
          print("Escolha inválida. Tente novamente.")
      else:
          indice = escolha - 1
          item = self.pecas_disponiveis[indice]
          quantidade_disponivel = item.quantidade
          quantidade = int(input(f"Quantidade de '{item.nome}' disponível: {quantidade_disponivel}, informe a quantidade desejada: "))

          if quantidade > 0 and quantidade <= quantidade_disponivel:
              if isinstance(item, ItemOnline):
                  preco_final = item.calcular_preco_final()
              else:
                  preco_final = item.preco

              self.lista_vendas.append((item.nome, quantidade, preco_final))
              item.quantidade -= quantidade
              print(f"{quantidade} '{item.nome}'(s) adicionado(s) ao carrinho.")
          elif quantidade > quantidade_disponivel:
              print("Quantidade indisponível. Tente novamente.")
          else:
              print("Quantidade inválida. Tente novamente.")
if __name__ == "__main__":

    nome_arquivo = "catalogo.txt"
    catalogo = Catalogo(nome_arquivo)

    print("Bem-vindo ao Sistema de Vendas!")

    while True:
      print("\nMenu:")
      print("1. Criar Novo Catálogo")
      print("2. Carregar Catálogo Existente")
      print("3. Realizar Venda")
      print("4. Concluir Venda")
      print("5. Exibir Catálogo")
      print("6. Realizar Venda Online")
      print("7. Sair")

      escolha = int(input("Escolha uma opção: "))

      if escolha == 1:
          catalogo.criar_catalogo()
          catalogo.salvar_catalogo()
      elif escolha == 2:
          catalogo.carregar_catalogo()
      elif escolha == 3:
          catalogo.realizar_venda()
      elif escolha == 4:
          catalogo.concluir_venda()
      elif escolha == 5:
          catalogo.exibir_catalogo()
      elif escolha == 6:
          catalogo.realizar_venda_online()
      elif escolha == 7:
        print("Saindo do programa.")
        break
      else:
          print("Opção inválida. Tente novamente.")