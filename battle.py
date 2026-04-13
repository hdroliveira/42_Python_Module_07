import sys
from ex0 import CreatureFactory, FlameFactory, AquaFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    try:
        base = factory.create_base()
        print(base.describe())
        print(base.attack())

        evolved = factory.create_evolved()
        print(evolved.describe())
        print(evolved.attack())
    except Exception as e:
        print(f"Error testing factory: {e}", file=sys.stderr)


def battle(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    print("\nTesting battle")
    try:
        fighter1 = factory1.create_base()
        fighter2 = factory2.create_base()
        print(f"{fighter1.describe()}\n vs.\n{fighter2.describe()}")
        print(" fight!")
        print(fighter1.attack())
        print(fighter2.attack())
    except Exception as e:
        print(f"Error during battle: {e}", file=sys.stderr)


def main() -> None:
    try:
        flame_factory = FlameFactory()
        aqua_factory = AquaFactory()

        test_factory(flame_factory)
        test_factory(aqua_factory)

        battle(flame_factory, aqua_factory)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
