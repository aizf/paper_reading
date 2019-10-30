# GraphScape A Model for Automated Reasoning about Visualization Similarity and Sequencing

ACM CHI是人机交互领域顶级国际学术会议

## ABSTRACT

GraphScape：可视化设计空间的有向图模型，支持可视化相似性和排序的自动推理。

Graph nodes represent grammar-based chart specifications
edges represent edits that transform one chart to another.

We contribute 
- (1) a method for deriving transition costs via a partial ordering of edit operations and the solution of a resulting linear program, and
- (2) a global weighting term that rewards consistency across transition subsequences.

最后，我们演示了GraphScapa在自动顺序可视化演示文稿中的应用，详细说明了可视化之间的转换路径，并推荐了设计方案。

## INTRODUCTION

为了充分理解数据的含义，可视化查看者不仅必须仔细检查单个图表，而且还要仔细检查它们之间的关系。

![avatar](.\res\1.png)

Hullman et al. 设想一个图形模型，其中可视化是节点，边缘表示图表之间的转换，而图形距离可以编码从一个图表到另一个图表转换的“成本”。

我们建立在这个概念的基础上，给出了一个**有向图结构**和**序列代价函数**，用于对图表之间的关系进行建模。

GraphScapa支持自动化的排序(automated sequencing)、**可视化之间路径的细化**(elaboration)以及可视化设计备选方案的推荐。

We offer four primary research contributions:

- directed graph model
- estimating transition costs
- sequence cost function，我们建立了一个序列成本函数来平衡成对过渡成本和全局序列分析
- we present results from two human-subjects experiments

我们演示了GraphScapa的应用：推荐序列，详细说明**转换路径**(elaborating transition paths)，并提出设计方案(例如，给定输入图表，找到可扩展到更大数据量的“最近”设计)。

## COMPARING CHART TRANSITION TYPES

### Step 1: Identifying Edit Operations

我们进一步将这些转换分组为标记类型(mark type)、数据转换(data transformation)和视觉编码转换(visual encoding transitions)的互斥(exclusive)类别。

![avatar](.\res\2.png)

### Step 2: Ranking Edit Operations

in terms of approximate interpretation difficulty (在给定源可视化的情况下解释目标可视化多困难).

Due to the large combinatorial space,为了减少空间，我们利用了关于过渡类别的**假设**：**标记类型转换 < 数据转换 < 可视化编码转换**。理由源于每种过渡类型的语义: ......

- **Mark Types.**
- **Data Transformations.** filter operations to be the most costly
- **Visual Encodings.** The color, shape, size, and text channels form a cluster exhibiting smaller distances among each other.**For all other encoding operations** are x, y > row, column > color > size > shape > text.Comparing **encoding operations**, the ranking Transpose > Move > Add, Remove > Replace.

### Step 3: Deriving(得到) Edit Operation Costs

线性规划解决一组所有编辑操作的成本估算。该解决方案还保留了加性距离，并允许不对称成本。

## 编辑操作排名的实证研究

## THE GRAPHSCAPE MODEL

- 有向图
- 过度成本 edge includes an **edit cost w(e)** , **transition cost T(u, v)** between visualizations u and v as the sum of edge weights along the shortest (lowest weight) path between them
- Filter Sequence Costs(This calculation is illustrated in Figure 4.), **F(S)**
- Global Weighting: Rewarding Consistent Subsequences(前面的工作和实验都发现，人们更喜欢按一致的顺序分组和排序的图表序列，即使这并不能完美地最小化编辑距离),**全局加权项W**
- The GraphScape Sequence Cost Function , **Cost(S)** ,图(c)


![avatar](.\res\3.png)
