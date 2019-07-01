<template>
    <div class="i">
        <a :href='info.link'>
            <img :src='info.img_url' width="180px" height="250px">
            <div class="info">
                <div class="title">
                    {{info.title}}
                </div>
                <div class="score">
                    {{info.score}}
                </div>
                <div class="stars">
                    {{info.stars}}
                </div>
            </div>
        </a>
    </div>
</template>

<script>
export default {
    name: 'popitem',
    props: ['info'],
    data() {
        return {
            
        }
    },
}
</script>

<style scoped>
.i{
    position: relative;
    color: white
}
a{
    display: block;
    height: 330px;
    text-decoration: none;
    color: white;
}
.info{
    position: relative;
    top: -5px;
}
.info .title{
    position: absolute;
    top: 0px;
    left: 0px;
    color: #eee;
    font-weight: 500;
    font-size: 18px
}
.info .title:hover{
    text-decoration: underline;
}
.info .stars{
    position: absolute;
    top: 30px;
    color: #aaa;
}
.info .score{
    position: absolute;
    top: -280px;
    right: -20px;
    color: #ffb400;
    font-style: oblique;
    font-size: 48px
}
</style>
