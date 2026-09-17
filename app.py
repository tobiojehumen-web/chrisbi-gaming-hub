
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Chrïṣbï Gaming Hub</title>

<style>
* {
    box-sizing: border-box;
    scroll-behavior: smooth;
}

body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: #050816;
    color: white;
}

header {
    padding: 18px 8%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: rgba(5, 8, 22, 0.95);
    border-bottom: 1px solid #24345e;
    position: sticky;
    top: 0;
    z-index: 10;
}

.logo {
    color: #00f7ff;
    font-size: 20px;
    font-weight: bold;
}

nav a {
    color: #c9d6f5;
    text-decoration: none;
    margin-left: 15px;
    font-size: 13px;
}

nav a:hover {
    color: #00f7ff;
}

.hero {
    text-align: center;
    padding: 75px 20px;
    background:
        radial-gradient(circle at top, #173b67, #050816 65%);
}

.badge {
    display: inline-block;
    padding: 8px 15px;
    border: 1px solid #00f7ff;
    border-radius: 30px;
    color: #00f7ff;
    font-size: 12px;
}

.hero h1 {
    font-size: clamp(32px, 8vw, 60px);
    margin: 20px 0 10px;
    color: #00f7ff;
    text-shadow: 0 0 20px #00f7ff;
}

.hero p {
    max-width: 550px;
    margin: 15px auto;
    color: #b8c6e5;
    line-height: 1.7;
}

.button {
    display: inline-block;
    padding: 13px 20px;
    margin: 8px 4px;
    border-radius: 10px;
    text-decoration: none;
    font-weight: bold;
    background: #00f7ff;
    color: #06101c;
    transition: 0.3s;
}

.button:hover {
    transform: translateY(-3px);
    background: white;
}

.button.secondary {
    background: transparent;
    border: 1px solid #00f7ff;
    color: #00f7ff;
}

.container {
    max-width: 1050px;
    margin: auto;
    padding: 35px 18px;
}

.section-title {
    text-align: center;
    margin-bottom: 25px;
}

.section-title h2 {
    color: #00f7ff;
    font-size: 30px;
}

.section-title p {
    color: #91a5cf;
}

.card {
    background: linear-gradient(145deg, #111d3b, #0a1228);
    border: 1px solid #263b69;
    border-radius: 18px;
    padding: 28px;
    margin-bottom: 25px;
    box-shadow: 0 8px 30px rgba(0,0,0,0.25);
}

.card h2 {
    color: #00f7ff;
}

.card p {
    color: #b8c6e5;
    line-height: 1.7;
}

.profile {
    width: 115px;
    height: 115px;
    display: flex;
    justify-content: center;
    align-items: center;
    margin: auto;
    border-radius: 50%;
    background: linear-gradient(135deg, #00f7ff, #5c00ff);
    color: white;
    font-size: 50px;
    font-weight: bold;
    box-shadow: 0 0 30px rgba(0,247,255,0.4);
}

.center {
    text-align: center;
}

.grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 18px;
}

.service {
    padding: 22px;
    background: #080f25;
    border: 1px solid #293765;
    border-radius: 14px;
    transition: 0.3s;
}

.service:hover {
    transform: translateY(-5px);
    border-color: #00f7ff;
}

.service h3 {
    color: white;
}

.service p {
    font-size: 14px;
}

.skills span {
    display: inline-block;
    background: #18294e;
    border: 1px solid #35538a;
    color: #c9eaff;
    padding: 9px 13px;
    border-radius: 20px;
    margin: 5px;
    font-size: 13px;
}

.gallery {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 12px;
}

.gallery div {
    min-height: 120px;
    display: flex;
    justify-content: center;
    align-items: center;
    background: #080f25;
    border: 1px solid #293765;
    border-radius: 14px;
    font-size: 38px;
}

footer {
    text-align: center;
    padding: 35px 15px;
    color: #7083ad;
    border-top: 1px solid #1e2b4d;
    font-size: 13px;
}

@media (max-width: 700px) {
    header {
        padding: 15px;
        flex-direction: column;
        gap: 12px;
    }

    nav a {
        margin: 0 6px;
    }

    .grid {
        grid-template-columns: 1fr;
    }

    .gallery {
        grid-template-columns: repeat(2, 1fr);
    }

    .card {
        padding: 22px 17px;
    }
}
</style>
</head>

<body>

<header>
    <div class="logo">CHRISBI HUB ⚡</div>

    <nav>
        <a href="#about">About</a>
        <a href="#services">Services</a>
        <a href="#contact">Contact</a>
    </nav>
</header>

<section class="hero">
    <span class="badge">🎮 GAMER • CREATOR • DEVELOPER</span>

    <h1>ChrïṣbïØtc11</h1>

    <p>
        Welcome to Chrïṣbï Gaming Hub —
        a growing digital brand focused on gaming,
        creativity, and beginner web development.
    </p>

    <a class="button" href="#services">Explore Services</a>
    <a class="button secondary" href="#contact">Work With Me</a>
</section>

<div class="container">

    <section class="card center" id="about">
        <div class="profile">C</div>

        <h2>About Chrïṣbï</h2>

        <p>
            I'm ChrïṣbïØtc11, a Free Fire enthusiast
            and beginner Python web developer.
            I'm building practical digital projects
            while improving my coding skills.
        </p>

        <div class="skills">
            <span>🎮 Free Fire</span>
            <span>🐍 Python</span>
            <span>🌐 HTML & CSS</span>
            <span>💡 Creativity</span>
        </div>
    </section>

    <section id="services">
        <div class="section-title">
            <h2>My Services</h2>
            <p>Simple digital solutions for individuals and small brands.</p>
        </div>

        <div class="grid">

            <div class="service">
                <h3>🎮 Gaming Websites</h3>
                <p>
                    Simple profile websites for gamers,
                    gaming communities, and personal brands.
                </p>
            </div>

            <div class="service">
                <h3>🌐 Personal Websites</h3>
                <p>
                    Basic responsive websites
                    for portfolios and small projects.
                </p>
            </div>

            <div class="service">
                <h3>🐍 Python Projects</h3>
                <p>
                    Beginner-level Python programs
                    and small learning projects.
                </p>
            </div>

        </div>
    </section>

    <section class="card" style="margin-top:30px;">
        <div class="section-title">
            <h2>Gaming Gallery</h2>
            <p>Sample gaming highlights and creative ideas.</p>
        </div>

        <div class="gallery">
            <div>🎮</div>
            <div>🔥</div>
            <div>🏆</div>
            <div>⚡</div>
        </div>

        <p class="center">
            Real screenshots and project examples
            will be added as my portfolio grows.
        </p>
    </section>

    <section class="card center" id="contact">
        <h2>💼 Let's Work Together</h2>

        <p>
            Need a simple gaming profile website
            or personal web project?
            Contact me to discuss your idea.
        </p>

        <!-- Replace this email with a safe contact address -->
        <a class="button"
           href="mailto:YOUR_EMAIL@example.com">
           📧 Contact Me
        </a>

        <p style="font-size:12px;">
            Use a parent/guardian-approved contact method.
        </p>
    </section>

</div>

<footer>
    © 2026 Chrïṣbï Gaming Hub | Built with Python & Flask ⚡
</footer>

</body>
</html>
"""

if __name__ == "__main__":
    import os

    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )
