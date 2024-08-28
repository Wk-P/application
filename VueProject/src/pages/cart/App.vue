<template>
    <OptionHeader />
    <div class="content-block">
        <ul class="item-list">
            <li v-for="item in itemList">
                <div class="left-check-box-style">
                    <input type="checkbox" />
                </div>
                <div class="right-info-box-style">
                    <div class="up-others-block">
                        <div class="left-item-img">
                            <img src="" alt="" />
                        </div>
                        <div class="right-label">
                            <ul>
                                <li>{{ item.title }}</li>
                                <li>{{ item.desc }}</li>
                                <li>{{ item.name }}</li>
                                <li>option</li>
                            </ul>
                        </div>
                    </div>
                    <div class="down-price-block">
                        {{ item.price }}
                    </div>
                </div>
            </li>
        </ul>
    </div>
    <div class="bottom-block"></div>
</template>

<script lang="ts" setup name="Cart">
import OptionHeader from "@/components/OptionHeader.vue";
import type { Item } from "@/types/index";
import { ref } from "vue";

const itemList = ref<Array<Item>>([]);
const item = ref<Item>({
    id: "001",
    name: "item1",
    title: "傻逼",
    desc: "货品……",
    price: 10,
});

for (let i = 0; i < 5; i++) {
    itemList.value.push(item.value);
}
</script>

<style scoped>
.content-block {
    width: 100%;
    padding: 0.5rem;
    list-style: none;
}
.item-list {
    width: 100%;
    padding: 0.5rem;
}
.content-block .item-list > li {
    display: flex;
    flex-direction: row;
    height: 50%;
}

.left-check-box-style {
    height: 100%;
}
</style>
