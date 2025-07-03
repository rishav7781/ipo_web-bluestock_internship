# 📊 Bluestock Fintech IPO Web Application & REST API

This is a web application developed as part of my internship at **Bluestock Fintech**. The platform displays IPO (Initial Public Offering) data to public users and provides an admin panel for managing IPO entries, along with REST APIs for integration with mobile apps and external platforms.

---

## 📌 Project Overview

- **Public Interface**
  - List of Upcoming, Ongoing, and Listed IPOs
  - IPO Detail Page with full information
  - Downloadable RHP and DRHP PDFs
  - Search & Filter IPOs by status or name

- **Admin Panel**
  - Secure login-based access
  - Add, Edit, and Delete IPO entries
  - Upload PDF files (RHP/DRHP)
  - Manage logos and all IPO fields via Django Admin

- **REST APIs**
  - `GET /api/ipo/` — Fetch list of IPOs
  - `GET /api/ipo/<id>/` — Fetch IPO details by ID
  - (Search & ordering APIs pending implementation)

---

## ⚙️ Tech Stack

- **Backend:** Python 3.12.3, Django 5.0.6, Django REST Framework 3.15.1
- **Database:** PostgreSQL 16.2
- **Frontend (Admin):** Django Admin Panel
- **Tools:** Git, GitHub, Postman
- **Deployment-Ready Code:** Configured with `.env` for sensitive credentials

---

## 📁 Project Structure

bluestock_ipo_web/
├── ipo_webapp_backend/
│ ├── ipo_project/
│ ├── ipo_app/
│ ├── media/
│ ├── manage.py
│ └── .env
└── README.md

---

## 📑 Features Implemented

- Django project and app setup
- PostgreSQL database configuration via `.env`
- IPO Model and Admin Panel
- Media upload setup for company logos and PDF files
- REST API for listing and fetching IPOs
- Dummy data population via admin interface
- API tested using Postman

---

## 📦 Pending Tasks

- API search, filter & ordering functionality
- Frontend (React/HTML Bootstrap) integration based on provided Figma designs
- Final deployment and documentation submission

---

## 👤 Author

**Rishav Gupta**  
Bluestock Fintech | Summer Internship 2025  
GitHub: [rishav7781](https://github.com/rishav7781)

---

## 📜 License

This project is proprietary and confidential. Developed for Bluestock Fintech internship submission.

