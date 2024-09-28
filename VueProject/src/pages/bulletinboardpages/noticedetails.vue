<template>
    <div class="body-container">
        <div class="notice-container">
            <h1>{{ notice?.title }}</h1>
            <p>{{ notice?.content }}</p>
        </div>
        <ul class="comment-block">
            <li v-for="comment in commentsContent">
                <h4>{{ comment.author?.username }}</h4>
                <p>{{ comment.content }}</p>
            </li>
        </ul>
        <div>
            <div class="editor-container">
                <textarea v-model="commentContent"></textarea>
            </div>
            <div class="button-group">
                <button @click="saveContent">Submit</button>
                <button @click="saveContent">Cancel</button>
            </div>
        </div>
    </div>
</template>

<script lang="ts" setup name="noticedetails">
import { ref, onMounted } from "vue";
import type { Notice, Comment } from "@/types/index";
import { useRouter, useRoute } from "vue-router";
import { useUserStore } from "@/stores/index";

const route = useRoute();
const router = useRouter();

// 从路由路径获取notice id
const notice_id = route.params.noticeId;
const notice = ref<Notice | null>(null);
const commentsContent = ref<Array<Comment>>([]);
const commentContent = ref("");

const getNoticeComments = () => {
    fetch(`/api/notice/comments/${notice_id}/`)
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
            notice.value = data.notice;
            commentsContent.value = data.comments;
        });
};

// 保存内容的函数
const saveContent = () => {
    const newComment: Comment = {
        id: "",
        content: commentContent.value,
        author: useUserStore().user,
        created_at: "",
        updated_at: "",
    };

    fetch(`/api/notice/comments/${notice_id}/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            newComment: newComment,
        }),
    })
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
        });
};
onMounted(() => {
    getNoticeComments();
});
</script>

<style scoped>
.body-container {
    overflow-y: auto;
    height: calc(100% - 5rem);
}
.notice-container {
    border: 2px solid black;
    height: 80vh;
    margin: 1rem;
    padding: 1rem 0.5rem;
}

.editor-container {
    box-sizing: border-box;
    width: 100vw;
    padding: 1rem;
    height: 35vh;
}

.editor-container textarea {
    box-sizing: border-box;
    border-radius: 0.5rem;
    height: 100%;
    width: 100%;
    border: 1px solid #fff;
    box-shadow: 0.1rem 0.2rem 1rem 0.1rem rgba(0, 0, 0, 0.2);
    padding: 1rem;
    outline: none;
    font-family: Arial, Helvetica, sans-serif;
}

.button-group {
    box-sizing: border-box;
    width: 100%;
    height: 2rem;
    display: flex;
    justify-content: end;
    padding-right: 1rem;
}

.button-group button {
    height: 100%;
    outline: none;
    margin: 0 1rem;
    padding: 0.5rem 1.5rem;
    border: none;
    background-color: black;
    color: white;
    border-radius: 0.5rem;
}

.comment-block {
    padding: 1rem;
    list-style: none;
}

.comment-block p {
    box-sizing: border-box;
    padding-left: 1rem;
}
</style>
