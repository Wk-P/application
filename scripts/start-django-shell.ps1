Write-Host "Starting the script..."

# 切换到 Django 项目的目录
cd C:\Projects\github\application\DjangoProject

# 激活虚拟环境
.\.venv\Scripts\Activate.ps1
Write-Host "Activated virtual environment"

# 切换到 BackendService 目录
cd C:\Projects\github\application\DjangoProject\BackendService
Write-Host "Changed directory to BackendService"

Write-Host "Start python shell"
python manage.py shell

# 切换到 Django 项目的目录
cd C:\Projects\github\application