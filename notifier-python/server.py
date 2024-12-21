import requests

url = "https://newsapi.org/v2/everything?q=tesla&from=2024-11-21&sortBy=publishedAt&apiKey=bcc8ccd488a148b5bbb402e1011098e5"

querystring = {"lr":"en-US"}

headers = {
	"x-rapidapi-key": "f2a2ec1628mshc0ca5f531f195c5p184100jsn5ebf23fcbcbd",
	"x-rapidapi-host": "google-news13.p.rapidapi.com"
}

response = requests.get(url, params=querystring)

print(response.json())