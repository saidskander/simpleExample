#!/usr/bin/python3
from cenema import app

if __name__ == "__main__":
    app.run(use_reloader=True, port=5000, debug=True)
