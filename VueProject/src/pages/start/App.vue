<template>
    <div class="containers-head" ref="containersHead">
        <OptionHeader />
        <FilterBlock />
    </div>
    <div class="containers" ref="containers">
        <waterFallFlow />
    </div>
</template>
<script lang="ts" setup name="start">
import waterFallFlow from "@/components/WaterFallFlow.vue";
import OptionHeader from "@/components/OptionHeader.vue";
import { onMounted, ref, watch, onUnmounted } from "vue";
import FilterBlock from "@/components/FilterBlock.vue";

const containersHead = ref<HTMLElement | null>(null);
const containers = ref<HTMLElement | null>(null);

// dynamic set height
const updateContainerHeight = () => {
    if (containersHead.value && containers.value) {
        const headHeight = containersHead.value.clientHeight;
        containers.value.style.marginTop = `${headHeight}px`;
    }
};

onMounted(() => {
    updateContainerHeight();
    // Optional: update height on window resize
    window.addEventListener("resize", updateContainerHeight);
});

watch(
    () => containersHead.value?.clientHeight,
    () => {
        updateContainerHeight();
    },
    { immediate: true }
);

onUnmounted(() => {
    window.removeEventListener("resize", updateContainerHeight);
});
</script>
<style scoped>
.containers {
    position: relative;
    width: 100%;
}

.containers-head {
    background-color: white;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    z-index: 1000;
}
</style>
