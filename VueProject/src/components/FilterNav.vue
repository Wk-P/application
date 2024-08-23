<template>
    <nav class="filter-nav">
        <ul>
            <li>
                <p>价格</p>
                <div class="custom-dropdown-container">
                    <div class="custom-select" @click="toggleDropdown('price')">
                        {{
                            selectedPriceOption
                                ? selectedPriceOption.text
                                : "请选择"
                        }}
                        <span class="arrow"></span>
                    </div>
                    <div v-if="isDropdownOpen === 'price'" class="options">
                        <div
                            v-for="option in priceOptions"
                            :key="option.value"
                            class="option"
                            @click="selectPriceOption(option)"
                        >
                            {{ option.text }}
                        </div>
                    </div>
                </div>
            </li>
            <li>
                <p>销量</p>
                <div class="custom-dropdown-container">
                    <div class="custom-select" @click="toggleDropdown('sale')">
                        {{
                            selectedSaleOption
                                ? selectedSaleOption.text
                                : "请选择"
                        }}
                        <span class="arrow"></span>
                    </div>
                    <div v-if="isDropdownOpen === 'sale'" class="options">
                        <div
                            v-for="option in saleOptions"
                            :key="option.value"
                            class="option"
                            @click="selectSaleOption(option)"
                        >
                            {{ option.text }}
                        </div>
                    </div>
                </div>
            </li>
            <li><button @click="filter" class="filter-button">筛选</button></li>
        </ul>
    </nav>
</template>

<script lang="ts" setup name="FilterNav">
import { ref } from "vue";

function filter() {
    console.log("Clicked filter button");
}

interface Option {
    value: string;
    text: string;
}

const priceOptions = ref<Option[]>([
    { value: "option1", text: "从高到低" },
    { value: "option2", text: "从低到高" },
]);

const saleOptions = ref<Option[]>([
    { value: "option1", text: "从高到低" },
    { value: "option2", text: "从低到高" },
]);

const selectedPriceOption = ref<Option | null>(null);
const selectedSaleOption = ref<Option | null>(null);
const isDropdownOpen = ref<string | null>(null);

const toggleDropdown = (dropdownType: string) => {
    if (isDropdownOpen.value === dropdownType) {
        isDropdownOpen.value = null;
    } else {
        isDropdownOpen.value = dropdownType;
    }
};

const selectPriceOption = (option: Option) => {
    selectedPriceOption.value = option;
    isDropdownOpen.value = null;
};

const selectSaleOption = (option: Option) => {
    selectedSaleOption.value = option;
    isDropdownOpen.value = null;
};
</script>

<style scoped>
    ul {
    display: flex;
    flex-direction: row;
    align-items: center;
    list-style: none;
    height: 50px;
    background-color: lightcoral;
    box-shadow: 2px 2px 5px 2px #444;
    border-radius: 15px;
    padding: 0 25px;
    margin: 0 25px;
}

ul li {
    display: flex;
    flex-direction: row;
    justify-content: space-evenly;
    align-items: center;
    height: 100%;
    width: 100%;
}

ul li > * {
    display: flex;
    flex-direction: row;
    align-items: center;
    margin: 0 20px;
    height: 80%;
    border: none;
}

.custom-dropdown-container {
    position: relative;
}

.custom-select {
    width: 150px;
    padding: 10px;
    font-size: 16px;
    border: 1px solid #ccc;
    border-radius: 4px;
    cursor: pointer;
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: white;
}

.arrow {
    width: 10px;
    height: 10px;
    background: url('data:image/svg+xml;charset=US-ASCII,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20viewBox%3D%220%200%204%205%22%3E%3Cpath%20fill%3D%22%23333%22%20d%3D%22M2%205%200%203h4L2%205zm0-5l2%202H0L2%200z%22/%3E%3C/svg%3E') no-repeat center;
}

.options {
    position: absolute;
    top: 100%;
    left: 0;
    width: 100%;
    background-color: white;
    z-index: 1000;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    transition: all 0.4s ease-out;
}


.option {
    padding: 10px;
    font-size: 16px;
    cursor: pointer;
    transition: all 0.3s ease-out;
}

.option:hover {
    color: black;
    background-color: aliceblue;
}

.option:first-child {
    border-top: none;
}

.option:hover {
    background-color: #f0f0f0;
}

ul li select:focus-visible {
    outline: none;
}

.filter-button {
    display: flex;
    flex-direction: row;
    justify-content: center;
    border-radius: 4px;
    width: 50%;
    height: 80%;
    background-color: #efe;
    transition: all 0.2s ease-out;
}

.filter-button:hover {
    cursor: pointer;
    background-color: #aaa;
    color: white;
}

</style>
