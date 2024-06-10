exports.manageMobility = async (req, res, next) => {
    try {
        const response = await axios.post('http://distributed-unit:5000/manage_mobility', req.body);
        res.status(200).json(response.data);
    } catch (error) {
        next(error);
    }
};
