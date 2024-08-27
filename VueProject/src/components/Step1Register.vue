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
                    <label class="hint-style"
                        >수취인 성명</label
                    >
                    <input type="text" v-model="name" />
                </div>
            </div>

            <div class="form-n">
                <h5 class="sub-title">이메일/휴대폰 번호</h5>
                <div class="sub-input">
                    <label class="hint-style"
                        >전화나 이메일 주소</label
                    >
                    <input type="text" v-model="tel_email" />
                    <label class="hint-label">{{ telEmailLabelText }}</label>
                </div>
            </div>

            <div class="button-block">
                <button
                    ref="nextButton"
                    :style="nextButtonStyle"
                    @click="nextStep"
                    :disabled="isDisabled"
                >
                    다음
                </button>
            </div>
        </form>
    </div>
</template>

<script lang="ts" setup name="Step1Register">
import { useUserStore } from "@/stores";
import { ref } from "vue";
import { onMounted } from "vue";
import { watch } from "vue";
import { useRouter } from "vue-router";

const progressText = ref<string>("1/2");
const name = ref<string>("");
const tel_email = ref<string>("");
const telEmailLabelText = ref<string>(" ");
const nextButton = ref<HTMLButtonElement | null>(null);
const nextButtonStyle = ref();
const router = useRouter();
const isDisabled = ref<boolean>(false);
const userStore = useUserStore();


function validateString(input: string): string {
    // 定义正则表达式模式
    const phonePattern = /^\d{11}$/;
    const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

    // 检测是否符合电话号码
    if (phonePattern.test(input)) {
        telEmailLabelText.value = "";
        return "tel";
    }
    // 检测是否符合电子邮件地址
    else if (emailPattern.test(input)) {
        telEmailLabelText.value = "";
        return "email";
    } else {
        telEmailLabelText.value = "이메일 주소나 전화번호가 맞지 않습니다";
        return "error";
    }
}

const nextStep = (event: Event): void => {
    event.preventDefault();
    // 输入检测
    const tel_email_type = validateString(tel_email.value);

    // 后端请求写入用户
    // username, email/tel
    // Here TODO ..

    // 保存入localStorage 下一个界面使用
    localStorage.setItem("name", name.value);
    if (tel_email_type == "tel") {
        localStorage.setItem("tel", tel_email.value);
        localStorage.setItem("email", "");
    } else if (tel_email_type == "email") {
        localStorage.setItem("email", tel_email.value);
        localStorage.setItem("tel", "");
    } else {
        return;
    }

    router.push({ name: "Step2Register" }).catch((err) => {
        console.error("Navigation error:", err);
    });
};

onMounted(() => {
    updateButtonStyle();
});

function updateButtonStyle(): void {
    if (name.value !== "" && tel_email.value !== "") {
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

watch([name, tel_email], updateButtonStyle);
</script>

<style scoped>
.hint-label {
    color: red;
    font-size: 0.3em;
}

.block {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: start;
    padding-top: 3em;
    margin-bottom: 1px;
    background-color: white;
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
    border: 2px solid #bbb;
    background-color: #bbb;
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

.hint-style {
    color: #1c1ccc;
    font-size: 0.2em;
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
