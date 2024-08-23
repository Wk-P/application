<template>
    <ul class="head">
        <li @click="usercenter"><img src="/img/user.png" alt="usercenter" /></li>
        <li class="title"><p>ASLIN</p></li>
        <li @click="favorite"><img src="/img/heart.png" alt="favorite" /></li>
        <li @click="cart"><img src="/img/cart.png" alt="cart" /></li>
    </ul>
    <ul class="filter-option">
        <li class="title"><p>BRAND</p></li>
        <li class="options-block">
            <select class="selector">
                <option value="brandOption1Sub1">brand1</option>
                <option value="brandOption1Sub2">brand2</option>
                <option value="brandOption1Sub3">brand3</option>
            </select>
        </li>
    </ul>
    <ul class="filter-option">
        <li class="title"><p>KIND</p></li>
        <li class="options-block">
            <select class="selector">
                <option value="brandOption1Sub1">brand1</option>
                <option value="brandOption1Sub2">brand2</option>
                <option value="brandOption1Sub3">brand3</option>
            </select>
        </li>
    </ul>
    <ul class="filter-option">
        <li class="title"><p>PEOPLE</p></li>
        <li class="options-block">
            <select class="selector">
                <option value="brandOption1Sub1">brand1</option>
                <option value="brandOption1Sub2">brand2</option>
                <option value="brandOption1Sub3">brand3</option>
            </select>
        </li>
    </ul>
    <div class="filter">
        <button @click="filterClick()">
            <span v-html="reloadTextContent"></span>filter
        </button>
    </div>
</template>

<script lang="ts" setup name="OptionHeader">
import { ref } from "vue";
import { useRouter } from "vue-router";

const reloadTextContent = ref("&#8635");

const router = useRouter();
function usercenter() {
    router.push("/usercenter");
}

function favorite() {
    router.push("/favorite");
}

function cart() {
    router.push("/cart");
}

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

.filter-title,
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

.head {
    padding: 0 5px;
    background-color: gray;
    height: 5vh;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
}

.head > li {
    box-sizing: border-box;
    height: 100%;
    width: auto;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 8px 5px;
}

.head img {
    height: 100%;
    width: auto;
}

.head .title {
    color: white;
    width: 50%;
    font-size: 1.3rem;
    font-weight: bold;
    text-align: center;
}

.filter-title .title,
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
