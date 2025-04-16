import requests



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




def optimize_cv(uploaded_cv, job_description, api_key):
    """
    Function to optimize a CV based on a job description.
    """
    optimized_cv = api_query(api_key, f"Optimize the following CV {uploaded_cv} for the job description: {job_description} in the Interests and About me sections.")
    

    return optimized_cv 





