# This file is for running the app in development, and should
# be substituted by Gunicorn in production.
from app import app

app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
print('champion-rotation-predictor started.')
