<h1>Social Media Web Application</h1>

This Django-based social media platform allows users to sign up, log in, post content, like posts, follow users, comment, and interact through direct messages.

Features

User Authentication: Sign up, log in, and log out functionalities.

Post Creation: Users can upload media and add captions to their posts.

Like System: Users can like/unlike posts.

Follow System: Users can follow/unfollow other users and see their posts.

Comments: Users can comment on posts, with support for nested comments.

Profile Management: Users can view their profile, posts, and followers/following details.

Search Functionality: Users can search for other users by name or username.


Views and Routes

/: Displays posts from followed users.

/login: Handles user login.

/signup: Handles user registration.

/searchUser: Allows searching for users.

/profile/<id>: Displays a user's profile and posts.

/addlike: Adds/removes likes on posts.

/addFollow: Adds/removes followers.

/detailPost/<id>: Displays detailed post and its comments.

/yourPost: Displays the logged-in user's posts.

/editPost/<id>: Edits an existing post.

/delPost/<id>: Deletes a post.


Setup Instructions

1. Clone the repository:

git clone <repository-url>


2. Install dependencies:

pip install -r requirements.txt


3. Database Setup:

python manage.py migrate


4. Run the Development Server:

python manage.py runserver


5. Open http://127.0.0.1:8000 in your browser.
