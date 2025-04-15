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
    optimized_cv = api_query(api_key, f"Optimize the following sections Interests and About me for the job description: {job_description}. Use 40 words. CV: {uploaded_cv}")
    

    # Save the optimized CV
    save_optimized_cv(optimized_cv)

    return optimized_cv 





