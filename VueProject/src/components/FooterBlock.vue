<template>
    <footer>
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
    </footer>
</template>

<script lang="ts" setup name="FooterBlock"></script>

<style scoped>

footer {
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: center;
}
.footer {
    width: 90%;
    height: 15vh;
    border-top: solid 1px white;
    display: flex;
    flex-direction: row;
    justify-content: space-evenly;
    font-size: 0.9rem;
    font-weight: bolder;
    border-top: 1px solid black;
}

.information1 {
    width: 50%;
    padding: 1em 1em;
}

.information2 {
    width: 50%;
    padding: 1em 1em;
}
</style>
