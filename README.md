# 🚀 TaskFlow - Personal Task Management App  

TaskFlow is a **simple and efficient personal task manager** built with **FastAPI (backend) and Vue.js (frontend)**. It helps users keep track of their daily tasks, set priorities, organize tasks by categories, and manage their workflow easily.  

---

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
```

### **2️⃣ Backend Setup (FastAPI)**  
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```
- Backend runs at: [http://127.0.0.1:8000](http://127.0.0.1:8000)  
- API Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) (FastAPI’s auto-generated API documentation)  

### **3️⃣ Frontend Setup (Vue.js)**  
```bash
cd frontend
npm install
npm run dev
```
- Frontend runs at: [http://localhost:5173](http://localhost:5173)  

---

## 🌟 Screenshots  

### 🔹 **Home Page**  
![Home Page](https://github.com/YDevStudio/taskflow/assets/your_image_hash_here)  

### 🔹 **Task Management View**  
![Task Management](https://github.com/YDevStudio/taskflow/assets/your_image_hash_here)  

### 🔹 **Task Editing & Sorting**  
![Task Editing](https://github.com/YDevStudio/taskflow/assets/your_image_hash_here)  

---

## 📌 API Endpoints  

| Method  | Endpoint          | Description                                   |  
|---------|------------------|----------------------------------------------|  
| **POST** | `/auth/register` | Register a new user                         |  
| **POST** | `/auth/login`    | Login user                                  |  
| **GET**  | `/tasks`         | Retrieve all tasks for the authenticated user |  
| **POST** | `/tasks`         | Create a new task                           |  
| **PUT**  | `/tasks/{id}`    | Update a task                              |  
| **DELETE** | `/tasks/{id}`  | Delete a task                              |  

- **Authentication:** API requests require a JWT Bearer Token.  
- **Authorization:** Users can only access their own tasks.  

---

## 🎯 Future Improvements  
- ✅ Dark Mode Support  
- ✅ Task Due Date Reminders  
- ✅ Drag & Drop Task Sorting  
- ✅ PWA (Offline Support)  
- ✅ Email Notifications for Upcoming Deadlines  

---

## 🛠️ Contributing  

Contributions are welcome! 🎉  
If you'd like to improve the project, feel free to fork the repository and submit a pull request.  

### **Steps to Contribute:**  
1. **Fork the repository**  
2. **Create a new branch** (`git checkout -b feature-branch`)  
3. **Commit your changes** (`git commit -m "Add new feature"`)  
4. **Push to your fork** (`git push origin feature-branch`)  
5. **Submit a Pull Request (PR)** for review  

---

## 📄 License  

**MIT License** © 2024 YDevStudio  
You are free to use and modify this project under the MIT license.  

---

## 🚀 Made with ❤️ by YDevStudio  

🎯 If you like this project, consider giving it a ⭐ on GitHub!  