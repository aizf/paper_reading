# SetCoLa: High-Level Constraints(约束) for Graph Layout

## Abstract

为了促进定制(customized)和可概括(generalizable)约束布局的规范，我们贡献SetCola：a domain-specific language for specifying high-level constraints relative to properties of the backing data(支持数据，后台数据).

用户根据数据或图形(data or graph)属性识别节点集，并在每个集合中应用高级约束。

## Introduction

**SetCola** a JavaScript library

Users partition nodes into sets based on node or graph properties,
and apply layout constraints to these sets.

这种方法允许用户在高级别指定布局需求，将实例级约束的生成推迟到底层运行时系统。

<https://uwdata.github.io/setcola/>

## 2. Related Work

### 2.1. General Graph Layout

“tidy”, Radial layouts,Sugiyama-style layouts....D3.js,Gephi , Graphviz , and Cytoscape

### 2.2. Constraint-Based Layout Techniques

Dig-CoLa,IPSep-CoLa,....,WebCoLa

### 2.3. Domain-Specific Graph Visualization

## 3. Design of SetCoLa

To provide a reusable(可重用的) specification(规范),SetCoLa将约束应用于由共享属性定义的节点组

The SetCoLa compiler generates one or more WebCoLa constraints for each SetCoLa constraint and produces a specification for WebCoLa

### 3.1. Specifying Sets in SetCoLa

- Partitioning Nodes into Sets
- Specifying Sets with Predicates(谓词)
- Collecting Nodes Using Keys
- 组合之前定义的集合