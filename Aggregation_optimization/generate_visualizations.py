#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
量子VPP论文分析可视化图表生成器
生成高质量、期刊级别的可视化图表
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import seaborn as sns
from matplotlib.patches import FancyBboxPatch, Circle, Arrow
from matplotlib.patches import ConnectionPatch
import matplotlib.gridspec as gridspec
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd

# 设置中文字体和样式
plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['font.size'] = 12

# 设置期刊级别的颜色方案
colors = {
    'primary': '#2E86AB',
    'secondary': '#A23B72', 
    'accent': '#F18F01',
    'success': '#C73E1D',
    'quantum': '#6A4C93',
    'classical': '#4ECDC4',
    'neutral': '#95A5A6',
    'light': '#ECF0F1',
    'dark': '#2C3E50'
}

def create_qubo_modeling_flowchart():
    """创建QUBO模型构建流程图"""
    fig, ax = plt.subplots(1, 1, figsize=(14, 10))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 12)
    ax.axis('off')
    
    # 定义流程步骤
    steps = [
        {"text": "虚拟电厂分布式资源\n解聚合优化问题", "pos": (5, 11), "color": colors['primary']},
        {"text": "目标函数分析\n• 总收益最大化\n• 调节次数惩罚", "pos": (2, 9), "color": colors['secondary']},
        {"text": "约束条件识别\n• 功率约束\n• 平衡约束\n• 偏差约束", "pos": (8, 9), "color": colors['secondary']},
        {"text": "数据离散化与\n二进制表达", "pos": (5, 7), "color": colors['accent']},
        {"text": "约束条件转换为\n惩罚项", "pos": (2, 5), "color": colors['quantum']},
        {"text": "目标函数转换为\nQUBO形式", "pos": (8, 5), "color": colors['quantum']},
        {"text": "QUBO模型构建\nmin Σβᵢⱼxᵢxⱼ + Σαᵢxᵢ", "pos": (5, 3), "color": colors['success']},
        {"text": "量子比特优化\n• 冗余约束消减\n• 量子比特共用", "pos": (5, 1), "color": colors['classical']}
    ]
    
    # 绘制步骤框
    boxes = []
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
        boxes.append(box)
        
        # 添加文本
        ax.text(step["pos"][0], step["pos"][1], step["text"],
                ha='center', va='center', fontsize=10, fontweight='bold',
                color='white', wrap=True)
    
    # 绘制箭头连接
    arrows = [
        ((5, 10.4), (2, 9.6)),  # 主问题到目标函数
        ((5, 10.4), (8, 9.6)),  # 主问题到约束条件
        ((2, 8.4), (5, 7.6)),   # 目标函数到离散化
        ((8, 8.4), (5, 7.6)),   # 约束条件到离散化
        ((5, 6.4), (2, 5.6)),   # 离散化到约束转换
        ((5, 6.4), (8, 5.6)),   # 离散化到目标转换
        ((2, 4.4), (5, 3.6)),   # 约束转换到QUBO
        ((8, 4.4), (5, 3.6)),   # 目标转换到QUBO
        ((5, 2.4), (5, 1.6))    # QUBO到优化
    ]
    
    for start, end in arrows:
        ax.annotate('', xy=end, xytext=start,
                   arrowprops=dict(arrowstyle='->', lw=2, color=colors['dark']))
    
    plt.title('QUBO模型构建流程图', fontsize=16, fontweight='bold', pad=20)
    plt.tight_layout()
    plt.savefig('qubo_modeling_flowchart.png', bbox_inches='tight', facecolor='white')
    plt.close()

def create_performance_comparison():
    """创建性能对比图表"""
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
    
    # 数据
    methods = ['光量子计算机', 'Gurobi', 'Cplex', '模拟退火', '禁忌搜索', '最速下降']
    times = [1.17, 14.30, 175.30, 793.84, 1676.62, 13.02]
    objectives = [33600, 33600, 33600, 33600, 33600, 31600]
    
    # 子图1: 计算时间对比（对数尺度）
    bars1 = ax1.bar(methods, times, color=[colors['quantum'], colors['classical'], colors['classical'], 
                                          colors['secondary'], colors['secondary'], colors['accent']])
    ax1.set_yscale('log')
    ax1.set_ylabel('计算时间 (ms)', fontsize=12)
    ax1.set_title('计算时间对比 (对数尺度)', fontsize=14, fontweight='bold')
    ax1.tick_params(axis='x', rotation=45)
    ax1.grid(True, alpha=0.3)
    
    # 添加数值标签
    for bar, time in zip(bars1, times):
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height*1.1,
                f'{time:.2f}', ha='center', va='bottom', fontweight='bold')
    
    # 子图2: 目标函数值对比
    bars2 = ax2.bar(methods, objectives, color=[colors['quantum'], colors['classical'], colors['classical'], 
                                               colors['secondary'], colors['secondary'], colors['accent']])
    ax2.set_ylabel('目标函数值 (元)', fontsize=12)
    ax2.set_title('求解精度对比', fontsize=14, fontweight='bold')
    ax2.tick_params(axis='x', rotation=45)
    ax2.grid(True, alpha=0.3)
    
    # 标注最优解
    optimal_line = ax2.axhline(y=33600, color='red', linestyle='--', linewidth=2, alpha=0.7)
    ax2.text(0.02, 0.95, '最优解: 33600元', transform=ax2.transAxes, 
             bbox=dict(boxstyle="round,pad=0.3", facecolor='red', alpha=0.2))
    
    # 子图3: 效率比较雷达图
    categories = ['计算速度', '求解精度', '稳定性', '可扩展性', '实用性']
    
    # 归一化评分 (0-10分)
    quantum_scores = [10, 10, 9, 7, 8]  # 光量子计算机
    classical_scores = [6, 10, 10, 9, 10]  # 经典优化器平均
    heuristic_scores = [4, 10, 7, 8, 8]  # 启发式算法平均
    
    angles = np.linspace(0, 2*np.pi, len(categories), endpoint=False).tolist()
    angles += angles[:1]  # 闭合图形
    
    quantum_scores += quantum_scores[:1]
    classical_scores += classical_scores[:1]
    heuristic_scores += heuristic_scores[:1]
    
    ax3 = plt.subplot(2, 2, 3, projection='polar')
    ax3.plot(angles, quantum_scores, 'o-', linewidth=2, label='光量子计算机', color=colors['quantum'])
    ax3.fill(angles, quantum_scores, alpha=0.25, color=colors['quantum'])
    ax3.plot(angles, classical_scores, 'o-', linewidth=2, label='经典优化器', color=colors['classical'])
    ax3.fill(angles, classical_scores, alpha=0.25, color=colors['classical'])
    ax3.plot(angles, heuristic_scores, 'o-', linewidth=2, label='启发式算法', color=colors['secondary'])
    ax3.fill(angles, heuristic_scores, alpha=0.25, color=colors['secondary'])
    
    ax3.set_xticks(angles[:-1])
    ax3.set_xticklabels(categories)
    ax3.set_ylim(0, 10)
    ax3.set_title('综合性能评估', fontsize=14, fontweight='bold', pad=20)
    ax3.legend(loc='upper right', bbox_to_anchor=(1.3, 1.0))
    
    # 子图4: 加速比分析
    speedup_ratios = [times[i]/times[0] for i in range(len(times))]
    bars4 = ax4.bar(methods[1:], speedup_ratios[1:], 
                    color=[colors['classical'], colors['classical'], colors['secondary'], 
                           colors['secondary'], colors['accent']])
    
    ax4.set_ylabel('相对光量子计算机的加速比', fontsize=12)
    ax4.set_title('计算速度加速比', fontsize=14, fontweight='bold')
    ax4.tick_params(axis='x', rotation=45)
    ax4.grid(True, alpha=0.3)
    ax4.set_yscale('log')
    
    # 添加数值标签
    for bar, ratio in zip(bars4, speedup_ratios[1:]):
        height = bar.get_height()
        ax4.text(bar.get_x() + bar.get_width()/2., height*1.1,
                f'{ratio:.1f}x', ha='center', va='bottom', fontweight='bold')
    
    plt.suptitle('量子计算机与传统方法性能对比分析', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.savefig('performance_comparison.png', bbox_inches='tight', facecolor='white')
    plt.close()

if __name__ == "__main__":
    print("开始生成量子VPP论文分析可视化图表...")
    
    try:
        # 生成图表
        create_qubo_modeling_flowchart()
        print("✓ QUBO模型构建流程图已生成")
        
        create_performance_comparison()
        print("✓ 性能对比图表已生成")
        
        print("\n可视化图表生成完成！")
        print("生成的图片文件：")
        print("- qubo_modeling_flowchart.png")
        print("- performance_comparison.png")
        
    except Exception as e:
        print(f"生成图表时出错: {e}")
        import traceback
        traceback.print_exc()