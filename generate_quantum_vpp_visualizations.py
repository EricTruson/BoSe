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

def create_quantum_computer_architecture():
    """创建光量子计算机架构图"""
    fig, ax = plt.subplots(1, 1, figsize=(16, 10))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # 光学系统部分
    optical_box = FancyBboxPatch(
        (1, 6), 6, 3,
        boxstyle="round,pad=0.2",
        facecolor=colors['quantum'],
        alpha=0.3,
        linewidth=2,
        edgecolor=colors['quantum']
    )
    ax.add_patch(optical_box)
    ax.text(4, 8.5, '光学系统', fontsize=14, fontweight='bold', ha='center')
    
    # 光学组件
    components_optical = [
        {"name": "飞秒光纤激光器", "pos": (2, 7.5), "size": (1.5, 0.6)},
        {"name": "PPLN1晶体\n(倍频)", "pos": (4.5, 7.5), "size": (1.2, 0.6)},
        {"name": "PPLN2晶体\n(参量转换)", "pos": (6, 7.5), "size": (1.2, 0.6)},
        {"name": "光纤环路\n(DOPO)", "pos": (2, 6.5), "size": (1.5, 0.6)},
        {"name": "相敏放大器", "pos": (4.5, 6.5), "size": (1.2, 0.6)},
        {"name": "光量子比特", "pos": (6, 6.5), "size": (1.2, 0.6)}
    ]
    
    for comp in components_optical:
        box = FancyBboxPatch(
            (comp["pos"][0] - comp["size"][0]/2, comp["pos"][1] - comp["size"][1]/2),
            comp["size"][0], comp["size"][1],
            boxstyle="round,pad=0.05",
            facecolor=colors['primary'],
            alpha=0.8,
            edgecolor='white'
        )
        ax.add_patch(box)
        ax.text(comp["pos"][0], comp["pos"][1], comp["name"],
                ha='center', va='center', fontsize=9, color='white', fontweight='bold')
    
    # 电气系统部分
    electrical_box = FancyBboxPatch(
        (9, 6), 6, 3,
        boxstyle="round,pad=0.2",
        facecolor=colors['classical'],
        alpha=0.3,
        linewidth=2,
        edgecolor=colors['classical']
    )
    ax.add_patch(electrical_box)
    ax.text(12, 8.5, '电气系统', fontsize=14, fontweight='bold', ha='center')
    
    # 电气组件
    components_electrical = [
        {"name": "平衡零差\n探测器(BHD)", "pos": (10, 7.5), "size": (1.5, 0.6)},
        {"name": "FPGA\n处理器", "pos": (12.5, 7.5), "size": (1.2, 0.6)},
        {"name": "上位机\n(PC)", "pos": (14, 7.5), "size": (1.2, 0.6)},
        {"name": "强度调制器\n(IM)", "pos": (10, 6.5), "size": (1.5, 0.6)},
        {"name": "相位调制器\n(PM)", "pos": (12.5, 6.5), "size": (1.2, 0.6)},
        {"name": "反馈控制", "pos": (14, 6.5), "size": (1.2, 0.6)}
    ]
    
    for comp in components_electrical:
        box = FancyBboxPatch(
            (comp["pos"][0] - comp["size"][0]/2, comp["pos"][1] - comp["size"][1]/2),
            comp["size"][0], comp["size"][1],
            boxstyle="round,pad=0.05",
            facecolor=colors['secondary'],
            alpha=0.8,
            edgecolor='white'
        )
        ax.add_patch(box)
        ax.text(comp["pos"][0], comp["pos"][1], comp["name"],
                ha='center', va='center', fontsize=9, color='white', fontweight='bold')
    
    # 工作流程
    workflow_box = FancyBboxPatch(
        (2, 2), 12, 3,
        boxstyle="round,pad=0.2",
        facecolor=colors['accent'],
        alpha=0.2,
        linewidth=2,
        edgecolor=colors['accent']
    )
    ax.add_patch(workflow_box)
    ax.text(8, 4.5, '相干伊辛机(CIM)工作流程', fontsize=14, fontweight='bold', ha='center')
    
    # 工作流程步骤
    workflow_steps = [
        "1. 激光脉冲生成",
        "2. 频率转换与放大", 
        "3. 光量子比特制备",
        "4. Ising问题映射",
        "5. 量子计算求解",
        "6. 结果读取与反馈"
    ]
    
    for i, step in enumerate(workflow_steps):
        x = 3 + (i % 3) * 4
        y = 3.5 - (i // 3) * 0.8
        ax.text(x, y, step, fontsize=10, ha='left', va='center',
                bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.8))
    
    # 连接箭头
    ax.annotate('', xy=(9, 7.5), xytext=(7.5, 7.5),
               arrowprops=dict(arrowstyle='<->', lw=3, color=colors['dark']))
    ax.text(8.25, 7.8, .png")landscapetimization_("- 3d_op    printpng")
ecture.tem_archit_sys"- vpp   print(g")
 ysis.pnization_analoptimt_t("- qubi    prin.png")
son_comparirmancent("- perfo pring")
   _evolution.piltonian"- hamrint( pg")
   lysis.pnolution_anaevse_"- pharint(
    pg") ecture.pnter_architompum_c("- quantunt)
    prihart.png"wcng_floodeli("- qubo_mrint")
    p文件："生成的图片   print(
 化图表生成完成！")"\n所有可视    print(")
    
D优化景观图已生成 3rint("✓
    pscape()n_landiooptimizateate_3d_
    cr)
    厂系统结构图已生成"int("✓ 虚拟电pr   iagram()
 em_d_vpp_systreate  c    
  成")
已生量子比特优化效果图"✓ t(prin
    hart()on_ctioptimiza_qubit_    create
    
能对比图表已生成")"✓ 性
    print(son()ance_compari_perform   create
   
  化曲线已生成")顿量演"✓ 哈密   print(lution()
 tonian_evote_hamil
    crea")
    比特相位演化图已生成量子int("✓ ot()
    prtion_plse_evoluhaate_p   
    cre")
 构图已生成"✓ 光量子计算机架 print(cture()
   ter_architeantum_compue_qucreat
    
    型构建流程图已生成")t("✓ QUBO模  prin
  chart()odeling_flowreate_qubo_m
    c# 生成所有图表  
    ")
  分析可视化图表...论文生成量子VPPint("开始  pr
  ain__":__m= "me__ =__na
if lose()
plt.c   
 white') facecolor='t','tighches=ng', bbox_inandscape.p_lptimizationig('3d_o plt.savefut()
   t.tight_layo 
    pld()
   ax.legen# 添加图例
     
    
   ct=5)=0.5, aspe shrinkrbar(surf,olo
    fig.c颜色条   # 添加 
 bold')
   tweight='size=14, fon路径', font量子计算求解优化问题景观与le('QUBOax.set_tit   ze=12)
 函数值', fontsi('目标set_zlabel  ax.ze=12)
  ontsi f'决策变量 X₂',ylabel( ax.set_
   tsize=12), fonl('决策变量 X₁'_xlabe ax.set题
     # 设置标签和标  路径')
    
'量子计算el=9, lab0.pha=h=4, alw', linewidtlor='yelloth_z, co path_y, paath_x,.plot(pax
    
    z.append(zi)h_  pat
      xi + yi))np.cos(2*.2 *        0     
  + 3*yi) .sin( * np3*xi)sin(.3 * np.  0          
  i**2)) + xi**2 + y*(.1exp(-0*2)) * np.(xi**2 + yi*np.sqrt = (np.sin(     zi
   ath_y[i]], p[i path_x    xi, yi =
    算路径上的Z值值计 # 插):
       ath_length range(p inr i   
    foh_z = []
 atgth)
    p_lenpathobal_min_y, pace(3, gl_y = np.lins
    pathlength)x, path_min_lobal_pace(-3, gnp.lins= x  path_ 50
   h =h_lengt径
    pat 模拟量子计算路 
    #  解')
 最优el='全局=100, labr='red', slo  co          in_z], 
  al_my], [glob[global_min_min_x], r([global_ ax.scatte   
   in_idx]
 obal_m[glmin_z = Zglobal_
    idx]l_min_global_min_y = Y[]
    globa_idxobal_minX[glx = in_bal_m
    glo), Z.shape).argmin(Z_index(npvelra.un = npobal_min_idx
    gl最优点全局  # 标记   
  a=0.6)
 lphs', a='viridi5, cmap.min()-0.z', offset=Z, zdir='ur(X, Y, Z.contos = ax  contour # 添加等高线
    
   e)
  liased=Trutiaewidth=0, an       lin                 0.8, 
  ', alpha=='viridis, Z, cmapsurface(X, Y= ax.plot_f sur        # 绘制表面
    
 + Y))
2*X.cos(2 * np0.   ) + 
      * np.sin(3*YX) (3* np.sin *       0.3
  2)) + Y**(X**2 + (-0.1* * np.exp + Y**2))*2(X*.sqrtnp (np.sin( Z =多个局部最优）
   创建复杂的优化景观（
    # , y)
    meshgrid(xX, Y = np.100)
    ace(-5, 5, y = np.linsp, 100)
    ce(-5, 5 np.linspa    x = 创建网格
  
    #3d')
  ojection='ot(111, prsubpld_fig.adax = )
    =(14, 10)gsizet.figure(fi plig ="""
    f"创建3D优化景观图"):
    "landscape(on_imizatid_optate_3
def cre
close()
    plt.r='white')facecolo', htigox_inches='tre.png', bbchitectup_system_arvefig('vp.sa
    plt_layout()ht plt.tigd=20)
    paight='bold',ntwefo16, ntsize=系统架构', fo资源解聚合优化虚拟电厂分布式tle('plt.ti 
    ']))
   tumors['quanol, color=c', lw=2le='->ct(arrowstyrowprops=diar       ,
        =(10, 2.75)ext, 2.75), xyt'', xy=(12notate(    ax.an连接到量子计算
  
    # 'white')
   color=',weight='bold11, fontize=     fonts, 
       center' va='r',ente, ha='c量子计算机\n求解'.75, '光3.5, 2ax.text(1   )
 boxh(quantum_atc.add_p   )
    ax'white'
 r=ecolo     edg   dth=2,
   linewi8,
     0.lpha=
        aquantum'],=colors['acecolor        f",
1d,pad=0.e="roun     boxstyl3, 1.5,
    (12, 2), ch(
       atncyBboxPm_box = Faquantu标注
    求解
    # 量子计算old')
    ontweight='bize=11, f       fonts    er', 
 r', va='centente优化', ha='c运行时段的解聚合 '8个2,8, 0.    ax.text(  

  0.6))y'], alpha=arlors['primcolor=co2", facee,pad=0.="circlct(boxstyledi bbox=         
      old',ght='bontweintsize=10, f'center', fo va='center',t, ha=slo, 1,  ax.text(x     * 1.5
  = 2 + i x       ):
  slotsme_merate(ti enur i, slot in8']
    fo 'T7', 'T'T6',5', 3', 'T4', 'T', 'T['T1', 'T2= s ime_slot注
    t # 时间段标
    
   ime_info)tch(t   ax.add_pa )
 ral']
   ors['neutcolor=col     edge   ewidth=1,
in l   0.8,
        alpha=
    '],olors['lightr=cecolo   fac,
     nd,pad=0.1"oue="rtyl        boxs
1,), 14,      (1, 0.5(
   ncyBboxPatche_info = Fa信息
    tim   # 时间段
    
 tsize=10) fonter','cencenter', va=ha='          束', 
  核约偏差考约束\n• 节范围\n• 能量平衡, '• 功率调ext(13, 9.5ax.t')
    ='boldntweighte=12, fosiz', font va='centercenter','约束条件', ha='0.5,  1.text(13,ax)
    nt_boxstraicon.add_patch( )
    ax]
   l'assicalors['clecolor=co      edg
  =2,linewidth
         alpha=0.3,],
       ssical'['clacolorscolor=   face  =0.2",
   und,padrotyle="      boxs), 4, 2,
    (11, 9  (
    xPatchx = FancyBboonstraint_bo   c
 条件约束   
    # tsize=10)
 ter', fon='cen', vaa='center    h
        , 约束条件满足'次数最小化\n• 益最大化\n• 调节• 运营商收.5, '.text(3, 9d')
    axtweight='bol=12, fonr', fontsize', va='cente ha='center标',0.5, '优化目x.text(3, 1box)
    ative_h(objecx.add_patc   )
    am']
 tucolors['quan  edgecolor=  h=2,
    ewidt      linha=0.3,
         alpuantum'],
 ors['qcollor=faceco
        ",und,pad=0.2xstyle="ro   bo
     2, (1, 9), 4,   (
     boxPatchcyBbox = Fan  objective_  # 优化目标
     
  pha=0.3))
  alow',ellor='yolecfac", und,pad=0.2="rooxstyle=dict(b  bbox   ,
       size=10 fontva='center',ft', ='le价格信号', ha交易\n.25, '中标ext(8.5, 6x.t]))
    ak's['darlor color=co lw=3,'<->',style=arrowdict(rops=wp        arro       =(8, 9),
ytext), x.5 xy=(8, 3('',tateax.anno接
    的连VPP到市场    
    # te')
or='whi', col'boldht=weigze=12, fontntsi      fo
      center', ', va='nter ha='ceMarket)',\n(Power  '电力市场75,.text(8, 2.
    ax(market_box)patchd_x.ad  a
    )
  ='white'color     edge,
    linewidth=2    a=0.8,
   alph],
        ors['accent'acecolor=col     f=0.2",
   round,padboxstyle="
         4, 1.5,),       (6, 2boxPatch(
 ox = FancyB    market_b  # 电力市场

    
  ha=0.6)lpth=2, anewid   'k-', li             9], 
  + 0.8,s"][1]ource["po 8], [res"pos"][0],source[x.plot([re a   
    PP    # 连接线到V          
  .8))
=0te', alphar='whilo faceco2",ound,pad=0.style="rdict(box       bbox=    
     ze=9, tsicenter', fonenter', va='     ha='c          ]}',
 ues[i {k_vali+1} =2, f'k{- 1.][1] s"ource["po0], res"pos"][source[.text(re    ax
    .5, 0.4]0.4, 0.6, 0es = [   k_valu标注
        # 收益比例  
     
      ite')or='whd', colt='boltweighon ffontsize=10,nter', va='cecenter',       ha='          
["name"],, resourcepos"][1]["urce[0], reso"pos"]ource[x.text(res a
       x)ch(res_bo_patddax.a        )
    ite'
    or='whcoledge        ,
    newidth=2    li       =0.8,
 ha         alp   lor=color,
     faceco
       ",und,pad=0.1oxstyle="ro  b      1.6,
     2,          ),
  "][1] - 0.8e["pos resourc"][0] - 1,se["po(resourc       
     tch(xPaboancyBx = Fres_bo   源框
      # 资     
     
     ondary']'secelse colors[p" ] == "u"type"e[ if resourc']ors['successcolr =     coloces):
    e(resourmerat in enuresource for i,    
     ]
 
  "}wn: "doype", 6), "tos": (14调)", "p\n(5MW下"分布式资源4{"name":         up"},
e": "), "typ0, 6 (1", "pos":n(5MW上调) "分布式资源3\ {"name":  },
     : "down""type",  6)"pos": (6,", 下调)\n(5MW2": "分布式资源name   {"
     p"},"type": "u (2, 6),  "pos":\n(5MW上调)",式资源1me": "分布"na        {rces = [
esou布式资源
    r
    # 分
    ='white')ld', color'botweight=, fon14fontsize=         nter', 
   ', va='ceter, ha='cenator)'\n(VPP Oper '虚拟电厂运营商xt(8, 10,ax.te
    h(vpp_box)d_patcx.ad a
    )
   lor='white'co     edge,
   ewidth=3     lin  ,
 alpha=0.8       ,
 ary']'primors[ecolor=col  fac  
    2",d=0.="round,patyle      boxs, 2,
  (6, 9), 4
        oxPatch(x = FancyBb vpp_bo拟电厂运营商
   
    # 虚ff')
    'oaxis(    ax.
m(0, 12)_yli  ax.set  lim(0, 16)
   ax.set_x
 12))gsize=(16, ts(1, 1, filt.subplo ax = p   fig,
 "厂系统结构图""创建虚拟电"" "
   :m_diagram()pp_syste create_v

deft.close())
    pllor='white'ht', facecoinches='tigbbox_', lysis.pngization_anait_optim('qublt.savefigout()
    pght_lay    plt.tit='bold')
ighe=16, fontwesiz化策略分析', font量子比特优title('  plt.sup
    
  ha=0.2)), alpred'r='facecoload=0.3", nd,pe="roustylbox=dict(box     b      s,
  Axe.transm=ax4transfor, 1000量子比特)'前硬件限制\n(~, '当, 0.8ext(0.7   ax4.twidth=2)
 a=0.7, line='--', alphnestyle', li'redolor=y=1000, cx4.axhline(
    a# 添加当前硬件限制线  
      log')
cale('4.set_ys()
    ax  ax4.legend
  .3) alpha=0rid(True,x4.gd')
    abolntweight='4, foe=1析', fontsiz模可扩展性分t_title('问题规.se    ax4ntsize=12)
量子比特数量', folabel('所需.set_y
    ax4tsize=12), fon布式资源数量'l('分labet_x   ax4.se 
 )
   bel='优化后'ess'], laolors['succr=c       colo 
      rsize=8,, markenewidth=3o-', lis, 'd_qubitimize optlem_sizes,plot(prob
    ax4.label='优化前')utral'], 'neor=colors[    col
         rsize=8, ke marewidth=3, linits, 'o-',uboriginal_qm_sizes, proble.plot(    ax4后需求
    
zes]  # 优化_siprobleme in 5 for siz [size * 2ts =timized_qubiop   # 原始需求
  sizes] m_oble in pr126 for size * bits = [sizeriginal_qu量
    o分布式资源数 64]  #  16, 32, 8,zes = [4,oblem_si pr扩展性分析
     # 子图4: 可
  e=12)
    d', fontsiztweight='bolbottom', fonnter', va='n}', ha='cereductio  f'{            + 5,
  , height idth()/2._w) + bar.get.get_x(xt(bar3.te
        axight()et_he.ght = bar      heigctions):
  rs3, redu(baction in zip, redubarr    
    fo
 'y')xis==0.3, a alphad(True, ax3.gri)
   ='bold'ontweight, f14fontsize=, 略效果对比'_title('优化策  ax3.setze=12)
  tsion', f特数量bel('减少的量子比.set_yla  
    ax3
  linewidth=2)or='white', .8, edgecolpha=0al                   ']], 
 s['quantum colorss'],['succers], coloaccent'or=[colors['       col           , 
   reductionss,tegier(stras3 = ax3.baar
    b特数量
      # 减少的量子比, 404], 152ons = [252educti  r'综合优化']
  , 冗余约束消减'['量子比特共用', '=  strategies 对比
   略效果图3: 优化策# 子      
')
  weight='bold14, fonte=fontsiz, 特优化分布'e('量子比titl2.set_0))
    ax05, e=(0.05, 0.explod, tartangle=90          s                          
  %','%1.1f%t= autopcrs_pie,olors=coloels, clabels=lab.pie(sizes, exts = ax2xts, autots, te
    wedge
    y']]['primarrs'], coloesscolors['succt'], ors['accen [collors_pie =用']
    co减', '最终使约束消'冗余比特共用减少',  ['量子 labels =]
   ts[2]qubit_coun[2], t_counts1] - qubi_counts[itts[1], qubt_coun- qubis[0] qubit_count sizes = [例饼图
   # 子图2: 减少比    
    
lor='red')cold', boight='ontwe    f        
    =0.2),ed', alphaecolor='rfacd=0.3", ,pa="roundoxstylex=dict(b         bbo
       ter', ', va='centercen}', ha='reduction   f'-{            ])/2, 
 _counts[i+1i] + qubits[it_count, (qubxt(i+0.51.te    ax    ounts[i+1]
it_c- qub_counts[i] qubitreduction =         ed'))
r='rw=3, coloyle='->', lct(arrowst=diwpropsarro              ,
      - 30)] bit_counts[i(i, quext= 30), xytounts[i+1] +i+1, qubit_ce('', xy=(annotatax1.      
  es)-1):nge(len(stag in rar i
    fo 添加减少箭头  
    #
  tsize=12)'bold', fonntweight=om', fo='bott'center', vaha=',    f'{count}           ht + 10,
  )/2., heiget_width( bar.g) +(bar.get_x(   ax1.text     ght()
t_heibar.ge= ht         heig):
tst_couns1, qubi zip(barr, count infor ba值标签
    # 添加数
    
    xis='y')ha=0.3, alpgrid(True, a1.')
    axht='boldfontweigtsize=14, 化过程', fon量子比特优.set_title(')
    ax1ize=12fonts特数量', '量子比t_ylabel(.se
    ax1
    inewidth=2)ite', lgecolor='wh, ed.8=0     alpha             , 
  ']]ors['success'], colors['accent'], cols['neutralcolor=[color                   ounts, 
 qubit_c, ar(stagesars1 = ax1.b化
    b1: 量子比特数量变  # 子图
    
   80.2][0, 50,ages = on_percent  reducti2, 100]
  504, 25 = [tsoun_cqubit
    ', '冗余约束消减']BO', '量子比特共用'原始QU  stages = [   # 数据
  
 
    , 12)) figsize=(15ts(2, 2,lt.subplo4)) = p(ax3, axax1, ax2), 
    fig, ((图"""量子比特优化效果  """创建
  rt():zation_chaubit_optimicreate_q
def close()
    plt.r='white')
olo facec'tight',es=bbox_inchon.png', comparisformance_'perig( plt.saveft()
   youht_la    plt.tigold')
ontweight='b=16, fize分析', fonts与传统方法性能对比e('量子计算机itl  plt.supt   
  ')
 weight='boldttom', fonta='bo, vha='center'}x', '{ratio:.1f       f,
         1.1ight*()/2., heidtht_w + bar.geet_x()4.text(bar.g ax()
       eightar.get_h  height = b    ]):
  tios[1:up_ras4, speedbar zip(o inti, raarfor b
    值标签    # 添加数g')
    
t_yscale('lo    ax4.se3)
, alpha=0.x4.grid(True
    ation=45)', rotaams(axis='x_par.tick)
    ax4='bold'tweight4, fon fontsize=1','计算速度加速比t_title(    ax4.setsize=12)
算机的加速比', fonl('相对光量子计labet_y  ax4.se])
    
  rs['accent'] coloy'],s['secondarolor          c            '], 
     ndaryecoolors['sical'], clors['class'], coicalolors['class  color=[c                os[1:], 
  eedup_rati spmethods[1:],bar(= ax4. bars4 
   ]en(times))n range(l] for i i/times[0times[i]p_ratios = [speedu加速比分析
    
    # 子图4:     1.3, 1.0))
to_anchor=(', bbox_'upper rightend(loc=
    ax3.leg)=20 padght='bold',, fontwei fontsize=14评估',tle('综合性能_tix3.set a
   0, 10)ylim(t_
    ax3.seories)s(categlabeltick_x   ax3.setes[:-1])
 ticks(anglset_x 
    ax3.y'])
   econdarr=colors['slopha=0.25, co_scores, alheuristicl(angles, fil3.  axdary'])
  cons['secolor=color, abel='启发式算法'ewidth=2, l', lin, 'o-oresc_scstiheuriot(angles,     ax3.plsical'])
rs['clasloolor=co.25, cs, alpha=0ssical_score clagles,x3.fill(an
    a'])calclassi['lor=colors, cobel='经典优化器', la=2', linewidth 'o-al_scores,assic, clplot(angles
    ax3.ntum'])quaors['lor=col=0.25, coalphas, scoreuantum_ll(angles, q   ax3.fiuantum'])
 =colors['q', color='光量子计算机th=2, labelinewid, l 'o-'ntum_scores,uat(angles, q3.ploar')
    axtion='polprojec2, 2, 3, lt.subplot(x3 = p    a
    
es[:1]uristic_scor heres +=ic_scoeurist[:1]
    hcoresl_s= classicacores +classical_s
    [:1]esquantum_scorores += m_sc
    quantu   闭合图形
  gles[:1]  #s += anngle)
    atolist(e).dpoint=Falsies), enlen(categor 2*np.pi, ace(0,nsp np.li   angles =
    
  启发式算法平均 #7, 8, 8]  [4, 10, cores =heuristic_s
    均优化器平 经典 #] , 9, 10, 106, 10= [s ssical_score cla机
   量子计算]  # 光10, 9, 7, 8s = [10, oreantum_sc0分)
    qu化评分 (0-1   # 归一 
 ']
   扩展性', '实用性 '稳定性', '可精度','求解, 速度'es = ['计算egori
    cat达图图3: 效率比较雷   
    # 子pha=0.2))
 ', alecolor='red0.3", facround,pad=style="=dict(box        bbox, 
     ransAxessform=ax2.t, tran: 33600元''最优解2, 0.95, xt(0.0ax2.te   pha=0.7)
 th=2, alinewid='--', llelinestyor='red', =33600, colaxhline(yne = ax2.imal_li   opt # 标注最优解
 )
    
   , alpha=0.3(True2.grid45)
    axtion=='x', rota_params(axisax2.tick    old')
t='bfontweightsize=14, , fon度对比'le('求解精t_tit.se
    ax2fontsize=12),  (元)'label('目标函数值 ax2.set_y])
   ['accent']ry'], colorss['seconda colory'],'secondarlors[        co                                       ssical'], 
lors['claical'], coors['classtum'], coluanors['q[colcolor=ves, ti objecr(methods,.bax2 = a比
    bars2 目标函数值对# 子图2:  
  
    t='bold')ntweigh', fottom'bo, va= ha='center'}',me:.2f'{ti f         
      1.1,eight*2., h_width()/.get) + barbar.get_x(t(   ax1.tex   t()
  get_heighbar.   height = ):
     ars1, timesme in zip(bar, ti  for b  标签

    # 添加数值=0.3)
    True, alphagrid(   ax1.on=45)
 otati(axis='x', ramsparick_  ax1.t
  ='bold')ontweightize=14, f尺度)', fonts比 (对数le('计算时间对ax1.set_tit2)
     fontsize=1'计算时间 (ms)',et_ylabel(    ax1.s')
yscale('log  ax1.set_])
  cent']ors['acy'], colndarlors['secodary'], coeconlors['s        co                              al'], 
    icolors['classal'], cclassiclors['um'], co'quantlor=[colors[ times, cods,(metho1.baraxars1 = 
    b对数尺度）间对比（ # 子图1: 计算时    
   31600]
 33600, 33600,33600, , 33600, 60033jectives = [
    ob.02]676.62, 130, 793.84, 1175.30, 17, 14.3imes = [1. t
   降']索', '最速下模拟退火', '禁忌搜Cplex', 'robi', '子计算机', 'Gu = ['光量
    methods    # 数据 
)
   2)=(16, 1izegs 2, fiots(2,t.subpl pl) = ax4)ax2), (ax3,(ax1, fig, ("
    比图表"""""创建性能对  son():
  rimpaformance_co_pereatecr

def lt.close()    p')
color='whitefaceght', ches='tiin bbox_g',lution.pnonian_evoiltvefig('ham.sa pltayout()
   ht_lig
    plt.tld')'boeight= fontwsize=16,化分析', font光量子计算机哈密顿量演uptitle('
    plt.s
    a=0.8))te', alph'whi facecolor=3",ound,pad=0.oxstyle="rict(b  bbox=d
           'top',alignment=s, verticalax2.transAxensform=    tra      , 
   energy:.1f}' {std_1f}\n标准差:an_energy:.平均能量: {me05, 0.95, f'ax2.text(0.)
    l_energies(fina.stdy = np   std_energenergies)
 l_.mean(fina npgy =  mean_ener信息
  加统计
    # 添  )
  .3 alpha=0rid(True, ax2.g   'bold')
tweight==14, fontsizefon段能量稳定性', 敛阶_title('收   ax2.settsize=12)
 密顿量能量', fon('哈el_ylabet)
    ax2.se=12', fontsizl('演化时间步_xlabe.set   ax2lpha=0.7)
 2, ah=dt, linewi':'yle=d', linest'rey, color=final_energhline(y=axx2.)
    aalpha=0.8width=2, mary'], linecolors['pries, color=l_energinafi00:], -2_steps[x2.plot(time示时间序列
    a # 主轴显
    
   fontsize=12)概率密度', label('t.set_x ax2_his   ')
rizontal'hotion=entaty=True, oritum'], densi'quanlor=colors[ co                                      0.6, 
  s=30, alpha=bins, ieenergal_hist(finhist.s = ax2_s, patcheinunts, b co
   2.twinx()st = ax
    ax2_hi # 创建能量分布直方图  
   
  0步的能量值  # 最后200:]20l[- energy_totaes =rginal_ene
    fi定性分析能量分布和稳   # 子图2: )
    
 敛区域', label='收cess']olors['suc0.2, color=cha=    alp           
       ].max()+20,tal[800:to0, energy_].min()-2[800:_total:], energy800s[me_stepbetween(ti ax1.fill_区域标注
   
    # 添加收敛
    d()legen)
    ax1., alpha=0.3grid(True')
    ax1.ld'boontweight= fontsize=14,能量演化', fe('哈密顿量总et_titl1.s2)
    axfontsize=1顿量能量', ('哈密abel_yl  ax1.set)
  e=12 fontsiz时间步',el('演化t_xlabax1.se   
    ='最优能量')
  labela=0.7,dth=2, alph=':', linewitylenesr='red', li, colonal_energyne(y=fi ax1.axhli)
   论收敛''理l=, labe--'le='h=3, linesty'], linewidtuccesslors['sin, color=coergy_maeps, en(time_stax1.plot)
    abel='实际能量'0.8, llpha= alinewidth=2,rimary'], s['plorcolor=total, corgy_teps, enelot(time_sx1.p演化过程
    a  # 子图1: 完整  
  + noise
  in ma = energy_energy_total   _steps))
 imelen(t(0, 0.1, alrm.random.no * np * 0.5)(time_stepsin.s) * np_steps/40(-timeexpude * np._amplit = noiseise   no噪声
 涨落# 添加量子
    
    5)ps/2_step(-timey) * np.ex final_energgy -ial_eneritnergy + (inl_eain = finanergy_m收敛曲线
    e  
    # 主要= 50
  itude pl_am
    noise50  # 对应最优解 = -8final_energy    = 1000
rgy l_ene initia
   敛过程 模拟能量收 #
    
    1000)e(0, 100,nspac = np.li_stepsme ti量演化数据
       # 生成哈密顿 6))
    
ize=(15, 2, figss(1,bplot.sux2) = plt (ax1, afig,   线"""
 顿量能量演化曲"""创建哈密  
  ution():n_evolamiltoniate_hrea)

def ct.close(te')
    pl'whiolor=, facecht'nches='tig_ioxbbg', nalysis.pntion_ase_evoluhaavefig('p
    plt.s_layout()tight    plt.bold')
ght='fontweiize=16, nts特相位演化分析', fo量子比ptitle('t.su  pl    
  lpha=0.3)
, aruerid(Tax4.gend()
    ax4.leg  
  'bold')eight=12, fontw fontsize=相位分布对比',_title('setx4.    ae=11)
', fontsizabel('概率密度.set_ylax4
    =11)tsize度)', fonbel('相位 (弧4.set_xla    
    axrue)
density=T终分布', ='最     label    , 
    tum']ancolors['qulor=coa=0.7, s=bins, alphhases, binal_pst(fin4.hi axue)
   ty=Tr densiabel='初始分布',  l           ral'], 
rs['neut color=colo alpha=0.5,=bins, binsl_phases,ist(initiaax4.h 20)
    , np.pi,p.pice(-nnspali = np.ins比
    b直方图对 子图4: 相位分布   
    #位 -π/2')
 el='目标相pha=0.5, lab'--', al, linestyle=olor='red'=-np.pi/2, chline(y  ax3.ax
  相位 +π/2')'目标el=a=0.5, labe='--', alph, linestylred'olor='.pi/2, cline(y=np ax3.axh  a=0.3)
 (True, alphid  ax3.grold')
  'bntweight=tsize=12, fo, fon子比特相位演化过程'e('量.set_titl
    ax3ntsize=11)(弧度)', foel('相位 3.set_ylab11)
    axfontsize=el('演化时间步', xlab  ax3.set_  =2)
    
newidth7, lipha=0.olor, alion, color=case_evoluteps, phime_st(t ax3.plot   ]
    y'econdarlors['s 0 else co target >ry'] if['primacolorscolor =      
   teps/30))time_sexp(-np.dx]) * (1 - qubit_iases[phtial_- ini (target it_idx] +phases[qubl_n = initiaase_evolutio   ph/2
     -np.pielse t_idx] > 0 ses[qubifinal_phaif 2 t = np.pi/     targets):
   qubited_te(selecin enumeraubit_idx  for i, q   
    
ace=False)ts, 10, replhoice(n_qubip.random.c= ns ted_qubit  selec
  3: 相位演化时间序列
    # 子图 1))
    (1.3,_to_anchor= bboxt', righpperegend(loc='ux2.l')
    a< 0 (σ = -1)el='相位 size=8, laby'], marker['secondarr=colors, colo], 'o'ot([], [    ax2.pl(σ = +1)')
bel='相位 > 0 ersize=8, lamary'], markcolors['priolor= [], 'o', c2.plot([],添加图例
    ax 
    # 
   =0.3)e, alphaid(Tru    ax2.gr'bold')
fontweight=12, ontsize=('最终相位分布', f2.set_title  ax
  ct('equal')et_aspeax2.s  , 1.2)
  _ylim(-1.2   ax2.set2)
 , 1.m(-1.2liax2.set_x      
  alpha=0.8)
ize=6, or, markerscolor=col', phase), 'oe), np.sin(cos(phasnp.ot( ax2.pl   
    dary']'seconelse colors[hase > 0 ry'] if p['primalor = colors   co):
     inal_phasesate(f enumer phase inr i, fo   
    
idth=2)0.3, linew alpha=heta), 'k-',(t.sineta), nps(thlot(np.co布
    ax2.p位分 子图2: 最终相  #
     3)
 ue, alpha=0.1.grid(Trax   
 d')ght='bol2, fontweiize=1分布', fonts初始相位('tleet_ti.s ax1')
   ('equalset_aspect   ax1.
 -1.2, 1.2)et_ylim( ax1.s   1.2, 1.2)
.set_xlim(-   
    ax1=0.7)
 ize=4, alphaersrk malor, color=coase), 'o',sin(ph), np.asephs(ot(np.co      ax1.pl
  tral']lors['neulor = coco  s):
      _phaseate(initial enumer i, phase in 
    for2)
   dth=.3, linewik-', alpha=0 '.sin(theta),, npos(theta)plot(np.c ax1.)
    100, 2*np.pi,space(0= np.lin   theta 
 相位分布# 子图1: 初始
        ion[-1])
olut_evses.append(phainal_phase        f))
/30(-time_steps np.exp) * (1 -al_phases[i]iti inarget - + (tphases[i]n = initial_utioase_evol
        phpi/2lse -np.5 endom() > 0.random.ranp. np.pi/2 if target =
        2收敛的过程 模拟相位向±π/ #       ts):
bi range(n_qur i in]
    foses = [final_pha中的相位变化
        # 演化过程  
s)
  qubit, n_pinp.pi, np.rm(-andom.unifos = np.ral_phaseti ini布（随机）
   始相位分   # 初
    
 = 101ubits 0)
    n_q00, 1, 100inspace(0 np.leps =    time_st成模拟数据
   # 生
    
 ))e=(14, 102, figsizbplots(2, 4)) = plt.su ax2), (ax3, axx1,, ((afig   
 特相位演化图""""创建量子比   ""n_plot():
 se_evolutiote_pha

def creaclose()  plt.')
  ite='wholor, faceches='tight'incbbox_re.png', tectu_archicomputerntum_ua'qfig(    plt.saveout()
_lay   plt.tight20)
 d='bold', pantweight==16, fo构', fontsize(相干伊辛机)系统架('光量子计算机  plt.title')
    
  ht='bold0, fontweigntsize=1fonter', ='ceha'数据交换', 