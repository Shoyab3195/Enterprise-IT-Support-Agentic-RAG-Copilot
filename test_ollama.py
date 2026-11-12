import requests
import time

url = "http://localhost:11434/api/generate"

payload = {
    "model": "qwen2.5:1.5b",
    "prompt": "Explain password reset in one sentence.",
    "stream": False,
    "options": {
        "num_predict": 50
    }
}

start = time.time()
response = requests.post(url, json=payload, timeout=300)

print("Status:", response.status_code)
print("Response:", response.json()["response"])
print("Time taken:", round(time.time() - start, 2), "seconds")