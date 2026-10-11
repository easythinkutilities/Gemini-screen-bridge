import os
import time
import tkinter as tk
from tkinter import scrolledtext
from google import genai
from PIL import Image

#latex removal
import re

def clean_math_text(text):
    text = text.replace("$", "")
    # Use [d]? so regex looks for the literal letter 'd', not a digit class
    text = re.sub(r'\\([d])?frac\{([^}]+)\}\{([^}]+)\}', r'(\2/\3)', text)
    text = text.replace(r"\times", "*")
    text = text.replace(r"\left", "").replace(r"\right", "")
    return text
# 1. Clean up old screenshot
if os.path.exists("screenshot.png"):
    os.remove("screenshot.png")
time.sleep(0.1)

# 2. Capture fresh screen image
os.system("scrot -p screenshot.png")
image = Image.open("screenshot.png")

# 3. Initialize Gemini Client & Chat Session
client = genai.Client()
chat_session = client.chats.create(model="gemini-3.5-flash-lite")

# Prime the chat with the screenshot and initial request
initial_prompt = [image, "Solve or explain what is visible on this screen clearly and concisely."]
initial_response = chat_session.send_message(initial_prompt)

# 4. Build the Interactive GUI Window
root = tk.Tk()
root.title("Gemini Screen Bridge - Chat")
root.geometry("550x520")
root.configure(background="#2d2d2d")
root.attributes("-topmost", True)

# Scrollable chat history area
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, bg="#1e1e1e", fg="#f0f0f0")
chat_area.pack(padx=10, pady=(10, 5), fill=tk.BOTH, expand=True)
cleaned_text = clean_math_text(initial_response.text)
chat_area.insert(tk.END, f"Gemini:\n{cleaned_text}\n\n")
# ------------------------

chat_area.configure(state='disabled')

# Input frame for follow-up questions
input_frame = tk.Frame(root, bg="#2d2d2d")
input_frame.pack(padx=10, pady=(5, 10), fill=tk.X)

user_input = tk.Entry(input_frame, font=("Arial", 11), bg="#3d3d3d", fg="#ffffff", insertbackground="white")
user_input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
user_input.focus_set()  # Automatically focuses the typing cursor here

def send_followup(event=None):
    question = user_input.get().strip()
    if not question:
        return
    
    # Display user question
    chat_area.configure(state='normal')
    chat_area.insert(tk.END, f"You: {question}\n")
    chat_area.configure(state='disabled')
    
    user_input.delete(0, tk.END)
    
    # Send to Gemini chat session
    response = chat_session.send_message(question)
    
    # Display Gemini response
    chat_area.configure(state='normal')
    chat_area.insert(tk.END, f"Gemini: {response.text}\n\n")
    chat_area.configure(state='disabled')
    chat_area.see(tk.END)

send_btn = tk.Button(input_frame, text="Ask", command=send_followup, bg="#007acc", fg="white", font=("Arial", 10, "bold"))
send_btn.pack(side=tk.RIGHT)

# Allow pressing Enter to submit
user_input.bind("<Return>", send_followup)

root.mainloop()
