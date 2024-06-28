import os

os.environ["DATABASE_URL"] = os.getenv("DATABASE_URL")
os.environ["SECRET_KEY"] = os.getenv("SECRET_KEY")
os.environ["CLOUDINARY_URL"] = os.getenv("CLOUDINARY_URL")
os.environ["GOOGLE_OAUTH_CLIENT_ID"] = os.getenv("GOOGLE_OAUTH_CLIENT_ID")
os.environ["GOOGLE_OAUTH_CLIENT_SECRET"] = os.getenv("GOOGLE_OAUTH_CLIENT_SECRET")
