$port = 3000

# Use netstat to check if the specified port is in use
$processInfo = netstat -aon | findstr ":$port"

# If the port is in use
if ($processInfo) {
    # Get the PID of the process using the port
    $processId = $processInfo.Split()[-1]

    # Check if PID is valid and not '0' (Idle process)
    if ($processId -match '^\d+$' -and $processId -ne 0) {
        Stop-Process -Id $processId -Force
        Write-Host "Released port $port, process with ID $processId has been terminated"
    } else {
        Write-Host "No valid process ID found or process is not terminable (e.g., Idle)"
    }
} else {
    Write-Host "Port $port is not in use"
}

Start-Sleep -Seconds 5

Write-Host "Change directory path"
cd C:\Projects\github\application\VueProject

Write-Host "Start Vue Project"
npm run dev

Write-Host "Change directory path"
cd C:\Projects\github\application
