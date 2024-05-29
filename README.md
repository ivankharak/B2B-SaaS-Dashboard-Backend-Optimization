# B2B SaaS Dashboard Backend Optimization

## Description
This Django project implements backend optimization for a B2B SaaS dashboard. The dashboard serves as a CRM, communication/newsletter tool, and loyalty asset manager. One of the main functionalities is to list, search, and filter contacts. The project includes a data model consisting of three tables: AppUser, Address, and CustomerRelationship.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/ivankharak/hello_again
2. Create Virtual environment
   ```bash
   python -m venv .venv
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
4. Apply migrations:
   ```bash
   python manage.py migrate
## Usage
1. Start the development server:
   ```bash
   python manage.py runserver 
2. Open your web browser and navigate to http://127.0.0.1:8000/ to access the application.
## Features
1. Use Django Debug Toolbar or other profiling tools to measure the performance of the views with various queries.

2. Benchmark the view with specific queries such as filtering by name, sorting by attribute, and loading initial lists including pagination.

3. Think about performance optimizations and implement them as a bonus. Compare the performance with initial benchmarks.