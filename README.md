# application
Test remote linux server to github.com with SSH 
Test remote linux server to github.com with SSH
Test remote linux server to github.com with SSH

# 自签发免费证书

1. 下载 certbot 并生成证书
```shell
sudo apt update
sudo apt install certbot python3-certbot-nginx

sudo certbot certonly --nginx -d cskbusiness.com
```

2. 更改 nginx 配置
```nginx.conf
server {
    listen 443 ssl;
    server_name cskbusiness.com www.cskbusiness.com;

    ssl_certificate /etc/letsencrypt/live/cskbusiness.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/cskbusiness.com/privkey.pem;

    ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
    ssl_ciphers HIGH:!aNULL:!MD5;
}
```

3. 重启 nginx 服务
```shell
sudo nginx -t

sudo systemctl restart nginx

```


# Django 类使用
## 1. 类本身
## 2. 类字段序列化