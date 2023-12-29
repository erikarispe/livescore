# livescore
Get live sport scores


using python

Need an API that will provide the live scores for certain sports

This will print out in the console of what is currenlty going on


#this is the url that is used to retreive the scores 
url = "https://livescore6.p.rapidapi.com/matches/v2/list-live"
#this is the caterogy of the sport that is being pulled. Time zone is set based on your preference
querystring = {"Category":"hockey","Timezone":"-7"}
# headers that are required are the key you gained from subscribing and the host
headers = {
	"X-RapidAPI-Key": "e3c5095309mshff95e53cb5aa311p13a46ejsn4a73799a7ede",
	"X-RapidAPI-Host": "livescore6.p.rapidapi.com"
}

#this will use the requests library , getting the necessary parameters to be able to grab the live scores
response = requests.get(url, headers=headers, params=querystring)

#you will then be able to print out the response in json format.
print(response.json())
