from weapons import Weapon, Sword, Hammer 
import pytest
import pygame

def test_weapon():
    stat = {"range": 10}
    sword = Sword(stat, 0)
    hammer = Hammer(stat, 0)

    print("\nGet attack area:")
    area = sword.get_attack_area((100, 100))
    print(area)
    assert area == pygame.Rect(100, 110, 10, 20)

    area = hammer.get_attack_area((100, 100))
    print(area)
    area == [pygame.Rect(100, 110, 5, 20), pygame.Rect(105, 110, 5, 20)]
