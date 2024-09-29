# Requests & Responses
get favorite items

- Request:
```javascript
{
    url: `/api/items/favorite/${username}/`,
    method: "GET",
}
```
- Response:
```javascript
{
    user: User,
    items: Array<Item> 
}
```

delete favoritem items
```javascript
{
    url: `/api/items/favorite/delete/${username}/`,
    method: "POST",
    headers: { "Content-Type": "application/json" },
    data: {
        item: Item,
        user: User
    }
}
```

get notices
- Request:
```javascript
{
    url: `/api/notice/all/`,
    method: "GET",
}
```

- Response:
```javascript
{
    Array<Notice>
}
```

get notice
- Request:
```javascript
{
    url: `/api/notice/${notice_id}/`,
    method: "GET",
}
```

- Response:
```javascript
{
    Array<Notice>
}
```