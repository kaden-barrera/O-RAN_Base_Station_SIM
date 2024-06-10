const morgan = require('morgan');

const logger = morgan('combined');

module.exports = logger;
