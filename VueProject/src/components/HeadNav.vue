<template>
    <nav class="head-nav">
        <ul>
            <li class="home-link">
                <RouterLink to="/" class="router-link-custom"
                    >个人选品网站</RouterLink
                >
            </li>
            <div class="left-blocks">
                <li class="search" v-if="isHomePage">
                    <input v-model="query" />
                    <button @click="search">搜索</button>
                </li>
                <li v-if="isLoggedIn" class="shopping-cart">
                    <RouterLink :to="{ name: 'cart' }">
                        <img src="/shopping-cart.png" alt="shopping cart" />
                    </RouterLink>
                </li>
                <li>
                    <RouterLink
                        v-if="isLoggedIn"
                        :to="{ name: 'usercenter' }"
                        class="router-link-custom"
                        >{{ username }}</RouterLink
                    >
                    <button
                        v-if="isLoggedIn"
                        class="logout-button"
                        @click="logout"
                    >
                        登出
                    </button>
                    <RouterLink v-else="" to="/login" class="router-link-custom"
                        >登录&nbsp;/&nbsp;注册</RouterLink
                    >
                </li>
            </div>
        </ul>
    </nav>
</template>

<script lang="ts" setup name="HeadNav">
import { computed, onMounted, ref } from "vue";
import { RouterLink, useRoute, useRouter } from "vue-router";
import { useSearchStore } from "@/stores/index";
import { userTokenStore } from "@/stores/index";
import type { Item } from "@/types";

const tokenStore = userTokenStore();
const route = useRoute();
const router = useRouter();
const isHomePage = computed(() => {
    if (route.name == "home") {
        return true;
    }
    return false;
});

const query = ref<string>("");
const store = useSearchStore();
const isLoggedIn = ref(false);
const username = ref<string | null>(null);

// loginCheck
function loginCheck() {
    isLoggedIn.value = tokenStore.isAuthenticated;
    username.value = tokenStore.username;
}

function search() {
    const url = "/backend/api/items/search";
    let params = query.value;
    // search
    if (params == "") {
        params += "/all/";
    } else {
        params += "/";
    }

    fetch(`${url}/${params}`)
        .then((response) => {
            if (!response.ok) {
                console.error(response.statusText);
                throw new Error("Network Invalid");
            }
            return response.json();
        })
        .then((res) => {
            let itemsList: Array<Item> = [];
            for (let i = 0;i < res.length;i++) {
                itemsList.push(res[i]);
            }
            store.setResults(itemsList);
        })
        .catch((error) => console.error(error.message));
}

function logout(event: Event) {
    event.preventDefault();
    const store = userTokenStore();
    store.clearToken();
    window.location.href = "/";
}

onMounted(() => {
    loginCheck();
});
</script>

<style>
.head-nav {
    width: 100%;
    display: flex;
    flex-direction: row;
    align-items: center;
    text-align: center;
    height: 80px;
    box-sizing: border-box;
}

.head-nav ul {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    list-style: none;
    background-color: #01000f;
    border: 2px solid #01000f;
    box-sizing: border-box;
}

.head-nav ul li:not(.search) {
    height: 100%;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    border: 2px solid #01000f;
    color: white;
    box-sizing: border-box;
    transition: all 0.2s ease-out;

}

.head-nav ul li:not(.search) a {
    height: 100%;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    border: 2px solid #01000f;
    color: white;
    box-sizing: border-box;
}

.head-nav ul li:not(.search) a:hover {
    cursor: pointer;
    height: 100%;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    border: 2px solid white;
    color: white;
    border-radius: 4px;
}

.left-blocks .shopping-cart:hover {
    cursor: pointer;
    height: 100%;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    color: white;
    border-radius: 4px;
}

.left-blocks .shopping-cart img {
    padding: 0 20px;
}

.router-link-custom {
    display: flex;
    padding: 0 20px;
    flex-direction: column;
    justify-content: center;
    color: white;
    height: 100%;
    width: 100%;
    text-decoration: none;
    transition: all 0.2s ease-out;
}

.left-blocks {
    display: flex;
    flex-direction: row;
    height: 100%;
    justify-content: end;
    align-items: center;
}

.search {
    height: 50%;
    display: flex;
    flex-direction: row;
    border: #01000f solid 2px;
    border-radius: 3px;
}

.search:focus-within {
    border: #efeaaa solid 2px;
    border-radius: 6px;
    box-shadow: 1px 1px 10px 1px #efeaaa;
}

.search input {
    outline: none;
    height: 100%;
    border: none;
    border-radius: 3px 0px 0px 3px;
    padding-left: 8px;
}

.search button {
    padding: 0 10px;
    height: 100%;
    border-top-right-radius: 3px;
    border-bottom-right-radius: 3px;
    background-color: #3ff;
    border: none;
    color: black;
    transition: all 0.2s ease-out;
}

.search button:hover {
    cursor: pointer;
    background-color: #efeaaa;
}

.logout-button {
    box-sizing: border-box;
    outline: none;
    border: 2px solid #01000f;
    background-color: #01000f;
    color: white;
    height: 100%;
    width: 100%;
    transition: all 0.2s ease-out;
    padding: 0 20px;
    font-size: 1rem;
}

.logout-button:hover {
    cursor: pointer;
    border: 2px solid white;
}

</style>
