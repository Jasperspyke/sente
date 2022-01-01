"""

Author: Arthur Wesley

"""

import os
from pathlib import Path
from unittest import TestCase

import sente.exceptions
from sente import sgf

from assert_does_not_raise import DoesNotRaiseTestCase


class BasicSGF(DoesNotRaiseTestCase):

    def test_all_sgfs(self):
        """

        tests to see if any of the sgf files in the directory raise any exceptions

        :return:
        """

        files = os.listdir("sgf")

        # sgf.load(os.path.join("sgf", "extra letter in move.sgf"))

        for file in files:
            with self.assertDoesNotRaise(Exception):
                game = sgf.load(str(Path("sgf")/file))
                game.play_default_sequence()

    def test_punctuation_ignored_inside_parens(self):
        """

        makes sure that punctuation is ignored inside parens

        """

        with self.assertDoesNotRaise(sente.exceptions.InvalidSGFException):
            game = sgf.load("sgf/punctuation ignored inside parentheses.sgf")
            game.play_default_sequence()

    def test_simple_single_branch_file(self):
        """

        tests to see if we can import a sgf file with a single branch

        :return:
        """

        B = sente.stone.BLACK
        W = sente.stone.WHITE
        _ = sente.stone.EMPTY

        game = sgf.load("sgf/simple sequence.sgf")
        game.play_default_sequence()

        print(game)

        expected_game = sente.Board19([[_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
                                       [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
                                       [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
                                       [_, _, _, B, _, _, _, _, _, _, _, _, _, _, _, _, B, _, _],
                                       [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
                                       [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
                                       [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
                                       [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
                                       [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
                                       [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
                                       [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
                                       [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
                                       [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
                                       [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
                                       [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
                                       [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
                                       [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, B, W, _],
                                       [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, W, _, W],
                                       [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, W, _, W]])

        self.assertEqual(expected_game, game.get_board())

    def test_full_single_branch_game(self):
        """

        tests to see if the module can keep track of an entire game

        :return:
        """

        game = sgf.load("sgf/34839594-255-IDW64-noob_bot_3.sgf")
        game.play_default_sequence()

        self.assertEqual(" 1  .  .  .  .  .  .  ⚫ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚫ .  .  .  .  .\n"
                         " 2  .  .  .  .  ⚪ ⚫ ⚫ ⚫ ⚪ ⚫ ⚫ ⚫ ⚪ ⚫ .  .  .  .  .\n"
                         " 3  .  .  ⚪ .  ⚪ ⚪ ⚫ ⚫ ⚫ .  ⚫ ⚫ ⚪ ⚫ ⚫ .  ⚪ .  .\n"
                         " 4  .  .  .  ⚪ .  .  ⚪ ⚫ ⚫ *  ⚫ ⚪ ⚪ ⚪ ⚫ ⚫ ⚪ .  .\n"
                         " 5  ⚪ ⚪ ⚪ ⚫ ⚪ ⚪ ⚪ ⚪ ⚫ ⚪ ⚪ .  ⚪ ⚪ ⚫ .  .  .  .\n"
                         " 6  ⚫ ⚫ ⚫ ⚫ ⚫ ⚪ ⚫ ⚫ ⚪ .  ⚪ .  .  .  ⚪ ⚪ .  .  .\n"
                         " 7  .  .  .  .  ⚫ ⚪ ⚫ ⚫ ⚪ .  ⚪ ⚪ ⚪ ⚪ .  ⚪ .  .  .\n"
                         " 8  ⚪ ⚪ ⚪ ⚪ ⚪ ⚫ ⚫ ⚪ ⚪ .  .  .  ⚪ .  ⚪ ⚪ ⚫ .  .\n"
                         " 9  ⚫ ⚫ ⚫ ⚪ ⚫ ⚫ ⚫ ⚫ ⚪ .  .  ⚪ ⚫ ⚫ .  .  .  .  .\n"
                         "10  .  .  ⚫ ⚪ ⚪ ⚫ .  ⚫ ⚪ *  .  ⚪ .  .  .  ⚪ ⚪ ⚪ .\n"
                         "11  .  .  ⚫ ⚫ ⚪ ⚫ .  ⚪ .  .  .  ⚪ .  ⚫ ⚫ ⚪ ⚫ ⚪ ⚪\n"
                         "12  ⚪ ⚪ ⚫ ⚫ ⚪ ⚫ .  ⚪ .  .  ⚪ ⚫ ⚫ ⚫ ⚪ ⚫ ⚫ ⚫ ⚪\n"
                         "13  ⚫ ⚪ ⚪ ⚫ ⚪ ⚫ ⚫ ⚫ ⚪ .  .  .  .  ⚫ ⚪ .  ⚫ ⚫ ⚪\n"
                         "14  ⚫ .  .  ⚪ ⚪ ⚫ ⚫ ⚫ ⚪ .  .  ⚪ ⚪ ⚪ ⚪ .  .  .  ⚫\n"
                         "15  ⚫ ⚫ ⚫ ⚫ ⚫ ⚪ ⚪ ⚪ .  .  ⚪ ⚪ ⚫ ⚪ .  ⚪ ⚫ ⚫ ⚫\n"
                         "16  ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚫ ⚫ ⚪ ⚪ ⚫ ⚫ ⚫ ⚫ ⚫ ⚪ ⚪ ⚪ ⚪\n"
                         "17  ⚫ ⚫ ⚫ ⚪ ⚫ .  .  ⚫ ⚫ ⚫ .  ⚫ .  ⚫ .  ⚪ ⚫ .  .\n"
                         "18  ⚫ ⚫ .  ⚪ ⚫ ⚫ ⚫ .  .  .  ⚫ ⚪ ⚫ .  .  ⚪ ⚫ ⚫ ⚫\n"
                         "19  .  ⚫ .  ⚪ ⚪ ⚫ .  ⚪ ⚪ .  ⚪ ⚪ ⚪ ⚪ .  ⚪ ⚫ ⚫ .\n"
                         "    A  B  C  D  E  F  G  H  J  K  L  M  N  O  P  Q  R  S  T\n"
                         "noob_bot_3: Thanks for playing. If you want a weaker/stronger bot match with you, "
                         "recommend try to play with 'ELOtest'. It can calculate & match your rank after few games.\n"
                         "noob_bot_3: Final score: W+368.5 (upper bound: 368.5, lower: 368.5)\n", str(game))

    def test_non_standard_komi(self):
        """

        tests to see if we can extract the komi from a game

        :return:
        """

        game = sgf.load("sgf/0.5 Komi.sgf")

        game.pss()
        game.pss()

        self.assertEqual(game.score().get_white_points(), 0.5)

    def test_semicolon_inside_brackets(self):
        """

        tests to see if semicolons inside a SGF's text field are ignored

        :return:
        """

        with self.assertDoesNotRaise(sente.exceptions.InvalidSGFException):
            game = sgf.load("sgf/commented semicolon.sgf")
            game.play_default_sequence()

    def test_nested_brackets(self):
        """

        tests to see if a file can be loaded with nested brackets

        :return:
        """

        with self.assertDoesNotRaise(sente.exceptions.InvalidSGFException):
            game = sgf.load("sgf/nested brackets.sgf")

    def test_backslash_close_brackets(self):
        """

        tests to see if a backslash followed by closing brackets is loaded correctly

        :return:
        """

        game = sgf.load("sgf/nested brackets.sgf")
        sequence = game.get_default_sequence()[:2]

        game.play_sequence(sequence)
        self.assertEqual(game.comment, "here are some nested brackets! []")

    def test_official_ff4_test_file(self):
        """

        tests to see if the official ff4 test file can be run

        :return:
        """

        with self.assertDoesNotRaise(sente.exceptions.InvalidSGFException):
            game = sgf.load("sgf/ff4_ex.sgf")


class StringLoad(DoesNotRaiseTestCase):
    """

    tests to see if SGFs can be loaded from strings and not just from files

    """

    def test_all_sgfs(self):
        """

        tests to see if any of the sgf files in the directory raise any exceptions

        :return:
        """

        files = os.listdir("sgf")

        # sgf.load(os.path.join("sgf", "extra letter in move.sgf"))

        for file in files:
            with self.assertDoesNotRaise(Exception):
                with open(str(Path("sgf")/file), encoding="utf-8") as sgf_file:
                    game = sgf.loads(sgf_file.read())
                    game.play_default_sequence()

    def test_simple_single_branch_file(self):
        """

        tests to see if we can import a sgf file with a single branch

        :return:
        """

        B = sente.stone.BLACK
        W = sente.stone.WHITE
        _ = sente.stone.EMPTY

        with open("sgf/simple sequence.sgf") as sgf_file:
            game = sgf.loads(sgf_file.read())
        game.play_default_sequence()

        expected_game = sente.Board19([[_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
                                 [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
                                 [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
                                 [_, _, _, B, _, _, _, _, _, _, _, _, _, _, _, _, B, _, _],
                                 [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
                                 [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
                                 [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
                                 [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
                                 [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
                                 [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
                                 [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
                                 [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
                                 [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
                                 [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
                                 [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
                                 [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
                                 [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, B, W, _],
                                 [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, W, _, W],
                                 [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, W, _, W]])

        self.assertEqual(expected_game, game.get_board())

    def test_full_single_branch_game(self):
        """

        tests to see if the module can keep track of an entire game

        :return:
        """

        B = sente.stone.BLACK
        W = sente.stone.WHITE
        _ = sente.stone.EMPTY

        with open("sgf/34839594-255-IDW64-noob_bot_3.sgf") as sgf_file:
            game = sgf.loads(sgf_file.read())
        game.play_default_sequence()

        self.assertEqual(" 1  .  .  .  .  .  .  ⚫ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚫ .  .  .  .  .\n"
                         " 2  .  .  .  .  ⚪ ⚫ ⚫ ⚫ ⚪ ⚫ ⚫ ⚫ ⚪ ⚫ .  .  .  .  .\n"
                         " 3  .  .  ⚪ .  ⚪ ⚪ ⚫ ⚫ ⚫ .  ⚫ ⚫ ⚪ ⚫ ⚫ .  ⚪ .  .\n"
                         " 4  .  .  .  ⚪ .  .  ⚪ ⚫ ⚫ *  ⚫ ⚪ ⚪ ⚪ ⚫ ⚫ ⚪ .  .\n"
                         " 5  ⚪ ⚪ ⚪ ⚫ ⚪ ⚪ ⚪ ⚪ ⚫ ⚪ ⚪ .  ⚪ ⚪ ⚫ .  .  .  .\n"
                         " 6  ⚫ ⚫ ⚫ ⚫ ⚫ ⚪ ⚫ ⚫ ⚪ .  ⚪ .  .  .  ⚪ ⚪ .  .  .\n"
                         " 7  .  .  .  .  ⚫ ⚪ ⚫ ⚫ ⚪ .  ⚪ ⚪ ⚪ ⚪ .  ⚪ .  .  .\n"
                         " 8  ⚪ ⚪ ⚪ ⚪ ⚪ ⚫ ⚫ ⚪ ⚪ .  .  .  ⚪ .  ⚪ ⚪ ⚫ .  .\n"
                         " 9  ⚫ ⚫ ⚫ ⚪ ⚫ ⚫ ⚫ ⚫ ⚪ .  .  ⚪ ⚫ ⚫ .  .  .  .  .\n"
                         "10  .  .  ⚫ ⚪ ⚪ ⚫ .  ⚫ ⚪ *  .  ⚪ .  .  .  ⚪ ⚪ ⚪ .\n"
                         "11  .  .  ⚫ ⚫ ⚪ ⚫ .  ⚪ .  .  .  ⚪ .  ⚫ ⚫ ⚪ ⚫ ⚪ ⚪\n"
                         "12  ⚪ ⚪ ⚫ ⚫ ⚪ ⚫ .  ⚪ .  .  ⚪ ⚫ ⚫ ⚫ ⚪ ⚫ ⚫ ⚫ ⚪\n"
                         "13  ⚫ ⚪ ⚪ ⚫ ⚪ ⚫ ⚫ ⚫ ⚪ .  .  .  .  ⚫ ⚪ .  ⚫ ⚫ ⚪\n"
                         "14  ⚫ .  .  ⚪ ⚪ ⚫ ⚫ ⚫ ⚪ .  .  ⚪ ⚪ ⚪ ⚪ .  .  .  ⚫\n"
                         "15  ⚫ ⚫ ⚫ ⚫ ⚫ ⚪ ⚪ ⚪ .  .  ⚪ ⚪ ⚫ ⚪ .  ⚪ ⚫ ⚫ ⚫\n"
                         "16  ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚫ ⚫ ⚪ ⚪ ⚫ ⚫ ⚫ ⚫ ⚫ ⚪ ⚪ ⚪ ⚪\n"
                         "17  ⚫ ⚫ ⚫ ⚪ ⚫ .  .  ⚫ ⚫ ⚫ .  ⚫ .  ⚫ .  ⚪ ⚫ .  .\n"
                         "18  ⚫ ⚫ .  ⚪ ⚫ ⚫ ⚫ .  .  .  ⚫ ⚪ ⚫ .  .  ⚪ ⚫ ⚫ ⚫\n"
                         "19  .  ⚫ .  ⚪ ⚪ ⚫ .  ⚪ ⚪ .  ⚪ ⚪ ⚪ ⚪ .  ⚪ ⚫ ⚫ .\n"
                         "    A  B  C  D  E  F  G  H  J  K  L  M  N  O  P  Q  R  S  T\n"
                         "noob_bot_3: Thanks for playing. If you want a weaker/stronger bot match with you, "
                         "recommend try to play with 'ELOtest'. It can calculate & match your rank after few games.\n"
                         "noob_bot_3: Final score: W+368.5 (upper bound: 368.5, lower: 368.5)\n", str(game))


class BranchedSGF(TestCase):

    def test_simple_branched_sgf(self):
        """

        tests to see if the SGF reader works for simple files

        :return:
        """

        game = sgf.load("sgf/simple fork.sgf")

        self.assertIn(sente.Move(15, 3, sente.stone.BLACK), game.get_branches())
        self.assertIn(sente.Move(16, 3, sente.stone.BLACK), game.get_branches())

    def test_long_branched_sgf(self):
        """

        tests to see if the SGF reader works for longer SGF files

        :return:
        """

        game = sgf.load("sgf/two josekis.sgf")

        self.assertEqual([sente.Move(16, 3, sente.stone.BLACK)], game.get_branches())
        game.play(17, 4)

        self.assertEqual([sente.Move(14, 2, sente.stone.WHITE), sente.Move(14, 3, sente.stone.WHITE)], game.get_branches())

    def test_complex_branched_sgf(self):
        """

        tests to see if the SGF parser can handle an SGF file with multiple branches

        :return:
        """

        game = sgf.load("sgf/3-4.sgf")  # a 3-4 joseki refrence with lots of branches

        # play all of the sequences
        game.play_default_sequence()
        game.advance_to_root()

        self.assertEqual([sente.Move(16, 3, sente.stone.BLACK)], game.get_branches())
        game.play(17, 4)

        self.assertEqual([sente.Move(14, 3, sente.stone.WHITE), sente.Move(14, 2, sente.stone.WHITE)],
                         game.get_branches())

    def test_load_comments(self):
        """

        tests to see if the code loads the comments for the file

        :return:
        """

        game = sgf.load("sgf/34839594-255-IDW64-noob_bot_3.sgf")

        self.assertEqual(game.comment, "noob_bot_3: Hi! This is bot. Join 'noob_bot' group and have fun! Undo will be accepted. You can send undo message if you need.\n")
        self.assertIn("noob_bot_3: Hi! This is bot. Join 'noob_bot' group and have fun! Undo will be accepted. You can send undo message if you need.", str(game))

        game.play_default_sequence()

        self.assertEqual(game.comment, "noob_bot_3: Thanks for playing. If you want a weaker/stronger bot match with you, recommend try to play with 'ELOtest'. It can calculate & match your rank after few games.\nnoob_bot_3: Final score: W+368.5 (upper bound: 368.5, lower: 368.5)\n")


class InvalidSGF(TestCase):

    def test_all_invalid_sgf(self):
        """

        tests to see if all of the files in the invalid SGF directory raise exceptions

        :return:
        """

        files = os.listdir("invalid sgf")

        for file in files:
            with self.assertRaises(sente.exceptions.InvalidSGFException):
                game = sgf.load(str(Path("invalid sgf")/file))

    def test_invalid_moves(self):
        """

        tests to see if moves that have invalid formatting throw an exception

        :return:
        """

        with self.assertRaises(sente.exceptions.InvalidSGFException):
            sgf.load("invalid sgf/extra letter in move.sgf")
        with self.assertRaises(sente.exceptions.InvalidSGFException):
            sgf.load("invalid sgf/extra square bracket.sgf")
        with self.assertRaises(sente.exceptions.InvalidSGFException):
            sgf.load("invalid sgf/missing letter in move.sgf")
        with self.assertRaises(sente.exceptions.InvalidSGFException):
            sgf.load("invalid sgf/missing square bracket.sgf")


    def test_incorrect_parentheses(self):
        """

        tests to see if the

        :return:
        """

        with self.assertRaises(sente.exceptions.InvalidSGFException):
            sgf.load("invalid sgf/branched missing 2 parens.sgf")

    def test_nonexistent_file(self):
        """

        tests to see if if we raises a fileNotFound Exception

        :return:
        """

        with self.assertRaises(FileNotFoundError):
            sgf.load("invalid sgf/potato.sgf")

    def test_non_sgf_file(self):
        """

        tests to see if an exception is thrown with a non SGF file

        :return:
        """

        with self.assertRaises(sente.exceptions.InvalidSGFException):
            sgf.load("invalid sgf/module.cpp")

    def test_binary_file(self):
        """

        tests to see if an exception is thrown with a binary file

        :return:
        """

        with self.assertRaises(sente.exceptions.InvalidSGFException):
            # raise sente.exceptions.InvalidSGFException()
            sgf.load("invalid sgf/octopus.jpeg")

    def test_non_go_file(self):
        """

        tests to see if a non go file raises an exception

        :return:
        """

        with self.assertRaises(sente.exceptions.InvalidSGFException):
            sgf.load("invalid sgf/backgammon.sgf")


class InvalidSGFWarnings(TestCase):

    def test_all_SGF_warnings(self):
        """

        tests to make sure that all of the files in the "SGF warnings" directory create warnings

        :return:
        """

        files = os.listdir("warning sgf")

        for file in files:
            with self.assertWarns(Warning):
                sgf.load(str(Path("warning sgf")/file))

    def test_silence_warnings(self):
        """

        makes sure that warnings can be silenced using the disable_warnings option

        :return:
        """

        files = os.listdir("warning sgf")

        for file in files:
            sgf.load(str(Path("warning sgf")/file), disable_warnings=True)

    def test_unsupported_file_formats(self):
        """

        tests to see if the program correclty identifies that an incorrect file format has been used

        :return:
        """

        with self.assertWarns(Warning):
            sgf.load("warning sgf/FF[1] with FF.sgf")
        with self.assertWarns(Warning):
            sgf.load("warning sgf/FF[2] with RU.sgf")

    def test_change_ff(self):
        """

        tests to see if sente successfully switches a file to a new format

        :return:
        """

        with self.assertWarns(Warning):
            sgf.load("warning sgf/LeeSedol-WangYao34615.sgf")

    def test_turn_off_fix_file_format(self):
        """

        tests to see if turning off the "fix file format" option causes stuff to error out

        :return:
        """

        with self.assertRaises(sente.exceptions.InvalidSGFException):
            sgf.load("warning sgf/FF[1] with FF.sgf", fix_file_format=False)
        with self.assertRaises(sente.exceptions.InvalidSGFException):
            sgf.load("warning sgf/FF[2] with RU.sgf", fix_file_format=False)
        with self.assertRaises(sente.exceptions.InvalidSGFException):
            sgf.load("warning sgf/LeeSedol-WangYao34615.sgf", fix_file_format=False)

    def test_turn_off_ignore_illegal_properties(self):
        """

        tests to see if turning off the "ignore invalid properties" option causes stuff to error out

        :return:
        """

        with self.assertRaises(sente.exceptions.InvalidSGFException):
            sgf.load("warning sgf/Jappanese Date (JD) property.sgf", ignore_illegal_properties=False)
        with self.assertRaises(sente.exceptions.InvalidSGFException):
            sgf.load("warning sgf/ParkJaegeun-LeeJihyun72148.sgf", ignore_illegal_properties=False)
