"""MINDVERSE smoke tests: run with python -m unittest discover -s tests."""
import pathlib
import re
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
HTML = (ROOT / "index.html").read_text(encoding="utf-8")
GAME = (ROOT / "assets/game.js").read_text(encoding="utf-8")
BACKEND = (ROOT / "backend/main.py").read_text(encoding="utf-8")

class SmokeTests(unittest.TestCase):
    def test_five_npcs_in_frontend_and_backend(self):
        for npc in ("Lia", "Mara", "Caio", "Orin", "Nilo"):
            self.assertIn("name:'" + npc + "'", GAME)
            self.assertIn('"' + npc + '"', BACKEND)

    def test_menu_moves_live_collection_safely(self):
        self.assertIn("[...quickActions.children]", HTML)
        self.assertIn("gameMenu.hidden", HTML)

    def test_memory_timer_is_contextual(self):
        self.assertIn("textContent!==observedTitle", HTML)

    def test_campaign_has_three_endings(self):
        for name in ("Aliança da Evidência", "Cidade em Desconfiança", "Equilíbrio Frágil"):
            self.assertIn(name, HTML)

    def test_api_has_quota_and_no_key_in_frontend(self):
        self.assertIn("reserve_quota", BACKEND)
        self.assertIn("OPENAI_API_KEY", BACKEND)
        self.assertNotIn("sk-proj-", HTML)
        self.assertIn('"store": False', BACKEND)

    def test_modular_assets(self):
        self.assertIn('src="./assets/game.js"', HTML)
        self.assertIn('href="./assets/game.css"', HTML)

    def test_third_quest(self):
        self.assertIn("s.quests.archive===2", GAME)
        self.assertIn("Arquivo de Nexus", GAME)

    def test_local_save_and_tutor(self):
        self.assertIn("localStorage.setItem(K", HTML)
        self.assertIn("function tutorAdvice()", HTML)

if __name__ == "__main__":
    unittest.main()
