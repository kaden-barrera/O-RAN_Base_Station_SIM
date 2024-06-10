const jwt = require('jwt-simple');
const secret = 'your_jwt_secret_key';

const payload = {
    user: 'testUser',
    role: 'admin',
    exp: Math.floor(Date.now() / 1000) + (60 * 60) // Token expires in 1 hour
};

const token = jwt.encode(payload, secret);
console.log(token);
