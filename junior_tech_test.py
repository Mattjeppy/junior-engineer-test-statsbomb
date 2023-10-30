import csv


def read_csv_file(file):
    with open(file, newline="") as csvfile:
        return list(csv.DictReader(csvfile))


def get_unique_teams(data):
    teams = set()
    for row in data:
        if "team_name" in row:
            teams.add(row["team_name"])
    return teams


def get_most_common_event_type(data):
    events = {}

    for row in data:
        if "event_type_name" in row:
            event_type = row["event_type_name"]
            if event_type in events:
                events[event_type] += 1
            else:
                events[event_type] = 1

    most_common_event = max(events, key=events.get)
    return most_common_event


def filter_by_team(data, team_name):
    filtered = []

    for row in data:
        if "team_name" in row:
            if row["team_name"] == team_name:
                filtered.append(row)

    return filtered


def count_event_type_by_team(data, team_name, event_type_name):
    count = 0

    for row in data:
        if "team_name" in row:
            if (
                row["team_name"] == team_name
                and row["event_type_name"] == event_type_name
            ):
                count += 1

    return count


def average_pass_length_by_team(data, team_name):
    pass_lengths = []

    for row in data:
        if row["team_name"] == team_name:
            try:
                pass_length = float(row["pass_length"])
                pass_lengths.append(pass_length)
            except (ValueError, TypeError):
                pass

    average_length = round(sum(pass_lengths) / len(pass_lengths), 1)

    return average_length


def filter_players_by_position(data, position_name):
    players = set()

    for row in data:
        if row["player_position_name"] == position_name:
            players.add(row["player_name"])

    return players


def count_successful_passes(data):
    index = []
    successful_passes = 0

    for row in data:
        if row["event_type_name"] == "Pass":
            successful_passes += 1

    return successful_passes

# not sure why this one is failing - looking forward to feedback

def filter_by_period(data, period):
    events = []

    for row in data:
        if row["period"] == period:
            events.append(row)

    return events


def count_shots_by_player(data, player_name):
    shots = 0
    index = []

    for row in data:
        if row["player_name"] == player_name and row["event_type_name"] == "Shot":
            if row["index"] not in index:
                index.append(row["index"])
                shots += 1

    return shots
