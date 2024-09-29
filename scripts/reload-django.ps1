Write-Host "Starting the script..."

# Set variables for paths
$projectPath = "C:\Projects\github\application\DjangoProject"
$backendServicePath = "$projectPath\BackendService"
$activateScript = "$projectPath\.venv\Scripts\Activate.ps1"
$dbFile = "$backendServicePath\db.sqlite3"
$managePy = "$backendServicePath\manage.py"

# Switch to the Django project directory
cd $projectPath
Write-Host "Changed directory to DjangoProject"

# Activate virtual environment
if (Test-Path $activateScript) {
    & $activateScript
    Write-Host "Activated virtual environment"
} else {
    Write-Host "Virtual environment activation script not found!"
    exit
}

# Switch to BackendService directory
cd $backendServicePath
Write-Host "Changed directory to BackendService"

# Delete db.sqlite3 file
if (Test-Path $dbFile) {
    Remove-Item $dbFile -Force
    Write-Host "Deleted db.sqlite3 file"
} else {
    Write-Host "db.sqlite3 file does not exist"
}

# Run database migrations
try {
    python $managePy makemigrations
    Write-Host "Made migrations"

    python $managePy migrate
    Write-Host "Applied migrations"
} catch {
    Write-Host "Error during migrations: $_"
    exit
}

# Collect static files
try {
    python $managePy collectstatic --noinput
    Write-Host "Collected static files"
} catch {
    Write-Host "Error during static file collection: $_"
    exit
}

# Create superusers or any custom user creation
try {
    python $managePy create_users
    Write-Host "Created users"
} catch {
    Write-Host "Error creating users: $_"
}

try {
    python $managePy create_item
    Write-Host "Created item"
} catch {
    Write-Host "Error creating item: $_"
}

# Switch back to application directory
cd C:\Projects\github\application

# Start development server
try {
    python $managePy runserver
    Write-Host "Started development server"
} catch {
    Write-Host "Error starting development server: $_"
}
