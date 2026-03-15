import sys

print("=== Player Score Analytics ===")

if len(sys.argv) == 1:
    print(f"No scores provided. Usage: python3 {sys.argv[0]} <score1> <score2>"
          f" ...")

elif len(sys.argv) > 1:
    score_list = []
    for received in sys.argv[1:]:
        try:
            score_list.append(int(received))
        except ValueError:
            pass
    if not score_list:
        print("No valid scores found to process.")
    else:
        players = len(score_list)
        total_score = sum(score_list)
        max_score = max(score_list)
        min_score = min(score_list)
        average = total_score / players
        score_ringe = max_score - min_score

        print(f"Scores processed: {score_list}")
        print(f"Total players: {players}")
        print(f"Total score: {total_score}")
        print(f"Average score: {average}")
        print(f"High score: {max_score}")
        print(f"Low score: {min_score}")
        print(f"Score range: {score_ringe}")
