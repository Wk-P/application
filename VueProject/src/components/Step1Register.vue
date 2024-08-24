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
                <h5 class="sub-title">이름</h5>
                <div class="sub-input">
                    <input type="text" v-model="username" />
                </div>
            </div>

            <div class="form-n">
                <h5 class="sub-title">이메일/휴대폰 번호</h5>
                <div class="sub-input">
                    <input type="text" v-model="tel_email" />
                </div>
            </div>

            <div class="button-block">
                <button
                    ref="nextButton"
                    :style="nextButtonStyle"
                    @click="handleClick"
                >
                    다음
                </button>
            </div>
        </form>
    </div>
</template>

<script lang="ts" setup name="Step1Register">
import { ref } from "vue";
import { getCSRFToken } from "@/utils/validate";
import { onMounted } from "vue";
import { watch } from "vue";
import { useRouter } from "vue-router";

const progressText = ref<string>("1/2");
const username = ref<string>("");
const tel_email = ref<string>("");
const email = ref<string>("");
const nextButton = ref<HTMLButtonElement | null>(null);
const nextButtonStyle = ref();
const password1 = ref<string>("");
const router = useRouter();

const handleClick = () => {
    router.push({ name: "Step2Register" }).catch((err) => {
        console.error("Navigation error:", err);
    });
};

function register(event: Event) {
    event.preventDefault();

    getCSRFToken().then((csrftoken) => {
        // 检查输入是否合规
        if (username.value == "") {
            alert("이름을 입력하세요!");
            return;
        }

        if (tel_email.value == "") {
            alert("비밀번호를 입력하세요!");
            return;
        }

        function isValidUsername(name: string) {
            const usernameRegex = /^[a-zA-Z0-9_]{3,20}$/;
            return usernameRegex.test(name);
        }

        function isValidEmail(email: string) {
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            return emailRegex.test(email);
        }

        function isValidTel(tel: string): boolean {
            const telRegex = /^\d{3}\d{4}\d{4}$/;
            return telRegex.test(tel);
        }

        function isValidPassword(password: string) {
            const passwordRegex =
                /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
            return passwordRegex.test(password);
        }

        if (!isValidUsername(username.value)) {
            alert("名称格式不正确");
            return;
        }

        // 注意修改后端需要分类保存
        if (!isValidEmail(tel_email.value) && !isValidTel(tel_email.value)) {
            alert("邮箱/电话格式不正确");
            return;
        }

        // test
        // true: 密码不做检查
        // false: 密码检查
        const passwordTest = true;
        if (!passwordTest) {
            if (!isValidPassword(password1.value)) {
                alert("密码格式不正确");
                return;
            }
        }

        const url = "/backend/api/user/register";
        let params = "";

        if (params == "") {
            params += "/";
        }

        // 发起后端请求
        fetch(`${url}/${params}`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrftoken,
            },
            body: JSON.stringify({
                username: username.value,
                password: password1.value,
                email: email.value,
            }),
        })
            .then((response) => {
                if (!response.ok) {
                    throw new Error("Register User Conflict");
                }
                return response.json();
            })
            .then((data) => {
                window.location.href = "/";
            })
            .catch((error) => {
                console.error(error);
                alert(error.message);
            });
    });
}

onMounted(() => {
    updateButtonStyle();
});

function updateButtonStyle() {
    const prefersLightScheme = window.matchMedia(
        "(prefers-color-scheme: light)"
    ).matches;

    if (prefersLightScheme) {
        nextButtonStyle.value = {
            color: "white",
            backgroundColor:
                username.value !== "" && tel_email.value !== ""
                    ? "black"
                    : "#ccc",
            borderColor:
                username.value !== "" && tel_email.value !== ""
                    ? "black"
                    : "#ccc",
        };
    } else {
        nextButtonStyle.value = {
            color: "white",
            backgroundColor:
                username.value !== "" && tel_email.value !== ""
                    ? "white"
                    : "#555",
            borderColor:
                username.value !== "" && tel_email.value !== ""
                    ? "white"
                    : "#555",
        };
    }
}

watch([username, tel_email], updateButtonStyle);

const mediaQuery = window.matchMedia("(prefers-color-scheme: light)");
mediaQuery.addEventListener("change", updateButtonStyle);
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
    animation: up-shift 0.5s ease-out forwards;
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
    width: 50%;
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

@media (prefers-color-scheme: dark) {
    .custom-progress {
        color-scheme: dark;
        background-color: white;
    }

    .progress-bar {
        color-scheme: dark;
        background-color: #444;
    }
}
</style>
