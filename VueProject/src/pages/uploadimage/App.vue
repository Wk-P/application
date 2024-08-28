<template>
    <div class="container">
        <div class="content-block">
            <p v-if="selectedFile">Selected file: {{ selectedFile.name }}</p>
        </div>
        <div class="button-group">
            <input
                type="file"
                ref="fileInput"
                style="display: none"
                @change="onFileSelected"
            />
            <button class="add-button" @click="triggerFileInput">
                Add File
            </button>
            <button
                class="upload-button"
                @click="uploadFile"
                :disabled="!selectedFile"
            >
                Upload File
            </button>
        </div>
    </div>
</template>

<script lang="ts" setup name="UploadImage">
import { ref } from "vue";
const selectedFile = ref<File | null>(null);
const fileInput = ref<HTMLInputElement | null>(null);
const triggerFileInput = () => {
    fileInput.value?.click();
};

const onFileSelected = (event: Event) => {
    const target = event.target as HTMLInputElement;
    if (target.files && target.files.length > 0) {
        selectedFile.value = target.files[0];
    }
};

// 上传文件
const uploadFile = () => {
    if (!selectedFile.value) return;

    const formData = new FormData();
    formData.append("file", selectedFile.value);

    // 发送文件到后端
    fetch("/api/items/upload", {
        method: "POST",
        body: formData,
    })
        .then((response) => response.json())
        .then((data) => {
            console.log("File uploaded successfully:", data);
            selectedFile.value = null; // 重置选中的文件
        })
        .catch((error) => {
            console.error("Error uploading file:", error);
        });
};
</script>

<style scoped>
.container {
    padding: 20px;
}

.content-block {
    margin-bottom: 20px;
}

.button-group {
    display: flex;
    gap: 10px;
}

.add-button,
.upload-button {
    padding: 10px 20px;
    cursor: pointer;
}

.upload-button:disabled {
    background-color: #ccc;
    cursor: not-allowed;
}
</style>
