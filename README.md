# PR Analyzer

A Django application that analyzes GitHub Pull Requests using LLM to provide code review feedback.

## Features
- Analyzes GitHub PR files for code style, bugs, and best practices
- Uses LLM for intelligent code review
- Async processing with Celery
- REST API endpoints

## Setup
1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   ```bash
   export GITHUB_TOKEN='your_github_token'
   ```
4. Run Redis server for Celery
5. Start Celery worker:
   ```bash
   celery -A next_app worker -l info
   ```
6. Run Django server:
   ```bash
   python manage.py runserver
   ```

## API Endpoints
- POST /start_task/ - Start PR analysis
- GET /task_status/<task_id>/ - Check task status

## Environment Variables
- GITHUB_TOKEN - GitHub Personal Access Token
- Other configuration in settings.py 

## Environment Setup

Create a `.env` file in the root directory with the following variables:
```
GITHUB_TOKEN=your_github_token
GROQ_API_KEY=your_groq_api_key
```

Make sure to never commit the `.env` file to version control. 