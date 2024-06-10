const express = require('express');
const connectionController = require('../controllers/connectionController');
const mobilityController = require('../controllers/mobilityController');

const router = express.Router();

router.post('/setup_connection', connectionController.setupConnection);
router.post('/manage_mobility', mobilityController.manageMobility);

module.exports = router;
