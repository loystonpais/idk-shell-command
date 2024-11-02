#!/usr/bin/env python
import os
import sys
import subprocess
import sqlite3
from pathlib import Path
import requests
import json

TASK = """
Please interpret the user's query to provide an appropriate Linux command concisely and accurately, without additional formatting or extraneous information. If the user requests a template or code snippet, avoid enclosing it within code blocks or extra formatting elements. Focus on clarity and directness, ensuring responses are professional and to the point.
"""

API_KEY = os.environ.get("IDK_GROQ_API_KEY")
if not API_KEY:
    print("Error: Missing GROQ API key.", file=sys.stderr)
    sys.exit(1)

API_URL = "https://api.groq.com/openai/v1/chat/completions"


DB_PATH = str(Path.home() / ".idk_history.db")
con = sqlite3.connect(DB_PATH)
cur = con.cursor()


cur.execute("""
    CREATE TABLE IF NOT EXISTS queryresponse (
        query TEXT PRIMARY KEY,
        response TEXT
    )
""")


query = " ".join(sys.argv[1:])
res = cur.execute("SELECT response FROM queryresponse WHERE query = ?", (query,)).fetchone()

if not res:
    payload = {
        "messages": [
            {
                "role": "system",
                "content": TASK,
            },
            {
                "role": "user",
                "content": query,
            }
        ],
        "temperature": 0.01,
        "model": "llama-3.1-70b-versatile"
    }

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code != 200:
        print(f"Error: {response.status_code} - {response.text}", file=sys.stderr)
        sys.exit(1)

    response_data = response.json()
    final = response_data["choices"][0]["message"]["content"]

    cur.execute("INSERT INTO queryresponse VALUES(?, ?)", (query, final))
    con.commit()
else:
    final = res[0]

print(final)
subprocess.run(['xclip', '-selection', 'clipboard'], input=final.encode())
con.close()