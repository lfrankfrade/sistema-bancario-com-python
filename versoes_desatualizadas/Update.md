# Criando um sistema bancário com Python

Este código tem como objetivo concluir um desafio de projeto do curso NTT DATA - Engenharia de Dados com Python - Secção: Trabalhando com coleções em Python, Oferecido pela [DIO](https://www.dio.me/bootcamp/engenharia-dados-python)

# Atualizando o sistema bancário com python para segunda versão

Separar as funções existentes de saque, depósito e extrato em funções de python.
Criar duas novas funções no sistema: cadastrar usuário (cliente) e cadastrar conta corrente.

As funções foram criadas para exercitar o conteúdo do Curso e cada função tem uma regra na passagem de argumentos.

## Saque

A função de saque recebe os argumentos apenas por nome (keyword only).
Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques.
Sugestão de retorno: saldo e extrato.

## Depósito

A função de depósito recebe os argumentos apenas por posição (positional only).
Sugestão de argumentos: saldo, valor, extrato.
Sugestão de retorno: saldo e extrato.

## Extrato

A função de extrato recebe os argumentos por posição e nome (positional only e keyword only).
Sugestão de argumentos posicionais: saldo.
Sugestão de argumentos nomeados: extrato.

## Novas funções: cadastrar usuário e conta corrente

Cadastrar usuário:
Armazenar os usuários em uma lista;
o usuário é composto por nome, data de nascimento, cpf e endereço;
O endereço é uma string no formato: "logradouro, nro - bairro - cidade/sigla estado";
Armazenar somente os números do cpf; 
Não é possível cadastrar dois usuários com o mesmo cpf.

Cadastrar conta corrente:
Armazenar as contas em uma lista;
A conta é composta por: agência, número da conta e usuário;
O número da conta é sequencial, iniciando em 1;
O número da agência é fixo: "0001";
O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.