export function getCSRFToken(): Promise<string> {
    return fetch("/api/csrftoken/")
    .then(response => {
        if (!response.ok) {
            throw new Error("无法获取令牌");
        } else {
            return response.json();
        }
    }).then(data => {
        return data['csrf-token'];
    }).catch(error => {
        return error;
    });
}