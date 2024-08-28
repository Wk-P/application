<template>
    <HeadHomeBar />
</template>

<script lang="ts" setup name="OptionHeader">
import { ref } from "vue";
import HeadHomeBar from "@/components/HeadHomeBar.vue"

const reloadTextContent = ref("&#8635");

function filterClick() {
    alert("Filter");
}


</script>
<style scoped>
.filter {
    width: 100%;
    height: 5vh;
}
.filter button {
    color: white;
    font-size: 1.1rem;
    font-weight: bold;
    background-color: gray;
    height: 100%;
    border: none;
    width: 100%;
}

.filter span {
    padding: 0 5px;
}

.filter-option {
    box-sizing: border-box;
    height: 5vh;
    background-color: gray;
    padding: 0 1rem;
    display: flex;
    flex-direction: row;
    align-items: center;
    list-style: none;
    justify-content: start;
}

.title {
    color: white;
    width: 50%;
    font-size: 1.3rem;
    font-weight: bold;
    text-align: center;
}

.filter-option .title {
    color: white;
    width: 25%;
    font-size: 1rem;
    font-weight: bold;
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: center;
}

.options-block {
    padding: 0 20px;
    height: 75%;
    color: white;
    font-size: 1.1rem;
    font-weight: bold;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 50%;
}

.selector {
    outline: none;
    border: none;
    width: 100%;
    appearance: none; /* For modern browsers */
    -webkit-appearance: none; /* For Safari */
    -moz-appearance: none; /* For Firefox */
    box-sizing: border-box;
    height: 100%;
    width: 100%;
    padding: 0 20px;
    border-radius: 5px;
}

.selector option {
    text-align: center;
}
</style>
