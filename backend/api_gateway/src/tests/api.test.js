require('dotenv').config();
const request = require('supertest');
const jwt = require('jwt-simple');
const { app, server } = require('../app');
const mockAxios = require('axios');

const secret = process.env.JWT_SECRET || 'your_jwt_secret_key';
const token = jwt.encode({ user: 'testUser', role: 'admin', exp: Math.floor(Date.now() / 1000) + (60 * 60) }, secret);

describe('API Tests', () => {
    afterAll(() => {
        server.close();
    });

    it('should setup connection', async () => {
        mockAxios.post.mockResolvedValue({ data: { status: 'Connection setup successfully' } });

        const response = await request(app)
            .post('/api/setup_connection')
            .set('Authorization', `Bearer ${token}`)
            .send({ connection: 'test-connection' });

        expect(response.status).toBe(200);
        expect(response.body.status).toBe('Connection setup successfully');
    });

    it('should manage mobility', async () => {
        mockAxios.post.mockResolvedValue({ data: { status: 'Mobility managed successfully' } });

        const response = await request(app)
            .post('/api/manage_mobility')
            .set('Authorization', `Bearer ${token}`)
            .send({});

        expect(response.status).toBe(200);
        expect(response.body.status).toBe('Mobility managed successfully');
    });
});
