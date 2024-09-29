<template>
    <ReturnBar />
    <div class="content-container">
        <h1 class="page-title">Notice</h1>
        <nav class="title-nav">
            <div>Title</div>
            <div>Created</div>
            <div>Author</div>
        </nav>
        <div class="notice-announcement">
            <ul>
                <li v-for="notice in announcement" class="notice-block">
                        <span><RouterLink :to="{ name: '', params: {}}" class="notice-link"><strong>{{ notice.title }}</strong></RouterLink></span>
                        <span>{{ notice.created_at }}</span>
                        <span>Admin</span>
                    

                </li>
            </ul>
        </div>
    </div>
</template>

<script lang="ts" setup name="announcementpage">
import { ref, onMounted } from "vue";
import type { Notice } from "@/types/index";
import ReturnBar from "@/components/ReturnBar.vue";

const announcement = ref<Array<Notice>>([]);

const getAllNotice = () => {
    fetch("/api/notice/all/")
        .then((response) => {
            if (!response.ok) {
                response.json().then((error) => {
                    console.log(error);
                    throw new Error(
                        `Error! HTTP status code ${response.status}`
                    );
                });
            }
            return response.json();
        })
        .then((data) => {
            console.log(data);
            announcement.value = data;
        });
};

onMounted(() => {
    getAllNotice();
});
</script>

<style scoped>
.content-container {
    padding-top: 2.8rem;
    padding-bottom: 4rem;
    overflow-y: auto;
    height: calc(100% - 8rem);
}

.page-title {
    padding: 0.5rem;
}
.title-nav {
    box-sizing: border-box;
    display: flex;
    flex-direction: row;
    width: 100%;
    background-color: #eee;
}
.title-nav div {
    padding: 0.5rem;
}

.title-nav div:nth-child(1) {
    width: 70%;
}



.notice-block {
    box-sizing: border-box;
    padding:0.5rem;
    width: 100%;
    display: flex;
    flex-direction: row;
    border-bottom: 1px solid #eee;
}

.notice-block span:nth-child(1) {
    width: 70%;
}

.notice-link {
    text-decoration: none;
    color: black;
    display: block;
    height: 100%;
}
</style>
