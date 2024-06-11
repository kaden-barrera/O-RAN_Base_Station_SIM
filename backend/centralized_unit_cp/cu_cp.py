from flask import Flask, request, jsonify
from flask_cors import CORS
from sqlalchemy.orm import Session
from database import engine, SessionLocal, Base
from models import Connection

app = Flask(__name__)
CORS(app)

Base.metadata.create_all(bind=engine)

@app.route('/setup_connection', methods=['POST'])
def setup_connection():
    session: Session = SessionLocal()
    try:
        data = request.json
        connection = Connection(name=data['connection'])
        session.add(connection)
        session.commit()
        session.refresh(connection)
        return jsonify({"status": "Connection setup successfully", "connection": connection.name})
    except Exception as e:
        session
