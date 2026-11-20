from django.shortcuts import render


# Personal Information
NAME = "Zubair Tahir"
ROLE = "Computer Engineering Student"
UNIVERSITY = "COMSATS University Islamabad"
LOCATION = "Lahore, Pakistan"

EMAIL = "m.zubairtahir17@gmail.com"

GITHUB = "github.com/zubairtahir17-ops"
GITHUB_URL = "https://github.com/zubairtahir17-ops"

LINKEDIN = "linkedin.com/in/zubair-tahir-95b393318"
LINKEDIN_URL = "https://www.linkedin.com/in/zubair-tahir-95b393318"


# Home Page
def home(request):
    context = {
        "name": NAME,
        "role": ROLE,
        "university": UNIVERSITY,
        "location": LOCATION,
    }

    return render(request, "pages/home.html", context)


# About Page
def about(request):
    context = {
        "name": NAME,
        "description": "I am a Computer Engineering student interested in web development, artificial intelligence, embedded systems, and FPGA design.",
        "location": LOCATION,
        "interests": [
            {
                "title": "Python & Django Development",
                "description": "Building web applications and learning backend development.",
            },
            {
                "title": "Full-Stack Web Development",
                "description": "Exploring frontend and backend technologies to build complete applications.",
            },
            {
                "title": "AI & Agentic Systems",
                "description": "Exploring artificial intelligence, local models, and autonomous AI systems.",
            },
            {
                "title": "Embedded Systems & STM32",
                "description": "Working with microcontrollers and hardware-based solutions.",
            },
            {
                "title": "FPGA & Digital Design",
                "description": "Learning digital logic design and programmable hardware.",
            },
        ],
    }

    return render(request, "pages/about.html", context)


# Projects Page
def projects(request):
    context = {
        "projects": [
            {
                "title": "DecisionOS",
                "description": "A local AI-powered decision analysis application.",
                "technology": "Python, FastAPI, React",
            },
            {
                "title": "DisasterGuard AI",
                "description": "An AI-based disaster monitoring and response prototype.",
                "technology": "React, FastAPI, Python",
            },
            {
                "title": "Ride Booking System",
                "description": "A database project for managing ride bookings, drivers, vehicles, and payments.",
                "technology": "SQL Server, Database Design",
            },
        ]
    }

    return render(request, "pages/projects.html", context)


# Contact Page
def contact(request):
    context = {
        "name": NAME,
        "email": EMAIL,
        "github": GITHUB,
        "github_url": GITHUB_URL,
        "linkedin": LINKEDIN,
        "linkedin_url": LINKEDIN_URL,
        "location": LOCATION,
    }

    return render(request, "pages/contact.html", context)