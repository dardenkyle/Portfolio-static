import os
import json
from collections import defaultdict

# Load post metadata
root_dir = os.path.dirname(os.path.abspath(__file__))
metadata_file = os.path.join(root_dir, "..", "posts_metadata.json")

with open(metadata_file, "r") as file:
    posts = json.load(file)

# Group posts by categories
categories = defaultdict(list)
for post in posts:
    for category in post.get("categories", []):  # Ensure it works for missing or empty 'categories'
        categories[category].append(post)

# HTML template for category pages
CATEGORY_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kyle Darden - Portfolio</title>
    <link rel="stylesheet" href="../css/styles.css">
    <link rel="icon" type="image/png" href="../assets/images/ann_favicon_16px.png">
</head>
<body>
    <div class="container">
        <div class="sidebar left-sidebar">
            <h1 class="name">Kyle Darden</h1>
            <img src="../assets/images/profile_picture.jpg" alt="Your Photo" class="profile-photo">
            <div class="summary">
                <p>I am a passionate and detail-oriented data professional eager to launch my career as a data analyst or data scientist. With a strong foundation in data analysis, statistical modeling, and data visualization, I am excited to transform complex data into actionable insights that drive meaningful impact.</p>
                <p>I recently completed a postgraduate program in Machine Learning and AI at the McCombs School of Business, University of Texas, earning a 4.22/4.33 GPA. I am ready to apply my knowledge and technical expertise to solve real-world problems while thriving in a collaborative and innovative environment. I look forward to contributing to a team and growing as a data professional through hands-on experience in data science and analytics.</p>

            </div>
            <div class="links">
                <a href="https://github.com/dardenkyle" target="_blank">GitHub</a>
                <a href="https://www.linkedin.com/in/kyle-darden" target="_blank">LinkedIn</a>
                <a href="https://www.kaggle.com/kyledarden" target="_blank">Kaggle</a>
            </div>
        </div>
        <div class="sidebar right-sidebar">
            <!-- Right sidebar content (left blank intentionally) -->
        </div>
        <div class="main-content">
            <nav class="nav-bar">
                <div class="nav-links">
                    <a href="/">Home</a>
                    <a href="/projects/">Projects</a>
                    <a href="/certificates/">Certificates</a>
                    <a href="/contact/">Contact</a>
                </div>
            </nav>
            <h1>{category}</h1>
            <section class="posts">
            {posts}
            </section>
        </div>
        <footer>
            <p>&copy; 2025 Kyle Darden. All rights reserved.</p>
        </footer>
    </div>
    
</html>
"""

# Generate category pages
output_dir = os.path.join(root_dir, "..", "category")
os.makedirs(output_dir, exist_ok=True)

for category, posts_list in categories.items():
    posts_html = ""
    for post in posts_list:
        # Generate links for categories at the end of each post
        sorted_categories = sorted(post["categories"])
        category_links = ", ".join(
            f"<a href='{category.lower().replace(' ', '-')}.html' class='category_category_link'>{category}</a>" for category in sorted_categories
        )
        posts_html += f"""
        <article>
            <h2><a href="../posts/{post['filename']}" class="category_post_link">{post['title']}</a></h2>
            <hr class="separator_category">
            <p>All Categories: {category_links}</p>
        </article>
        """
    category_page = CATEGORY_TEMPLATE.format(category=category, posts=posts_html)
    with open(os.path.join(output_dir, f"{category.lower().replace(' ', '-')}.html"), "w") as file:
        file.write(category_page)

print("Category pages generated successfully!")

# Generate posts with category links
posts_output_dir = os.path.join(root_dir, "..", "posts")
os.makedirs(posts_output_dir, exist_ok=True)

POST_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kyle Darden - Portfolio</title>
    <link rel="stylesheet" href="../css/styles.css">
    <link rel="icon" type="image/png" href="assets/images/ann_favicon_16px.png">
</head>
<body>
    <div class="container">
        <div class="sidebar left-sidebar">
            <h1 class="name">Kyle Darden</h1>
            <img src="../assets/images/profile_picture.jpg" alt="Your Photo" class="profile-photo">
            <div class="summary">
                <p>I am a passionate and detail-oriented data professional eager to launch my career as a data analyst or data scientist. With a strong foundation in data analysis, statistical modeling, and data visualization, I am excited to transform complex data into actionable insights that drive meaningful impact.</p>
                <p>I recently completed a postgraduate program in Machine Learning and AI at the McCombs School of Business, University of Texas, earning a 4.22/4.33 GPA. I am ready to apply my knowledge and technical expertise to solve real-world problems while thriving in a collaborative and innovative environment. I look forward to contributing to a team and growing as a data professional through hands-on experience in data science and analytics.</p>
            </div>
            <div class="links">
                <a href="https://github.com/dardenkyle" target="_blank">GitHub</a>
                <a href="https://www.linkedin.com/in/kyle-darden" target="_blank">LinkedIn</a>
                <a href="https://www.kaggle.com/kyledarden" target="_blank">Kaggle</a>
            </div>
        </div>
        <div class="sidebar right-sidebar">
            <!-- Right sidebar content (left blank intentionally) -->
        </div>
        <div class="main-content">
            <nav class="nav-bar">
                <div class="nav-links">
                    <a href="/">Home</a>
                    <a href="/projects/">Projects</a>
                    <a href="/certificates/">Certificates</a>
                    <a href="/contact/">Contact</a>
                </div>
            </nav>
            <article>
            <h1>{title}</h1>
            <p class="date">Posted on {date}</p>
            <p>{content}</p>
            <hr class="separator_category">
            <p>Categories: {category_links}</p>
            </article>
            <footer>
                <p>&copy; 2025 Kyle Darden. All rights reserved.</p>
            </footer>
        </div>
     
    </div>
    
</html>
"""

for post in posts:
    post_path = os.path.join(posts_output_dir, post["filename"])
    # Check if post page exists and skip if so
    if os.path.exists(post_path):
        print(f"Post page {post['filename']} already exists. Skipping.")
        continue
    category_links = ", ".join(
        f"<a href='../category/{category.lower().replace(' ', '-')}.html' class='post_category_links'>{category}</a>" 
        for category in post["categories"]
    )
    post_content = POST_TEMPLATE.format(
        title=post["title"],
        date=post["date"],
        content="Post content goes here...",  # Replace with actual content
        category_links=category_links
    )
    with open(post_path, "w") as file:
        file.write(post_content)

print("Post pages generated successfully!")

# Update the updates (index) page
updates_page_path = os.path.join(root_dir, "..", "index.html")
updates_html = ""
for post in sorted(posts, key=lambda x: x["date"], reverse=True)[:5]:
    updates_html += f"""
    <article>
        <h4><a href=\"posts/{post['filename']}\", class="updates_title">{post['title']}</a></h4>
        <p>{post['summary']}</p>
        <p class=\"date\">Posted on {post['date']}</p>
        <hr class="separator_category">
    </article>
    """

UPDATES_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kyle Darden - Portfolio</title>
    <link rel="stylesheet" href="css/styles.css">
    <link rel="icon" type="image/png" href="assets/images/ann_favicon_16px.png">
</head>
<body>
    <div class="container">
        <div class="sidebar left-sidebar">
            <h1 class="name">Kyle Darden</h1>
            <img src="assets/images/profile_picture.jpg" alt="Your Photo" class="profile-photo">
            <div class="summary">
                <p>I am a passionate and detail-oriented data professional eager to launch my career as a data analyst or data scientist. With a strong foundation in data analysis, statistical modeling, and data visualization, I am excited to transform complex data into actionable insights that drive meaningful impact.</p>
                <p>I recently completed a postgraduate program in Machine Learning and AI at the McCombs School of Business, University of Texas, earning a 4.22/4.33 GPA. I am ready to apply my knowledge and technical expertise to solve real-world problems while thriving in a collaborative and innovative environment. I look forward to contributing to a team and growing as a data professional through hands-on experience in data science and analytics.</p>
            </div>
            <div class="links">
                <a href="https://github.com/dardenkyle" target="_blank">GitHub</a>
                <a href="https://www.linkedin.com/in/kyle-darden" target="_blank">LinkedIn</a>
                <a href="https://www.kaggle.com/kyledarden" target="_blank">Kaggle</a>
            </div>
        </div>
        <div class="sidebar right-sidebar">
            <!-- Right sidebar content (left blank intentionally) -->
        </div>
        <div class="main-content">
            <nav class="nav-bar">
                <div class="nav-links">
                    <a href="/" class="current">Home</a>
                    <a href="/projects/">Projects</a>
                    <a href="/certificates/">Certificates</a>
                    <a href="/contact/">Contact</a>
                </div>
            </nav>
            <h2 class="title">Recent Updates</h2>
            <hr class="separator_category">
            <section class=\"updates\">
            {updates}
            </section>
            <footer>
                <p>&copy; 2025 Kyle Darden. All rights reserved.</p>
            </footer>                   
        </div>
    </div>
    
</body>
</html>

"""

with open(updates_page_path, "w") as file:
    file.write(UPDATES_TEMPLATE.format(updates=updates_html))

print("Updates page generated successfully!")