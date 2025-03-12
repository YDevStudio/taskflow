# 🚀 TaskFlow - Task Management App

TaskFlow is a **modern and responsive task management application** built with **FastAPI (backend) and Vue.js (frontend)**. It helps users organize tasks efficiently with categorization, priority management, and a user-friendly UI.

## 🎯 Features
- ✅ **User Authentication (Register/Login/Logout)**
- ✅ **CRUD Tasks (Create, Edit, Delete, Mark as Complete)**
- ✅ **Task Prioritization (High, Medium, Low)**
- ✅ **Task Categorization (Work, Personal, Study, etc.)**
- ✅ **Sorting (Date, Priority, Name, Category)**
- ✅ **Persistent User Sessions (LocalStorage + Pinia)**
- ✅ **JWT Authentication (Secure API Requests)**
- ✅ **Modern UI with Animations & Transitions**
- ✅ **FastAPI Backend with PostgreSQL Database**

---

## ⚙️ Technologies Used
### **Frontend (Vue 3 + Pinia + Tailwind CSS)**
- Vue 3 (Composition API)
- Pinia (State Management)
- Tailwind CSS (Styling)
- Vite (Fast Development Server)

### **Backend (FastAPI + PostgreSQL)**
- FastAPI (Lightweight Python Web Framework)
- SQLAlchemy (ORM for Database Management)
- PostgreSQL (Relational Database)
- JWT Authentication (Secure User Sessions)

---

## 🚀 Setup & Installation

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/YDevStudio/taskflow.git
cd taskflow



⸻

2️⃣ Backend Setup (FastAPI)

cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload

	•	Backend runs at: http://127.0.0.1:8000
	•	You can visit http://127.0.0.1:8000/docs for FastAPI’s auto-generated API documentation.

⸻

3️⃣ Frontend Setup (Vue.js)

cd frontend
npm install
npm run dev

	•	Frontend runs at: http://localhost:5173

⸻

🌟 Screenshots

🔹 Home Page
![Home Page](https://github.com/user-attachments/assets/5a08107c-c147-479a-9cc3-eb4970dbb0ed)
🔹 Task Management View
![Task Management](https://github.com/user-attachments/assets/c7d1da91-105e-458b-af8f-a7b811b4c0d1)
🔹 Calendar
![Task Editing](https://github.com/user-attachments/assets/cbf462d4-fc2c-4add-b70d-9e44afa3ff10)
(Upload actual images and replace your-image-link.com with the correct links.)

⸻

📌 API Endpoints

Method	Endpoint	Description
POST	/auth/register	Register a new user
POST	/auth/login	Login user
GET	/tasks	Retrieve all tasks for the authenticated user
POST	/tasks	Create a new task
PUT	/tasks/{id}	Update a task
DELETE	/tasks/{id}	Delete a task

	•	Authentication: API requests require a JWT Bearer Token.
	•	Authorization: Users can only access their own tasks.

⸻

🎯 Future Improvements
	•	✅ Dark Mode Support
	•	✅ Task Due Date Reminders
	•	✅ Drag & Drop Task Sorting
	•	✅ PWA (Offline Support)
	•	✅ Email Notifications for Upcoming Deadlines

⸻

🛠️ Contributing

We welcome contributions! 🎉
Feel free to fork this repository, submit a pull request, or suggest improvements.
	1.	Fork the repository
	2.	Create a new branch
	3.	Commit your changes
	4.	Push to your fork
	5.	Submit a Pull Request

⸻

📄 License

MIT License © 2024 YDevStudio
You are free to use and modify this project under the MIT license.

⸻

🚀 Made with ❤️ by YDevStudio

🎯 If you like this project, consider giving it a ⭐ on GitHub!