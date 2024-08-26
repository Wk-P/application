<template>
    <HomeBar />
    <div class="page-block">
        <h2 class="title">회원가입</h2>
        <div class="form-block">
            <RouterView />
        </div>
        <FooterBlock />
    </div>
</template>

<script lang="ts" setup name="Register">
import FooterBlock from "@/components/FooterBlock.vue";
import HomeBar from "@/components/HomeBar.vue";
</script>
<style scoped>
.page-block {
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    overflow-y: hidden; /* 防止水平滚动条出现 */
}

.title {
    display: block;
    padding-top: 3rem;
    width: 100%;
    text-align: center;
}

.form-block {
    flex: 4;
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

.footer-block {
    display: flex;
    flex-direction: row;
    justify-content: center;
    width: 100%;
    flex: 1;
    flex-shrink: 0;
}
</style>
