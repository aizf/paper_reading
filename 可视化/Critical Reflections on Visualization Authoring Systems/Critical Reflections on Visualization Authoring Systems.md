#

我们的批判性反思(critical reflections)集中在三个互动系统的设计上，用于创作表达性的可视化，以达到交流的目的

based on widely used visualization terms(such as marks, scales, axes, and layout),but subtle(微妙的) differences exist in how each system defines these terms, or introduce new ones.

<https://vis-tools-reflections.github.io/>

- Unified Terminology(统一的术语)
- Summary of Main Components for the Three Systems

### 4.1 Marks

拖拽法只需要一个动作就能创建一个标记，从而增加了直接性，而系统将需要为标记提供合理的默认位置和大小。When such choice is not valid, the author may
see unexpected results.

### 4.2 Data Binding

core operation that involves:

(1) generating glyphs(字形,符号) based on data, and

(2) specifying a mapping between **data fields** and **mark properties** such as position, color, or size.

#### 4.2.1 What Data Does a Glyph Represent?

#### 4.2.2 Mapping Data Values to Visual Properties

dragging to resize, rotate, or move

warn

### 4.3 Scales, Axes, and Legends

Our systems all use three constructs to operationalize data bindings:

- (1)**scales**, functions that **map** the data domain to a range of visual values;
- (2) **axes**, visualizations of spatial scales; and,
- (3) **legends**, visualizations of scales of non-spatial properties such as color, shape, or size.

#### 4.3.1 Scale Visibility

When a data binding interaction is performed, all three systems automatically construct any necessary scale functions.

The level of visibility has clear implications for expressivity.

However, this expressivity comes with a non-trivial(非平凡的;重大有意义的;非没价值) complexity cost.

如何最好地解决这一复杂性，而又不失去表现力的收益，仍不清楚。

HCI(Human Computer Interaction,人机交互) theory

#### 4.3.2 Manipulating Axes & Legends

### 4.4 Layout

## 5 CRITICAL REFLECTIONS ON OUR SHARED ASSUMPTIONS

### 5.2 The Data: Cleaned & Pre-Processed

the data is static

相反，这些系统必须开发更高级别的脚手架，在必要时自动推断或建议适当的转换，类似于它们现有的数据绑定机制。

### 5.3 The Task: Authoring, not Designing

Another assumption people want to author a chart,not design one.

目前尚不清楚这些假设在实践中如何站得住脚。