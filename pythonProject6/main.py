def input_scores(team_name):
    scores = []
    total_score = 0
    for quarter in range(1, 5):
        score = int(input(f"Enter score for {team_name} in Quarter {quarter}: "))
        total_score += score
        print(f"{team_name} total score after Quarter {quarter}: {total_score}")
        scores.append(score)
    return total_score, scores

def main():
    team_a_name = input("Enter name for Team A: ")
    team_b_name = input("Enter name for Team B: ")

    print(f"\nInput scores for {team_a_name}:")
    total_score_a, scores_a = input_scores(team_a_name)

    print(f"\nInput scores for {team_b_name}:")
    total_score_b, scores_b = input_scores(team_b_name)

    print("\nGame Results:")
    print(f"{team_a_name} total score: {total_score_a}")
    print(f"{team_b_name} total score: {total_score_b}")

    if total_score_a > total_score_b:
        print(f"{team_a_name} wins!")
    elif total_score_a < total_score_b:
        print(f"{team_b_name} wins!")
    else:
        print("The game is tied! Overtime starts...")

        # Play overtime until a team wins
        while True:
            overtime_score_a = int(input(f"Enter overtime score for {team_a_name}: "))
            total_score_a += overtime_score_a

            overtime_score_b = int(input(f"Enter overtime score for {team_b_name}: "))
            total_score_b += overtime_score_b

            print(f"{team_a_name} total score: {total_score_a}")
            print(f"{team_b_name} total score: {total_score_b}")

            if total_score_a > total_score_b:
                print(f"{team_a_name} wins in overtime!")
                break
            elif total_score_a < total_score_b:
                print(f"{team_b_name} wins in overtime!")
                break
            else:
                print("Overtime tied. Continue playing...")

if __name__ == "__main__":
    main()
