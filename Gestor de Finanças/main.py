from tag import Categoria
from transaction import *
from tools import *

categoria_DispesasFixas = cadastrarCategoria("Dispesas fixas")
categoria_Receita = cadastrarCategoria("Receita")

fevereiro = cadastrarReceita(
  valorReceita = 1518.0,
  categoriaReceita = categoria_Receita,
  descriçãoReceita = "salário"
),
cadastrarDispesa(
  valorDispesa= 300.0,
  categoriaDispesa= categoria_DispesasFixas,
  descriçãoDispesa= "Conta de água"
)

saldoTotal()
