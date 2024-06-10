const axios = require('axios');

exports.setupConnection = async (req, res, next) => {
    try {
        const { connection } = req.body;
        const response = await axios.post('http://localhost:5000/setup_connection', { connection }); // Use localhost for local testing
        res.status(200).json(response.data);
    } catch (error) {
        next(error);
    }
};
