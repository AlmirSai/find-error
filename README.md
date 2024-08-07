# find-error

##You need to generate django key and create file .env
    touch .env
        #.env file
        SECRET_KEY='your key'

##start:
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

## I tried to add logs, path for logs root/confog/logs/logs.log
You need to create this file and folder

##commands
    cd root/config
    mkdir logs && cd logs
    touch logs.log

##Adding template for logs in settings.py
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