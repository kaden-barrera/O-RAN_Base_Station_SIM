const axios = require('axios');

exports.setupConnection = async (req, res, next) => {
    try {
        const { connection } = req.body;
        const response = await axios.post('http://distributed-unit:5000/setup_connection', { connection });
        res.status(200).json(response.data);
    } catch (error) {
        next(error);
    }
};
