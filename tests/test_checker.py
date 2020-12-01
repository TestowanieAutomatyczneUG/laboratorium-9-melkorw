import unittest
from unittest.mock import *
from Checker import Checker


class TestChecker(unittest.TestCase):
    def setUp(self):
        self.temp = Checker()

    def test_checker_before_17(self):
        file = 'File'
        self.temp.play.get_time = Mock(name='get_time')
        self.temp.play.get_time.return_value = 16
        self.temp.play.wav_was_played = Mock(name='wav_was_played')
        self.temp.play.wav_was_played.return_value = False
        result = self.temp.was_played(file)
        self.assertEqual(result, False)

    def test_checker_after_17(self):
        file = 'File'
        self.temp.play.get_time = Mock(name='get_time')
        self.temp.play.get_time.return_value = 19
        self.temp.play.wav_was_played = Mock(name='wav_was_played')
        self.temp.play.wav_was_played.return_value = True
        result = self.temp.was_played(file)
        self.assertEqual(result, True)
