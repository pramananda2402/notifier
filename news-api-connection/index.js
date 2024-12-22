import express from "express";
const app = express();
const port = 3000;


const url = "https://newsapi.org/v2/everything?q=tesla&from=2024-11-21&sortBy=publishedAt&apiKey=bcc8ccd488a148b5bbb402e1011098e5"

await fetch(url).then(response => response.json()).then(data => console.log(data));

await fetch(url).then(response => response.json()).then(data => console.log(data));



app.use(express.json());

app.get("/",  (req, res) => {
    
    res.send({
        message: "news api in console"
    })
});



app.listen(port, () => {
    console.log(` App listening on http://localhost:${port}`);
});