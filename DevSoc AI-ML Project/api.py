from google import genai
import os
import json 
import time

def call_api(prompt):

    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    response = client.models.generate_content(
        model="gemma-3-27b-it",
        contents=prompt
    )
    
    return response.text

def main():
    prompts =[]
    with open("text.txt", "r", encoding="utf-8") as f:
        for line in f:
            prompts.append(line.strip())

    results = []
    for i,prompt in enumerate(prompts, start=1):
        print(f"[{i}/{len(prompts)}] Prompting: {prompt}...")
        response_text = call_api(prompt)
        results.append({
            "prompt":prompt,
            "response":response_text
        })

        time.sleep(1)

    with open("responses.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

   

main()