from tag import Categoria
from transaction import Transação

ListaCategorias = []
ListaReceitas = []
ListaDispesas = []

def cadastrarCategoria(nome):
  novaCategoria = Categoria(name=nome)
  ListaCategorias.append(novaCategoria)

  return novaCategoria

def cadastrarReceita(valorReceita,categoriaReceita,descriçãoReceita):
  novaReceita = Transação(
    valor = valorReceita,
    descrição = descriçãoReceita,
    categoria = categoriaReceita
  )
  ListaReceitas.append(novaReceita)

  return novaReceita

def cadastrarDispesa(valorDispesa,categoriaDispesa,descriçãoDispesa):
  novaDispesa = Transação(
    valor = valorDispesa,
    descrição = descriçãoDispesa,
    categoria = categoriaDispesa
  )
  ListaDispesas.append(novaDispesa)

  return novaDispesa

def saldoTotal():
  totalreceita = 0
  totaldispesa = 0
  for r in ListaReceitas:
    totalreceita += r.valor
  for d in ListaDispesas:
    totaldispesa += d.valor
  saldofinal = print(f"Saldo Final: {totalreceita - totaldispesa}")

  return saldofinal