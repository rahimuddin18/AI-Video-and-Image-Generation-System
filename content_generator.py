import os
import sqlite3
import openai
import requests
from datetime import datetime
import time

# Configure OpenAI API Key 
openai.api_key = "your_openai_api_key"

# Dummy RunwayML API URL (Replace with actual endpoint and API Key)
RUNWAYML_API_URL = "https://api.runwayml.com/v1/generate"  
RUNWAYML_API_KEY = "your_runwayml_api_key"


def generate_images(prompt, user_id):
    """
    Generate images using DALL·E and save them locally.
    """
    folder = f"static/{user_id}/"
    os.makedirs(folder, exist_ok=True)

    images = []
    print("Generating images using DALL·E...")
    for i in range(5):
        try:
            # Generate image using DALL·E
            response = openai.Image.create(prompt=prompt, n=1, size="512x512")
            image_url = response['data'][0]['url']

            # Save image locally
            image_path = f"{folder}image{i+1}.png"
            with open(image_path, "wb") as f:
                f.write(requests.get(image_url).content)

            images.append(image_path)
            print(f"Generated image {i+1}: {image_path}")
        except Exception as e:
            print(f"Error generating image {i+1}: {e}")

    return images


def generate_videos(prompt, user_id):
    """
    Generate videos using RunwayML and save them locally.
    """
    folder = f"static/{user_id}/"
    os.makedirs(folder, exist_ok=True)

    headers = {
        "Authorization": f"Bearer {RUNWAYML_API_KEY}",
        "Content-Type": "application/json",
    }

    videos = []
    print("Generating videos using RunwayML...")
    for i in range(5):
        try:
            # Generate video using RunwayML (example structure)
            payload = {"prompt": prompt, "output_format": "mp4"}
            response = requests.post(RUNWAYML_API_URL, json=payload, headers=headers)

            if response.status_code == 200:
                video_url = response.json()["output_url"]

                # Save video locally
                video_path = f"{folder}video{i+1}.mp4"
                with open(video_path, "wb") as f:
                    f.write(requests.get(video_url).content)

                videos.append(video_path)
                print(f"Generated video {i+1}: {video_path}")
            else:
                print(f"RunwayML API error for video {i+1}: {response.text}")
        except Exception as e:
            print(f"Error generating video {i+1}: {e}")

    return videos


# Database and user management
DATABASE = "database.db"

def add_user_to_db(user_id, prompt):
    """
    Add a new user record to the database with initial status.
    """
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (user_id, prompt, status, generated_at) VALUES (?, ?, ?, ?)",
                   (user_id, prompt, "Processing", datetime.now().isoformat()))
    conn.commit()
    conn.close()


def update_db(user_id, videos, images):
    """
    Update the database with the generated content and set status to 'Completed'.
    """
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""UPDATE users 
                      SET video_paths = ?, image_paths = ?, status = 'Completed'
                      WHERE user_id = ?""",
                   (",".join(videos), ",".join(images), user_id))
    conn.commit()
    conn.close()


# Main Execution
if __name__ == "__main__":
    user_id = input("Enter user ID: ")
    prompt = input("Enter text prompt: ")

    # Add user and set status to 'Processing'
    add_user_to_db(user_id, prompt)

    print("Generating content...")
    
    # Generate content
    images = generate_images(prompt, user_id)
    videos = generate_videos(prompt, user_id)

    # Simulate time delay for generation (if required)
    time.sleep(5)

    # Update database with generated content
    update_db(user_id, videos, images)
    print("Content generation completed. Check the static folder.")
