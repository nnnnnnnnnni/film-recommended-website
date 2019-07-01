<template>
    <div>
        <div class="top">
            <div class="title"><a href="/"></a></div>
            <top-nav class="t"></top-nav>
        </div>
        <div class="container">
            <div class="left">
                <div class="title">热门榜单</div>
                <ul>
                    <li v-for="item in poplist" :key="item.index">
                        <span class="rank">{{item.rank}}.</span><span class="title">{{item.title}}</span><span class="score">{{item.score}}</span>
                    </li>
                </ul>
                <div class="data">数据支持：<a href="https://maoyan.com/">猫眼</a> </div>
            </div>
            <div class="right" ref='viewBox'>
                <div class="search">
                    <div class="searchInput" >
                        <input type="text" v-model="searchKey"  @keyup.enter="get_search(),searching=true,resultlist=[]" >
                        <img src="../../static/input.png" alt="" width="20px" height="20px" @click="get_search">
                    </div>
                </div>
                <div class="result">
                    <div class="title">搜索 <span class="key">{{key}}</span> 的结果:</div>
                    <div v-if="searching" class="loading ">
                        <h2>Loading ......</h2>
                        <span></span>
                        <span></span>
                        <span></span>
                        <span></span>
                        <span></span>
                        <span></span>
                        <span></span>
                    </div>
                    <div class="film" v-for="item in resultlist" :key="item.index">
                        <div class="icon">
                            <img v-if="item.from == 'aqiyi'" src="../../static/aqiyi.png" alt="">
                            <img v-else-if="item.from == 'dytt'" src="../../static/dytt.png" alt="">
                            <img v-else-if="item.from == 'douban'" src="../../static/mtime.png" alt="">
                            <img v-else src="../../static/txsp.png" alt="">
                        </div>
                        <div v-if="item.code == 200" class="info">
                            <div class="info_top">
                                <div class="film_name">
                                    片名：<a :href="item.link"> <font color='#F56C6C'>{{item.title}}</font> </a>
                                </div>
                                
                                <div class="film_from" v-if="item.from == 'aqiyi'">资源来源：<a href="http://www.iqiyi.com/">爱奇艺</a></div>
                                <div class="film_from" v-if="item.from == 'dytt'">资源来源：<a href="http://dytt8.net">电影天堂</a></div>
                                <div class="film_from" v-if="item.from == 'douban'">资源来源：<a href="http://www.mtime.com">时光电影</a></div>
                                <div class="film_from" v-if="item.from == 'txsp'">资源来源：<a href="https://v.qq.com/">腾讯视频</a></div>
                                <div class="film_time">电影时间：{{item.time}}</div>
                            </div>
                            <div class="info_bot">
                                <div class="i">简介：</div><p v-if="item.cv">{{item.cv}}</p><p v-else>暂无简介</p>
                            </div>
                        </div>
                        <div  class="info" v-else >
                            未查到信息！
                        </div>
                    </div>
                    <div class="rem">
                        <div class="title" @click="tp()">
                            --> 我觉得你会喜欢：
                        </div>
                        <div class="table">
                            <el-table :data="tableData1" style="width: 100%" :empty-text="请稍后">
                                <el-table-column prop="rank" label="#" width="40"></el-table-column>
                                <el-table-column prop="title" label="片名" width="220"></el-table-column>
                                <el-table-column prop="time" label="时间" width="180"></el-table-column>
                                <el-table-column prop="url" label="地址"></el-table-column>
                            </el-table>
                        </div>
                        <div class="title" >
                            --> 喜欢这部电影的人还喜欢：
                        </div>
                        <div class="table">
                            <el-table :data="tableData" style="width: 100%" :empty-text="请稍后">
                                <el-table-column prop="rank" label="#" width="40"></el-table-column>
                                <el-table-column prop="title" label="片名" width="220"></el-table-column>
                                <el-table-column prop="time" label="时间" width="180"></el-table-column>
                                <el-table-column prop="url" label="地址"></el-table-column>
                            </el-table>
                        </div>
                    </div>
                </div>
            </div> 
        </div>
    </div>
</template>

<script>
import topNav from './topNav.vue'
import Axios from 'axios';
export default {
    name: 'result',
    data() {
        return {
            key: this.$route.params.key,  //this.$route.params.key
            poplist: [],
            resultlist: [],
            searchKey: '',
            searching: true,
            userId: '',
            tableData: [],
            tableData1:[]
        }
    },
    components:{
        topNav
    },
    methods: {
        tp: function(){
            Axios({
                methods:'GET',
                url:'http://127.0.0.1:5000/api/tp',
                params:{
                    userid:this.userId,
                    cls:this.resultlist[2]['genres']
                }
            }).then((res)=>{
                this.tableData=res.data
                console.log(res.data)
            })
        },
        search: function(){ 
            Axios.get('http://127.0.0.1:5000/api/search?key='+this.key)
                .then( (res)=>{
                    this.resultlist=res.data
                    this.searching=false
                    console.log(this.resultlist)
                })
        },
        get_search: function(){
            this.key=this.searchKey
            this.resultlist=[]
            Axios.get('http://127.0.0.1:5000/api/search?key='+this.searchKey)
                .then( (res)=>{
                    this.resultlist=res.data
                    this.searching=false   
                    console.log(this.resultlist)
                })
        },
        get_rmd: function(){
            Axios({
                methods:'GET',
                url:'http://127.0.0.1:5000/api/rmd',
                params:{
                    userid:this.userId
                }
            }).then((res)=>{
                this.tableData1=res.data
                console.log(res.data)
            })
        },
        // get_itemcf(){
        //     Axios({
        //         methods:'GET',
        //         url:'http://127.0.0.1:5000/api/itemcf',
        //         params:{
        //             userid:this.userId
        //         }
        //     }).then((res)=>{
        //         this.tableData=res.data
        //         console.log(res.data)
        //     })
        // }
    },
    computed: {
        
    },
    mounted() {
        this.userId=document.cookie.split('=')[1]
        this.poplist=JSON.parse(localStorage.getItem('list'))
        this.search()
        if(this.userId!=''){
            this.get_rmd();
        }
        this.tp()
    },
}
</script>

<style scoped>
.top{
    background-color: #303133;
    position: absolute;
    width: 100%;
    z-index: 999;
    min-width: 1700px;
}
.show{
    display: none;
}
.top .title{
    line-height: 40px;
    position: absolute;
    height: 40px;
    left: 50px;
    z-index: 99;
    color: #F56C6C;
    font-size: 22px;
}
.top .title a{
    display: block;
    width: 70px;
    height: 40px;
    background-image: url('../../static/flimhub.png');
    background-size: cover;
}
.container{
    position: absolute;
    top: 40px;
    bottom: 0;
    height: clac(100%-40px);
    width: 100%;
    min-width: 1700px;
}
.top a,.top a:hover,.top a:visited{
    color: #F56C6C;
    text-decoration: none
}
.left{
    width: 10%;
    background-color: #363636;
    float: left;
    height: 100%;
    z-index: -10;
    min-width: 168px;
    max-width: 185px;
    color: #bbb;
}
.left .title{
    width: 100%;
    text-align: center;
    margin: 100px 0 20px 0px;
    font-size: 20px;
}
.left ul{
    list-style: none;
    margin: 30px 0 0 10px ;
    padding: 0px;
}
.left ul li{
    margin: 20px 0 0 0 ;
    position: relative;
}
.left ul li .rank{
    font-size: 22px;
    margin-right: 10px;
}
.left ul li .title{
    font-size: 14px;
    margin-right: 10px;
}
.left ul li .score{
    font-size: 18px;
    position: absolute;
    right: 10px;
    top: 2px;
    line-height: 30px;
}
.left .data{
    position: fixed;
    bottom: 10px;
    font-size: 8px;
    left: 20px;
}
.right{
    float: left;
    height: 100%;
    width: 90%;
    overflow: scroll;
    position: relative;
}
.right .result{
    overflow: hidden;
}
.right::-webkit-scrollbar {/*滚动条整体样式*/
    width: 10px;     /*高宽分别对应横竖滚动条的尺寸*/
    height: 1px;
}
.right::-webkit-scrollbar-thumb {/*滚动条里面小方块*/
    border-radius: 5px;
    /* -webkit-box-shadow: inset 0 0 5px rgba(0,0,0,0.2); */
    background: #535353;
}
.right::-webkit-scrollbar-track {/*滚动条里面轨道*/
    /* -webkit-box-shadow: inset 0 0 5px rgba(0,0,0,0.2); */
    border-radius: 10px;
    background: transparent;
}
.right .search{
    width: 100%;
    height: 30px;
    padding: 10px 0;
}
.right .search .searchInput{
    width: 330px;
    height: 30px;
    background-color: transparent;
    margin: 0px auto;
    border-radius: 15px;
    padding-left: 10px;
    position: relative;
    border: 1px solid #bbb;
}
.right .search .searchInput input{
    background-color: transparent;
    outline: none;
    width: 300px;
    height: 20px;
    padding: 5px 0px;
    font-size: 16px;
    border: 0;
    line-height: 28px;
}
.right .search .searchInput img{
    margin-top: 5px;
    float: right;
    margin-right: 10px;
    cursor: pointer;
}
.right .result{
    margin-left: 50px;
    position: relative;
    background-color: transparent;
    margin-top: 20px;
}
.right .result .title{
    margin-bottom: 30px;
}
.right .result .key{
    color: #F56C6C;
    font-size: 22px;
}
.right .film{
    overflow: hidden;
    padding-bottom: 20px;
    border-bottom: 1px solid #ccc;
    width: 65%;
    margin-bottom: 30px;
    min-width: 1000px;
}
.right .film .icon{
    position: relative;
    float: left;
}
.right .film .info{
    position: relative;
    float: left;
    margin-left: 20px;
}
.right .film .info .info_top{
    position: relative;
    width: 950px;
    overflow: hidden;
}
.right .film .info .info_top .film_name{
    float: left;
    position: relative;
}
.right .film .info .info_top .film_from{
    float: right;
    position: relative;
}
.right .film .info .info_top .film_time{
    float: right;
    position: relative;
    margin-right: 100px;
}
.right .film .info .info_bot{
    position: relative;
    margin-top: 15px;
    float: left;
}
.right .film .info .info_bot .i{
    position: relative;
    float: left;
}
.right .film .info .info_bot p{
    position: relative;
    float: left;
    margin: 0px;
    padding: 0px;
    max-width: 900px;
}
a,a:hover,a:visited{
    color: #000;
    text-decoration: none;
}
 a:hover{
    text-decoration: underline;
    color: #F56C6C;
}
.right .rem{
    width: 70%;
    min-width: 1000px;
}
.right .rem .title{
    font-size: 24px;
}
.loading{
    width: 200px;
    margin: 200px auto 200px auto;
}
.loading span {
  display: inline-block;
  vertical-align: middle;
  width: .6em;
  height: .6em;
  margin: .19em;
  background: #007DB6;
  border-radius: .6em;
  -webkit-animation: loading 1s infinite alternate;
  animation: loading 1s infinite alternate;
}

.loading span:nth-of-type(2) {
  background: #008FB2;
  -webkit-animation-delay: 0.2s;
  animation-delay: 0.2s;
}

.loading span:nth-of-type(3) {
  background: #009B9E;
  -webkit-animation-delay: 0.4s;
  animation-delay: 0.4s;
}

.loading span:nth-of-type(4) {
  background: #00A77D;
  -webkit-animation-delay: 0.6s;
  animation-delay: 0.6s;
}

.loading span:nth-of-type(5) {
  background: #00B247;
  -webkit-animation-delay: 0.8s;
  animation-delay: 0.8s;
}

.loading span:nth-of-type(6) {
  background: #5AB027;
  -webkit-animation-delay: 1.0s;
  animation-delay: 1.0s;
}

.loading span:nth-of-type(7) {
  background: #A0B61E;
  -webkit-animation-delay: 1.2s;
  animation-delay: 1.2s;
}

/*
   * Animation keyframes
   * Use transition opacity instead of keyframes?
   */
@-webkit-keyframes loading {
  0% {
    opacity: 0;
  }

  100% {
    opacity: 1;
  }
}

@keyframes loading {
  0% {
    opacity: 0;
  }

  100% {
    opacity: 1;
  }
}

</style>
