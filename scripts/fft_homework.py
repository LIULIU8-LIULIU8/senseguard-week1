import numpy as np
import matplotlib.pyplot as plt
import os

fs = 1000        # 采样率 (Hz)
duration = 1.0
f0 = 20 + 37
noise = 0.8
# 1. 生成时间轴 t
t = np.arange(0, duration, 1 / fs)

# 2. 生成信号 x (纯正弦波 + 随机噪声)
# 注释里给的噪声写法：
x = np.sin(2 * np.pi * f0 * t) + noise * np.random.default_rng().normal(size=t.size)

# 3. 算频谱 (用 FFT 做快速傅里叶变换)
X_f = np.abs(np.fft.rfft(x))

# 4. 算每个点对应的频率
freqs = np.fft.rfftfreq(t.size, 1 / fs)

# 5. 找频谱最高点的下标，并打印对应的频率
peak_idx = np.argmax(X_f)
peak_freq = freqs[peak_idx]
print(f"检测到的最高频率是: {peak_freq} Hz")

# 6. 画图并保存
fig, axs = plt.subplots(2, 1, figsize=(8, 6)) # 上下两张图

# 上图：前 0.2 秒的波形
# 0.2秒就是 200 个采样点，我们只画前 200 个
axs[0].plot(t[:200], x[:200])
axs[0].set_title("Time Domain (First 0.2s)")
axs[0].set_xlabel("Time (s)")
axs[0].set_ylabel("Amplitude")

# 下图：频谱图
axs[1].plot(freqs, X_f)
axs[1].set_title("Frequency Domain (FFT)")
axs[1].set_xlabel("Frequency (Hz)")
axs[1].set_ylabel("Magnitude")

# 确保 output 文件夹存在，否则保存会报错
if not os.path.exists("output"):
    os.makedirs("output")

plt.tight_layout() # 自动调整间距
plt.savefig("output/fft.png") # 保存图片
print("图片已保存至 output/fft.png")
