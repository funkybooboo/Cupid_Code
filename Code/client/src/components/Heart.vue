<script setup>
    const props = defineProps(['active'])
</script>
<template>
    <!--https://www.svgrepo.com/svg/532473/heart-->
    <svg class = "heart" :data-active="active" viewBox="0 0 24 24">
        <path fill-rule="evenodd" clip-rule="evenodd" d="M12 6.00019C10.2006 3.90317 7.19377 3.2551 4.93923 5.17534C2.68468 7.09558 2.36727 10.3061 4.13778 12.5772C5.60984 14.4654 10.0648 18.4479 11.5249 19.7369C11.6882 19.8811 11.7699 19.9532 11.8652 19.9815C11.9483 20.0062 12.0393 20.0062 12.1225 19.9815C12.2178 19.9532 12.2994 19.8811 12.4628 19.7369C13.9229 18.4479 18.3778 14.4654 19.8499 12.5772C21.6204 10.3061 21.3417 7.07538 19.0484 5.17534C16.7551 3.2753 13.7994 3.90317 12 6.00019Z" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        </path>
    </svg>
</template>
<style scoped>
    .heart {
        background-color: #0000;
        margin: auto;
        width: 60px;
        height: 60px;
        display:flex;
        justify-content: center;
        align-content: center;
        transition: all 0.8s ease;
        fill: var(--secondary-red);
        transition: all 0.3s ease;
    }

    .heart[data-active=true]{
        fill: var(--primary-red);
    }
    .heart[data-active=true] > path{
        stroke: #FFCCFF;
    }
</style>
