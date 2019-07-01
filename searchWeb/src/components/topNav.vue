<template>
    <div class="top">
      <div class="left">
        <span>源站导航:</span>
        <a href="https://www.mtime.cn/">时光电影</a>
        <a href="https://maoyan.com/">猫眼</a>
        <a href="http://dytt8.net/">电影天堂</a>
      </div>
      <div class="right">
        <p v-if="!islogin" class="username" @click="isactive =!isactive">{{name}}</p>
        <p v-else class="username">{{name}}</p>
        <div class="bb"> 
          <div v-if="!islogin" class="userico" @click="isactive =!isactive"></div>
          <div v-else class="userico" ></div>
        </div>
      </div>
      <div class="dialog" :class="{active:isactive}">
        <p>Login on</p>
        <div class="un item">
          <input type="text" name=""  placeholder="Count/Mail" v-model="username">
        </div>
        <div class="pd item">
          <input type="password" name=""  placeholder="Password" v-model="password">
        </div>
        <div class="btn">
          <el-button type="primary" plain @click="Login">登录</el-button>
        </div>
      </div>
    </div>
</template>

<script>
import Axios from 'axios';
export default {
  name: 'topNav',
  data() {
    return {
      name: '登录',
      username: '',
      password: '',
      isactive: true,
      islogin: false
    }
  },
  methods: {
    Login : function(){
      Axios({
        method:'POST',
        url:'http://127.0.0.1:5000/api/login',
        params: {
          username : this.username,
          password : this.password
        }
      }).then((res)=>{
        const info=res.data
        if(info['code']!='200'){
          alert(info['info'])
          this.password=''
        }
        else{
          this.name=info['userId']
          this.isactive= !this.isactive
          this.islogin= !this.islogin
          document.cookie='userId='+info['userId']
        }
      })
    },
  },
  mounted() {
    if(document.cookie.length!=0){
      this.name=document.cookie.split('=')[1]
    }
  },
}
</script>

<style scoped>
.top{
  color: #bbb;
  width: calc(100%);
  height: 30px;
  padding-top: 5px;
  padding-bottom: 5px;
  min-width: 1200px;
  position: relative;
  font-weight: 400;
  font-size: 14px;
  background-color: transparent;
  z-index: 888;
}
p{
  margin: 0px;
}
a,a:visited{
  color: #bbb;
  text-decoration: none;
}
a:hover{
  color: #fff;
}
.userico{
  background-image: url('../../static/userLogin.png');
  background-size: cover;
  display: block;
  width: 16px;
  height: 16px;
  margin-left: 7px;
  margin-top: 6px;
}
.left{
  float: left;
  margin-top: 5px;
  margin-left: 200px;
}
.left span{
  float: left;
  margin-right: 20px;
}
.left a{
  float: left;
  margin-right: 20px;
}
.right{
  float: right;
  color: #fff;
  width: 250px;
  position: relative;
}
.right .username{
  float: left;
  margin-right: 20px;
  cursor: pointer;
  line-height: 30px;
}
.right .bb{
  float: left;
  cursor: pointer;
  width: 30px;
  height: 30px;
  border-radius: 50%;
  background-color: #fff;
}
.dialog{
  position: absolute;
  top: 50px;
  right: 120px;;
  opacity: 0.55;
  background-color: #000;
  width: 220px;
  height: 300px;
  border-radius: 5px;
  z-index: 999;
}
.dialog p{
  text-align: center;
  font-size: 22px;
  padding: 10px 0px;
  height: 30px;
  line-height: 30px;
  border-bottom: 1px solid #fff;
}
.dialog .item{
  background-color: #fff;
  width: 160px;
  padding-left: 10px;
  height: 40px;
  margin: 30px auto;
  border-radius: 10px;
}
.dialog input{
  height: 34px;
  width: 150px;
  margin-top: 3px;
  border: 0px;
  line-height: 40px;
  font-size: 18px;
  outline: none;
}
.btn{
  width: 100px;
  margin: 30px  auto;
}
.active{
  display: none;
}
</style>
