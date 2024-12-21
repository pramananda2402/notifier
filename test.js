import axios from 'axios';

const options = {
  method: 'GET',
  url: 'https://google-news13.p.rapidapi.com/business',
  params: {lr: 'en-US'},
  headers: {
    'x-rapidapi-key': 'f2a2ec1628mshc0ca5f531f195c5p184100jsn5ebf23fcbcbd',
    'x-rapidapi-host': 'google-news13.p.rapidapi.com'
  }
};

try {
	const response = await axios.request(options);
	console.log(response.data);
} catch (error) {
	console.error(error);
}