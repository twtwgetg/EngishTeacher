const express = require('express');
const app = express();
const path = require('path');

// 静态文件服务，将public目录作为静态资源目录
app.use(express.static(path.join(__dirname, 'public')));

// 根路径访问主页
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

const port = process.env.PORT || 3000;
app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
