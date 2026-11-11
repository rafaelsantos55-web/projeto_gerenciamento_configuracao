"""Exemplo didático de controle de itens de configuração."""

VERSAO = "1.1.1"


def listar_artefatos():
    """Retorna artefatos de exemplo controlados pelo projeto."""
    return [
        {"nome": "requisitos.md", "tipo": "documentacao", "versao": "1.0"},
        {"nome": "controle_configuracao.py", "tipo": "codigo-fonte", "versao": VERSAO},
        {"nome": "testes_unitarios.py", "tipo": "teste", "versao": "1.0"},
        {"nome": "CHANGELOG.md", "tipo": "documentacao", "versao": "1.1.1"},
    ]


def resumo_projeto():
    """Apresenta um resumo simples dos itens versionados."""
    artefatos = listar_artefatos()
    return f"Projeto SCM: {len(artefatos)} artefatos cadastrados (versão {VERSAO})."


if __name__ == "__main__":
    print(resumo_projeto())
    for item in listar_artefatos():
        print(f"- {item['nome']} | {item['tipo']} | v{item['versao']}")
