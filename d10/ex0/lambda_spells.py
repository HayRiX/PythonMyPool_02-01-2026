artifacts = [{'name': 'Lightning Rod', 'power': 117, 'type': 'focus'},
             {'name': 'Lightning Rod', 'power': 116, 'type': 'armor'},
             {'name': 'Ice Wand', 'power': 88, 'type': 'focus'},
             {'name': 'Light Prism', 'power': 64, 'type': 'focus'}]

mages = [{'name': 'Casey', 'power': 91, 'element': 'earth'},
         {'name': 'Luna', 'power': 92, 'element': 'shadow'},
         {'name': 'Luna', 'power': 89, 'element': 'lightning'},
         {'name': 'Sage', 'power': 83, 'element': 'earth'},
         {'name': 'Zara', 'power': 77, 'element': 'wind'}]

spells = ['tornado', 'darkness', 'shield', 'flash']


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda item: item['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    if not mages:
        return {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}

    max_p = max(mages, key=lambda m: m['power'])['power']
    min_p = min(mages, key=lambda m: m['power'])['power']

    total_power = sum(map(lambda m: m['power'], mages))
    avg_p = round(total_power / len(mages), 2)

    return {
        'max_power': max_p,
        'min_power': min_p,
        'avg_power': avg_p
    }


def main() -> None:
    print("\nTesting artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    name1, power1 = sorted_artifacts[0]['name'], sorted_artifacts[0]['power']
    name2, power2 = sorted_artifacts[1]['name'], sorted_artifacts[1]['power']
    print(f"{name1} ({power1} power) comes before {name2} ({power2} power)")

    print("\nTesting spell transformer...")
    the_spells = spell_transformer(spells)
    print(" ".join(the_spells))


if __name__ == "__main__":
    main()
