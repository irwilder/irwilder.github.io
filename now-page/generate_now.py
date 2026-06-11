import json
import os

with open("now-page/now.json", "r") as f:
    data = json.load(f)

current_cert = data["certifications"]["current"]["name"]
current_cert_date = data["certifications"]["current"]["target_date"]
current_cert_progress = data["certifications"]["current"]["target_date"]
recent_cert = data["certifications"]["recent"]["name"]
recent_cert_date = data["certifications"]["recent"]["date_earned"]

lab_platform = data["labs"]["platform"]
lab_url = data["labs"]["profile_url"]
lab_focus = data["labs"]["current_focus"]

book_title = data["reading"]["title"]
book_author = data["reading"]["author"]

school_degree = data["school"]["degree"]
school_institution = data["school"]["institution"]

html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Now | Ian Wilder</title>
    <style>
        body {{
            font-family: sans-serif;
            max-width: 660;
            margin: 60px auto;
            padding: 0 20px;
            color: #333;
            line-height: 1.6;

        }}
        h1 {{ font-size 1.5rem; margin-bottom: 4px; }}
        .subtitle {{ color: #888; font-size: 0.9rem; margin-bottom: 2rem; }}
        .section-label {{
            font-size: 0.7rem;
            font-weight: 600;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            color: #999;
            margin: 1.5rem 0 0.5rem;
        }}
        .card {{
            border: 1px solid #e5e5e5;
            border-radius: 8px;
            padding: 1rem 1.25rem;
            margin-bottom: 10px;
        }}
        .card-title{{ font-size: 0.8rem; color: #888; margin: 0 0 4px }}
        .card-value{{ font-size 1rem; font-weight: 500; margin: 0; }}
        .card-sub{{ font-size: 0.8rem; color: #aaa; margin: 4px 0 0; }}
        .grid-2 {{ display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }}
        .progress-bar {{
            height: 4px;
            background: #eee;
            border-radius: 4px;
            margin-top: 10px;
        }}
        .progress-fill {{
            height: 4px;
            border-radius: 4px;
            background: #185FA5;
            width: {current_cert_progress}%;
        }}
    </style>
</head>
<body>

    <h1>What I'm working on</h1>
    <p class="subtitle">Updated June 2026 - a live snapshot of where my focus is right now.</p>
    
    <p class="selection-label">Certifications</p>
    <div class="grid-2">
        <div class="card">
            <p class="card-title">Current goal</p>
            <p class="card-value">{current_cert}</p>
            <p class="card-sub>Target: {current_cert_date}</p>
            <div class="progress-bar">
                <div class="progress-fill"></div>
            </div>
        </div>
        <div class="card">
            <p class="card-title">Recently earned</p>
            <p class="card-value">{recent_cert}</p>
            <p class="card-sub">Completed {recent_cert_date}</p>
        </div>
    </div>

    <p class="section-label">Labs &amp; practice</p>
    <div class="card">
        <p class="card-title">Platform</p>
        <p class="card-value">{lab_platform}</p>
        <p class="card-sub"><a href="{lab_url}">View my profile</a></p>
    </div>
    <div class="card">
        <p class="card-title">Current focus</p>
        <p class="card-value">{lab_focus}</p>
    </div>

    <p class="section-label">Currently reading</p>
    <div class="card">
        <p class="card-title">Book</p>
        <p class="card-value">{book_title}</p>
        <p class="card-sub">{book_author}</p>
    </div>

    <p class="section-label">School</p>
    <div class="card">
        <p class="card-title">{school_institution}</p>
        <p class="card-value">{school_degree}</p>
    </div>

</body>
</html>
"""

os.makedirs("static/now", exist_ok=True)

with open("static/now/index.html", "w") as f:
    f.write(html)

print("now page generated successfully")