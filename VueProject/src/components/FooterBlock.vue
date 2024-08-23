<template>
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
</template>

<script lang="ts" setup name="FooterBlock"></script>

<style scoped>
.footer {
    width: 100%;
    border-top: solid 1px white;
    display: flex;
    flex-direction: row;
    justify-content: space-evenly;
    font-size: 0.9rem;
    font-weight: bolder;
}

.information1 {
    width: 50%;
    padding: 20px 15px;
}

.information2 {
    width: 50%;
    padding: 20px 15px;
}
</style>
