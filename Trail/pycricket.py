import requests

url = "https://cricbuzz-cricket.p.rapidapi.com/teams/v1/2/players"

headers = {
	"x-rapidapi-key": "b4e8d996eemsh208da09d16f6673p142a98jsn79353c00a7c1",
	"x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.get(url, headers=headers)

print(response.json())

pip install requests

import requests

url = "https://cricbuzz-cricket.p.rapidapi.com/teams/v1/2/players"

headers = {
	"x-rapidapi-key": "b4e8d996eemsh208da09d16f6673p142a98jsn79353c00a7c1",
	"x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.get(url, headers=headers)

print(response.json())
pl=response.json()
pl
import json
import pandas as pd

with open("pl.json", "r") as file:
    data = json.load(file)

df = pd.json_normalize(data["player"])

print(df)
import pandas as pd

df = pd.read_json("pl.json")

df = pd.DataFrame(df["player"].tolist())

print(df)
import pandas as pd

players = pl['player']

result = []
category = None

for player in players:

    if 'id' not in player:
        category = player['name']

    elif category == 'BATSMEN':
        result.append({
            'player_id': player['id'],
            'player_name': player['name']
        })

df = pd.DataFrame(result)

print(df)

import requests

url = "https://cricbuzz-cricket.p.rapidapi.com/stats/v1/topstats/0"

querystring = {"statsType":"mostRuns","matchType":"1"}

headers = {
	"x-rapidapi-key": "b4e8d996eemsh208da09d16f6673p142a98jsn79353c00a7c1",
	"x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
test_most_runs=response.json()
test_most_runs

# Top 10 highest run scorers
stats_df = pd.DataFrame([test_most_runs])
column_names = stats_df.at[0, "headers"]
player_rows = stats_df.at[0, "values"]

most_runs_df = pd.DataFrame(
    [row["values"][1:] for row in player_rows],
    columns=column_names
)
most_runs_df["R"] = pd.to_numeric(most_runs_df["R"])
most_runs_df.sort_values("R", ascending=False).head(10)
# Find Tendulkar's player ID
stats_df = pd.DataFrame([test_most_runs])
column_names = ["player_id"] + stats_df.at[0, "headers"]
player_rows = stats_df.at[0, "values"]

players_df = pd.DataFrame(
    [row["values"] for row in player_rows],
    columns=column_names
)
players_df[players_df["Batter"].str.contains("Tendulkar", case=False, na=False)]
print(test_most_runs.keys())
print(test_most_runs["filter"])
filter=test_most_runs["filter"]
filter

print(test_most_runs["headers"])
print(test_most_runs["values"])
print(test_most_runs[])
import requests

url = "https://cricbuzz-cricket.p.rapidapi.com/teams/v1/2/players"

headers = {
	"x-rapidapi-key": "b4e8d996eemsh208da09d16f6673p142a98jsn79353c00a7c1",
	"x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.get(url, headers=headers)
indian_players_response = response.json()
indian_players_response

print(indian_players)
indian_players
indian_players = []
current_role = None

for player in indian_players_response["player"]:
    if "id" not in player:
        current_role = player["name"]
        continue

    indian_players.append({
        "id": player["id"],
        "name": player["name"],
        "role": current_role
    })

indian_players
indian_players = []
current_role = None

for player in indian_players_response["player"]:
    if "id" not in player:
        current_role = player["name"]
        continue

    indian_players.append({
        "id": player["id"],
        "name": player["name"],
        "role": current_role
    })

indian_players
indian_players
for player in indian_players_response["player"]:
    print(player)
import pandas as pd

df = pd.DataFrame(indian_players_response["player"])

print(df)
df = df.drop_duplicates()
print(df)
print(df["id"].duplicated().sum())
df.drop_duplicates(subset="id")
df.columns
df.dropna()
import requests

url = "https://cricbuzz-cricket.p.rapidapi.com/venues/v1/45/matches"

headers = {
	"x-rapidapi-key": "b4e8d996eemsh208da09d16f6673p142a98jsn79353c00a7c1",
	"x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.get(url, headers=headers)

print(response.json())
matches_data=response.json()
matches_data
import pandas as pd

matches = []

for item in matches_data["matchDetails"]:

    if "matchDetailsMap" in item:

        for match in item["matchDetailsMap"]["match"]:

            info = match["matchInfo"]

            matches.append({
                "matchDescription": info["matchDesc"],
                "team1": info["team1"]["teamName"],
                "team2": info["team2"]["teamName"],
                "venue": info["venueInfo"]["ground"],
                "city": info["venueInfo"]["city"],
                "matchDate": info["startDate"]
            })

df = pd.DataFrame(matches)

df["matchDate"] = pd.to_datetime(
    df["matchDate"],
    unit="ms"
)

df = df.sort_values(
    "matchDate",
    ascending=False
)

print(df)
df.dropna
df=df.dataframe
print(df)
import requests

url = "https://cricbuzz-cricket.p.rapidapi.com/series/v1/3641"

headers = {
	"x-rapidapi-key": "b4e8d996eemsh208da09d16f6673p142a98jsn79353c00a7c1",
	"x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.get(url, headers=headers)

print(response.json())
matches_details=response.json()
df.columns
match_rows = []

for item in matches_details.get("matchDetails", []):
    match_map = item.get("matchDetailsMap", {})

    for match in match_map.get("match", []):
        match_info = match.get("matchInfo", {})
        team1 = match_info.get("team1", {})
        team2 = match_info.get("team2", {})
        venue = match_info.get("venueInfo", {})

        match_rows.append({
            "match_id": match_info.get("matchId"),
            "description": match_info.get("matchDesc"),
            "team1": team1.get("teamName"),
            "team2": team2.get("teamName"),
            "venue": venue.get("ground"),
            "city": venue.get("city"),
            "status": match_info.get("status"),
            "start_date": match_info.get("startDate")
        })

matches_df = pd.DataFrame(match_rows)

if not matches_df.empty:
    matches_df["start_date"] = pd.to_datetime(
        pd.to_numeric(matches_df["start_date"], errors="coerce"),
        unit="ms"
    )

matches_df
pd.DataFrame([matches_details])
df=matches_df.drop_duplicates(subset="match_id", keep="last")
df=matches_df.drop_duplicates(subset="match_id", keep="last")
df=df.dropna()
df.head
df.columns
df
import requests
import pandas as pd
 "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/recent
url ="
headers = {
	"x-rapidapi-key": "b4e8d996eemsh208da09d16f6673p142a98jsn79353c00a7c1",
	"x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.get(url, headers=headers)
recent_matches_data = response.json()

match_rows = []
for match_type in recent_matches_data.get("typeMatches", []):
    for series in match_type.get("seriesMatches", []):
        series_wrapper = series.get("seriesAdWrapper", {})

        for match in series_wrapper.get("matches", []):
            match_info = match.get("matchInfo", {})
            team1 = match_info.get("team1", {})
            team2 = match_info.get("team2", {})
            venue = match_info.get("venueInfo", {})

            match_rows.append({
                "description": match_info.get("matchDesc"),
                "team1": team1.get("teamName"),
                "team2": team2.get("teamName"),
                "venue": venue.get("ground"),
                "city": venue.get("city"),
                "match_date": match_info.get("startDate")
            })

recent_matches_df = pd.DataFrame(match_rows)
recent_matches_df["match_date"] = pd.to_datetime(
    pd.to_numeric(recent_matches_df["match_date"], errors="coerce"),
    unit="ms"
)

cutoff_date = pd.Timestamp.now() - pd.Timedelta(days=7)
recent_matches_df = recent_matches_df[
    recent_matches_df["match_date"] >= cutoff_date
].sort_values("match_date", ascending=False).reset_index(drop=True)

recent_matches_df
df.head(10)
df.sort_values("start_date", ascending=False).head(10)
recent_matches_df
df.tail(10)
recent_matches_df.sort_values(
    "match_date",
    ascending=False
).head(40)
import requests

url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/live"

headers = {
	"x-rapidapi-key": "b4e8d996eemsh208da09d16f6673p142a98jsn79353c00a7c1",
	"x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.get(url, headers=headers)

print(response.json())
International_matches=response.json()
International_matches
import requests

url = "https://cricbuzz-cricket.p.rapidapi.com/mcenter/v1/41881/overs"

querystring = {"iid":"1"}

headers = {
	"x-rapidapi-key": "b4e8d996eemsh208da09d16f6673p142a98jsn79353c00a7c1",
	"x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
Top_scorer=response.json()
Top_scorer
import pandas as pd

pd.Series(Top_scorer['miniscore']).index
import requests
import pandas as pd

url = "https://cricbuzz-cricket.p.rapidapi.com/stats/v1/topstats/0"
querystring = {"statsType": "mostRuns", "matchType": "2"}
headers = {
	"x-rapidapi-key": "b4e8d996eemsh208da09d16f6673p142a98jsn79353c00a7c1",
	"x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.get(url, headers=headers, params=querystring)
odi_most_runs = response.json()
odi_most_runs
import requests

url = "https://cricbuzz-cricket.p.rapidapi.com/series/v1/international"

headers = {
	"x-rapidapi-key": "b4e8d996eemsh208da09d16f6673p142a98jsn79353c00a7c1",
	"x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.get(url, headers=headers)

print(response.json())
Top_scorer=response.json()
import requests

url = "https://cricbuzz-cricket.p.rapidapi.com/stats/v1/topstats/0"

querystring = {"statsType":"mostRuns","matchType":"2"}

headers = {
	"x-rapidapi-key": "b4e8d996eemsh208da09d16f6673p142a98jsn79353c00a7c1",
	"x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
odi_match=response.json()
odi_match

import pandas as pd

df = pd.DataFrame(
    [x['values'] for x in odi_match['values']],
    columns=['id', 'Batter', 'M', 'I', 'R', 'SR']
)
print(df)


df.dtypes
df=df.apply(pd.to_numeric, errors='ignore')
print(df.dtypes)
df.head(20)
df.reset_index(drop=True)
top_20 = df.nlargest(20, 'R')
print(top_20)
df.index = range(1, len(df) + 1)
temp=30
if temp > 25:
    print("It's hot outside!")
    temp-=10
if temp < 20:
    print("still hot outside!")
else:
    print("cooled down!")
