# codezax
Codezax is an educational platform which contains information like blog, courses, etc..!!


## Installation
1. Clone the repository to your local machine.
```
git clone https://github.com/username/project.git
```

2. Create a virtual environment.
```
python -m venv env
```

3. Activate the virtual environment.
```
source env/bin/activate
```

4. Install the dependencies.
```
pip install -r requirements.txt
```

5. Create a .env file and add the necessary environment variables (e.g. database credentials).
```
SECRET_KEY=your_secret_key_here
DATABASE_NAME=your_database_name_here
DATABASE_USER=your_database_user_here
DATABASE_PASSWORD=your_database_password_here
DATABASE_HOST=your_database_host_here
DATABASE_PORT=your_database_port_here
```
* for this project I have added .env, you have to change the values here. *

6. Run the migrations.
```
python manage.py migrate
```

## Usage
1. Run the development server.
```
python manage.py runserver
```

2. Open the browser and go to http://localhost:8000/ to view the project.



## Contributing
1. Fork the repository.
2. Create a new branch with your changes.
```
git checkout -b your-branch-name
```

3. Make your changes and commit them.
```
git commit -m "your commit message"
```

4. Push your changes to your fork.
```
git push origin your-branch-name
```

5. Create a pull request.
