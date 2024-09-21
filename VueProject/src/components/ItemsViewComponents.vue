<template>
    <ul class="item-view-list">
        <li></li>
    </ul>
</template>

<script lang="ts" setup name="ItemsViewComponents">
import { ref, onMounted } from 'vue';
import type { Item } from "@/types/index";
const itemsList = ref<Array<Item>>([]);


onMounted(() => {

})

</script>

<style scoped></style>