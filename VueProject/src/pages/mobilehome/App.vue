<template>
    <div class="background-canvas">
        <div class="containers"> 
            <div class="title1"><span>A-LIN</span><span>ACCESSORIES</span></div>
            <div class="title2">
                <p>Super Level</p>
                <p>Full Brand</p>
            </div>
            <div class="button-group">
                <button @click="start">START NOW</button>
                <button @click="login">LOG IN</button>
            </div>
            <div class="footer">
                <div class="information1">
                    <div>Tiktok:</div>
                    <div>Instagram:</div>
                </div>
                <div class="information2">
                    <div>KakaoTalk:</div>
                    <div>Tel:</div>
                    <div>Email:</div>
                </div>
            </div>
        </div>
    </div>
</template>
<script lang="ts" setup name="mobilehome">
import { useRouter } from 'vue-router';

const router = useRouter();
function start() {
    router.push('/start');
}

function login() {
    router.push('/login');
}

</script>
<style scoped>
    .background-canvas {
        position: relative;
        width: 100%;
        height: 100%;
        background-image: url("/img/image1m.png");
        background-repeat: no-repeat;
        background-position: center;
    }
    .background-canvas::after {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.68);
        z-index: 1;
    }

    .containers {
        height: 100%;
        position: relative;
        z-index: 2; /* 内容的 z-index 要大于伪元素 */
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        align-items: center;
        color: white;
        
    }

    .title1 {
        margin-top: 30%;
        width: 100%;
        display: flex;
        flex-direction: row;
        justify-content: space-evenly;
        font-size: 1.8rem;
        font-weight: bolder;
    }

    .title2 {
        text-align: center;
        font-size: 1.5rem;
        font-weight: bold;
    }

    .button-group {
        display: flex;
        flex-direction: column;
    }

    .button-group button {
        font-size: 0.9rem;
        font-weight: normal;
        outline: none;
        color: white;
        background: none;
        padding: 12px 25px;
        border: solid white 2px;
        box-sizing: border-box;
        margin: 10px;
        border-radius: 10px;
    }

    .footer {
        width: 90%;
        border-top: solid 1px white;
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        font-size: 0.9rem;
    }

    .information1 {
        width: 50%;
        padding: 20px 15px
    }

    .information2 {
        width: 50%;
        padding: 20px 15px
    }
</style>