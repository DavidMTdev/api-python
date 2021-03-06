from flask import Flask, render_template, url_for, jsonify
import requests


app = Flask(__name__)

headers = {
    'x-rapidapi-host': "api-nba-v1.p.rapidapi.com",
    'x-rapidapi-key': "2192cfd498msh57e0635f835ae9ep1136b6jsnc62e3942f5b4"
}


@app.route('/')
def index():
    url = "https://api-nba-v1.p.rapidapi.com/teams/league/standard"

    response = requests.request("GET", url, headers=headers)

    teams = response.json()['api']['teams']

    return render_template('index.html', teams=teams)


@app.route('/team/<int:id>')
def team(id):
    url = "https://api-nba-v1.p.rapidapi.com/players/teamId/" + str(id)
    teams = "https://api-nba-v1.p.rapidapi.com/teams/league/standard"


    response = requests.request("GET", url, headers=headers)
    responses = requests.request("GET", teams, headers=headers)

    players = response.json()['api']['players']
    teams = responses.json()['api']['teams']
    team = ""

    for value in teams: 
        if value['teamId'] == str(id):
            team = value

    return render_template('player.html', players=players, team=team)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
