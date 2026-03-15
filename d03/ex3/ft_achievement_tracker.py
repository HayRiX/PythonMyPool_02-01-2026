data = {
  "alice": [
      'first_kill',
      'level_10',
      'treasure_hunter',
      'speed_demon'
      ],
  "bob": [
      'first_kill',
      'level_10',
      'boss_slayer',
      'collector'
      ],
  "charlie": [
      'level_10',
      'treasure_hunter',
      'boss_slayer',
      'speed_demon',
      'perfectionist'
      ],
}


alice = set(data['alice'])
bob = set(data['bob'])
charlie = set(data['charlie'])

# ti7ad "player | player" or "set.union()"
all_achievements = alice.union(bob, charlie)

# ta9atto3 "player & player" or "set.intersection()"
common = alice.intersection(bob, charlie)

alice_unique = alice.difference(bob.union(charlie))
bob_unique = bob.difference(alice.union(charlie))
charlie_unique = charlie.difference(alice.union(bob))

# tamayuz
rare_achievements = alice_unique.union(bob_unique, charlie_unique)

aliceB_unique = alice.difference(bob)
bobA_unique = bob.difference(alice)

print("=== Achievement Tracker System ===")
print(f"\nPlayer alice achievements: {set(data['alice'])}")
print(f"Player bob achievements: {set(data['bob'])}")
print(f"Player charlie achievements: {set(data['charlie'])}\n")

print("=== Achievement Analytics ===")
print(f"All unique achievements: {all_achievements}")
print(f"Total unique achievements: {len(all_achievements)}\n")

print(f"Common to all players: {common}")
print(f"Rare achievements (1 player): {rare_achievements}\n")

print(f"Alice vs Bob common: "
      f"{set(data['alice']).intersection(set(data['bob']))}")
print(f"Alice unique: {aliceB_unique}")
print(f"Bob unique: {bobA_unique}")
