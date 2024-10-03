# Get the directory of the current script
$appDir = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Definition)
$managePyDir = "$appDir\DjangoProject\BackendService"

# Navigate to the Django project root directory
Set-Location "$appDir\DjangoProject"

# Check if the virtual environment exists and activate it
if (Test-Path "$appDir\DjangoProject\.venv\Scripts\Activate") {
    .\.venv\Scripts\Activate
    Write-Host "Virtual environment activated."
} else {
    Write-Host "Virtual environment not found. Please create one first."
    exit
}

Set-Location "$managePyDir"

# Remove the existing SQLite database file (if exists)
if (Test-Path "db.sqlite3") {
    Remove-Item "db.sqlite3"
    Write-Host "Removed existing db.sqlite3 file"
}

# Recreate the database and apply migrations
python $managePyDir\manage.py makemigrations
python $managePyDir\manage.py migrate

# Create test user and admin user
python $managePyDir\manage.py create_users
python $managePyDir\manage.py create_item

# Run the Django development server
python $managePyDir\manage.py runserver
