import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def evaluate_decision(parsed_query, retrieved_clauses):
    prompt = f"""
You are an expert insurance policy analyst. Based on the following query and policy clauses, decide if the treatment is approved.

Query:
Age: {parsed_query['age']}
Location: {parsed_query['location']}
Treatment: {parsed_query['treatment']}
Policy Duration: {parsed_query['policy_duration']} months

Clauses:
{retrieved_clauses}

Give a JSON response with:
- Decision (Approved/Rejected)
- Amount (if applicable)
- Justification
- Clause (text)

Respond in valid JSON.
"""
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return eval(response.text)  # Unsafe in prod, replace with json.loads
