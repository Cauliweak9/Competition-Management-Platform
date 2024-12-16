<template>
    <div class="top-show-id">
        <div class="top-container">
            <div class="avatar">
                <img src="../assets/images/shark.jpg" alt="shark">
            </div>
            <div class="top-info">
                <h3>{{ user.id }}</h3>
                <p>{{ user.email }}</p>
            </div>
        </div>
    </div>
    <div class="main-container">
    <div class="main">
        <div class="discribtion">
            <div class="dis-container">
                <div class="sus-info-container">
                <div class="suscrib-info">
                    <div class="suscriber">
                        <h3>关注者</h3>
                        <p>0</p>
                    </div>
                    <div class="sus-mid">
                        |
                    </div>
                    <div class="fans">
                        <h3>粉丝</h3>
                        <p>0</p>
                    </div>
                </div>
                </div>
                <div class="boder-divider"></div>
                <div class="edit-user-info">
                    <div class="edit-user-info-container">
                        <p>编辑个人信息</p>
                    </div>
                </div>
                <div class="dis-info-top" >
                    <h2>个人简介</h2>
                </div>
                <div class="dis-info">
                    <h3>姓名：林星辰</h3>
                </div>
                <div class="dis-info">
                    <h3>学号：2022150152</h3>
                </div>
                <div class="dis-info">
                    <h3>邮箱：lxc@szu.edu.cn</h3>
                </div>
                <div class="dis-info">
                    <h3>学校：深圳大学</h3>
                </div>
                <div class="dis-info">
                    <h3>专业：计算机科学与技术</h3>
                </div>
                <div class="dis-info">
                    <h3>ip:广东</h3>
                </div>
                <div class="boder-divider"></div>
                <div class="skill">
                    <svg xmlns="http://www.w3.org/2000/svg" class="skill-icon" width="64" height="64" viewBox="0 0 64 64" fill="none" stroke="#666" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><!-- 标签主体 --><path d="M16 32L32 16L56 40L40 56L16 32Z" /><!-- 标签上的小孔 --><circle cx="36" cy="36" r="2" /></svg>
                    <span>技能:</span>
                    <span>HTML、CSS、JavaScript、Vue、flask、c语言、c++</span>
                </div>
            </div>
        </div>
        <div class="main-right-container">
            <div class="main-info">
                <div class="main-btn">
                    <span>参与比赛</span>
                </div>
                <div class="main-btn">
                    <span>讨论发布</span>
                </div>
                <div class="main-btn">
                    <span>收藏</span>
                </div>
            </div>
            <div class="boder-divider" id='boder-divider-right'></div>
            <compt></compt>
        </div>
    </div>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  import Cookies from 'js-cookie';
  import competition from "../components/competition.vue";

  export default {
    data() {
      return {
        user: {
            id:'',
            email:'',
            password:''
        }
      };
    },
    components: {
        'compt': competition
    },
    created() {
      this.fetchUserData();
    },
    methods: {
      fetchUserData() {
        const token = Cookies.get('token');
        console.log("token:", token);
        axios.post("http://127.0.0.1:5173/user", {
                token: token
            }) 
          .then(response => {
            if (response.data.code === 1) {
              this.user = response.data.data;
            } else {
              alert("用户信息加载失败，请重新登录！");
              this.$router.push("/login");
            }
          })
          .catch(error => {
            console.error("获取用户信息失败：", error);
            alert("用户信息加载失败，请重新登录！");
            this.$router.push("/login");
          });
      }
    }
  };
  </script>
  
<style>
/* 顶部展示用户信息 */
.top-show-id{
    height:96px;
    width:100%;
    display:flex;
    align-items:center;
    justify-content:center;
    box-sizing:border-box
}
.top-show-id .top-container{
    width:1300px;
    padding:10px;
    display:flex;
}
.top-show-id .top-container .avatar{
    height:80px;
    width:80px;
    display:flex;
    border-radius:6px;
}
.avatar img{
    height:80px;
    width:80px;
    border-radius:6px;
}
.top-show-id .top-container .top-info{
    display:flex;
    width:100px;
    flex-direction:column;
    justify-content:center;
}
.top-info h3{
    font-size: 30px;
    margin-left:15px;

}
.top-info p{
    margin-left:15px;
    color: rgb(54, 54, 54);
}


/* 主体内容左侧样式 */
.main-container{
    width:100%;
    display:flex;
    justify-content: center;
    align-items: center;
    margin-top: 30px;
}
.main-container .main{
    width:1320px;
    display:grid;
    grid-template-columns: 1fr 3fr; /* 设置列宽比例1：5 */
}
.main .discribtion{
    background-color: rgb(244, 242, 242);
    border:2px solid rgb(189, 189, 189);
    border-radius: 10px;
    max-height: 700px;
}
.discribtion .dis-container{
    display:flex;
    flex-direction:column;
    
    padding:10px;
}
.dis-container h3{
    text-align: center;
}
.dis-container h2{
    text-align: center;
}
.sus-info-container{
    display:flex;
    align-items: center;
    justify-content: center;
}
.dis-info{
    margin-top:30px;
}
.dis-info h3{
    color: rgb(39, 39, 39);
}
.suscrib-info{
    width:100%;
    display:flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    gap:20px;
}
.suscrib-info p{
    text-align: center;
}
.edit-user-info{
    margin-top:10px;
    height:100px;
    display:flex;
    justify-content: center;
    align-items: center;
}
.edit-user-info-container{
    height:100%;
    width:100%;
    pad:50px;
    display:flex;
    justify-content: center;
    align-items: center;
}
.edit-user-info-container p{
    height:60px;
    width:180px;
    border-radius: 9px;
    background-color: rgb(57, 57, 57);
    color:rgb(255, 255, 255);
    display: flex;
    justify-content: center; /* 水平居中 */
    align-items: center; /* 垂直居中 */
    transition: background-color 0.3s ease-in-out;
    cursor: pointer;
}
.edit-user-info-container p:hover{
    background-color:rgb(17, 17, 17);
}
.boder-divider{
    height:1px;
    width:308px;
    margin:30px 0 10px 0;
    background-color: rgb(147, 147, 147);
}
.skill{
    margin-top:15px;
}
.skill svg{
    position:relative;
    top:5px;
    left:25px;
    width: 30px;
    height:30px;
}
.skill span{
    position:relative;
    left:25px;
}

/*主体内容右侧 */
.main-right-container{
    min-height: 1200px;
}
.main-right-container{
    display:flex;
    flex-direction: column;
    align-items: center;
    background-color: rgb(244, 242, 242);
    border:2px solid rgb(189, 189, 189);
    border-radius: 10px;
    padding:10px;
}
.main-info{
    display:flex;
    flex-direction: row;
    justify-content: center;
    width:100%;
    height:80px;
    gap:30px;
}
.main-info .main-btn{
    width:150px;
    height:60px;
    display:flex;
    justify-content: center;
    align-items: center;
    border-radius: 10px;
    cursor: pointer;
    transition: background-color 0.3s ease-in-out;
}
.main-btn span{
    font-size: 20px;
}
.main-info .main-btn:hover{
    background-color:rgb(156, 156, 156);
}
#boder-divider-right{
    position:relative;
    bottom:30px;
    width:700px;
}
</style>