---
title: Tokenization的三种方式
date: 2021-11-17 20:22:08
tags:
- NLP
- Tokenization
- Subword
categories:
- NLP
---
## Tokenization

在NLP中，Tokenization是非常重要的步骤之一。

相对简单的Tokenization是将短语、句子、段落、一个或多个文本文档拆分为较小单元的过程。 这些较小的单元中的每一个都称为Token。这些标记可以是任何东西：一个单词，一个子单词，甚至一个字符。不同的算法在执行Tokenization时遵循不同的过程，以下为这三者之间差异的基本概念。

<!-- more -->

原始文本：

`“Let us learn tokenization.”`

word-based tokenization：

`[“Let”, “us”, “learn”, “tokenization.”]`

subword-based tokenization：

`[“Let”, “us”, “learn”, “token”, “ization.”]`

character-based tokenization：

`[“L”, “e”, “t”, “u”, “s”, “l”, “e”, “a”, “r”, “n”, “t”, “o”, “k”, “e”, “n”, “i”, “z”, “a”, “t”, “i”, “o”, “n”, “.”]`

目前，所有NLP模型都在token级别处理原始文本。这些标记用于形成词汇表，词汇表是语料库（NLP中的数据集）中的唯一标记。然后将这些词汇表转换为数字（ID）并帮助我们建模。 

### Word-based tokenization

基于Word的tokenization将一段文本拆分为基于分隔符的单词。 英文中最常用的分隔符是空格。 也可以使用多个分隔符来拆分文本，如标点符号等。 根据您使用的分隔符，您将获得不同的token。

Example:

`“Is it weird I don’t like coffee?”`

`[“Is”, “it”, “weird”, “I”, “don’t”, “like”, “coffee?”]`

此时`“don’t”`和`“coffee？”`都带有标点符号，如果在我们的语料库中有另一个像这样的原始文本（句子）：`“I love coffee.”`，将会构建一个新的token`“coffee.”`。可能会引导模型学习`“coffee”`这个词的不同表示（`“coffee？”`和`“coffee.”`），并使字的表示不理想。

更进的方式是将标点符号也作为一个token。

`[“Is”, “it”, “wierd”, “I”, “don”, “’”, “t”, “like”, “coffee”, “?”]`

此时会发现`“don’t”`被拆分为`“don”`，`“'”`，`“t”`，但是模型想要学习到的应该是`“do”`,`“n't”`。此时就需要使用一些 `trick `将`“do”`,`“n't”`保留下来。

#### 优点

每个单词都用一个ID表示，每个ID包含大量信息，因为句子中的一个单词通常包含大量上下文和语义信息。

#### 缺点

1. 输入、输入层维度过大

这种方式的标记化会需要大量语料库，从而产生大量词汇。 Transformer XL使用空格和标点符号标记，词汇量为267735。太大了！这个庞大的词汇表导致输入层和输出层都有一个巨大的嵌入矩阵，从而导致模型更重，需要更多的计算资源。

为了解决这个巨大的词汇问题，可以限制添加到词汇表中的单词数量。例如，只能保存我们词汇表中最常见的5000个单词（基于语料库中单词的出现频率）。然后，该模型将为这5000个常用单词创建ID，并将其余单词标记为OOV（词汇表外）。但这会导致信息丢失，因为模型无法了解OOV单词的任何信息。这对模型来说是一个很大的折损，因为它将为所有未知单词学习相同的OOV表示。🙄

2. 无法学习到相似的词

这种标记化还为`“boy”`和`“boys”`等词提供了不同的ID，它们在英语中几乎是相似的词（一个是单数，另一个是复数）。实际上，我们想让我们的模型知道这样的词是相似的。

3. 拼写错误的单词被标记为OOV

如果语料库将“knowledge”拼错为“knowledge”，模型将为后面的单词分配OOV标记。

4. 稀疏问题

某些出现频率低的词得不到充分训练

因此，为了解决所有这些问题，提出了基于字符的标记化。

### Character-based tokenization

基于字符的Tokenization将原始文本拆分为单个字符。这种标记化背后的逻辑是，一种语言有许多不同的单词，但有固定数量的字符。这导致了非常小的词汇量。

例如，在英语中，使用256个不同的字符（字母、数字、特殊字符），而它的词汇表中有近170000个单词。因此，与基于单词的Tokenization相比，基于字符的Tokenization将使用更少的标记。

#### 优点

1. 没有或者很少OOV词

基于字符的标记化的一个主要优点是没有或很少有未知或OOV单词。因此，它可以使用每个字符的表示创建未知单词的表示（训练期间未看到的单词）。

2. 拼写错误的单词不会被标记为OOV

拼写错误的单词可以正确拼写，而不是将它们标记为OOV标记并丢失信息。

#### 缺点

1. 非常简单，可以大大降低内存和时间复杂性。
2. 在英语和类似的语言中，字符通常不像单词那样具有任何意义或信息。（但是在中文中应该字符就具有特殊的意义和信息，所以在中文的模型通常是基于字符的Tokenization，例如，BERT等模型）
3. 序列长度过长。在基于字符的Tokenization中，减少词汇表大小与序列长度之间存在权衡。每个单词被分割成每个字符，因此，Tokenization的序列比初始原始文本长得多。例如，单词“knowledge”将有9个不同的标记。

### Subword-based tokenization

基于子词的Tokenization，它是一种介于基于词和基于字符的标记化之间的解决方案。其主要思想是解决基于单词的Tokenization（非常大的词汇量、大量的OOV标记以及非常相似的单词的不同含义）和基于字符的Tokenization（非常长的序列和意义较小的单个标记）所面临的问题。基于子字的Tokenization算法使用以下原则。

1. 不要将经常使用的单词分成更小的子单词。
2. 将稀有词拆分为较小的有意义的子词。

例如，`“boy”`不应拆分，但`“boys”`应拆分为`“boy”`和`“s”`。这将有助于模型了解`“boys”`一词是由`“boy”`一词构成的，意思稍有不同，但词根相同。将单词“tokenization”分为“token”和“ization”，其中“token”是根单词，“ization”是第二个子单词，标记为根单词的附加信息。子词拆分将有助于模型了解与“token”、“tokens”、“tokens”和“tokenizing”等具有相同词根的词在意义上是相似的。它还将帮助模型了解`“Tokenization”`和`“modernization”`由不同的词根组成，但具有相同的后缀`“ization”`，并且在相同的句法情况下使用。另一个例子是`“surprisingly”`一词。基于子词的Tokenization将其分为`“surprising”`和`“ly”`，因为这些独立子词将更频繁地出现。基于子字的Tokenization算法通常使用一个特殊符号来指示哪个字是token的开始，哪个字是token开始的结束。例如，`“tokenization”`可以分为`“token”`和`“##ization”`，表示`“token”`是单词的开头，`“##ization”`是单词的结尾。

不同的NLP模型使用不同的特殊符号来表示子词。`“##”`由BERT模型用于第二个子词。值得注意的是，特殊符号也可以添加到单词的开头的。在英语中SOTA的大多数模型都使用某种子词Tokenization算法。一些常见的基于子词的Tokenization算法有BERT和DistilBERT使用的WordPiece、XLNet和ALBERT使用的Unigram以及GPT-2和RoBERTa使用的BPE。 基于子词的Tokenization允许模型具有适当的词汇量，并且能够学习有意义的上下文无关表示。模型甚至可以处理OOV词，因为可能分成已知子词。

更多关于Subword-based tokenizaion文章：{% post_link NLP/subword算法:BPE、WordPiece与Unigram %}

