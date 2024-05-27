# PollApp

## Description
PollApp is a simple web application built with Django that allows users to create and participate in polls. Users can view available polls, vote on their favorite options, and see the results. This project demonstrates basic Django functionality including models, views, templates, and user authentication.

## Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Credits](#credits)

## Installation
To install and run this project locally, follow these steps:

1. **Clone the repository**:
    ```sh
    git clone https://github.com/YourUsername/PollApp.git
    ```

2. **Navigate to the project directory**:
    ```sh
    cd PollApp
    ```

3. **Create a virtual environment**:
    ```sh
    python -m venv venv
    ```

4. **Activate the virtual environment**:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

5. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

6. **Apply the migrations**:
    ```sh
    python manage.py migrate
    ```

7. **Create a superuser**:
    ```sh
    python manage.py createsuperuser
    ```

8. **Run the development server**:
    ```sh
    python manage.py runserver
    ```

## Usage
1. **Open your web browser** and navigate to `http://127.0.0.1:8000/` to view the application.
2. **Log in to the admin panel** at `http://127.0.0.1:8000/admin/` using the superuser credentials.
3. **Create and manage polls** from the admin panel.
4. **Vote on polls** and view results on the main site.

![PollApp Screenshot](screenshot.png)

## Credits
Author: Sammy Astroblast
