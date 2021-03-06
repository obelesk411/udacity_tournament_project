#!/usr/bin/env python
#
# Test cases for tournament.py

from tournament import *


def test_delete_tournaments():
    """Test case for deleting tournaments"""
    delete_tournaments()
    print "2. Tournaments can be deleted."


def test_delete_matches():
    """Test case for deleting matches"""
    delete_matches()
    print "3. Old matches can be deleted."


def test_delete():
    """Test case for deleting player and match records """
    delete_matches()
    delete_players()
    print "4. Player records can be deleted."


def test_count():
    """Test case for counting players and matches """
    delete_matches()
    delete_players()
    c = count_players()
    if c == '0':
        raise TypeError(
            "count_players() should return numeric zero, not string '0'.")
    if c != 0:
        raise ValueError("After deleting, count_players should return zero.")
    print "5. After deleting, count_players() returns zero."


def test_register_tournament():
    """Test case for registering tournaments """
    register_tournament("topcoder")
    c = count_tournaments()
    if c != 1:
        raise ValueError(
            "After one tournament registers, count_tournaments() should be 1.")
    print "1. After registering a tournament, count_tournaments() returns 1."

def test_register():
    """Test case for registering players """
    delete_matches()
    delete_players()
    register_player("Chandra Nalaar")
    c = count_players()
    if c != 1:
        raise ValueError(
            "After one player registers, count_players() should be 1.")
    print "6. After registering a player, count_players() returns 1."


def test_register_count_delete():
    """Test case for registering and deleting players """
    delete_matches()
    delete_players()
    register_player("Markov Chaney")
    register_player("Joe Malik")
    register_player("Mao Tsu-hsi")
    register_player("Atlanta Hope")
    c = count_players()
    if c != 4:
        raise ValueError(
            "After registering four players, delete_players should be 4.")
    delete_players()
    c = delete_players()
    if c != 0:
        raise ValueError("After deleting, delete_players should return zero.")
    print "7. Players can be registered and deleted."


def test_standings_before_matches():
    """Test case for player standings before matches """
    delete_matches()
    delete_players()
    register_player("Melpomene Murray")
    register_player("Randy Schwartz")
    standings = player_standings()
    if len(standings) < 2:
        raise ValueError("Players should appear in player_standings even "
                         "before they have played any matches.")
    elif len(standings) > 2:
        raise ValueError("Only registered players should appear in standings.")
    if len(standings[0]) != 4:
        raise ValueError("Each player_standings row should have four columns.")
    [(id1, name1, wins1, matches1), (id2, name2, wins2, matches2)] = standings
    if matches1 != 0 or matches2 != 0 or wins1 != 0 or wins2 != 0:
        raise ValueError(
            "Newly registered players should have no matches or wins.")
    if set([name1, name2]) != set(["Melpomene Murray", "Randy Schwartz"]):
        raise ValueError("Registered players' names should appear in "
                         "standings, even if they have no matches played.")
    print "8. Newly registered players appear in the standings with no matches."


def test_report_matches():
    """Test case for reporting matches """
    delete_matches()
    delete_players()
    register_player("Bruno Walton")
    register_player("Boots O'Neal")
    register_player("Cathy Burton")
    register_player("Diane Grant")
    standings = player_standings()
    [id1, id2, id3, id4] = [row[0] for row in standings]
    report_match(0,id1, id2)
    report_match(0,id3, id4)
    standings = player_standings()
    for (i, n, w, m) in standings:
        if m != 1:
            raise ValueError("Each player should have one match recorded.")
        if i in (id1, id3) and w != 1:
            raise ValueError("Each match winner should have one win recorded.")
        elif i in (id2, id4) and w != 0:
            raise ValueError("Each match loser should have zero wins recorded.")
    print "9. After a match, players have updated standings."


def test_pairings():
    """Test case for player pairings """
    delete_matches()
    delete_players()
    register_player("Twilight Sparkle")
    register_player("Fluttershy")
    register_player("Applejack")
    register_player("Pinkie Pie")
    standings = player_standings()
    [id1, id2, id3, id4] = [row[0] for row in standings]
    report_match(0,id1, id2)
    report_match(0,id3, id4)
    pairings = swiss_pairings()
    if len(pairings) != 2:
        raise ValueError(
            "For four players, swissPairings should return two pairs.")
    [(pid1, pname1, pid2, pname2), (pid3, pname3, pid4, pname4)] = pairings
    correct_pairs = set([frozenset([id1, id3]), frozenset([id2, id4])])
    actual_pairs = set([frozenset([pid1, pid2]), frozenset([pid3, pid4])])
    if correct_pairs != actual_pairs:
        raise ValueError(
            "After one match, players with one win should be paired.")
    print "10. After one match, players with one win are paired."


if __name__ == '__main__':
    test_register_tournament()
    test_delete_tournaments()
    test_delete_matches()
    test_delete()
    test_count()
    test_register()
    test_register_count_delete()
    test_standings_before_matches()
    test_report_matches()
    test_pairings()

    print "Success!  All tests pass!"


