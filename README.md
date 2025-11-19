# Document Analyzer - Gemini AI

A Flask web application that uses Google Gemini AI to analyze various document types (PDF, Images, Word, PowerPoint, Text) and extract information with copy-to-clipboard functionality.

## Features

✅ **Multi-format Support**: Analyze PDFs, JPG, PNG, GIF, BMP, WebP, DOC, DOCX, PPT, PPTX, and TXT files
✅ **AI-Powered Analysis**: Uses Google Gemini API for intelligent document analysis
✅ **Copy Functionality**: Easily copy analysis results to clipboard
✅ **Drag & Drop Upload**: Simple and intuitive file upload interface
✅ **Beautiful UI**: Modern, responsive web interface
✅ **Large File Support**: Handles up to 50MB files

## Installation

### Prerequisites

- Python 3.8 or higher
- Google Gemini API Key

### Setup Steps

1. **Clone or download the project**
   ```
   cd "New folder"
   ```

2. **Create a virtual environment** (recommended)
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. **Install dependencies**
   ```powershell
   pip install -r requirements.txt
   ```

4. **Get your Gemini API Key**
   - Visit: https://makersuite.google.com/app/apikey
   - Create a new API key
   - Copy the key

5. **Set the API Key environment variable**
   
   **PowerShell:**
   ```powershell
   $env:GEMINI_API_KEY='your-api-key-here'
   ```
   
   **Command Prompt:**
   ```cmd
   set GEMINI_API_KEY=your-api-key-here
   ```
   
   **Or create a `.env` file** (optional):
   ```
   GEMINI_API_KEY=your-api-key-here
   ```
   
   Then load it before running:
   ```powershell
   Get-Content .env | ForEach-Object {
       $key, $value = $_ -split '=', 2
       [Environment]::SetEnvironmentVariable($key, $value)
   }
   ```

## Running the Application

1. **Activate virtual environment** (if using one)
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

2. **Set the API key** (if not already set)
   ```powershell
   $env:GEMINI_API_KEY='your-api-key-here'
   ```

3. **Run the application**
   ```powershell
   python app.py
   ```

4. **Open in browser**
   - Navigate to: `http://localhost:5000`

## How to Use

1. Open the application in your web browser
2. Click on the upload area or drag & drop a document
3. Select a file (PDF, Image, Word, PowerPoint, or Text file)
4. Click "Analyze Document" button
5. Wait for the AI to analyze your document
6. View the results and click "📋 Copy All" to copy the analysis to clipboard

## File Format Details

### Images (JPG, PNG, GIF, BMP, WebP)
- Analyzes image content, text within images, and visual elements
- Best for screenshots, diagrams, and photo documents

### PDF
- Converts first page to image and analyzes content
- Extracts text and information from the document

### Word Documents (DOCX)
- Extracts all text content
- Analyzes structure, paragraphs, and formatting

### PowerPoint (PPTX)
- Extracts text from all slides
- Provides slide-by-slide analysis

### Text Files (TXT)
- Reads plain text content
- Provides summary and key information

## API Limits

- **File Size**: Maximum 50MB per upload
- **Free Tier**: Check Gemini API documentation for rate limits
- **Processing Time**: Depends on file size and complexity

## Troubleshooting

### Error: "GEMINI_API_KEY environment variable not set"
- Make sure you've set the API key environment variable correctly
- Restart the application after setting the variable

### Error: "File type not allowed"
- Check that your file has the correct extension
- Supported formats: PDF, JPG, JPEG, PNG, GIF, BMP, WebP, DOC, DOCX, PPT, PPTX, TXT

### Error: "Unable to process PDF"
- Install pdf2image: `pip install pdf2image`
- On Windows, you may need: `pip install pdf2image pillow`

### Connection Error
- Make sure the Flask server is running
- Check that you're accessing `http://localhost:5000`
- Check firewall settings

### API Rate Limit Error
- Wait a few minutes before making another request
- Check your Gemini API quota at https://makersuite.google.com

## Project Structure

```
New folder/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── README.md          # This file
├── templates/
│   └── index.html     # Main HTML template
├── static/
│   ├── style.css      # Styling
│   └── script.js      # Frontend JavaScript
└── uploads/           # Temporary upload folder (auto-created)
```

## Security Notes

- Files are processed and immediately deleted after analysis
- No files are permanently stored on the server
- All communication with Gemini API is encrypted
- Uploaded files are not logged or tracked

## Requirements

- Flask 2.3.2
- google-generativeai 0.3.0
- Pillow 10.0.0
- python-docx 0.8.11
- python-pptx 0.6.21
- pdf2image 1.16.3

## Limitations

- PDF analysis shows first page as image
- For better OCR on PDFs, use image-based documents
- Large documents may take longer to process
- Some complex formatting may not be fully captured

## License

This project is open source and available for personal and educational use.

## Support

For issues with the Gemini API, visit: https://support.google.com/makersuite

## Future Improvements

- [ ] Multi-page PDF analysis
- [ ] Document comparison
- [ ] Extract specific data types (tables, images)
- [ ] Support for more file formats
- [ ] Export results as PDF/Word
- [ ] Batch processing

---

**Made with ❤️ using Flask and Google Gemini AI**
