import type { User } from "@/types/index";
import { useUserStore } from "@/stores/index";
import { useRouter, useRoute } from "vue-router"


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

export async function login(
    event: Event,
    username: string,
    password: string,
    route: any,
): Promise<{ success: boolean; user?: User }> {
    event.preventDefault();

    function isInputEmpty() {
        if (username === "") {
            alert("Username no input");
            return false;
        }

        if (password === "") {
            alert("Password no input");
            return false;
        }
        return true;
    }

    if (!isInputEmpty()) return { success: false };

    const current_path = route.path;

    if (username === "admin" && !current_path.startsWith('/admin')) {
        alert("관리자 계정으로 로그인 금지");
        return { success: false };
    }

    try {
        const tokenResponse = await fetch("/api/token/auth/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ username, password }),
        });

        if (!tokenResponse.ok) {
            if (tokenResponse.status === 400 || tokenResponse.status === 403) {
                alert("비밀번호 아이디 정보가 일치하지 않습니다");
            } else {
                throw new Error(`HTTP error! status: ${tokenResponse.status}`);
            }
            return { success: false };
        }

        const tokenData = await tokenResponse.json();
        const token = tokenData.token;

        const userResponse = await fetch("/api/user/login/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ username, password }),
        });

        if (!userResponse.ok) {
            throw new Error(`HTTP error! status: ${userResponse.status}`);
        }

        const userData = await userResponse.json();

        const userObj: User = {
            id: userData.user.id,
            uid: userData.user.uid,
            email: userData.user.email,
            name: userData.user.name,
            tel: userData.user.tel,
            username: username,
            token: token,
        };

        return { success: true, user: userObj };

    } catch (error) {
        console.error("Error during login:", error);
        return { success: false };
    }
}


export function logout() {
    const userStore = useUserStore();
    const token = userStore.user?.token; // 获取 token
    console.log(token);

    if (!token) {
        console.error("No token found");
        return;
    }

    fetch('/api/user/logout/', {
        method: 'POST',
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Token ${userStore.user?.token}`
        },
        body: JSON.stringify({})
    }).then(async (response) => {
        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.message || 'Logout failed');
        } else {
            return response.json();
        }
    }).then((data) => {
        alert("Logout success");
    }).catch((error: Error) => {
        alert("Logout failed")
        console.error(error.message);
    });
    userStore.clearUser();
}