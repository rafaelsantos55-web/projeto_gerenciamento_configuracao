import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from controle_configuracao import listar_artefatos, resumo_projeto


class TestControleConfiguracao(unittest.TestCase):
    def test_lista_artefatos(self):
        self.assertEqual(len(listar_artefatos()), 4)
        self.assertIn("controle_configuracao.py", [x["nome"] for x in listar_artefatos()])

    def test_resumo(self):
        self.assertIn("4 artefatos", resumo_projeto())


if __name__ == "__main__":
    unittest.main()
