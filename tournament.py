import sys
from typing import List, Tuple
from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
    StrategyError
)

Opponent = Tuple[CreatureFactory, BattleStrategy]


def battle(opponents: List[Opponent]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            print("\n* Battle *")
            factory1, strategy1 = opponents[i]
            factory2, strategy2 = opponents[j]
            try:
                creature1 = factory1.create_base()
                creature2 = factory2.create_base()

                print(creature1.describe())
                print(" vs")
                print(creature2.describe())
                print(" now fight!")

                strategy1.act(creature1)
                strategy2.act(creature2)
            except StrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                return
            except Exception as e:
                print(f"Unexpected error: {e}", file=sys.stderr)
                return


def main() -> None:
    try:
        flame_factory = FlameFactory()
        aqua_factory = AquaFactory()
        healing_factory = HealingCreatureFactory()
        transform_factory = TransformCreatureFactory()

        normal_strat = NormalStrategy()
        aggro_strat = AggressiveStrategy()
        def_strat = DefensiveStrategy()

        print("Tournament 0 (basic)")
        print(" [ (Flameling+Normal), (Healing+Defensive) ]")
        battle([
            (flame_factory, normal_strat),
            (healing_factory, def_strat)
        ])

        print("\nTournament 1 (error)")
        print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
        battle([
            (flame_factory, aggro_strat),
            (healing_factory, def_strat)
        ])

        print("\nTournament 2 (multiple)")
        print(" [ (Aquabub+Normal), (Healing+Defensive), "
              "(Transform+Aggressive) ]")
        battle([
            (aqua_factory, normal_strat),
            (healing_factory, def_strat),
            (transform_factory, aggro_strat)
        ])

    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
