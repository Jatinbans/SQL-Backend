from flask import Flask, jsonify, request
from sqlalchemy.exc import SQLAlchemyError
from models import db, Faq

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///faqs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Ensuring database tables are created
with app.app_context():
    db.create_all()

# Custom error handler for 404 and 500 errors
@app.errorhandler(404)
def resource_not_found(error):
    return jsonify({'error': 'Resource not found'}), 404

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({'error': 'Internal server error'}), 500

# Get all FAQs
@app.route('/faqs', methods=['GET'])
def get_faqs():
    try:
        faqs = Faq.query.all()
        if not faqs:
            return jsonify({'message': 'No FAQs available'}), 200
        return jsonify([faq.to_dict() for faq in faqs]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': 'Database error'}), 500

# Get a single FAQ by ID
@app.route('/faqs/<int:id>', methods=['GET'])
def get_faq(id):
    try:
        faq = Faq.query.get(id)
        if not faq:
            return jsonify({'error': 'FAQ not found'}), 404
        return faq.to_dict(), 200
    except SQLAlchemyError as e:
        return jsonify({'error': 'Database error'}), 500

# Create a new FAQ
@app.route('/faqs', methods=['POST'])
def create_faq():
    data = request.json
    if not data or 'question' not in data or 'answer' not in data:
        return jsonify({'error': 'Question and answer are required'}), 400
    
    try:
        new_faq = Faq(question=data['question'], answer=data['answer'])
        db.session.add(new_faq)
        db.session.commit()
        return new_faq.to_dict(), 201
    except SQLAlchemyError as e:
        return jsonify({'error': 'Database error'}), 500

# Update an existing FAQ by ID
@app.route('/faqs/<int:id>', methods=['PUT'])
def update_faq(id):
    try:
        faq = Faq.query.get(id)
        if not faq:
            return jsonify({'error': 'FAQ not found'}), 404

        data = request.json
        if not data or ('question' not in data and 'answer' not in data):
            return jsonify({'error': 'At least one field (question or answer) is required to update'}), 400
        
        faq.question = data.get('question', faq.question)
        faq.answer = data.get('answer', faq.answer)
        db.session.commit()
        return faq.to_dict(), 200
    except SQLAlchemyError as e:
        return jsonify({'error': 'Database error'}), 500

# Delete an FAQ by ID
@app.route('/faqs/<int:id>', methods=['DELETE'])
def delete_faq(id):
    try:
        faq = Faq.query.get(id)
        if not faq:
            return jsonify({'error': 'FAQ not found'}), 404
        
        db.session.delete(faq)
        db.session.commit()
        return jsonify({'message': 'FAQ deleted successfully'}), 200
    except SQLAlchemyError as e:
        return jsonify({'error': 'Database error'}), 500

# Global exception handler
@app.errorhandler(Exception)
def handle_unexpected_error(error):
    return jsonify({'error': str(error)}), 500

if __name__ == '__main__':
    app.run(debug=True)
