<h1 align="center">
    <img src="https://github.com/user-attachments/assets/e62e896a-070c-470d-88d4-52f53fb584f5" alt="logo" height="70px" align="center"/><br>
    HireHive
</h1>

# How to install
To keep a copy of our project, you can follow the next steps:
1. (Optional) Fork the repository.
2. Clone the repository.
  ```bash
    git clone https://github.com/svillav4/HireHive.git
  ```
  * Make sure you are in the folder:
  ```bash
    cd ./HireHive
  ```
3. Create a Python virtual environment.
  ```bash
    python -m venv venv
  ```
4. Activate the virtual environment.
  ```bash
    ./venv/scripts/activate
  ``` 
5. Install the required libraries, using the ``` requirements.txt ``` file.
  ```bash
    pip install -r requirements.txt
  ```
  * Up to this point, your folder should look like this:
  ```bash
    HireHive
    ├───accounts                    
    ├───hirehive_project
    ├───locale
    ├───media
    ├───payments
    ├───services
    ├───venv
    ├───.gitignore
    ├───db.sqlite3
    ├───manage.py
    ├───README.md
    └───requirements.txt
  ```
6. Internationalization (i18n) and Translations

This project supports multiple languages using Django's built-in internationalization system. Translation files are located in the `locale/` directory and include `.po` files (editable text) and `.mo` files (compiled binary used by Django). Install GNU gettext tools. These are required to compile `.po` files into `.mo` files.

See the complete documentation of Django translation [here](https://docs.djangoproject.com/en/5.1/topics/i18n/translation/#the-set-language-redirect-view)

- Linux (Ubuntu/Debian):
  ```bash
  sudo apt update && sudo apt install gettext
  ```
  
- macOS (using Homebrew):
  ```bash
  brew install gettext
  brew link gettext --force
  ```
  
- Windows:
  Download and install from https://mlocati.github.io/articles/gettext-iconv-windows.html
  
  Then add the bin/ folder to your system PATH.


- Compile Translation Files
  From your Django project root, run:
  ```bash
    python manage.py compilemessages
  ```
  
- This will generate .mo files in the corresponding locale folders
  ```bash
  ├───locale
      └── es/
          └── LC_MESSAGES/
              ├── django.po
              └── django.mo  ← generated after compilemessages
      └── en/
          └── LC_MESSAGES/
              ├── django.po
              └── django.mo  ← generated after compilemessages
  ```
  
7.  Run the development server.
  ```bash
    python manage.py runserver
  ```

# License
Copyright 2025, Samuel Villa, Juan José Botero, Mateo García. All rights reserved HireHive.
