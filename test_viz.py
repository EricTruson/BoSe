import matplotlib.pyplot as plt
import numpy as np

print("开始测试...")

# 创建简单的测试图
fig, ax = plt.subplots(figsize=(10, 6))
x = np.linspace(0, 10, 100)
y = np.sin(x)
ax.plot(x, y)
ax.set_title('测试图表')
plt.savefig('test_plot.png')
plt.close()

print("测试图表已生成: test_plot.png")