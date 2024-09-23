cd "D:\github\application\DjangoProject\"

# Activate virtual environment (if applicable)
.\.venv\Scripts\Activate

# Navigate to the Django project directory
cd "D:\github\application\DjangoProject\BackendService"

# Remove the existing SQLite database file (if exists)
if (Test-Path "db.sqlite3") {
    Remove-Item "db.sqlite3"
    Write-Host "Removed existing db.sqlite3 file"
}

cd "D:\github\application\DjangoProject\BackendService\"


# Recreate the database and apply migrations
python manage.py makemigrations
python manage.py migrate

# create test user and admin user
python manage.py create_users

# Run the Django development server
python manage.py runserver


cd "D:\github\application\"