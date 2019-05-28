# Modeling Color Difference for Visualization Design

为可视化设计建模色差

## Abstract

关注散点图中的对角对称标记、条形图中的细长标记和线图中的非对称细长标记。

我们证实了先前的发现，感知到的颜色差异与大小成反比，并发现细长的标记为编码设计者提供了更大的识别力。我们的结果为可视化提供了色差的概率模型。

大多数有效的视觉色彩选择准则都是基于在最佳视觉环境中使用大而均匀的视野测量的色彩感知，或者基于定性的直觉

可视化通常使用小而长的标记，这些限制可能会导致可视化中的数据误读。

目标是开发量化指标，帮助人们在可视化中更有效地使用颜色。

>three common mark types:points, bars, and lines.

>effective encoding design

## 1 INTRODUCTION

However, many visualization systems rely on CIELAB and similar metrics to construct encodings, leading them to systematically underestimate the perceived differences between colors .

This underestimation can lead to ineffective encoding choices by, for example, mapping continuous data to too narrow a range or encoding ranked or categorical data with colors that are too close together.

## 2 BACKGROUND

### 2.1 Color in Visualization

In all of these studies, leveraging color effectively requires selecting color maps that span an appropriate encoding range to highlight important differences in the distribution.

ColorBrewer, amongthe most common color encoding tools currently in use.

The ramps emerging from these studies were then hand-tuned for aesthetics and performance. Subsequent studies provide algorithmic approximations of the resulting encodings by
interpolating in CIELUV .

Colorgorical optimizes across perceptual distance,nameability, and aesthetic considerations to generatecategorical palettes.

### 2.2 Color Difference Metrics

Color difference metrics normalize color space such that the geometric and perceptual differences between colors are aligned.

`色差度量标准使颜色空间规范化，从而使颜色之间的几何和知觉差异对齐。`

我们的研究使用CIELAB[25]，一个由三个主轴组成的颜色空间：l∗(亮度)，a∗(红色或绿色的数量)和b∗(蓝色或黄色的数量)。

### 2.3 Color Difference in Practice

## 3 VISUALIZATION FACTORS IN COLOR PERCEPTION

Visualizations violate the assumptions of conventional color science models in three ways:

1. The Simple World Assumption
2. The Isolation Assumption
3. The Geometric Assumption

To capture the possible variations from mark size, we first enumerated the different ways that mark size varies with values in a visualization (e.g., thickness, diameter, length, arc length, linearity, and area). Based on these enumerations, we identified four primary categories of marks that might affect color perceptions.

`为了捕捉标记大小的可能变化，我们首先列举了在可视化中标记大小随值变化的不同方式(例如，厚度、直径、长度、弧长、线性度和面积)。基于这些枚举，我们确定了可能影响颜色感知的四个主要标记类别。`

- Diagonally Symmetric Marks:高度和宽度相等的标记(例如，散点图中的点，热图中的细胞，地图上的气泡)。
- Elongated Marks:使用一个维度中的长度对数据进行编码的标记，但沿所有其他维度固定（例如，条形图中的条、圆环图中的圆弧）。
- Asymmetric Marks(不对称标记)：其长度根据其内部点的位置变化，但厚度固定的标记(例如，线图中的线，连通散点图中的弧线，平行线中的线)
- Area Marks:使用其总面积而不是标记的任何特定维度来传递信息的标记(例如，流图中的区域、饼中的楔形区域、平面图中的区域)。

## 4 GENERAL METHODS

Amazon’s Mechanical Turk

在这三个实验中，主要的依赖度量是辨别率(感知颜色差异的频率)，自变量是标记大小、颜色差异和测试轴s (L∗, a∗, and b∗).

### 4.1 Stimuli(刺激？)

我们将测试标记映射到两种不同的颜色：一种是目标颜色，另一种是由固定颜色从目标颜色调整而来的颜色。

just-noticeable difference (JND)
`最小可觉差`

### 4.2 Procedure

测试过程

### 4.3 Analysis & Modeling

根据每个轴上收集的判别率重新命名CIElab∆E，以考虑轴向的变化。

The model computes ∆Ep,s as follows:

1. Preprocessing:
2. Size × Axis Models:p = mx ∗∆x (1),where p is the proportion of detected color differences (p = 50% is a
typical JND), m is the regression line slope, and x is the current CIELAB axis.
我们还可以计算出在∆E中实现p%显著差异(ND(P)所需的色差如下：$ND_x(p,s)=\frac{p}{c_x+\frac{k_x}{s}}$
3. Size-Independent Models:$ND_x(p)=\frac{p}{m_x}$,where c and k are constants derived from a linear fit of slopes to inverse size.得到的模型对应于基于标记的几何性质的每个标记类型的最小可分辨色差的定量界。
4. Normalized Color Difference (∆Ep,s):$\Delta E_{p,s}=\sqrt{(\frac{\Delta L}{ND_L(p,s)})^2+(\frac{\Delta a}{ND_a(p,s)})^2+(\frac{\Delta b}{ND_b(p,s)})^2}$,对于给定的标记大小，∆E{P,s}=1.0的色差将被p%的观看者检测到。

![avatar](.\res\1559061722.jpg)

## 5 EXPERIMENT ONE: SCATTERPLOTS

## 9 CONCLUSION

本文对可视化中色差感知的影响因素进行了测量，并建立了数据驱动模型.这些模型集中于三种标记类型--点、柱和线--跨d建模。 不同的尺寸参数，以生成一组用于指导颜色编码设计和评估的概率度量。我们发现，我们的模型与以往的实际色差模型很好地吻合。 但是，细长的标记，通常用于视觉化，显著增加了对固定厚度模型的判读能力.我们把这些指标看作是在可视化中建立对颜色感知的定量理解的第一步，并对受控感知模式的适应性进行了更广泛的讨论。