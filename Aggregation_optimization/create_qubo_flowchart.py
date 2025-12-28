import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.patches as mpatches

plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 150

colors = {'primary': '#2E86AB', 'secondary': '#A23B72', 'accent': '#F18F01', 
          'success': '#C73E1D', 'quantum': '#6A4C93', 'classical': '#4ECDC4'}

fig, ax = plt.subplots(1, 1, figsize=(14, 10))
ax.set_xlim(0, 10)
ax.set_ylim(0, 12)
ax.axis('off')

# 定义流程步骤
steps = [
    {"text": "Virtual Power Plant\nDistributed Resource\nDisaggregation Problem", "pos": (5, 11), "color": colors['primary']},
    {"text": "Objective Function\n• Revenue Maximization\n• Regulation Penalty", "pos": (2, 9), "color": colors['secondary']},
    {"text": "Constraint Identification\n• Power Constraints\n• Balance Constraints\n• Deviation Constraints", "pos": (8, 9), "color": colors['secondary']},
    {"text": "Data Discretization &\nBinary Representation", "pos": (5, 7), "color": colors['accent']},
    {"text": "Constraints → \nPenalty Terms", "pos": (2, 5), "color": colors['quantum']},
    {"text": "Objective → \nQUBO Form", "pos": (8, 5), "color": colors['quantum']},
    {"text": "QUBO Model Construction\nmin Σβᵢⱼxᵢxⱼ + Σαᵢxᵢ", "pos": (5, 3), "color": colors['success']},
    {"text": "Qubit Optimization\n• Redundancy Reduction\n• Qubit Sharing", "pos": (5, 1), "color": colors['classical']}
]

# 绘制步骤框
for step in steps:
    box = FancyBboxPatch(
        (step["pos"][0] - 1.2, step["pos"][1] - 0.6),
        2.4, 1.2,
        boxstyle="round,pad=0.1",
        facecolor=step["color"],
        edgecolor='white',
        alpha=0.8,
        linewidth=2
    )
    ax.add_patch(box)
    
    ax.text(step["pos"][0], step["pos"][1], step["text"],
            ha='center', va='center', fontsize=10, fontweight='bold',
            color='white')

# 绘制箭头连接
arrows = [
    ((5, 10.4), (2, 9.6)),   # 主问题到目标函数
    ((5, 10.4), (8, 9.6)),   # 主问题到约束条件
    ((2, 8.4), (5, 7.6)),    # 目标函数到离散化
    ((8, 8.4), (5, 7.6)),    # 约束条件到离散化
    ((5, 6.4), (2, 5.6)),    # 离散化到约束转换
    ((5, 6.4), (8, 5.6)),    # 离散化到目标转换
    ((2, 4.4), (5, 3.6)),    # 约束转换到QUBO
    ((8, 4.4), (5, 3.6)),    # 目标转换到QUBO
    ((5, 2.4), (5, 1.6))     # QUBO到优化
]

for start, end in arrows:
    ax.annotate('', xy=end, xytext=start,
               arrowprops=dict(arrowstyle='->', lw=2, color='black', alpha=0.7))

plt.title('QUBO Model Construction Flowchart', fontsize=16, fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig('qubo_modeling_flowchart.png', bbox_inches='tight', facecolor='white')
plt.close()

print("QUBO modeling flowchart generated: qubo_modeling_flowchart.png")