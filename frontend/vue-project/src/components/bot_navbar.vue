template:
<template>
<body>
<div class="footer">
    <div class="footer-section">
        <div>
            <h4>竞赛交流平台</h4>
            <a href="#">竞赛</a>
            <a href="#">资源</a>
            <a href="#">讨论社区</a>
        </div>
        <div>
            <h4>企业服务</h4>
            <a href="#">在线面试</a>
            <a href="#">企业测评</a>
            <a href="#">招聘</a>
        </div>
        <div>
            <h4>关于我们</h4>
            <a href="#">加入我们</a>
            <a href="#">工作机会</a>
        </div>
    </div>
    <div class="bottom-bar">
        <p>&copy; 2024 深圳大学软件工程课程小组第二组</p>
        <p>深圳大学软件工程课程小组第二组版权所有 | 首抄不究 | 再抄必究</p>
    </div>
    </div>

</body>
</template>

style:
<style>
        .footer {
            margin-top:60px;
            background-color: #1a1a1a;
            padding: 20px 0;
            text-align: center;
            width:100%;
            box-sizing: border-box; /* 确保盒模型的宽度包括padding和border */
        }
        .footer .footer-section {
            display: flex;
            justify-content: center;
            gap: 200px;
            flex-wrap: wrap;
            margin-bottom: 20px;
        }
        .footer .footer-section div {
            text-align: left;
        }
        .footer h4 {
            color: #ffffff;
            margin-bottom: 10px;
            font-size: 16px;
        }
        .footer a {
            color: #b0b0b0;
            text-decoration: none;
            display: block;
            margin: 5px 0;
            font-size: 14px;
        }
        .footer a:hover {
            color: #ffffff;
        }
        .footer .bottom-bar {
            border-top: 1px solid #333333;
            padding-top: 10px;
            font-size: 12px;
            color: #666666;
        }
    </style>
