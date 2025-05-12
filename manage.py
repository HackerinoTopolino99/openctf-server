#!/usr/bin/env python3
import os

from flask_migrate import Migrate

from openctf.app import create_app
from openctf.models import db

app = create_app()
migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, use_debugger=True, use_reloader=True)

