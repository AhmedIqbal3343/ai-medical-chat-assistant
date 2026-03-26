# 🩺 MedChain AI Chatbot  
### AI-Powered Healthcare Assistant using LangChain & OpenRouter

An intelligent healthcare chatbot built using **LangChain**, **Flask**, and **OpenRouter LLMs**, designed to simulate real doctor-like conversations.  
The system provides medically-grounded responses, basic guidance, and interactive health assessments while maintaining conversational context across sessions.

---

## 📌 Problem Statement

Access to immediate medical guidance is often limited, especially for minor symptoms or early-stage concerns.  
This project aims to bridge that gap by providing:

- Quick preliminary medical advice  
- Symptom-based conversational interaction  
- Context-aware follow-up questions  

---

## 🚀 Features

- 🧠 **Doctor-like AI Responses**
  - Calm, professional, medically grounded tone  
  - Simulates real clinical conversation  

- 💬 **Session-Based Memory**
  - Maintains conversation history per user  
  - Context-aware responses  

- 🔄 **Multi-Session Support**
  - Each user has independent chat history  

- 🌐 **REST API Backend**
  - Built with Flask  
  - Easily integratable with any frontend  

- ⚡ **OpenRouter LLM Integration**
  - Uses powerful LLM (`gpt-oss-20b`)  

- 🧹 **Session Management**
  - Clear chat history  
  - Retrieve past conversations  

---

## 🧠 How It Works

1. User sends a message via frontend/API  
2. Backend constructs:
   - System message (Doctor persona)
   - Conversation history
   - Current input  
3. LangChain processes messages  
4. OpenRouter LLM generates response  
5. Response stored in session memory  

---

## 🏗️ Tech Stack

| Category        | Technology |
|----------------|-----------|
| Backend        | Flask |
| AI Framework   | LangChain |
| LLM Provider   | OpenRouter |
| Model Used     | `openai/gpt-oss-20b` |
| Frontend       | HTML, CSS, JavaScript |
| Environment    | Python, dotenv |

---

## 📂 Project Structure
medchain-ai-chatbot/
│
├── app.py # Flask backend API
├── .env # API keys (not included)
├── requirements.txt # Dependencies
├── templates/
│ └── index.html # Frontend UI
│
└── README.md


---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/medchain-ai-chatbot.git
cd medchain-ai-chatbot

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

2) Setup Environment Variables

Create .env file:

OPENROUTER_API_KEY=your_api_key_here

▶️ Run the Application
python app.py

Server will start at:

http://localhost:5000

