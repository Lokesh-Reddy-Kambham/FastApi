# Hi Everyone, Welcome to My FastAPI Journey!

<p align="center">
  <img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI Logo" width="240" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/FastAPI-Framework-009688?logo=fastapi&logoColor=white" alt="FastAPI Badge" />
  <img src="https://img.shields.io/badge/React-Frontend-61DAFB?logo=react&logoColor=black" alt="React Badge" />
  <img src="https://img.shields.io/badge/Python-Backend-3776AB?logo=python&logoColor=white" alt="Python Badge" />
</p>

This repository contains a **full-stack Product Management app** built with:
- **FastAPI backend**
- **React frontend**

I use this project to practice API development, frontend integration, and CRUD operations.

---

## Course / Project Overview
- **Project Type:** Full Stack Practice App
- **Backend:** FastAPI + Pydantic
- **Frontend:** React + Axios
- **Status:** Ongoing improvements

---

## Repository Structure
- `main.py` - FastAPI app and API routes
- `models.py` - Pydantic data model (`Product`)
- `frontend/` - React application
- `myenv/` - Local Python virtual environment

---

## Tech & Tools Used
- **Frontend:** React, JavaScript, Axios, CSS
- **Backend:** FastAPI, Python, Pydantic, Uvicorn
- **Version Control:** Git & GitHub

---

## API Endpoints
- `GET /` - Welcome message
- `GET /products` - Fetch all products
- `GET /product/{id}` - Fetch product by ID
- `POST /add_product` - Add a new product
- `PUT /update_product?id={id}` - Update an existing product
- `DELETE /delete_products?id={id}` - Delete a product

---

## Run Locally

### 1. Start Backend

```powershell
# from repo root
.\myenv\Scripts\Activate.ps1
pip install fastapi uvicorn
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Backend URL: `http://localhost:8000`

### 2. Start Frontend

```powershell
# from repo root
cd frontend
npm install
npm start
```

Frontend URL: `http://localhost:3000`

---

## Notes
- Product data is stored in memory (list), so data resets when backend restarts.
- Frontend currently uses REST-style paths such as `/products/` and `/products/{id}`.

---

## Connect with Me

[![GitHub](https://img.shields.io/badge/GitHub-Profile-black?logo=github)](https://github.com/Lokesh-Reddy-Kambham/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?logo=linkedin)](https://www.linkedin.com/in/lokesh-reddy-kambham/)
[![HackerRank](https://img.shields.io/badge/HackerRank-Profile-green?logo=hackerrank)](https://www.hackerrank.com/profile/Lokesh_Reddy_)
[![LeetCode](https://img.shields.io/badge/LeetCode-Profile-orange?logo=leetcode)](https://leetcode.com/u/Lokesh-Reddy-Kambham/)
[![SoloLearn](https://img.shields.io/badge/SoloLearn-Profile-Blue?logo=sololearn)](https://www.sololearn.com/en/profile/30363693)

---

> **"First, solve the problem. Then, write the code." - John Johnson**