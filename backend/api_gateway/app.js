const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
app.use(bodyParser.json());
app.use(cors());

app.post('/api/setup_connection', (req, res) => {
    const data = req.body;
    // Add your setup connection logic here
    res.status(200).json({
        status: 'Connection setup successfully',
        data: data
    });
});

app.post('/api/manage_mobility', (req, res) => {
    const data = req.body;
    // Add your manage mobility logic here
    res.status(200).json({
        status: 'Mobility managed successfully',
        data: data
    });
});

const PORT = process.env.PORT || 8080;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
