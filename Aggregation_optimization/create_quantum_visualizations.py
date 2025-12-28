#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
量子VPP论文分析可视化图表生成器
"""

import matplotlib
matplotlib.use('Agg')  # 设置非交互式后端
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300

# 颜色方案
colors = {
    'primary': '#2E86AB',
    'secondary': '#A23B72', 
    'accent': '#F18F01',
    'success': '#C73E1D',
    'quantum': '#6A4C93',
    'classical': '#4ECDC4',
    'neutral': '#95A5A6'
}

def create_performance_comparison():
    """创建性能对比图表"""
    print("正在生成性能对比图表...")
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
    
    # 数据
    methods = ['光量子\n计算机', 'Gurobi', 'Cplex', '模拟退火', '禁忌搜索', '最速下降']
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
    ax2.axhline(y=33600, color='red', linestyle='--', linewidth=2, alpha=0.7)
    ax2.text(0.02, 0.95, '最优解: 33600元', transform=ax2.transAxes, 
             bbox=dict(boxstyle="round,pad=0.3", facecolor='red', alpha=0.2))
    
    # 子图3: 加速比分析
    speedup_ratios = [times[i]/times[0] for i in range(len(times))]
    bars3 = ax3.bar(methods[1:], speedup_ratios[1:], 
                    color=[colors['classical'], colors['classical'], colors['secondary'], 
                           colors['secondary'], colors['accent']])
    
    ax3.set_ylabel('相对光量子计算机的加速比', fontsize=12)
    ax3.set_title('计算速度加速比', fontsize=14, fontweight='bold')
    ax3.tick_params(axis='x', rotation=45)
    ax3.grid(True, alpha=0.3)
    ax3.set_yscale('log')
    
    # 添加数值标签
    for bar, ratio in zip(bars3, speedup_ratios[1:]):
        height = bar.get_height()
        ax3.text(bar.get_x() + bar.get_width()/2., height*1.1,
                f'{ratio:.1f}x', ha='center', va='bottom', fontweight='bold')
    
    # 子图4: 量子比特优化效果
    stages = ['原始QUBO', '量子比特共用', '冗余约束消减']
    qubit_counts = [504, 252, 100]
    
    bars4 = ax4.bar(stages, qubit_counts, 
                    color=[colors['neutral'], colors['accent'], colors['success']], 
                    alpha=0.8, edgecolor='white', linewidth=2)
    
    ax4.set_ylabel('量子比特数量', fontsize=12)
    ax4.set_title('量子比特优化效果', fontsize=14, fontweight='bold')
    ax4.grid(True, alpha=0.3, axis='y')
    
    # 添加数值标签
    for bar, count in zip(bars4, qubit_counts):
        height = bar.get_height()
        ax4.text(bar.get_x() + bar.get_width()/2., height + 10,
                f'{count}', ha='center', va='bottom', fontweight='bold', fontsize=12)
    
    plt.suptitle('量子计算机与传统方法性能对比分析', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.savefig('performance_comparison.png', bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 性能对比图表已生成: performance_comparison.png")

def create_hamiltonian_evolution():
    """创建哈密顿量能量演化曲线"""
    print("正在生成哈密顿量演化图表...")
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # 生成哈密顿量演化数据
    time_steps = np.linspace(0, 100, 1000)
    
    # 模拟能量收敛过程
    initial_energy = 1000
    final_energy = -850  # 对应最优解
    noise_amplitude = 50
    
    # 主要收敛曲线
    energy_main = final_energy + (initial_energy - final_energy) * np.exp(-time_steps/25)
    
    # 添加量子涨落噪声
    noise = noise_amplitude * np.exp(-time_steps/40) * np.sin(time_steps * 0.5) * 0.1
    energy_total = energy_main + noise
    
    # 子图1: 完整演化过程
    ax1.plot(time_steps, energy_total, color=colors['primary'], linewidth=2, alpha=0.8, label='实际能量')
    ax1.plot(time_steps, energy_main, color=colors['success'], linewidth=3, linestyle='--', label='理论收敛')
    ax1.axhline(y=final_energy, color='red', linestyle=':', linewidth=2, alpha=0.7, label='最优能量')
    
    ax1.set_xlabel('演化时间步', fontsize=12)
    ax1.set_ylabel('哈密顿量能量', fontsize=12)
    ax1.set_title('哈密顿量总能量演化', fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    
    # 子图2: 收敛阶段能量稳定性
    final_energies = energy_total[-200:]  # 最后200步的能量值
    
    ax2.plot(time_steps[-200:], final_energies, color=colors['primary'], linewidth=2, alpha=0.8)
    ax2.axhline(y=final_energy, color='red', linestyle=':', linewidth=2, alpha=0.7)
    ax2.set_xlabel('演化时间步', fontsize=12)
    ax2.set_ylabel('哈密顿量能量', fontsize=12)
    ax2.set_title('收敛阶段能量稳定性', fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    
    # 添加统计信息
    mean_energy = np.mean(final_energies)
    std_energy = np.std(final_energies)
    ax2.text(0.05, 0.95, f'平均能量: {mean_energy:.1f}\n标准差: {std_energy:.1f}', 
             transform=ax2.transAxes, verticalalignment='top',
             bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.8))
    
    plt.suptitle('光量子计算机哈密顿量演化分析', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.savefig('hamiltonian_evolution.png', bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 哈密顿量演化图表已生成: hamiltonian_evolution.png")

def create_phase_evolution():
    """创建量子比特相位演化图"""
    print("正在生成相位演化图表...")
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))
    
    # 生成模拟数据
    n_qubits = 101
    
    # 初始相位分布（随机）
    np.random.seed(42)
    initial_phases = np.random.uniform(-np.pi, np.pi, n_qubits)
    
    # 最终相位分布（收敛到±π/2）
    final_phases = []
    for i in range(n_qubits):
        target = np.pi/2 if np.random.random() > 0.5 else -np.pi/2
        final_phases.append(target + np.random.normal(0, 0.1))
    
    # 子图1: 初始相位分布
    theta = np.linspace(0, 2*np.pi, 100)
    ax1.plot(np.cos(theta), np.sin(theta), 'k-', alpha=0.3, linewidth=2)
    
    for i, phase in enumerate(initial_phases):
        ax1.plot(np.cos(phase), np.sin(phase), 'o', color=colors['neutral'], markersize=4, alpha=0.7)
    
    ax1.set_xlim(-1.2, 1.2)
    ax1.set_ylim(-1.2, 1.2)
    ax1.set_aspect('equal')
    ax1.set_title('初始相位分布', fontsize=12, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    
    # 子图2: 最终相位分布
    ax2.plot(np.cos(theta), np.sin(theta), 'k-', alpha=0.3, linewidth=2)
    
    for i, phase in enumerate(final_phases):
        color = colors['primary'] if phase > 0 else colors['secondary']
        ax2.plot(np.cos(phase), np.sin(phase), 'o', color=color, markersize=6, alpha=0.8)
    
    ax2.set_xlim(-1.2, 1.2)
    ax2.set_ylim(-1.2, 1.2)
    ax2.set_aspect('equal')
    ax2.set_title('最终相位分布', fontsize=12, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    
    # 添加图例
    ax2.plot([], [], 'o', color=colors['primary'], markersize=8, label='相位 > 0 (σ = +1)')
    ax2.plot([], [], 'o', color=colors['secondary'], markersize=8, label='相位 < 0 (σ = -1)')
    ax2.legend(loc='upper right')
    
    # 子图3: 相位演化时间序列
    time_steps = np.linspace(0, 100, 1000)
    selected_qubits = np.random.choice(n_qubits, 10, replace=False)
    
    for i, qubit_idx in enumerate(selected_qubits):
        target = final_phases[qubit_idx]
        phase_evolution = initial_phases[qubit_idx] + (target - initial_phases[qubit_idx]) * (1 - np.exp(-time_steps/30))
        color = colors['primary'] if target > 0 else colors['secondary']
        ax3.plot(time_steps, phase_evolution, color=color, alpha=0.7, linewidth=2)
    
    ax3.set_xlabel('演化时间步', fontsize=11)
    ax3.set_ylabel('相位 (弧度)', fontsize=11)
    ax3.set_title('量子比特相位演化过程', fontsize=12, fontweight='bold')
    ax3.grid(True, alpha=0.3)
    ax3.axhline(y=np.pi/2, color='red', linestyle='--', alpha=0.5)
    ax3.axhline(y=-np.pi/2, color='red', linestyle='--', alpha=0.5)
    
    # 子图4: 相位分布直方图对比
    bins = np.linspace(-np.pi, np.pi, 20)
    ax4.hist(initial_phases, bins=bins, alpha=0.5, color=colors['neutral'], 
             label='初始分布', density=True)
    ax4.hist(final_phases, bins=bins, alpha=0.7, color=colors['quantum'], 
             label='最终分布', density=True)
    
    ax4.set_xlabel('相位 (弧度)', fontsize=11)
    ax4.set_ylabel('概率密度', fontsize=11)
    ax4.set_title('相位分布对比', fontsize=12, fontweight='bold')
    ax4.legend()
    ax4.grid(True, alpha=0.3)
    
    plt.suptitle('量子比特相位演化分析', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.savefig('phase_evolution_analysis.png', bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 相位演化图表已生成: phase_evolution_analysis.png")

def create_vpp_system_diagram():
    """创建虚拟电厂系统结构图"""
    print("正在生成VPP系统结构图...")
    
    fig, ax = plt.subplots(1, 1, figsize=(16, 12))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 12)
    ax.axis('off')
    
    # 虚拟电厂运营商
    vpp_box = FancyBboxPatch(
        (6, 9), 4, 2,
        boxstyle="round,pad=0.2",
        facecolor=colors['primary'],
        alpha=0.8,
        linewidth=3,
        edgecolor='white'
    )
    ax.add_patch(vpp_box)
    ax.text(8, 10, '虚拟电厂运营商\n(VPP Operator)', ha='center', va='center', 
            fontsize=14, fontweight='bold', color='white')
    
    # 分布式资源
    resources = [
        {"name": "分布式资源1\n(5MW上调)", "pos": (2, 6), "type": "up"},
        {"name": "分布式资源2\n(5MW下调)", "pos": (6, 6), "type": "down"},
        {"name": "分布式资源3\n(5MW上调)", "pos": (10, 6), "type": "up"},
        {"name": "分布式资源4\n(5MW下调)", "pos": (14, 6), "type": "down"}
    ]
    
    for i, resource in enumerate(resources):
        color = colors['success'] if resource["type"] == "up" else colors['secondary']
        
        # 资源框
        res_box = FancyBboxPatch(
            (resource["pos"][0] - 1, resource["pos"][1] - 0.8),
            2, 1.6,
            boxstyle="round,pad=0.1",
            facecolor=color,
            alpha=0.8,
            linewidth=2,
            edgecolor='white'
        )
        ax.add_patch(res_box)
        ax.text(resource["pos"][0], resource["pos"][1], resource["name"],
                ha='center', va='center', fontsize=10, fontweight='bold', color='white')
        
        # 收益比例标注
        k_values = [0.4, 0.6, 0.5, 0.4]
        ax.text(resource["pos"][0], resource["pos"][1] - 1.2, f'k{i+1} = {k_values[i]}',
                ha='center', va='center', fontsize=9, 
                bbox=dict(boxstyle="round,pad=0.2", facecolor='white', alpha=0.8))
        
        # 连接线到VPP
        ax.plot([resource["pos"][0], 8], [resource["pos"][1] + 0.8, 9], 
                'k-', linewidth=2, alpha=0.6)
    
    # 电力市场
    market_box = FancyBboxPatch(
        (6, 2), 4, 1.5,
        boxstyle="round,pad=0.2",
        facecolor=colors['accent'],
        alpha=0.8,
        linewidth=2,
        edgecolor='white'
    )
    ax.add_patch(market_box)
    ax.text(8, 2.75, '电力市场\n(Power Market)', ha='center', va='center', 
            fontsize=12, fontweight='bold', color='white')
    
    # VPP到市场的连接
    ax.annotate('', xy=(8, 3.5), xytext=(8, 9),
               arrowprops=dict(arrowstyle='<->', lw=3, color='black'))
    ax.text(8.5, 6.25, '中标交易\n价格信号', ha='left', va='center', fontsize=10,
            bbox=dict(boxstyle="round,pad=0.2", facecolor='yellow', alpha=0.3))
    
    # 量子计算求解标注
    quantum_box = FancyBboxPatch(
        (12, 2), 3, 1.5,
        boxstyle="round,pad=0.1",
        facecolor=colors['quantum'],
        alpha=0.8,
        linewidth=2,
        edgecolor='white'
    )
    ax.add_patch(quantum_box)
    ax.text(13.5, 2.75, '光量子计算机\n求解', ha='center', va='center', 
            fontsize=11, fontweight='bold', color='white')
    
    # 连接到量子计算
    ax.annotate('', xy=(12, 2.75), xytext=(10, 2.75),
               arrowprops=dict(arrowstyle='->', lw=2, color=colors['quantum']))
    
    # 时间段信息
    time_slots = ['T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8']
    for i, slot in enumerate(time_slots):
        x = 2 + i * 1.5
        ax.text(x, 0.5, slot, ha='center', va='center', fontsize=10, fontweight='bold',
                bbox=dict(boxstyle="circle,pad=0.2", facecolor=colors['primary'], alpha=0.6))
    
    ax.text(8, 0.2, '8个运行时段的解聚合优化', ha='center', va='center', 
            fontsize=11, fontweight='bold')
    
    plt.title('虚拟电厂分布式资源解聚合优化系统架构', fontsize=16, fontweight='bold', pad=20)
    plt.tight_layout()
    plt.savefig('vpp_system_architecture.png', bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ VPP系统结构图已生成: vpp_system_architecture.png")

if __name__ == "__main__":
    print("开始生成量子VPP论文分析可视化图表...")
    print("=" * 50)
    
    try:
        # 生成所有图表
        create_performance_comparison()
        create_hamiltonian_evolution()
        create_phase_evolution()
        create_vpp_system_diagram()
        
        print("=" * 50)
        print("✅ 所有可视化图表生成完成！")
        print("\n生成的图片文件：")
        print("- performance_comparison.png (性能对比分析)")
        print("- hamiltonian_evolution.png (哈密顿量演化)")
        print("- phase_evolution_analysis.png (相位演化分析)")
        print("- vpp_system_architecture.png (VPP系统架构)")
        
    except Exception as e:
        print(f"❌ 生成图表时出错: {e}")
        import traceback
        traceback.print_exc()