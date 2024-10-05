<template>
    <ul>
        <li v-for="link in linksTextContent">
            <RouterLink :to="{ name: ''}" class="link">
                <div>{{ link.en }}</div>
                <img src="/src_img/arrow-right.png" alt="">
            </RouterLink>
        </li>
    </ul>
</template>

<script lang="ts" setup name="ClassListBlock">
import { ref } from "vue";
import { RouterLink } from "vue-router";


const linksTextContent = ref([
    {
        en: "All",
    },
    {
        en: "necklace",
    },
    {
        en: "bracelet"
    },
    {
        en: "ring",
    },
    {
        en: "earrings",
    },
    {
        en: "others",
    },
    {
        en: "men",
    },
    {
        en: "women",
    },
]);

</script>

<style scoped>
ul {
    list-style: none;
}

ul li {
    display: flex;
    flex-direction: row;
}

.link {
    width: 100%;
    color: black;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    height: 3rem;
    text-decoration: none;
}

.link div {
    display: flex;
    flex-direction: column;
    justify-content: center;
    flex: 1;
}

.link img {
    box-sizing: border-box;
    display: block;
    padding: .6rem;
}

</style>