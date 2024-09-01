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
        <div class="item-view-block">
            <ul>
                <li v-for="(name, index) in allFileNames" :key="index">
                    <div>{{ name }}</div>
                    <button class="delete-button" @click="handleDelete(index)">
                        삭제
                    </button>
                </li>
            </ul>
        </div>
    </div>
</template>

<script lang="ts" setup name="UploadImage">
import { ref, onMounted } from "vue";
const selectedFile = ref<File | null>(null);
const fileInput = ref<HTMLInputElement | null>(null);
const triggerFileInput = () => {
    fileInput.value?.click();
};

const handleDelete = (index: number) => {
    if (allFileNames.value) {
        const deleteFileName = allFileNames.value[index];

        if (!confirm(`Delete: ${deleteFileName} ?`)) {
            return;
        }
        fetch(`/api/items/upload/`, {
            method: "DELETE",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                file_name: deleteFileName,
            }),
        })
            .then((response) => {
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                return response.json();
            })
            .then((data) => {
                console.log(data);
                // 成功后可以从列表中移除已删除的文件
                allFileNames.value?.splice(index, 1);
            })
            .catch((error) => {
                console.error("Error:", error);
                alert("파일 삭제에 실패했습니다!");
            });
    } else {
        alert("파일이 없습니다!");
    }
};

const onFileSelected = (event: Event) => {
    const target = event.target as HTMLInputElement;
    if (target.files && target.files.length > 0) {
        selectedFile.value = target.files[0];
    }
};

const allFileNames = ref<Array<string> | null>([]);
const getAllFilesName = () => {
    fetch("/api/items/upload/")
        .then((response) => response.json())
        .then((data) => {
            allFileNames.value = data;
        })
        .catch((error: Error) => {
            console.log(error.message);
        });
};

onMounted(() => {
    getAllFilesName();
});

// 上传文件
const uploadFile = () => {
    if (!selectedFile.value) return;

    const formData = new FormData();
    formData.append("file", selectedFile.value);

    // 发送文件到后端
    fetch("/api/items/upload/", {
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
.item-view-block {
    box-sizing: border-box;
    width: 100%;
}

.item-view-block ul {
    box-sizing: border-box;
    width: 100%;
    list-style: none;
    padding: 0.6rem;
}

.item-view-block ul li {
    box-sizing: border-box;
    width: 100%;
    padding: 0.5rem;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
}

.item-view-block .delete-button {
    padding: 0.5rem;
    font-size: 0.8rem;
}

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
