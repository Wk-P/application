<template>
    <nav>
        <ul>
            <li><img src="" alt="img1"></li>
            <li><img src="" alt="img2"></li>
            <li><img src="" alt="img3"></li>
            <li><img src="" alt="img4"></li>
            <li><img src="" alt="img5"></li>
            <li><img src="" alt="img6"></li>
            <li><img src="" alt="img7"></li>
        </ul>
    </nav>
</template>

<script lang="ts" setup name="Page3">
    
</script>

<style scoped>
nav {
    box-sizing: border-box;
    display: flex;
    flex-direction: row;
    height: 50vh; 
    width: 100%;
    overflow-x: auto; 
    scrollbar-width: none; /* firefox */
    -ms-overflow-style: none; /* IE 10+ */
    scroll-snap-type: x mandatory; 
    animation: 0.3s linear 0.1s slideIn;
}

nav::-webkit-scrollbar {
    display: none;
}
nav > ul {
    box-sizing: border-box;
    height: 100%;
    display: flex;
    list-style: none;
    white-space: nowrap; 
    margin: 0;
    padding: 0;
}

nav > ul > li {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100vw;
    height: 100%; 
    background-color: #5a5c;
    scroll-snap-align: center; 
}

nav > ul > li > img {
    max-width: 100%;
    max-height: 100%;
    object-fit: cover; 
}

@keyframes slideIn {
    from {
        opacity: 0;
        transform: translateX(-5rem);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}
</style>