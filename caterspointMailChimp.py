from jinja2 import Template

links = [
    {"title": "Home", "url": "https://www.caterspoint.com/"},
    {"title": "Instagram", "url": "https://www.instagram.com/caterspoint/"},
    {"title": "Twitter", "url": "https://twitter.com/caterspoint"},
    {"title": "LinkedIn", "url": "https://www.linkedin.com/company/caterspoint/mycompany/"},
    {"title": "Zomato", "url": "https://www.zomato.com/ncr/caterspoint-jangpura-new-delhi"},
    {"title": "Swiggy", "url": "https://www.swiggy.com/search?query=caterspoint"},
]

template = Template("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Links</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 50px;
        }
        .link {
            margin: 10px 0;
            display: block;
            padding: 10px;
            background-color: #693452;
            text-decoration: none;
            color: #333;
            border-radius: 5px;
        }
        .link:hover {
            background-color: #ddd;
            transform: perspective(1000px) rotateY(90deg) rotateX(0deg)
        }
    </style>
</head>
<body>
    <h1>Caterspoint</h1>
    {% for link in links %}
        <a class="link" href="{{ link.url }}">{{ link.title }}</a>
    {% endfor %}
</body>
</html>
""")

html_content = template.render(links=links)

with open("linksMailchimp.html", "w") as file:
    file.write(html_content)

print("HTML file has been generated successfully.")
