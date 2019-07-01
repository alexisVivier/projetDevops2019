const express = require('express');
const app = express();
const automateRoute = require('./api/automate')
let cors = require('cors');

app.use(cors());

app.get('/', function (req, res) {
    res.send('Hello World!')
});

app.listen(4200, function () {
    console.log('Example app listening on port 3000!')
});

app.use('/automates', automateRoute)