def update_leaderboard(file_name, player_name, score):
    with open(file_name, 'a') as file:
        file.write(f'{player_name},{score}\n')

def show_leaderboard(file_name, top=10):
    with open(file_name, 'r') as file:
        scores = file.readlines()

    # Parse scores and sort in descending order
    scores = [line.strip().split(',') for line in scores]
    scores = [(name, int(score)) for name, score in scores]
    scores.sort(key=lambda x: x[1], reverse=True)

    return scores[:top]