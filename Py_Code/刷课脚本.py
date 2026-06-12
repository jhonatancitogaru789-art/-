console.log("【全自动多集连播脚本已启动】...");

// ==========================================
// 1. 核心：监听视频结束，自动切换下一集
// ==========================================
function autoPlayNext() {
    const video = document.querySelector('video');
    if (!video) return;

    // 每次切换新视频，确保正常速度和静音
    video.playbackRate = 1; 
    video.muted = true;
    if (video.paused) video.play();

    // 监听视频播放结束事件
    video.onended = function() {
        console.log("【提示】当前视频已播放完毕，正在寻找下一集...");
        
        // 1. 寻找当前页面右侧列表里的所有集数（寻找未完成的圆圈或列表项）
        // 这里的选择器基于国家研修平台的常见结构
        const courseItems = document.querySelectorAll('.course-item, li, tr, a');
        let clickNext = false;

        for (let i = 0; i < courseItems.length; i++) {
            const item = courseItems[i];
            const text = item.innerText || "";
            
            // 如果找到了“第X集”字样
            if (text.includes('第') && text.includes('集')) {
                // 如果当前项包含正在播放的特征（比如高亮、或者是我们刚才记录的项），就准备点它下面的一项
                // 稳妥起见：直接寻找进度为 "0%" 或者未打勾的下一集
                if (text.includes('0%')) {
                    item.click();
                    console.log(`【成功】已自动为你跳转到：${text.split('\n')[0]}`);
                    clickNext = true;
                    break;
                }
            }
        }

        // 2. 如果通过文字没找到，尝试兜底逻辑：直接寻找页面上的“下一讲”或“下一关”按钮
        if (!clickNext) {
            const buttons = document.querySelectorAll('button, a, .btn');
            buttons.forEach(btn => {
                const btnText = btn.innerText || "";
                if (btnText.includes('下一讲') || btnText.includes('下一节') || btnText.includes('下一关')) {
                    btn.click();
                    console.log("【成功】已通过“下一讲”按钮跳转。");
                    clickNext = true;
                }
            });
        }

        if (!clickNext) {
            console.log("【警告】未找到下一集，请手动点击下一集。脚本会在新视频载入后继续生效。");
        }
    };
}

// ==========================================
// 2. 定时器：解决 21 分钟防挂机弹窗 + 维持播放状态
// ==========================================
setInterval(() => {
    // 自动点掉“继续播放”弹窗
    const elements = document.querySelectorAll('button, a, input[type="button"], .btn');
    elements.forEach(el => {
        const text = el.innerText || el.value || "";
        if (text.includes('继续') || text.includes('确定') || text.includes('我还在看')) {
            el.click();
            console.log(`【提示】检测到弹窗并已自动点击。`);
        }
    });

    // 确保视频没有因为异常暂停
    autoPlayNext();
}, 5000);

// ==========================================
// 3. 破解切窗口暂停限制
// ==========================================
window.onblur = null;
document.onvisibilitychange = null;
Object.defineProperty(document, 'visibilityState', { value: 'visible', writable: true });
Object.defineProperty(document, 'hidden', { value: false, writable: true });

// 首次运行初始化
autoPlayNext();
