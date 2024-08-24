<template>
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
            <div>
                <label class="checkbox-label">
                    <input type="checkbox" name="autologin" value="autologin" />
                    <div class="custom-checkbox"></div>
                    <span> 자동그로인 </span>
                </label>
            </div>
            <div class="button-block">
                <button @click="login"> 로그인 </button>
            </div>
            <div class="recover-link">
                <a href="#">{{ linkText }} </a>
            </div>
            <div class="login-register-link">
                <RouterLink to="/register/step1"><button class="register-button"> 회원가입 </button></RouterLink>
            </div>
        </form>
        <footer><FooterBlock /></footer>
    </div>
</template>

<script lang="ts" setup name="login">
import { ref } from "vue";
import { RouterLink } from "vue-router";
import { useRouter } from "vue-router";
import { userTokenStore } from "@/stores/index";
import { getCSRFToken } from "@/utils/validate";
import FooterBlock from "@/components/FooterBlock.vue";

const tokenStore = userTokenStore();
const router = useRouter();
const username = ref("");
const password = ref("");
const linkText = ref('아이디 찾기/비밀번호 찾기 >                               ');


async function login(event: Event) {
    event.preventDefault();

    getCSRFToken()
        .then((csrfToken) => {
            if (csrfToken === null) {
                throw new Error("Invalid Token");
            }

            const url = "/backend/api/user/login";
            let params = "";

            if (params == "") {
                params += "/";
            }

            // 向后端Token处理器发出请求
            fetch(`${url}/${params}`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": csrfToken,
                },
                body: JSON.stringify({
                    username: username.value,
                    password: password.value,
                }),
            })
                .then((response) => {
                    if (!response.ok) {
                        throw new Error("Authentication Invalid");
                    }
                    return response.json();
                })
                .then((data) => {
                    // save token and into pinia

                    tokenStore.setToken(csrfToken, username.value);
                    router.push("/");
                })
                .catch((error) => {
                    console.error(error);
                    alert(error.message);
                });
        })
        .catch((error) => {
            console.error(error.message);
        });
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
    padding-left: 5%;
}

.recover-link a {
    text-decoration: none;
    color: black;
}

.recover-link a:hover {
    cursor: pointer;
}

.login-register-link {
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
