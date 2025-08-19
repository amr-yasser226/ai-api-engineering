# Getting Started with OpenAI API

This file uses the **OpenAI Python SDK**.  
To run the script, you need an API key from OpenAI.

---

## 1. Get your OpenAI API Key
1. Go to [https://platform.openai.com/](https://platform.openai.com/)  
2. Sign in (or create an account).  
3. Navigate to **View API keys** in your account settings.  
4. Click **Create new secret key** and copy it.

---

## 2. Set your API Key locally
Instead of editing the script, set an environment variable:

### Linux / macOS (bash/zsh)
```bash
export OPENAI_API_KEY="sk-xxxxxx"
```

### Windows (PowerShell)
```bash
setx OPENAI_API_KEY "sk-xxxxxx"
```

Restart your terminal so the variable is loaded.