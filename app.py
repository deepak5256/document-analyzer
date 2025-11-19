from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os
from dotenv import load_dotenv
import PyPDF2
import io

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure Gemini
api_key = os.getenv('GEMINI_API_KEY')
model_name = os.getenv('GEMINI_MODEL', 'gemini-2.0-flash-exp')

if not api_key:
    raise ValueError("Please set GEMINI_API_KEY in your environment variables")

genai.configure(api_key=api_key)

def extract_text_from_pdf(file):
    """Extract text from PDF file"""
    try:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
        return text
    except Exception as e:
        raise Exception(f"Error reading PDF: {str(e)}")

def analyze_document(text, analysis_type):
    """Analyze document using Gemini"""
    try:
        model = genai.GenerativeModel(model_name)
        
        prompts = {
            'summary': f"Please provide a concise summary of the following document:\n\n{text}",
            'key_points': f"Extract the main key points and important information from this document:\n\n{text}",
            'entities': f"Extract important entities (people, organizations, locations, dates) from this document:\n\n{text}",
            'custom': f"Analyze this document and provide insights:\n\n{text}"
        }
        
        prompt = prompts.get(analysis_type, prompts['custom'])
        
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error analyzing document: {str(e)}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file uploaded'}), 400
        
        file = request.files['file']
        analysis_type = request.form.get('analysis_type', 'summary')
        
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        # Check file size (10MB limit)
        file.seek(0, 2)  # Seek to end
        file_size = file.tell()
        file.seek(0)  # Reset seek position
        if file_size > 10 * 1024 * 1024:  # 10MB in bytes
            return jsonify({'error': 'File size too large. Maximum 10MB allowed.'}), 400
        
        # Extract text based on file type
        if file.filename.lower().endswith('.pdf'):
            text = extract_text_from_pdf(file)
        elif file.filename.lower().endswith('.txt'):
            text = file.read().decode('utf-8')
        else:
            return jsonify({'error': 'Unsupported file type. Please upload PDF or TXT files.'}), 400
        
        if not text.strip():
            return jsonify({'error': 'The document appears to be empty or could not be read.'}), 400
        
        # Analyze the document
        result = analyze_document(text, analysis_type)
        
        return jsonify({
            'success': True,
            'analysis': result,
            'text_preview': text[:500] + '...' if len(text) > 500 else text
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Add health check endpoint for Render
@app.route('/health')
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)