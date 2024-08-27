<template>
    <div class="block">
        <div class="progress-bar-block">
            <div class="progress-bar">
                <div class="custom-progress"></div>
            </div>
            <div class="progress-text-block">
                <span>{{ progressText }}</span>
            </div>
        </div>
        <form>
            <div class="form-n">
                <h5 class="sub-title">이이디</h5>
                <div class="sub-input">
                    <input type="text" v-model="username" />
                    <label ref="usernameFor">{{ usernameLabalText }}</label>
                </div>
            </div>
            <div class="form-n">
                <h5 class="sub-title">비밀번호</h5>
                <div class="sub-input">
                    <input type="password" v-model="password1" />
                    <label ref="passwordFor">{{ passwordLabelText }}</label>
                </div>
            </div>

            <div class="button-block">
                <button
                    ref="nextButton"
                    :style="nextButtonStyle"
                    @click="register"
                    :disabled="isDisabled"
                >
                    등록
                </button>
            </div>
        </form>
    </div>
</template>

<script lang="ts" setup name="Step1Register">
import router from "@/router";
import { ref } from "vue";
import { onMounted } from "vue";
import { watch } from "vue";
import type { User } from "@/types/index";
import { useUserStore } from "@/stores";

const usernameLabalText = ref<string>(" ");
const passwordLabelText = ref<string>(" ");

const userStore = useUserStore();

const progressText = ref<string>("2/2");
const username = ref<string>("");
const nextButton = ref<HTMLButtonElement | null>(null);
const nextButtonStyle = ref();
const password1 = ref<string>("");

const isDisabled = ref<boolean>(false);

function isValidUsername(name: string) {
    const usernameRegex = /^[a-zA-Z0-9_]{3,20}$/;
    return usernameRegex.test(name);
}

function isValidPassword(password: string) {
    const passwordRegex =
        /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
    return passwordRegex.test(password);
}

async function register(event: Event) {
    event.preventDefault();

    // if (!isValidUsername(username.value)) {
    //     alert("名称格式不正确");
    //     return;
    // }

    // // 注意修改后端需要分类保存
    // if (!isValidPassword(password1.value)) {
    //     alert("密码格式不正确");
    //     return;
    // }

    // 从前面获取name和 tel email
    const userinfo = {
        name: localStorage.getItem("name") !== null ? localStorage.getItem("name") : '',
        email: localStorage.getItem("email") !== null ? localStorage.getItem("email") : '',
        tel: localStorage.getItem("tel") !== null ? localStorage.getItem("tel") : '',
        username: username.value,
        password: password1.value,
    };

    localStorage.clear();

    // 先申请向后端数据库保存用户数据, 再清除本地使用过的痕迹
    fetch("/api/user/register/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(userinfo),
    })
        .then((response) => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const data = response.json();
            return data;
        })
        .then((data) => {
            console.log(data);

            router.push({ name: "login" }).catch((err) => {
                console.error("Navigation err:", err);
            });
        })
        .catch((error: Error) => {
            console.error(error);
        });
}

onMounted(() => {
    // 检测localStorage 是否有前置 step1 信息
    localStorage.getItem("name");
    updateButtonStyle();
});

function updateButtonStyle() {
    if (username.value !== "" && password1.value !== "") {
        isDisabled.value = false;
        nextButtonStyle.value = {
            color: "white",
            backgroundColor: "black",
            borderColor: "black",
        };
    } else {
        isDisabled.value = true;
        nextButtonStyle.value = {
            color: "white",
            backgroundColor: "#bbb",
            borderColor: "#bbb",
        };
    }
}

watch([username, password1], updateButtonStyle);
</script>

<style scoped>
.block {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: start;
    padding-top: 3em;
    margin-bottom: 1px;
}

form {
    font-family: "Courier New", Courier, monospace;
    width: 100%;
    height: 75%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-evenly;
    animation: left-shift 0.5s ease-out forwards;
}

.progress-bar-block {
    width: 75%;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.form-n {
    width: 75%;
}

.sub-title {
    width: 100%;
    text-align: left;
}

.sub-input {
    padding: 2% 0 5% 0;
    width: 100%;
}

.sub-input input {
    outline: none;
    box-sizing: border-box;
    padding: 15px;
    border-radius: 0;
    font-size: 0.8rem;
    border: 1px solid #bbb;
    font: 13px;
    width: 100%;
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

.progress-bar {
    height: 2px;
    width: 100%;
    background-color: #bbb;
}

.custom-progress {
    height: 100%;
    width: 100%;
    background-color: black;
}

.progress-text-block {
    padding-top: 5%;
    font-size: 0.8rem;
}

.progress-text-block span {
    font-weight: bold;
    font-family: "Courier New", Courier, monospace;
}

@keyframes left-shift {
    from {
        opacity: 0;
        transform: translateX(100px);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}
</style>
