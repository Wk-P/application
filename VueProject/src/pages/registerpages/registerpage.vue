<template>
    <ReturnBar />
    <div class="page-block">
        <h2 class="title">회원가입</h2>
        <div class="form-block">
            <RouterView></RouterView>
        </div>
    </div>
</template>

<script lang="ts" setup name="Register">
import ReturnBar from "@/components/ReturnBar.vue";
</script>
<style scoped>
.page-block {
    height: calc(100% - 5rem);
    box-sizing: border-box;
    padding: 3rem 1rem 5rem 1rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    overflow-y: auto;
    overflow-x: hidden;
}

.form-block {
    box-sizing: border-box;
    width: 100%;
    padding: 0 2rem;
}

</style>
