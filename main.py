import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players: dict = json.load(file)

    for name, player in players.items():
        race, _ = Race.objects.get_or_create(
            name=player["race"]["name"],
            defaults={"description": player["race"]["description"]},
        )

        for skill in player["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                defaults={"bonus": skill["bonus"], "race": race}
            )

        guild_data = player.get("guild")
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data["description"]},
            )
        else:
            guild = None

        Player.objects.get_or_create(
            nickname=name,
            defaults={
                "email": player["email"],
                "bio": player["bio"],
                "race": race,
                "guild": guild,
            },
        )


if __name__ == "__main__":
    main()
