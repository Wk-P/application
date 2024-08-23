<template>
    <div class="block">
        <h2 class="title">회원가입</h2>
        <div class="progress-bar-block">
            <div class="progress-bar">
                <div class="custom-progress"></div>
            </div>
            <div class="progress-text-block">{{ progressText }}</div>
        </div>
        <form>
            <div>
                <h5 class="sub-title">이름</h5>
            </div>
            <div class="sub-input">
                <input type="text" v-model="username" />
            </div>
            <div>
                <h5 class="sub-title">이메일/휴대폰 번호</h5>
            </div>
            <div class="sub-input">
                <input type="text" v-model="tel_email" />
            </div>
            <div class="button-block">
                <button @click="next" ref="nextButton" :style="nextButtonStyle">
                    다음
                </button>
            </div>
        </form>
        <footer><FooterBlock /></footer>
    </div>
</template>

<script lang="ts" setup name="register1">
import { ref } from "vue";
import { getCSRFToken } from "@/utils/validate";
import FooterBlock from "@/components/FooterBlock.vue";
import { onMounted } from "vue";
import { watch } from "vue";
import { RouterView } from "vue-router";
import { computed } from "vue";

const progressText = ref<string>("");
const username = ref<string>("");
const tel_email = ref<string>("");
const email = ref<string>("");
const nextButton = ref<HTMLButtonElement | null>(null);
const nextButtonStyle = ref();

const password1 = ref<string>("");

function next(event: Event) {
    event.preventDefault();
}

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
    nextButtonStyle.value = {
        color: "white",
        backgroundColor: "#ccc",
        borderColor: "#ccc",
    };

    progressText.value = "1/3";
});

watch([username, tel_email], ([newUsername, newTelEmail]) => {
    if (newUsername !== "" && newTelEmail !== "") {
        nextButtonStyle.value = {
            color: "white",
            backgroundColor: "black",
            borderColor: "black",
        };
    } else {
        nextButtonStyle.value = {
            color: "white",
            backgroundColor: "#ccc",
            borderColor: "#ccc",
        };
    }
});
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

footer {
    border-top: 2px solid black;
    box-sizing: border-box;
    width: 90%;
}

.title {
    width: 100%;
    text-align: center;
}

form {
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
}

form div {
    width: 75%;
}

footer {
    border-top: 2px solid black;
    box-sizing: border-box;
    width: 90%;
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
    width: 33%;
    background: black;
}

.progress-bar-block {
    width: 75%;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.progress-text-block {
    padding-top: 5%;
    font-size: 0.8rem;
}
</style>
