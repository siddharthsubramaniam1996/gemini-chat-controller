# Gemini Chat Controller

A simple Python command-line tool for chatting with Google AI Studio’s Gemini models.  
Features: **response length control**, **device/network info**, **secure API key storage** in `keys.txt`, and **easy GitHub setup**.

---

## 🚀 Quick Start

### 1. Get the Code

**Option A: Download the ZIP**  
Go to your GitHub repository, click **Code > Download ZIP**, then unzip the folder.

**Option B: Clone with Git**  
Open your **terminal** (Command Prompt, PowerShell, Terminal, etc.) and run:

git clone https://github.com/YOURGITHUBUSERNAME/gemini-chat-controller.git
cd gemini-chat-controller

*(Replace `YOURGITHUBUSERNAME` with your actual GitHub username.)*

---

### 2. Install Dependencies

Make sure you have **Python 3.8+** installed.  
In your terminal, from the `gemini-chat-controller` folder, run:

pip install-r requirements.txt

*(This installs everything you need: `google-generativeai`, `psutil`, and `tiktoken`.)*

---

### 3. Set Up Your API Keys

- Open the file **`keys.txt`** in your project folder.
- Add your Google AI Studio and OpenAI API keys like this:

GOOGLE_AI_STUDIO_API_KEY=your-gemini-key-here
OPENAI_API_KEY=your-openai-key-here

*(Replace `your-gemini-key-here` with your actual key. The OpenAI key is optional but included for flexibility.)*

**Save and close the file.**

---

### 4. Run the Chat Tool

In your terminal, still inside the project folder, run:

python gemini_chat.py

This starts the chat.  
You’ll see your device/network info and then a prompt to start chatting.

---

## 🖥️ How It Works

- **Type your message** when prompted.
- **Choose response length**:  
  1 = Very Short (≤10 words),  
  2 = Short (≤50 words),  
  3 = Medium (≤150 words),  
  4 = Long (no limit).
- **See the reply**, estimated token count, and (for Very Short) the actual word count.
- **Type `quit`, `exit`, or `q`** to end.
- **You can chat as long as you want!**  
  Just keep answering when prompted.

---

## 🔥 Features

- **Chat with Google Gemini** (`gemini-1.5-pro-latest` by default)
- **Control response length**—save energy, tokens, and time!
- **Device & network info**—see your OS and connection type
- **Secure key storage**—keys are in `keys.txt`, not hardcoded
- **Cross-platform**—works on Windows, Mac, or Linux

---

## 🔒 Important Security

- **Never commit real API keys in open code.**  
  This project uses `keys.txt` to keep your keys out of the main script.
- **Add `keys.txt` to your `.gitignore` file** if you plan to make your project public.  
  Do this **before** you commit, by running in your project folder:

echo "keys.txt">>.gitignore

- **Rotate your API keys** regularly for maximum security.
- **Do not share `keys.txt`** if you are making the repository public.

---

## 🔧 Customization

- **Use a different Gemini model** by editing the `model_name` variable in `gemini_chat.py`.
- **Add other AI providers** by expanding `keys.txt` and the code logic.
- **Modify, fork, or share** as you like!

---

## 📋 Project Files

| File             | What it does                                 |
|------------------|---------------------------------------------|
| `gemini_chat.py` | Main chat program                           |
| `requirements.txt` | Lists required Python modules              |
| `keys.txt`       | Add your API keys here (keep private!)      |
| `README.md`      | This guide                                 |

---

## ❓ Need Help?

Open an **Issue** on your GitHub repository, or contact the project owner.

---

## 🚀 Let’s Go!

Once your keys are in `keys.txt` and dependencies are installed, open your terminal, go to the project folder, and run:

python gemini_chat.py


**Enjoy fast, eco-friendly, and intelligent conversations with Gemini!**
