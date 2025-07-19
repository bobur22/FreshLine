<div align="center" style="display: flex; justify-content: center; align-items: center; gap: 20px;">

  <a href="https://fresh-line.uz/">
    <img width="300px" height="100px" src="https://www.fresh-line.uz/assets/logom-BD7_HYib.png" />
  </a>

</div>

<h1 align="center">👋 Welcome to Fresh Line project.</h1>
<h3 align="center">A passionate backend developer from Uzbekistan</h3>

---

## 🌐 Live Links

- 🔗 [Live Website](https://fresh-line.uz/)
- 🖥️ [Frontend Repository](https://github.com/murodil01/fresh_line_front.git)

---

## 🧠 Introduction

This is the official repository for the **Fresh Line Platform**.  
It is a backend API developed to efficiently manage and serve business-critical data for the Fresh Line platform.

---

## ⚙️ Getting Started

Follow the steps below to set up the project on your local machine.

## Before start clone the repository to your lap top.
    git@github.com:bobur22/FreshLine.git
    
## And then open your terminal and start creating by venv file
      python3 -m venv venv
      
## then activate venv file.

## And after that go on installing requirements.txt
    pip install -r requirements.txt
    
## then make a migrations.
    python3 manage.py makemigrations
    
## and after that migrate it.
    python3 manage.py migrate

## before runing server create super user in order to open admin panel.
    python3 manage.py createsuperuser

## then finally start project.
    python3 manage.py runserver

#Then you can open website on your local host.
## and project is ready.
