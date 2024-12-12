from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime
import os

app = Flask(__name__)

DATABASE = "database.db"
CONTENT_FOLDER = "static/"

# Create database if it doesn't exist
def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        user_id TEXT PRIMARY KEY,
                        prompt TEXT,
                        video_paths TEXT,
                        image_paths TEXT,
                        status TEXT,
                        generated_at TEXT)''')
    conn.commit()
    conn.close()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_id = request.form["user_id"]
        prompt = request.form["prompt"]
        notification_time = request.form.get("notification_time", None)
        
        # Process the form data or redirect to generation logic
        return redirect(url_for("user_content", user_id=user_id))
    return render_template("index.html")

@app.route("/gallery/<user_id>")
def gallery(user_id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    user = cursor.fetchone()
    conn.close()

    if user:
        status, videos, images = user[4], user[2], user[3]
        if status == "Processing":
            return render_template("processing.html")
        else:
            videos = videos.split(",")
            images = images.split(",")
            return render_template("gallery.html", videos=videos, images=images)
    else:
        return "User not found."

@app.route("/user/<user_id>")
def user_content(user_id):
    # Dummy data for demonstration
    user_data = {
        "user_id": user_id,
        "status": "Completed",  # Or "Processing"
        "videos": [f"/static/{user_id}/video1.mp4", f"/static/{user_id}/video2.mp4"],
        "images": [f"/static/{user_id}/image1.png", f"/static/{user_id}/image2.png"],
    }
    
    return render_template(
        "content.html",
        user_id=user_data["user_id"],
        status=user_data["status"],
        videos=user_data["videos"],
        images=user_data["images"]
    )


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
