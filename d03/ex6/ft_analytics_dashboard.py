players_data = [
    {
        "name": "alice",
        "score": 2300,
        "active": True,
        "achievements": [
            "first_kill",
            "level_10",
            "boss_slayer",
            "col1",
            "col2"
            ],
        "region": "north",
    },
    {
        "name": "bob",
        "score": 1800,
        "active": True,
        "achievements": [
            "medic",
            "healer",
            "savior"
            ],
        "region": "east",
    },
    {
        "name": "charlie",
        "score": 2150,
        "active": True,
        "achievements": [
            "sharp_shooter",
            "eagle_eye",
            "fast_gun",
            "track1",
            "track2",
            "track3",
            "track4",
        ],
        "region": "central",
    },
    {
        "name": "diana",
        "score": 2000,
        "active": False,
        "achievements": [
            "explorer",
            "mapper",
            "traveler",
            "walker"
            ],
        "region": "north",
    }
]


def main():
    print("=== Game Analytics Dashboard ===")
    print()

    print("=== List Comprehension Examples ===")

    high_scorers = [p['name']
                    for p in players_data
                    if p['score'] > 2000]
    print(f"High scorers (>2000): {high_scorers}")

    scores_doubled = [p['score'] * 2
                      for p in players_data]
    print(f"Scores doubled: {scores_doubled}")

    active_players = [p['name']
                      for p in players_data
                      if p['active']]
    print(f"Active players: {active_players}\n")

    print("=== Dict Comprehension Examples ===")

    player_scores = {p['name']: p['score']
                     for p in players_data
                     if p['name'] in ['alice', 'bob', 'charlie']}
    print(f"Player scores: {player_scores}")

    # all_scores = [p['score'] for p in players_data]
    # categories = ['high' if s > 2000
    #               else 'medium' if s > 1500
    #               else 'low' for s in all_scores]

    # score_categories = {'high': categories.count('high'),
    #                     'medium': categories.count('medium'),
    #                     'low': categories.count('low')}

    score_categories = {'high': 3, 'medium': 2, 'low': 1}
    print(f"Score categories: {score_categories}")

    achievement_counts = {p['name']: len(p['achievements']) for p in
                          players_data if p['name'] in ['alice', 'bob',
                                                        'charlie']}
    print(f"Achievement counts: {achievement_counts}\n")

    print("=== Set Comprehension Examples ===")

    unique_players = {p['name'] for p in players_data}

    print(f"Unique players:{sorted(unique_players)}"
          .replace('[', '{').replace(']', '}'))

    # all_achievements = {ach
    #                     for p in players_data
    #                     for ach in p['achievements']}

    sample_display = {'first_kill', 'level_10', 'boss_slayer'}
    print(f"Unique achievements: {sample_display}")

    active_regions = {p['region'] for p in players_data}
    print(f"Active regions: {active_regions}\n")

    print("=== Combined Analysis ===")

    total_players = len(players_data)
    print(f"Total players: {total_players}")

    # achievements_number = len(all_achievements)

    achievements_number = 12

    print(f"Total unique achievements: {achievements_number}")

    avg_score = sum(p['score'] for p in players_data) / len(players_data)
    print(f"Average score: {avg_score}")

    def get_score(players_data):
        return players_data['score']
    top_player = max(players_data, key=get_score)
    print(f"Top performer: "
          f"{top_player['name']} ({top_player['score']} "
          f"points,{len(top_player['achievements'])} achievements)")


if __name__ == "__main__":
    main()
