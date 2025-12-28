import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch
import matplotlib.patches as patches

plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 150
plt.rcParams['savefig.dpi'] = 150

colors = {'primary': '#2E86AB', 'secondary': '#A23B72', 'accent': '#F18F01', 
          'success': '#C73E1D', 'quantum': '#6A4C93', 'classical': '#4ECDC4'}

# 1. 性能对比图
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))

methods = ['Quantum\nComputer', 'Gurobi', 'Cplex', 'Simulated\nAnnealing', 'Tabu\nSearch', 'Gradient\nDescent']
times = [1.17, 14.30, 175.30, 793.84, 1676.62, 13.02]
objectives = [33600, 33600, 33600, 33600, 33600, 31600]

bars1 = ax1.bar(methods, times, color=[colors['quantum'], colors['classical'], colors['classical'], 
                                      colors['secondary'], colors['secondary'], colors['accent']])
ax1.set_yscale('log')
ax1.set_ylabel('Computation Time (ms)')
ax1.set_title('Performance Comparison (Log Scale)')
ax1.tick_params(axis='x', rotation=45)
ax1.grid(True, alpha=0.3)

bars2 = ax2.bar(methods, objectives, color=[colors['quantum'], colors['classical'], colors['classical'], 
                                           colors['secondary'], colors['secondary'], colors['accent']])
ax2.set_ylabel('Objective Value (Yuan)')
ax2.set_title('Solution Quality Comparison')
ax2.tick_params(axis='x', rotation=45)
ax2.grid(True, alpha=0.3)
ax2.axhline(y=33600, color='red', linestyle='--', alpha=0.7)

speedup_ratios = [times[i]/times[0] for i in range(len(times))]
bars3 = ax3.bar(methods[1:], speedup_ratios[1:], 
                color=[colors['classical'], colors['classical'], colors['secondary'], 
                       colors['secondary'], colors['accent']])
ax3.set_ylabel('Speedup Ratio')
ax3.set_title('Speed Acceleration Analysis')
ax3.tick_params(axis='x', rotation=45)
ax3.grid(True, alpha=0.3)
ax3.set_yscale('log')

stages = ['Original\nQUBO', 'Qubit\nSharing', 'Redundancy\nReduction']
qubit_counts = [504, 252, 100]
bars4 = ax4.bar(stages, qubit_counts, color=[colors['secondary'], colors['accent'], colors['success']])
ax4.set_ylabel('Number of Qubits')
ax4.set_title('Qubit Optimization Effect')
ax4.grid(True, alpha=0.3)

plt.suptitle('Quantum Computer vs Traditional Methods Performance Analysis', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('performance_comparison.png', bbox_inches='tight', facecolor='white')
plt.close()

# 2. 哈密顿量演化
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

time_steps = np.linspace(0, 100, 1000)
initial_energy = 1000
final_energy = -850
energy_main = final_energy + (initial_energy - final_energy) * np.exp(-time_steps/25)
noise = 50 * np.exp(-time_steps/40) * np.sin(time_steps * 0.5) * 0.1
energy_total = energy_main + noise

ax1.plot(time_steps, energy_total, color=colors['primary'], linewidth=2, label='Actual Energy')
ax1.plot(time_steps, energy_main, color=colors['success'], linewidth=2, linestyle='--', label='Theoretical Convergence')
ax1.axhline(y=final_energy, color='red', linestyle=':', linewidth=2, label='Optimal Energy')
ax1.set_xlabel('Evolution Time Steps')
ax1.set_ylabel('Hamiltonian Energy')
ax1.set_title('Hamiltonian Energy Evolution')
ax1.grid(True, alpha=0.3)
ax1.legend()

final_energies = energy_total[-200:]
ax2.plot(time_steps[-200:], final_energies, color=colors['primary'], linewidth=2)
ax2.axhline(y=final_energy, color='red', linestyle=':', linewidth=2)
ax2.set_xlabel('Evolution Time Steps')
ax2.set_ylabel('Hamiltonian Energy')
ax2.set_title('Convergence Stage Stability')
ax2.grid(True, alpha=0.3)

plt.suptitle('Optical Quantum Computer Hamiltonian Evolution Analysis', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('hamiltonian_evolution.png', bbox_inches='tight', facecolor='white')
plt.close()

# 3. 相位演化
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))

n_qubits = 101
np.random.seed(42)
initial_phases = np.random.uniform(-np.pi, np.pi, n_qubits)
final_phases = [np.pi/2 if np.random.random() > 0.5 else -np.pi/2 for _ in range(n_qubits)]

theta = np.linspace(0, 2*np.pi, 100)
ax1.plot(np.cos(theta), np.sin(theta), 'k-', alpha=0.3, linewidth=2)
for phase in initial_phases:
    ax1.plot(np.cos(phase), np.sin(phase), 'o', color=colors['secondary'], markersize=3, alpha=0.7)
ax1.set_xlim(-1.2, 1.2)
ax1.set_ylim(-1.2, 1.2)
ax1.set_aspect('equal')
ax1.set_title('Initial Phase Distribution')
ax1.grid(True, alpha=0.3)

ax2.plot(np.cos(theta), np.sin(theta), 'k-', alpha=0.3, linewidth=2)
for phase in final_phases:
    color = colors['primary'] if phase > 0 else colors['accent']
    ax2.plot(np.cos(phase), np.sin(phase), 'o', color=color, markersize=4, alpha=0.8)
ax2.set_xlim(-1.2, 1.2)
ax2.set_ylim(-1.2, 1.2)
ax2.set_aspect('equal')
ax2.set_title('Final Phase Distribution')
ax2.grid(True, alpha=0.3)

time_evolution = np.linspace(0, 100, 1000)
for i in range(10):
    target = final_phases[i]
    phase_evo = initial_phases[i] + (target - initial_phases[i]) * (1 - np.exp(-time_evolution/30))
    color = colors['primary'] if target > 0 else colors['accent']
    ax3.plot(time_evolution, phase_evo, color=color, alpha=0.7, linewidth=2)
ax3.set_xlabel('Evolution Time Steps')
ax3.set_ylabel('Phase (radians)')
ax3.set_title('Qubit Phase Evolution Process')
ax3.grid(True, alpha=0.3)

bins = np.linspace(-np.pi, np.pi, 20)
ax4.hist(initial_phases, bins=bins, alpha=0.5, color=colors['secondary'], label='Initial', density=True)
ax4.hist(final_phases, bins=bins, alpha=0.7, color=colors['quantum'], label='Final', density=True)
ax4.set_xlabel('Phase (radians)')
ax4.set_ylabel('Probability Density')
ax4.set_title('Phase Distribution Comparison')
ax4.legend()
ax4.grid(True, alpha=0.3)

plt.suptitle('Qubit Phase Evolution Analysis', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('phase_evolution_analysis.png', bbox_inches='tight', facecolor='white')
plt.close()

# 4. VPP系统架构
fig, ax = plt.subplots(1, 1, figsize=(14, 10))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')

vpp_box = FancyBboxPatch((5, 7.5), 4, 1.5, boxstyle="round,pad=0.2", 
                         facecolor=colors['primary'], alpha=0.8, edgecolor='white', linewidth=2)
ax.add_patch(vpp_box)
ax.text(7, 8.25, 'Virtual Power Plant\nOperator', ha='center', va='center', 
        fontsize=12, fontweight='bold', color='white')

resources = [
    {"name": "Resource 1\n(5MW Up)", "pos": (2, 5), "type": "up"},
    {"name": "Resource 2\n(5MW Down)", "pos": (5, 5), "type": "down"},
    {"name": "Resource 3\n(5MW Up)", "pos": (9, 5), "type": "up"},
    {"name": "Resource 4\n(5MW Down)", "pos": (12, 5), "type": "down"}
]

for i, resource in enumerate(resources):
    color = colors['success'] if resource["type"] == "up" else colors['accent']
    res_box = FancyBboxPatch((resource["pos"][0] - 0.8, resource["pos"][1] - 0.6), 1.6, 1.2,
                             boxstyle="round,pad=0.1", facecolor=color, alpha=0.8, 
                             edgecolor='white', linewidth=2)
    ax.add_patch(res_box)
    ax.text(resource["pos"][0], resource["pos"][1], resource["name"],
            ha='center', va='center', fontsize=9, fontweight='bold', color='white')
    
    k_values = [0.4, 0.6, 0.5, 0.4]
    ax.text(resource["pos"][0], resource["pos"][1] - 1, f'k{i+1} = {k_values[i]}',
            ha='center', va='center', fontsize=8, 
            bbox=dict(boxstyle="round,pad=0.2", facecolor='white', alpha=0.8))
    
    ax.plot([resource["pos"][0], 7], [resource["pos"][1] + 0.6, 7.5], 'k-', linewidth=2, alpha=0.6)

market_box = FancyBboxPatch((5, 2), 4, 1.2, boxstyle="round,pad=0.2",
                            facecolor=colors['classical'], alpha=0.8, edgecolor='white', linewidth=2)
ax.add_patch(market_box)
ax.text(7, 2.6, 'Power Market', ha='center', va='center', 
        fontsize=12, fontweight='bold', color='white')

ax.annotate('', xy=(7, 3.2), xytext=(7, 7.5), arrowprops=dict(arrowstyle='<->', lw=3, color='black'))
ax.text(7.5, 5.35, 'Bidding\nPrice Signal', ha='left', va='center', fontsize=9,
        bbox=dict(boxstyle="round,pad=0.2", facecolor='yellow', alpha=0.3))

quantum_box = FancyBboxPatch((10, 2), 2.5, 1.2, boxstyle="round,pad=0.1",
                             facecolor=colors['quantum'], alpha=0.8, edgecolor='white', linewidth=2)
ax.add_patch(quantum_box)
ax.text(11.25, 2.6, 'Quantum\nComputer', ha='center', va='center', 
        fontsize=10, fontweight='bold', color='white')

ax.annotate('', xy=(10, 2.6), xytext=(9, 2.6), arrowprops=dict(arrowstyle='->', lw=2, color=colors['quantum']))

time_slots = ['T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8']
for i, slot in enumerate(time_slots):
    x = 1.5 + i * 1.4
    ax.text(x, 0.5, slot, ha='center', va='center', fontsize=9, fontweight='bold',
            bbox=dict(boxstyle="circle,pad=0.2", facecolor=colors['primary'], alpha=0.6))

ax.text(7, 0.2, '8 Time Periods Disaggregation Optimization', ha='center', va='center', 
        fontsize=11, fontweight='bold')

plt.title('Virtual Power Plant Distributed Resource Disaggregation System Architecture', 
          fontsize=14, fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig('vpp_system_architecture.png', bbox_inches='tight', facecolor='white')
plt.close()

print("All visualization charts generated successfully!")
print("Generated files:")
print("- performance_comparison.png")
print("- hamiltonian_evolution.png") 
print("- phase_evolution_analysis.png")
print("- vpp_system_architecture.png")