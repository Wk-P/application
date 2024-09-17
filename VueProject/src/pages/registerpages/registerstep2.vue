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
                <h3 class="sub-title">이이디</h3>
                <div class="sub-input">
                    <label class="hint-style"
                        >사용자 이름은 3~20개의 문자, 숫자 또는 밑줄로
                        구성되어야 합니다</label
                    >
                    <input type="text" v-model="username" />
                    <label class="hint-label">{{ usernameLabelText }}</label>
                </div>
            </div>
            <div class="form-n">
                <h3 class="sub-title">비밀번호</h3>
                <div class="sub-input">
                    <label class="hint-style"
                        >비밀번호는 다음을 포함해야 합니다. 최소 소문자 (a-z)
                        최소 이니셜 (A-Z) 최소 하나의 숫자(0-9) 비밀번호 길이:
                        최소 6자 이상.</label
                    >
                    <input type="password" v-model="password" />
                    <label class="hint-label">{{ passwordLabelText }}</label>
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

const usernameLabelText = ref<string>(" ");
const passwordLabelText = ref<string>(" ");

const userStore = useUserStore();

const progressText = ref<string>("2/2");
const username = ref<string>("");
const nextButton = ref<HTMLButtonElement | null>(null);
const nextButtonStyle = ref();
const password = ref<string>("");

const isDisabled = ref<boolean>(false);

function isValidUsername(name: string) {
    const usernameRegex = /^[a-zA-Z0-9_]{3,20}$/;
    return usernameRegex.test(name);
}

function isValidPassword(password: string) {
    const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{6,}$/;
    return passwordRegex.test(password);
}

async function register(event: Event) {
    event.preventDefault();
    if (!isValidUsername(username.value)) {
        usernameLabelText.value = "사용할 수 없는 사용자 이름";
        return;
    } else {
        usernameLabelText.value = "";
    }

    // 注意修改后端需要分类保存
    if (!isValidPassword(password.value)) {
        passwordLabelText.value = "사용할 수 없는 암호";
        return;
    } else {
        passwordLabelText.value = "";
    }

    // 从前面获取name和 tel email
    const userinfo = {
        name:
            localStorage.getItem("name") !== null
                ? localStorage.getItem("name")
                : "",
        email:
            localStorage.getItem("email") !== null
                ? localStorage.getItem("email")
                : "",
        tel:
            localStorage.getItem("tel") !== null
                ? localStorage.getItem("tel")
                : "",
        username: username.value,
        password: password.value,
        address:
            localStorage.getItem("address") !== null
                ? localStorage.getItem("address")
                : "",
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
        .then(async (response) => {
            console.log(response);
            if (!response.ok) {
                if (response.status === 409) {
                    const errorData = await response.json();
                    // 获取 error_code
                    const errorCode = errorData.error_code;
                    if (errorCode == 1) {
                        alert(`전화번호가 이미 등록되어 있습니다`);
                        router.push({ name: "register" });
                    }
                }
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const data = response.json();
            console.log(data);
            return data;
        })
        .then((data) => {
            console.log(data);
            alert(`회원가입 성공됐습니다!`)
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
    updateButtonStyle();
});

function updateButtonStyle() {
    if (username.value !== "" && password.value !== "") {
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

watch([username, password], updateButtonStyle);
</script>

<style scoped>.block {
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    width: 100%;
    align-items: center;
}

.progress-bar-block {
    box-sizing: border-box;
    width: 100%;
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2rem 3rem 0 3rem;
}

.progress-bar {
    box-sizing: border-box;
    width: 100%;
    height: 2px;
    background-color: #ccc;
}

.custom-progress {
    width: 50%;
    height: 100%;
    background-color: black;
}

.progress-text-block {
    box-sizing: border-box;
    padding: 1rem 0;
    font-size: 0.9rem;
}

form {
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    width: 100%;
}

.form-n {
    box-sizing: border-box;
    width: 100%;
    padding-bottom: 1rem;
}

.sub-input {
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
}

.sub-input input {
    box-sizing: border-box;
    display: block;
    border: 2px solid black;
    padding: 0.7rem;
    font-size: 1.1rem;
    width: 100%;
    outline: none;
    border-radius: 0;
}

.sub-title {
    padding: 0.2rem 0;
}
.hint-style {
    color:rgb(3, 3, 209);
    font-size: 0.8rem;
}

.button-block {
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding-top: 2rem;
}

.button-block button {
    width: 100%;
    padding: 1rem;
    border: none;
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
