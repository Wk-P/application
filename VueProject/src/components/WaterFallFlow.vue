<template>
    <ul class="waterfall-ul">
        <li
            v-for="(item, index) in itemsList"
            :key="index"
            @click="pushToDetailPage(item)"
        >
            <img :src="item.image" alt="" />
            <div class="name-block">{{ item.name }}</div>
            <!-- <div class="tool-block">
                <span>heart | </span>
                <span>cart</span>
            </div> -->
        </li>
    </ul>
    <p ref="loader" class="loader-text">{{ loaderText }}</p>
    <div class="to-top">
        <button v-if="loaderText != initLoadText" @click="scrollToTop">
            Back to Top
        </button>
    </div>
    <FooterBlock />
</template>

<script lang="ts" setup name="Waterfallflow">
import { nextTick, onMounted, ref, onUnmounted, computed } from "vue";
import { useRouter } from "vue-router";
import FooterBlock from "./FooterBlock.vue";
import type { Item } from "@/types/index";
import { useItemsListStore, useItemStore, useQueryStore } from "@/stores/index";

const queryStore = useQueryStore();
const itemsList = ref<Array<Item>>([]);
const waitingItemsList = ref<Array<Item>>([]);
const router = useRouter();
const itemsListStore = useItemsListStore();
const itemStore = useItemStore();

const query = computed(() => queryStore.query);

const pushToDetailPage = (item: Item) => {
    itemStore.setCustomItem(item);
    router.push({ path: `/details/${item.id}` });
};

const queryItem = () => {
    if (
        query.value !== null &&
        query.value !== undefined &&
        query.value.trim() !== ""
    ) {
        fetch(`/api/items/search/${query.value}/`)
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
                console.log("Search results:", data);
                itemsList.value = data;
                itemsListStore.setItemsList(itemsList.value);
            })
            .catch((error) =>
                console.error("Error fetching search results:", error.message)
            );
    }
};

const fetchAllItemLink = () => {
    fetch("/api/items/all/")
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
            itemsList.value = data;
            itemsListStore.setItemsList(itemsList.value);
        })
        .catch((error) =>
            console.error("Error fetching all items:", error.message)
        );
};

const fetchItems = () => {
    if (query.value) {
        queryItem();
    } else {
        fetchAllItemLink();
    }
};

// to Top
const scrollToTop = () => {
    window.scrollTo({
        top: 0,
        behavior: "smooth", // smooth scrolling
    });
};

let waitingIndex = 0;

const loader = ref(null);
const isLoading = ref(false);
const initLoadText = "Loading...";
const loaderText = ref(initLoadText);

// simulate data loading
const loadMore = () => {
    if (isLoading.value) return;
    isLoading.value = true;

    if (waitingIndex >= waitingItemsList.value.length) {
        isLoading.value = false;
        loaderText.value = "- End -";
        return;
    }

    // simulate http request
    itemsList.value.push(waitingItemsList.value[waitingIndex]);
    waitingIndex += 1;
    itemsList.value.push(waitingItemsList.value[waitingIndex]);
    waitingIndex += 1;
    isLoading.value = false;
};

let observer: IntersectionObserver | null = null;

onMounted(() => {
    fetchItems(); // Initial fetch

    // observer object
    observer = new IntersectionObserver(
        ([entry]) => {
            if (entry.isIntersecting) {
                loadMore();
            }
        },
        { threshold: 0.6 }
    );

    // bind target DOM element to observer （绑定监视对象）
    nextTick(() => {
        if (loader.value && observer) {
            observer.observe(loader.value);
        }
    });
});

onUnmounted(() => {
    sessionStorage.removeItem("searchQuery");
    sessionStorage.removeItem("searchQueryResult");
    queryStore.clearQuery();

    // bind target
    if (loader.value && observer) {
        observer.unobserve(loader.value);
    }
});
</script>

<style scoped>
.loader-text {
    text-align: center;
    font-size: 0.8rem;
    padding: 20px 0;
}

.to-top {
    text-align: center;
    font-size: 0.8rem;
    padding: 20px 0;
}

.to-top button {
    appearance: none;
    padding: 0.8rem 0.8rem;
    border: 1px solid #999;
    background-color: white;
    border-radius: 5px;
    outline: none;
    width: 50%;
    color: black;
}

.name-block,
.tool-block {
    font-size: 0.8rem;
    padding-left: 20px;
}

.waterfall-ul {
    margin: 0 auto;
    height: auto;
    width: 85%;
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    list-style: none;
    padding: 50px 0;
}

.waterfall-ul li {
    border: 1px solid #888;
    display: flex;
    flex-direction: column;
}

.waterfall-ul li:nth-child(n + 2) {
    margin-top: -1px;
}

.waterfall-ul li:nth-child(odd) {
    box-sizing: border-box;
    width: 100%;
    grid-column: 1;
    grid-row: auto;
    transform: translateY(-25px);
}

.waterfall-ul li:nth-child(even) {
    box-sizing: border-box;
    margin-left: -1px;
    grid-column: 2;
    grid-row: auto;
    transform: translateY(15px);
}

.waterfall-ul li img {
    box-sizing: border-box;
    height: auto;
    width: 100%;
    height: 100%;
}
</style>
