<template>
    <div>
        <div class="bg"></div>
        <top-nav></top-nav>
        <div v-bind:class="{cover:bgActive}"></div>
        <div class="searchDialog">
            <div class="title">
                <img src="../../static/film.png" alt="" width="40px" height="40px">
                <div>最懂你的电影天地</div>
            </div>
            <div class="inputDialog">
                <input type="text" placeholder="" @focus="bgActive=!bgActive" @blur="bgActive=!bgActive" v-model="searchKey" @keyup.enter="search">
                <img src="../../static/input.png" alt="" width="30px" height="30px" @click="search">
            </div>
        </div>
        <div class="poplist">
            <div class="name">流行榜单 <span>数据源于：猫眼数据</span> </div>
            <div class="item">
                <popitem v-for="pop in poplist" :info="pop" :key="pop.index"
                ></popitem>
            </div>
        </div>
        <div class="bot">
            <ul>
                <li>本站资料取自于 豆瓣电影、猫眼电影、电影天堂</li>
                <li>|</li>
                <li>背景图片取自bing搜索国内版</li>
                <li>|</li>
                <li>技术支持:</li>
                <li><a href="https://cn.vuejs.org/">Vue2.0</a></li>
                <li><a href="https://www.python.org/">Python3.6</a></li>
                <li><a href="http://nodejs.cn/">Node.js 10.2</a></li> 
                <li @click="search()">result</li>
            </ul>
        </div>
    </div>
</template>

<script>
import topNav from './topNav.vue'
import popitem from './popitem.vue'
import axios from 'axios'
export default {
  name: 'searchPage',
  data() {
    return {
      input: '',
      bgActive: false,
      searchKey: '',
      poplist: []
    }
  },
  components:{
      topNav,popitem
  },
  mounted() {
      var date =new Date()
      var day= date.getDate()
      var localday=localStorage.getItem('time')
      if(day == localday){
          this.poplist=JSON.parse(localStorage.getItem('list'))
          console.log('you quchu')
          console.log(this.poplist)
      }
      else{
          axios.get('http://127.0.0.1:5000/api/pop')
            .then((res)=>{
                this.poplist=res.data
                localStorage.setItem('time',day)
                localStorage.setItem('list',JSON.stringify(res.data))
            })
      }
  },
  methods: {
      search: function(){
          this.$router.push({
              name: 'result',
              params : {
                  key:this.searchKey
              }
          })
      }
  }
}
</script>

<style scoped>
.bg{
    background-image: url('../../static/v1.png');
    background-repeat: no-repeat;
    background-size: cover;
    width: 100%;
    position: absolute;
    z-index: -99;
    top: 0;
    bottom: 0;
    opacity: 1;
    min-width: 1400px;
    min-height: 820px
}
top-nav{
    position: fixed;
    z-index: -10;
    top: 0px;
}
.cover{
    width: 100%;
    position: absolute;
    z-index: -5;
    top: 0;
    bottom: 0;
    visibility: visible;
    opacity: 0.55;
    background-color: #000;
}

.searchDialog{
    margin-left: 200px;
    margin-top: 150px;
    color: #ccc;
}
.searchDialog .title{
    width: 630px;
    height: 45px;
    position: relative;
    overflow: hidden;
    font-size: 18px;
}
.searchDialog .title img{
    position: absolute;
    left: 5px;
    bottom: 0px;
}
.searchDialog .title div{
    position: absolute;
    left: 55px;
    bottom: 5px;
    color: #fff;
}
.searchDialog .inputDialog{
    background-color: #fff;
    width: 630px;
    height: 50px;
    position: relative;
    border-radius: 5px;
}
.searchDialog .inputDialog img{
    position: absolute;
    right: 5px;
    margin-top: 10px;
    cursor: pointer;
}
.searchDialog .inputDialog input{
    height: 35px;
    width: 580px;
    margin: 5px 0px 0px 15px;
    background-color: transparent;
    outline: none;
    border: 0;
    font-size: 20px;
}
.poplist {
    margin-top: 80px;
    margin-left: 200px;
}
.poplist .name{
    color: #F56C6C;
    font-size: 28px;
} 
.poplist .name span{
    color: #222;
    font-size: 12px;
    margin-left: 10px;
}
.poplist .item{
    margin-top: 40px;
    min-width: 1200px;
}
.poplist .item .i{
    width: 180px;
    height: 330px;
    margin-right: 50px;
    float: left;
}
.bot{
    position: fixed;
    bottom: 0px;
    height: 30px;
    width: 100%;
    min-width: 1200px;
    color: #666;
    background-color: #333;
    font-size: 14px;
}
.bot ul{
    list-style: none;
    position: relative;
    margin: 0 0 0 40px;
    padding: 0px;  
}
.bot ul li{
    line-height: 30px;
    float: left;
    margin-right: 20px;
}
a{
    color: #666;
    text-decoration: none;
}
a:hover{
    text-decoration-line: underline;
    color: #fff;
}
</style>
