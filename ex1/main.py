from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main():
    print("\n=== DataDeck Deck Builder ===\n")
    print("Building deck with different card types...")

    deck = Deck("Mixed Deck")

    bolt = SpellCard("Lightning Bolt", 3, "Common", "Deal 3 damage to target")

    crystal = ArtifactCard("Mana Crystal", 2, "Rare", 5,
                           "Permanent: +1 mana per turn")

    dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

    deck.add_card(bolt)
    deck.add_card(crystal)
    deck.add_card(dragon)

    print(f"Deck stats: {deck.get_deck_stats()}")

    print("\nDrawing and playing cards:")

    for _ in range(3):
        card = deck.draw_card()
        if card:
            c_type = card.get_card_info().get("type")
            print(f"\nDrew: {card.name} ({c_type})")
            print(f"Play result: {card.play({})}")

    print("\nPolymorphism in action: Same interface, "
          "different card behaviors!")


if __name__ == "__main__":
    main()
