import requests
import json

def api_query(api_key, prompt):
    """
    Function to query the Gemini API with a given prompt.
    """
    url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}'
    headers = {
        'Content-Type': 'application/json',
    }
    data = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json() 





def optimize_cv():
    """
    Function to optimize a CV based on a job description.
    """
    # Load the pre-trained model
    model = load_model()

    # Get the CV and job description from the user
    cv_text = get_cv_text()
    job_description = get_job_description()

    # Optimize the CV using the model
    optimized_cv = model.optimize(cv_text, job_description)

    # Save the optimized CV
    save_optimized_cv(optimized_cv)

    return optimized_cv