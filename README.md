# 🚀 NEXTSTEP

> **Democratizing Access to Quality Technical Education**

[![Django](https://img.shields.io/badge/Django-4.2+-092E20?style=flat&logo=django)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python)](https://www.python.org/)
[![Alpine.js](https://img.shields.io/badge/Alpine.js-3.x-8BC0D0?style=flat&logo=alpine.js)](https://alpinejs.dev/)
[![SQLite](https://img.shields.io/badge/SQLite-3.x-003B57?style=flat&logo=sqlite)](https://www.sqlite.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

---

## 📋 Table of Contents

- [Problem Statement](#-problem-statement)
- [Solution](#-solution)
- [Key Features](#-key-features)
- [System Modules](#-system-modules)
- [Technical Stack](#-technical-stack)
- [Quick Start](#-quick-start)
- [Project Structure](#-project-structure)
- [CSV Bulk Import](#-csv-bulk-import)
- [Contributing](#-contributing)
- [License](#-license)

---

## ❗ Problem Statement

Students often waste months searching for reliable learning paths and distinguishing between high-quality free resources and expensive paid courses. This leads to:

- ⏳ Delayed skill acquisition
- 💸 Unnecessary expenditure on suboptimal courses
- 📉 Increased educational inequality
- 🤯 "Analysis paralysis" from information overload

---

## 💡 Solution

**NEXTSTEP** provides an automated, systematic, and transparent platform that:

✅ Generates step-by-step learning roadmaps based on career goals  
✅ Explicitly categorizes resources into **Free** 🔵 and **Paid** 🟢 tiers  
✅ Tracks progress with visual analytics (Matplotlib/Seaborn)  
✅ Connects learners with peers at similar progress stages  
✅ Eliminates guesswork with verified, curated content  

> *"Stop searching. Start learning."*

---

## ✨ Key Features

| Feature | Description |
|---------|-------------|
| 🎯 **Dynamic Roadmap Generator** | Sequential, topic-by-topic learning paths tailored to roles like Data Scientist, Full Stack Developer, etc. |
| 💰 **Budget-Aware Filtering** | Toggle between "Free Resources Only" or "Best Quality (Free + Paid)" to match financial constraints. |
| 📊 **Progress Analytics** | Visual bar charts and skill heatmaps generated server-side with Matplotlib/Seaborn. |
| 👥 **Peer Matching (Module E)** | Connects students on the same roadmap/stage to foster accountability and collaboration. |
| 📝 **Articles & Tutorials** | Community-driven content platform for sharing insights and best practices. |
| 💼 **Internship Board** | Curated opportunities with direct application links. |
| 🗂️ **CSV Bulk Import** | Admins can seed hundreds of resources instantly via Pandas-powered CSV ingestion. |
| 🔐 **Secure Authentication** | Email/password registration with Django's built-in auth system and custom user preferences. |

---

## 🧩 System Modules
NEXTSTEP
├── Module A: User Onboarding & Profile
│ ├── Secure registration/login
│ ├── Career goal selection
│ ├── Budget & learning style preferences
│ └── Personalized dashboard
│
├── Module B: Dynamic Roadmap Generator
│ ├── Vertical timeline UI
│ ├── Smart resource cards (Free/Paid)
│ ├── "Mark as Complete" progress tracking
│ └── Next-step highlighting
│
├── Module C: Progress Analytics
│ ├── Completion % bar charts
│ ├── Skill domain heatmaps
│ └── Time-estimation calculator
│
├── Module D: Content Management
│ ├── CSV bulk import via Pandas
│ ├── Resource verification tagging
│ └── User statistics dashboard
│
└── Module E: Community Peer-Matching
├── Study buddy suggestions
├── Same-stage peer discovery
└── Group collaboration tools


---

## 🛠️ Technical Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | Django 4.2 (Python 3.10+) |
| **Frontend** | HTML5, Tailwind CSS, Alpine.js 3.x |
| **Database** | SQLite3 (development), PostgreSQL-ready |
| **Visualization** | Matplotlib, Seaborn (server-side PNG generation) |
| **Data Processing** | Pandas (CSV import, analytics) |
| **Authentication** | Django Auth with custom `CustomUser` model |
| **Deployment** | WSGI (Gunicorn), Docker-ready |

---

## 🚀 Quick Start

### Prerequisites
- Python 3.10 or higher
- pip (Python package manager)
- Git

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/nextstep.git
cd nextstep

# 2. Create and activate virtual environment
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations
python manage.py makemigrations core
python manage.py migrate

# 5. Create admin user
python manage.py createsuperuser

# 6. (Optional) Seed initial roadmaps via CSV
python manage.py import_roadmaps roadmaps_seed.csv

# 7. Run development server
python manage.py runserver