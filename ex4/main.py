from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main():
    print("\n=== DataDeck Tournament Platform ===")

    platform = TournamentPlatform()

    print("\nRegistering Tournament Cards...\n")

    dragon = TournamentCard("Fire Dragon", 5, "Legendary", 7, 5, 1200)
    d_id = platform.register_card(dragon)

    print(f"{dragon.name} (ID: {d_id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {dragon.rating}")
    print(f"- Record: {dragon.wins}-{dragon.losses}")

    wizard = TournamentCard("Ice Wizard", 4, "Rare", 3, 4, 1150)
    w_id = platform.register_card(wizard)

    print(f"\n{wizard.name} (ID: {w_id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {wizard.rating}")
    print(f"- Record: {wizard.wins}-{wizard.losses}")

    print("\nCreating tournament match...")
    match_res = platform.create_match(d_id, w_id)
    print(f"Match result: {match_res}")

    print("\nTournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    for entry in leaderboard:
        print(entry)

    print("\nPlatform Report:")
    print(platform.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
