from unittest import TestCase
from main import Check_flag

class TestCheck_Flag_Function (TestCase):

    def test_is_straigh_true(self):
        card_list = [
        {"num": 6, "mark": 1},
        {"num": 5, "mark": 2}, 
        {"num": 4, "mark": 2},
        {"num": 3, "mark": 3},
        {"num": 2, "mark": 3},
        ]
        self.assertIs(Check_flag().is_straight(card_list), True)

    def test_is_straigh_true2(self):
        card_list = [
        {"num": 14, "mark": 1},
        {"num": 5, "mark": 2}, 
        {"num": 4, "mark": 2},
        {"num": 3, "mark": 3},
        {"num": 2, "mark": 3},
        ]
        self.assertIs(Check_flag().is_straight(card_list), True)

    def test_is_straigh_false(self):
        card_list = [
        {"num": 14, "mark": 1},
        {"num": 5, "mark": 2}, 
        {"num": 2, "mark": 2},
        {"num": 3, "mark": 3},
        {"num": 2, "mark": 3},
        ]
        self.assertIs(Check_flag().is_straight(card_list), False)

    def test_is_flush_true(self):
        card_list = [
        {"num": 14, "mark": 2},
        {"num": 5, "mark": 2}, 
        {"num": 2, "mark": 2},
        {"num": 3, "mark": 2},
        {"num": 2, "mark": 2},
        ]
        self.assertIs(Check_flag().is_flush(card_list), True)

    def test_is_flush_true(self):
        card_list = [
        {"num": 14, "mark": 4},
        {"num": 5, "mark": 4}, 
        {"num": 2, "mark": 2},
        {"num": 3, "mark": 2},
        {"num": 2, "mark": 2},
        ]
        self.assertIs(Check_flag().is_flush(card_list), False)


