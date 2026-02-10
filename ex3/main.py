from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


def main():
    print("\n=== DataDeck Game Engine ===\n")
    print("Configuring Fantasy Card Game...")

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    engine = GameEngine()

    engine.configure_engine(factory, strategy)

    engine.cards_created = 3
    engine.total_damage = 8

    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {strategy.get_strategy_name()}")
    print(f"Available types: {factory.get_supported_types()}")

    print("\nSimulating aggressive turn...")

    dragon = factory.create_creature("dragon")
    goblin = factory.create_creature("goblin")
    bolt = factory.create_spell("lightning")

    hand = [dragon, goblin, bolt]

    hand_str = ", ".join([f"{c.name} ({c.cost})" for c in hand])
    print(f"Hand: [{hand_str}]")

    print("\nTurn execution:")
    print(f"Strategy: {strategy.get_strategy_name()}")

    actions = strategy.execute_turn(hand, [])
    print(f"Actions: {actions}")

    engine.simulate_turn()

    print("\nGame Report:")
    print(engine.get_engine_status())

    print("\nAbstract Factory + Strategy Pattern: "
          "Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
