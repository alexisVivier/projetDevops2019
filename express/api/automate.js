const express = require ('express');
const router  = express.Router();
const mysql   = require('mysql');
const cors = require('cors');
const app = express();

// app.use(cors());

let corsOption = {
    origin : 'http://localhost:8080'
} 

let connection = mysql.createConnection({
    host     : 'localhost',
    user     : 'root',
    password : 'root',
    database : 'devops',
    port: '8889'
});

connection.connect();

router.get("/get", cors(corsOption), (req, res)=> {
    console.log("Connected to database")
    let query = 'SELECT * FROM automate;'
    connection.query(query, (err, result, fields)=> {
        if (err) throw err;
        res.status(200).send(result)
    })
})

module.exports = router;