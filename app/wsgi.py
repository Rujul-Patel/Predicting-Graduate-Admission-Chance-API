from app.app import app
import os

port = int(os.environ.get("PORT",5000))

#app related
if __name__ == "__main__":
    app.run(port=port)
