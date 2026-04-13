import sys
from ex1 import (
    HealingCreatureFactory,
    TransformCreatureFactory,
    HealCapability,
    TransformCapability
)


def test_healing_creature() -> None:
    print("Testing Creature with healing capability")
    try:
        factory = HealingCreatureFactory()

        print(" base:")
        base = factory.create_base()
        print(base.describe())
        print(base.attack())
        if isinstance(base, HealCapability):
            print(base.heal())

        print(" evolved:")
        evolved = factory.create_evolved()
        print(evolved.describe())
        print(evolved.attack())
        if isinstance(evolved, HealCapability):
            print(evolved.heal())

    except Exception as e:
        print(f"Error testing healing creatures: {e}", file=sys.stderr)


def test_transforming_creature() -> None:
    print("\nTesting Creature with transform capability")
    try:
        factory = TransformCreatureFactory()

        print(" base:")
        base = factory.create_base()
        print(base.describe())
        print(base.attack())
        if isinstance(base, TransformCapability):
            print(base.transform())
            print(base.attack())
            print(base.revert())

        print(" evolved:")
        evolved = factory.create_evolved()
        print(evolved.describe())
        print(evolved.attack())
        if isinstance(evolved, TransformCapability):
            print(evolved.transform())
            print(evolved.attack())
            print(evolved.revert())

    except Exception as e:
        print(f"Error testing transforming creatures: {e}", file=sys.stderr)


def main() -> None:
    test_healing_creature()
    test_transforming_creature()


if __name__ == "__main__":
    main()
