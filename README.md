# Projeto de Gerenciamento de Configuração

**Disciplina:** Projeto de Software – U4/A1  
**Aluno:** Rafael dos Santos Oliveira  
**Curso:** Análise e Desenvolvimento de Sistemas  
**Polo:** Anhanguera/Pirituba

## Objetivo
Demonstrar o controle de versão de artefatos de software usando Git e GitHub, incluindo organização dos arquivos, rastreabilidade de alterações, commits e sincronização com repositório remoto.

## Estrutura
- `src/`: código-fonte do projeto.
- `tests/`: testes automatizados.
- `docs/`: documentação técnica.
- `CHANGELOG.md`: histórico resumido de alterações.

## Execução
Requer Python 3.10 ou superior.

```bash
python src/controle_configuracao.py
```

## Testes
```bash
python -m unittest discover -s tests -v
```

## Fluxo Git utilizado
```bash
git status
git add .
git commit -m "mensagem descritiva"
git push -u origin main
```

## Repositório remoto pretendido
https://github.com/rafaelsantos55-web/projeto_gerenciamento_configuracao

> Observação: o envio ao GitHub deve ser confirmado após autenticação no computador do aluno. O relatório diferencia as operações locais efetivamente executadas da publicação remota ainda pendente.
