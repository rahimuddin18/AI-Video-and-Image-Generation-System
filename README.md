# AI-Video-and-Image-Generation-System
Overview
This project is an AI Content Generator that allows users to generate videos and images based on text prompts. The system integrates with AI models to generate videos and images and provides users with a web interface to interact with the generated content.

Features
Text-to-Video and Text-to-Image Generation: Users can input text prompts, and the system will generate videos and images using AI tools.
Content Storage: Videos and images are saved locally and stored in a structured directory.
Status Tracking: The system keeps track of the status of content generation and notifies users when their content is ready.
Web Interface: A user-friendly interface built using Flask to allow users to view their generated content.
Responsive Design: The web interface is designed to be responsive, adapting to both mobile and desktop views.
Project Structure


AI-Content-Generator/
│
├── app.py                     # Main Flask application script
├── requirements.txt           # List of dependencies required for the project
├── templates/                 # Folder containing HTML templates
│   ├── index.html             # Landing page for the user to input data
│   ├── content.html           # Content display page for generated content
├── static/                    # Folder to store generated videos and images
│   └── <user_id>/             # User-specific folder for storing content
│       ├── video1.mp4         # Example video
│       ├── video2.mp4         # Example video
│       ├── image1.png         # Example image
│       └── image2.png         # Example image
├── database.db                # SQLite database for storing user data and content status
└── README.md                  # Documentation for the project
Setup
1. Clone the repository
Clone this repository to your local machine:
git clone <repository-url>
cd AI-Content-Generator

2. Install Dependencies
Create a virtual environment and install the required packages:
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt

3. Run the Application
Run the Flask application:
python app.py
The application will be accessible at http://127.0.0.1:5000/ in your browser.

4. Requirements
Make sure you have the following tools and libraries installed:
Flask: Web framework for Python
SQLite: Database to store user data and content status
Bootstrap: For responsive, modern UI design
AI APIs (RunwayML, OpenAI, etc.): Used for generating video and image content (replace placeholders with actual API integrations)

5. Dependencies
In your requirements.txt, include the following dependencies:
Flask==2.2.2
Flask-SQLAlchemy==2.5.1
requests==2.28.1
Make sure to install other libraries based on the AI tools you use for video and image generation.

How It Works
Part 1: Text-to-Video and Text-to-Image Generation
User Input: The user enters their unique User ID and a text prompt.
Content Generation:
The system calls APIs (like RunwayML, OpenAI, or others) to generate videos and images based on the prompt.
Videos are saved as .mp4 files, and images are saved as .jpg or .png.
Files are saved in the directory static/<user_id>/ for user-specific content storage.
Part 2: Content Management and Database
Database Structure:
User data, including User ID, prompt, video paths, image paths, and status, are stored in the SQLite database (database.db).
The status of content generation is tracked as "Processing" or "Completed".
Status Updates:
Once the content generation is complete, the system updates the status to "Completed" and notifies the user that their content is ready.
Part 3: User Access and Web Display
Login: Users access their content using their unique User ID.
Generated Content:
If the content generation is complete, the user will see a gallery of their generated videos and images.
If the content is still being processed, a message will display: "Your content is being generated. Please check back later."
Web Interface: The user can interact with a grid of images and videos. A responsive layout ensures a good experience across devices.
Part 4: Notifications
Content Completion Notification: Users can specify a notification time, and the system will notify them via a console message or email once their content is ready.
Notification Mechanism:
Email notifications can be integrated using libraries like smtplib or Flask-Mail for notifying the user when their content is ready.
Example Flow
The user visits the landing page at http://127.0.0.1:5000/.
They input their User ID and a text prompt.
The system generates videos and images based on the prompt.
Once the content is ready, the user receives a notification and can log in to view their generated content at http://127.0.0.1:5000/user/<user_id>.
Conclusion
This project demonstrates an AI-powered content generation system using Flask, AI APIs, and a simple SQLite database. The project is designed to be modular, allowing you to plug in different AI services and expand the functionality as needed. You can also customize the UI to match your branding and deploy the system on any server.

