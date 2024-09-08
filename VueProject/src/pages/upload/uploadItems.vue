<template>
    <div class="container">
        <div class="item-info-block">
            <div class="line-input">
                <span class="input-title">item filename</span>
                <input
                    type="text"
                    :value="selectedFile ? selectedFile.name : ''"
                    readonly
                />
            </div>
        </div>
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
            <button @click="clearFile" class="clear-button">Clear Files</button>
        </div>
        <div class="hint">
            <p><strong>Hint: </strong>Please add the specific content of the Item in the Django Admin interface</p>
            <p style="color: blue"><strong>item filename</strong> -> <strong>Filename</strong></p>
            <a href="http://localhost:8000/admin/items/item/" target="_blank">To Django Admin Interface Link</a>
        </div>
        <div class="item-view-block">
            <div class="sub-title">저장된 파일들</div>
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

<script lang="ts" setup name="uploadItems">
import { ref, onMounted, onUnmounted } from "vue";
import type { Item } from "@/types/index";
import { useUserStore } from "@/stores/index";
import { useRouter } from "vue-router";
const userStore = useUserStore();
const router = useRouter();
const selectedFile = ref<File | null>(null);
const fileInput = ref<HTMLInputElement | null>(null);
const item = ref<Item>({
    id: "",
    name: "",
    desc: "",
    price: 0,
    title: "",
    imgLink: "",
});
const triggerFileInput = () => {
    fileInput.value?.click();
};

const clearFile = () => {
    selectedFile.value = null;
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
        const file = target.files[0];

        // 检查文件类型是否为 jpg 或 png
        const allowedTypes = ["image/jpeg", "image/png"];
        if (!allowedTypes.includes(file.type)) {
            alert("Only JPG and PNG files are allowed!");
            selectedFile.value = null; // 重置选中的文件
            return;
        }

        selectedFile.value = file;

        item.value.imgLink = selectedFile.value.name;
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
    console.log(userStore.user?.loginStatus);
    if (userStore.user?.loginStatus !== true) {
        router.push({ name: "customadmin" });
    }
    getAllFilesName();
});

onUnmounted(() => {
    selectedFile.value = null;
    allFileNames.value = null;
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
            alert(`Upload successfully!`);
            console.log("File uploaded successfully:", data);
            selectedFile.value = null; // 重置选中的文件
            location.reload();
        })
        .catch((error) => {
            console.error("Error uploading file:", error);
        });

    // 发送 item 信息给后端创建
    fetch("/api/items/upload/", {
        method: "POST",
        body: JSON.stringify({
            item: item,
        }),
    })
        .then((response) => response.json())
        .then((data) => {
            console.log(data);
        }).catch;
};
</script>

<style scoped>
.hint {
    color: red;
    padding: 1rem 1rem 1.5rem 1rem;
}
.hint a {
    color: #222;
}
.line-input {
    display: flex;
    flex-direction: row;
    justify-content: space-evenly;
}
.line-input > input {
    outline: none;
    border: 2px solid black;
    padding: 0.3rem;
}
.input-title {
    display: block;
}

.clear-button {
    padding: 0.5rem;
}

.sub-title {
    padding: 0.5rem;
    text-align: center;
}

.item-view-block {
    box-sizing: border-box;
    width: 100%;
    border-top: 2px solid black;
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
    padding: 1rem 0;
    display: flex;
    flex-direction: row;
    justify-content: space-evenly;
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
