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
                <h3 class="sub-title">이름</h3>
                <div class="sub-input">
                    <label class="hint-style">수취인 성명</label>
                    <input type="text" v-model="name" />
                </div>
            </div>

            <div class="form-n">
                <h3 class="sub-title">이메일/휴대폰 번호</h3>
                <div class="sub-input">
                    <label class="hint-style">전화나 이메일 주소</label>
                    <input type="text" v-model="tel_email" />
                    <label class="hint-label">{{ telEmailLabelText }}</label>
                </div>
            </div>

            <div class="form-n">
                <h3 class="sub-title">주소</h3>
                <div class="sub-input">
                    <label class="hint-style">메일 주소</label>
                    <input type="text" v-model="address" />
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

const address = ref<string>("");
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
    localStorage.setItem("address", address.value);
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
.block {
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
