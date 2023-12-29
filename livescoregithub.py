import requests

url = "https://livescore6.p.rapidapi.com/matches/v2/list-live"

querystring = {"Category":"hockey","Timezone":"-7"}

headers = {
	"X-RapidAPI-Key": "e3c5095309mshff95e53cb5aa311p13a46ejsn4a73799a7ede",
	"X-RapidAPI-Host": "livescore6.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())