#!flask/bin/python
import os
from app import app

# For c9 Development
app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))