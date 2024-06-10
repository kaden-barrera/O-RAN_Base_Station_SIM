module.exports = {
    jwtSecret: process.env.JWT_SECRET || 'your_jwt_secret_key',
    apiGatewayPort: process.env.API_GATEWAY_PORT || 8080
};
