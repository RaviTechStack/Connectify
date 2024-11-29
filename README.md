<h1 align="center">🌐 Connectify</h1>

<p align="center">
  A Django-based social media web application that allows users to connect, share, and engage with others.
</p>

---

<h2>📖 About Connectify</h2>
<p>
  <strong>Connectify</strong> is a modern social media web application designed for seamless interaction. Users can sign up, log in, post content, like posts, follow other users, comment on posts. It replicates the core functionalities of a social networking platform.
</p>

---

<h2>🚀 Features</h2>
<ul>
  <li><strong>User Authentication:</strong> Sign up, log in, and log out functionalities.</li>
  <li><strong>Post Creation:</strong> Upload media and add captions to posts.</li>
  <li><strong>Like System:</strong> Like and unlike posts.</li>
  <li><strong>Follow System:</strong> Follow or unfollow other users and view their posts.</li>
  <li><strong>Comments:</strong> Comment on posts with support for nested comments.</li>
  <li><strong>Profile Management:</strong> View profiles, posts, and followers/following details.</li>
  <li><strong>Search Functionality:</strong> Search for other users by name or username.</li>
</ul>

---

<h2>📂 Views and Routes</h2>
<ul>
  <li><code>/</code>: Displays posts from followed users.</li>
  <li><code>/login</code>: Handles user login.</li>
  <li><code>/signup</code>: Handles user registration.</li>
  <li><code>/searchUser</code>: Allows searching for users.</li>
  <li><code>/profile/&lt;id&gt;</code>: Displays a user's profile and posts.</li>
  <li><code>/addlike</code>: Adds/removes likes on posts.</li>
  <li><code>/addFollow</code>: Adds/removes followers.</li>
  <li><code>/detailPost/&lt;id&gt;</code>: Displays detailed post and its comments.</li>
  <li><code>/yourPost</code>: Displays the logged-in user's posts.</li>
  <li><code>/editPost/&lt;id&gt;</code>: Edits an existing post.</li>
  <li><code>/delPost/&lt;id&gt;</code>: Deletes a post.</li>
</ul>

---

<h2>⚙ Setup Instructions</h2>
<ol>
  <li><strong>Clone the repository:</strong>
    <pre><code>git clone &lt;repository-url&gt;</code></pre>
  </li>
  <li><strong>Database Setup:</strong>
    <pre><code>python manage.py migrate</code></pre>
  </li>
  <li><strong>Run the Development Server:</strong>
    <pre><code>python manage.py runserver</code></pre>
  </li>
  <li><strong>Access the application:</strong>
    Open <a href="http://127.0.0.1:8000" target="_blank">http://127.0.0.1:8000</a> in your browser.
  </li>
</ol>

---

<h2>📬 Contact</h2>
<p>
  Have questions or want to connect? Reach out to me:
</p>
<ul>
  <li>Email: <a href="mailto:codes.ravisingh@gmail.com">codes.ravisingh@gmail.com</a></li>
  <li>LinkedIn: <a href="https://www.linkedin.com/in/ravi-singh-53894933a?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app" target="_blank">Ravi Singh</a></li>
</ul>
