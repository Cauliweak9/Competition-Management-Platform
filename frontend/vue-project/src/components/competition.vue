<template>
<div class="compt-container">
                <div class="compt-info">
                    <span class="compt-tag" id="not-start">
                        未开始
                    </span>
                    <span class="compt-title">
                        深圳大学英雄联盟比赛
                    </span>
                    <span class="compt-time">
                        2024-12-20 10:00:00 ~ 2024-12-20 19:00:00
                    </span>
                </div>
                <div class="compt-divider"></div>
                <div class="compt-info">
                    <span class="compt-tag" id="not-start">
                        未开始
                    </span>
                    <span class="compt-title">
                        深圳大学英语演讲大赛
                    </span>
                    <span class="compt-time">
                        2024-12-18 10:00:00 ~ 2024-12-31 21:00:00
                    </span>
                </div>
                <div class="compt-divider"></div>
                <div class="compt-info">
                    <span class="compt-tag" id="is-going">
                        进行中
                    </span>
                    <span class="compt-title">
                        深圳大学诗词大赛
                    </span>
                    <span class="compt-time">
                        2024-12-15 10:00:00 ~ 2024-12-20 19:00:00
                    </span>
                </div>
                <div class="compt-divider"></div>
                <div class="compt-info">
                    <span class="compt-tag" id="is-going">
                        进行中
                    </span>
                    <span class="compt-title">
                        深圳大学软件设计大赛
                    </span>
                    <span class="compt-time">
                        2024-12-13 10:00:00 ~ 2024-12-21 20:00:00
                    </span>
                </div>
                <div class="compt-divider"></div>
                <div class="compt-info">
                    <span class="compt-tag" id="is-end">
                        已结束
                    </span>
                    <span class="compt-title">
                        深圳大学数学建模大赛
                    </span>
                    <span class="compt-time">
                        2024-12-8 10:00:00 ~ 2024-12-12 19:00:00
                    </span>
                </div>
                <div class="compt-divider"></div>
            </div>
</template>
<script>

</script>
<style>
.main-right-container{
    display:flex;
    flex-direction: column;
    align-items: center;
    background-color: rgb(222, 222, 222);
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
/* 竞赛信息 */

.compt-container{
    width:100%;
    height:100%;
    display:flex;
    flex-direction: column;
}
.compt-info{
    margin-top: 20px;
    height:80px;
    display:flex;
    align-items: center;
}
.compt-tag{
    height:40px;
    width:90px;
    display: flex;
    justify-content: center; /* 水平居中 */
    align-items: center; /* 垂直居中 */
    background-color: rgb(165, 158, 158);
    color: aliceblue;
    border-radius: 5px;
    margin-left:20px;
}
.compt-title{
    height:40px;
    margin-left: 30px;
    display: flex;
    justify-content: center; /* 水平居中 */
    align-items: center; /* 垂直居中 */
    font-size: 20px;
    font-weight: 800;
}
.compt-time{
    height:40px;
    
    display: flex;
    justify-content: flex-end; /* 水平居中 */
    align-items: center; /* 垂直居中 */
    flex-grow: 1; /* 子元素将填满剩余空间 */
}
.compt-divider{
    height:1px;
    width:100%;
    background-color: rgb(147, 147, 147);
}
#not-start{
    background-color: rgb(165, 158, 158);
}
#is-going{
    background-color: rgb(10, 161, 4);
}
#is-end{
    background-color: rgb(195, 4, 4);
}
</style>