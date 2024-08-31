<template>
    <HomeBar />
    <div class="block">
        <h2 class="title">로그인</h2>
        <form>
            <div>
                <h5 class="sub-title">아이디</h5>
            </div>
            <div class="sub-input">
                <input type="text" v-model="username" />
            </div>
            <div>
                <h5 class="sub-title">비밀번호</h5>
            </div>
            <div class="sub-input">
                <input type="password" v-model="password" autocomplete="on" />
            </div>
            <div class="button-block">
                <button @click="login">로그인</button>
            </div>
            <div class="recover-link">
                <p @click="find">{{ linkText }}</p>
            </div>
            <div class="register-link">
                <RouterLink to="/register/step1"
                    ><button class="register-button">
                        회원가입
                    </button></RouterLink
                >
            </div>
        </form>
        <FooterBlock />
    </div>
</template>

<script lang="ts" setup name="login">
import { ref } from "vue";
import { RouterLink } from "vue-router";
import { useRouter } from "vue-router";
import FooterBlock from "@/components/FooterBlock.vue";
import HomeBar from "@/components/HomeBar.vue";
import { useUserStore } from "@/stores/index";
import { onMounted, computed } from "vue";
import type { User } from "@/types/index";

const userStore = useUserStore();
const router = useRouter();
const username = ref("");
const password = ref("");
const linkText = ref(
    "아이디 찾기/비밀번호 찾기 >                               "
);
const isLoggedIn = ref<boolean>(userStore.user?.loginStatus === true ? true : false);
const find = () => {
    alert("No function");
};

onMounted(() => {
    if (isLoggedIn.value) {
        router.push("/start");
    }
});


function login(event: Event) {
    event.preventDefault();
    function isInputEmpty() {
        // check idInput
        if (username.value == "") {
            alert("Username no input");
            return;
        }

        if (password.value == "") {
            alert("Password no input");
            return;
        }
    }

    // login, token, csrf-token
    isInputEmpty();

    if (username.value == "admin") {
        alert("관리자 계정으로 로그인 금지");
        return;
    }

    // get token
    fetch("/api/token/auth/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            username: username.value,
            password: password.value,
        }),
    })
        .then((response) => {
            if (!response.ok) {
                if (response.status == 400 || response.status == 403) {
                    alert("비밀번호 아이디 정보가 일치하지 않습니다");
                } else {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                return;
            }
            const data = response.json();
            return data;
        })
        .then((data) => {
            const token = data.token;
            fetch("/api/user/login/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    username: username.value,
                    password: password.value,
                }),
            })
                .then((response) => {
                    if (!response.ok) {
                        throw new Error(
                            `HTTP error! status: ${response.status}`
                        );
                    }
                    return response.json();
                })
                .then((data) => {
                    isLoggedIn.value = true;
                    const userObj: User = {
                        id: data.user.id,
                        uid: data.user.uid,
                        email: data.user.email,
                        name: data.user.name,
                        tel: data.user.tel,
                        username: data.user.username,
                        loginStatus: isLoggedIn.value,
                        token: token,
                        cookies: data.user.cookies,
                        address: data.user.address,
                    };
                    if (username.value !== "admin") {
                        userStore.setUser(userObj);
                    }
                    router
                        .push("/start")
                        .catch((err) => console.error("Navigation err:", err));
                })
                .catch((error: Error) => {
                    console.error(error);
                });
        });

    // user id and password authenticate
}
</script>
<style scoped>
.block {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-evenly;
    padding: 5% 0;
    border-bottom: 1px solid black;
    margin-bottom: 1px;
}

form {
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    animation: up-shift 0.5s forwards;
}

form div {
    width: 75%;
}

footer {
    box-sizing: border-box;
    width: 90%;
}

.title {
    width: 100%;
    text-align: center;
}

.sub-title {
    width: 100%;
    text-align: left;
}

.sub-input {
    padding: 2% 0 5% 0;
    width: 75%;
}

.sub-input input {
    outline: none;
    box-sizing: border-box;
    padding: 15px;
    border-radius: 0;
    border: 2px solid black;
    font: 13px;
    width: 100%;
}

/* 隐藏原生复选框 */
input[type="checkbox"] {
    position: absolute;
    display: none;
}

/* 创建自定义复选框样式 */
input[type="checkbox"] + .custom-checkbox {
    position: relative;
    display: inline-block;
    width: 20px;
    height: 20px;
    background-color: #fff; /* 背景色为白色 */
    border: 2px solid #000; /* 边框为黑色 */
    border-radius: 3px;
    cursor: pointer;
}

/* 勾选后的样式 */
input[type="checkbox"]:checked + .custom-checkbox {
    background-color: #000; /* 背景色为黑色 */
    border-color: #000; /* 边框保持黑色 */
}

/* 勾选标记 */
input[type="checkbox"]:checked + .custom-checkbox::after {
    content: "";
    position: absolute;
    left: 5px;
    top: 0px;
    width: 6px;
    height: 12px;
    border: solid #fff; /* 对勾颜色为白色 */
    border-width: 0 3px 3px 0;
    transform: rotate(45deg);
}

.checkbox-label {
    display: flex;
    flex-direction: row;
    align-items: center;
}

.checkbox-label span {
    padding-left: 2%;
}

.button-block {
    padding: 10% 0 10px 0;
    width: 75%;
}

.button-block button {
    border: 2px solid black;
    background-color: black;
    color: white;
    box-sizing: border-box;
    width: 100%;
    padding: 15px;
    font-size: 0.8em;
    outline: none;
}

.register-button {
    border: 2px solid black;
    background-color: white;
    color: black;
    box-sizing: border-box;
    width: 100%;
    padding: 25px;
    font-size: 0.8em;
    outline: none;
}

.recover-link {
    font-size: 0.7rem;
    border-bottom: 1px solid black;
    width: 80%;
    padding: 0 0.5em;
}

.recover-link p {
    padding: 0 1em;
    text-decoration: none;
    color: black;
}

.recover-link p:hover {
    cursor: pointer;
}

.register-link {
    padding: 5% 0;
}

@keyframes up-shift {
    from {
        opacity: 0;
        transform: translateY(100px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
</style>
