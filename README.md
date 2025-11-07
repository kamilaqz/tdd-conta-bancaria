# Sistema de Conta Bancária - TDD

## a. Projeto Escolhido

**Opção 2: Sistema de Conta Bancária**

Implementação de uma conta bancária simplificada utilizando a metodologia TDD (Test-Driven Development). O sistema permite:

- ✅ Criar uma conta com saldo inicial zero
- ✅ Realizar depósitos válidos
- ✅ Realizar saques válidos
- ✅ Consultar o saldo atual
- ✅ Transferir valores entre contas
- ✅ Visualizar extrato de transações
- ✅ Validações: não permite sacar valores maiores que o saldo disponível
- ✅ Validações: não permite operações com valores menores ou iguais a zero

## b. Ferramenta de Teste Utilizada

**pytest** - Framework de testes para Python

- Versão: 7.4.0 ou superior
- Escolhido por sua sintaxe simples e recursos poderosos
- Suporte nativo a assertions e fixtures
- Relatórios de teste claros e detalhados

## c. Como Executar os Testes

### Pré-requisitos
- Python 3.11 ou superior instalado
- pip (gerenciador de pacotes Python)

### Instalação

1. Clone o repositório ou navegue até o diretório do projeto:
```bash
cd "c:\Users\Kamila Queiroz\OneDrive\Área de Trabalho\P7\tdd"
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

### Executar os Testes

```bash
# Executar todos os testes
python -m pytest -v

# Executar com mais detalhes
python -m pytest -vv

# Executar um arquivo de teste específico
python -m pytest tests/test_account.py -v

# Executar um teste específico
python -m pytest tests/test_account.py::test_deposit_increases_balance -v
```

### Estrutura de Testes

O projeto possui 6 testes implementados:

1. `test_create_account_with_zero_balance` - Verifica criação de conta com saldo zero
2. `test_deposit_increases_balance` - Testa funcionalidade de depósito
3. `test_withdraw_decreases_balance` - Testa funcionalidade de saque
4. `test_get_balance_returns_current_balance` - Valida consulta de saldo
5. `test_transfer_between_accounts` - Verifica transferências entre contas
6. `test_account_statement` - Valida histórico de transações

## d. Experiência Utilizando TDD

A experiência com TDD foi bastante positiva e educativa. O processo seguiu rigorosamente o ciclo: RED ---> GREEN ---> REFACTOR.
Nunca tinha usado desse método antes, e entendi porque é famoso. Utilizando o TDD, o desenvolvedor consegue focar mais funcionalidades. É realmente muito interessante construir os metodos sabendo do que eles precisam para funcionarem. Além de que os problemas são detectados imediatamente durante o desenvolvimento.

O unico desafio que encontrei foi manter o foco em cada funcionalidade e nao pular etapas.

### Conclusão

TDD transformou a forma de desenvolver, tornando o processo mais metódico e confiável. A sensação de ter todos os testes passando após cada ciclo traz segurança e satisfação.


