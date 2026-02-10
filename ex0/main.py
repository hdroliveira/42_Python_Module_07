from ex0.CreatureCard import CreatureCard


def main():
    print("\n=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")

    dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

    print("CreatureCard Info:")
    print(dragon.get_card_info())

    mana = 6
    print(f"\nPlaying {dragon.name} with {mana} mana available:")
    print(f"Playable: {dragon.is_playable(mana)}")

    game_state = {}
    print(f"Play result: {dragon.play(game_state)}")

    target = "Goblin Warrior"
    print(f"\n{dragon.name} attacks {target}:")
    print(f"Attack result: {dragon.attack_target(target)}")

    low_mana = 3
    print(f"\nTesting insufficient mana ({low_mana} available):")
    print(f"Playable: {dragon.is_playable(low_mana)}")

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
