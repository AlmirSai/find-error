## Setting up your Django Project

This guide will walk you through the essential steps to set up your Django project, including environment configuration, dependency installation, and logging setup.

### 1. Environment Setup

 Generate a Django Secret Key:
   ```bash
   touch .env
   ```

    Inside your `.env` file:
      ```
      SECRET_KEY='your_unique_secret_key'
      ```
      Replace `'your_unique_secret_key'` with a strong, randomly generated secret key. You can use a tool like [https://www.random.org/strings/](https://www.random.org/strings/) to generate a secure key.

 Create a Virtual Environment:
   ```bash
   python -m venv venv
   source venv/bin/activate 
   ```
 Install Dependencies:
   ```bash
   pip install -r requirements.txt 
   ```

### 2. Logging Configuration

 Create the Log File and Directory:
   ```bash
   cd root/config
   mkdir logs && cd logs
   touch logs.log
   ```

 Update your `settings.py`:

   ```python
   import os
   from pathlib import Path

   # ... other settings ...

   BASE_DIR = Path(__file__).resolve().parent.parent

   LOGGING = {
       'version': 1,
       'disable_existing_loggers': False,
       'handlers': {
           'file': {
               'level': 'ERROR',
               'class': 'logging.FileHandler',
               'filename': os.path.abspath(os.path.join(BASE_DIR, 'logs', 'logs.log'))
           },
           'console': {
               'level': 'DEBUG',
               'class': 'logging.StreamHandler',
           },
       },
       'loggers': {
           'django': {
               'handlers': ['file', 'console'],
               'level': 'INFO',
           },
       },
   }
   ```

### Explanation

 `.env` file: Stores your secret key (and other sensitive information) separate from your codebase to prevent accidental exposure.
 Virtual Environment: Isolates your project's dependencies from other Python projects, avoiding potential conflicts.
 Logging: Allows you to track events and errors in your Django application.

   `LOGGING` Dictionary:
       `version`: Specifies the logging version.
       `disable_existing_loggers`: Prevents conflicts with default loggers.
       `handlers`: Defines where log messages are sent.
           `file`: Logs errors to the `logs.log` file.
           `console`: Logs debug messages to the console.
       `loggers`: Configures specific loggers.
           `django`: Logs Django-related information (errors, startup events).

Remember:

 Replace `'your_unique_secret_key'` in `.env` with a strong, randomly generated key.
 Adapt logging levels to your specific needs.  For example, you might want to log warnings to the file and only critical errors to the console.
 Consider using a dedicated logging framework like `structlog` or `loguru` for more advanced logging features.
