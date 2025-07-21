# LLM Document Decision System

This project is a Streamlit web app that analyzes policy documents and answers natural language queries using document retrieval and Gemini (Google Generative AI).

## Features
- Upload policy documents (PDF, DOCX, EML)
- Extract and chunk document text
- Embed and index document chunks using Sentence Transformers and FAISS
- Retrieve relevant clauses for a user query
- Use Gemini LLM to reason over the query and retrieved clauses
- Display decision and justification in JSON format

## Setup

1. **Clone the repository**
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   pip install google-generativeai
   ```
3. **Set up your API key**
   - Create a `.env` file in the project root:
     ```env
     GOOGLE_API_KEY=your-gemini-api-key-here
     ```
   - Get your Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey)

4. **Run the app**
   ```bash
   streamlit run streamlit_app.py
   ```

## Usage
- Upload one or more policy documents
- Enter a natural language query (e.g., "Is a 45-year-old in Texas covered for knee surgery under a 12-month policy?")
- Click "Get Decision" to see the LLM's response

## File Structure
- `streamlit_app.py` - Main Streamlit app
- `app/` - Core logic modules (embedding, retrieval, LLM reasoning, etc.)
- `data/` - (Optional) Store data files
- `models/` - (Optional) Store model files

## Notes
- Requires a valid Gemini API key
- For production, replace `eval()` with `json.loads()` for safety

---

Feel free to customize and extend this project for your own document analysis needs!
