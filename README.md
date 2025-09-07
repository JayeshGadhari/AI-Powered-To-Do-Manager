# AI-Powered To-Do Manager

A web-based task management application where users can enter a task title, and **AI automatically generates a detailed description**. Users can also update, delete, and summarize tasks in real-time using AI.

---

## 🛠 Tools & Tech Stack Used

- **Backend:** Flask (Python web framework)  
- **Frontend:** HTML, CSS, JavaScript  
- **AI/NLP:** Hugging Face Transformers (`google/flan-t5-small`) for text generation  
- **Libraries:**
  - `torch` (for model inference)  
  - `transformers` (for text generation pipeline)  
  - `langchain` & `langchain-huggingface` (optional, for future enhancements)  

- **Deployment:** Runs locally via Flask development server  

---

## ⚙ Features Implemented

1. **Add Task with AI-generated Description**  
   - User enters a task title (idea).  
   - AI generates a detailed description automatically.  

2. **CRUD Operations**  
   - **Create:** Add new task with AI description.  
   - **Read:** View all tasks in a table format.  
   - **Update:** Modify task title, description, or status (pending/done).  
   - **Delete:** Remove a task.  

3. **Task Summary with AI**  
   - AI generates a concise summary of all tasks and their statuses.  

4. **Real-time Updates**  
   - Tasks table updates automatically after add/update/delete operations.  

---

## 🚀 How to Run the Project

1. **Clone the repository:**

```bash
git clone <https://github.com/JayeshGadhari/AI-Powered-To-Do-Manager.gitl>
```

2. **Create a virtual environment (optional but recommended):**

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Run the Flask app:**

```bash
python app.py
```

5. **Open in browser:**

```
http://127.0.0.1:5000
```

6. **Usage:**
   - Enter a task title → Click **Generate Task** → AI generates description.  
   - Update or delete tasks using inline inputs and buttons.  
   - Click **Summarize Tasks** to view an AI-generated summary.  

---

## 📸 Screenshot

You can add a screenshot of your running web app here:

`![App Screenshot]("images/Task2.png")`

---

## 🎬 Demo Video

You can add a link to your demo video here:

`[Watch Demo](https://drive.google.com/file/d/1SRSM8-QwvTlpP8qcKBEEf1LYGrC0zE_2/view?usp=sharing)`

