# Python-Mini-Projects:
1 - Gestor de Finanças utilizando POO em python:

Basicamente um estudo simples de Programação Orientada a objetos com algumas funcionalidades:
- Opcao de cadastro para categorias de despesas e receitas
- Opcoes de cadastro para as despesas e receitas contendo valores, descrição e categoria
- Opcao de visualização de cadastro final automatizado dentro do sistema

2 - Jogo de adivinhação de nímeros:

Sistema simples utilizando python e interação de terminal:
- Tratamento de erro simples para uma experiencia mais dinâmica
- Funcionamento de um orientador para facilitar o usuario
- Contador funcional de tentativas para aprimorar ainda mais a experiencia

3 - Gerador de arquivo VCF-Cards para whatsapp:

Esta API em **FastAPI** gera dinamicamente arquivos `.vcf` (vCard) para importação direta de contatos no WhatsApp.
- Endpoint: `GET /generate_vcf`
- Parâmetros via query:
  - `nome` (string obrigatória)
  - `telefone` (string obrigatória)
    
**Ao receber a requisição:**

1. O nome é normalizado (`slugify`) para gerar um nome de arquivo seguro.
2. É criado um arquivo `.vcf` contendo:
   - `FN` → Nome do contato
   - `TEL` → Número de telefone
3. O arquivo é salvo temporariamente na pasta `vcf_files/`.
4. A API retorna a URL pública do arquivo:
   ```json
   {
     "vcf_url": "/vcf/nome_timestamp.vcf",
     "filename": "nome_timestamp.vcf"
   }
