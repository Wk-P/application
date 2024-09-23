# 等待 5 秒
Start-Sleep -Seconds 5

# 定义要检查的端口
$port = 3000

# 获取所有网络接口信息，排除虚拟网卡
$nets = Get-NetIPAddress -AddressFamily IPv4 | Where-Object { $_.AddressFamily -eq 'IPv4' -and $_.InterfaceAlias -notlike '*Virtual*' }

# 查找 192.x.x.x 地址
$localIPAddress = $nets | Where-Object { $_.IPAddress -like '192.*' } | Select-Object -First 1 -ExpandProperty IPAddress

# 检查是否找到了有效的 IP 地址
if (-not $localIPAddress) {
    Write-Host "No private IP address found, using localhost."
    $localIPAddress = "localhost"
} else {
    Write-Host "Found private IP address: $localIPAddress"
}

# 检查端口是否在使用中
$tcpConnection = Get-NetTCPConnection -LocalPort $port -ErrorAction SilentlyContinue
if ($tcpConnection) {
    $processId = $tcpConnection | Select-Object -First 1 -ExpandProperty OwningProcess
    if ($processId) {
        $processInfo = Get-Process -Id $processId
        Write-Host "Port $port is currently in use by process $($processInfo.Name) (ID $($processInfo.Id))."
        Write-Host "Stopping process..."
        Stop-Process -Id $processInfo.Id -Force
        Write-Host "Process stopped."
    } else {
        Write-Host "Port $port is in use, but no process ID found."
    }
} else {
    Write-Host "Port $port is not in use."
}

# 进入 Vue 项目目录
cd "D:\github\application\VueProject"

# 启动 Vue 开发服务器
npm run dev
