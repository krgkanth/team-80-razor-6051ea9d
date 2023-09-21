from unittest import TestCase
from levelup.controller import GameStatus

class TestGameStatusDefaultCharacterName(TestCase):
    def test_init(self):
        DEFAULT_CHARACTER_NAME = "Character"
        testobj = GameStatus()
        self.assertEqual(DEFAULT_CHARACTER_NAME, testobj.character_name)
