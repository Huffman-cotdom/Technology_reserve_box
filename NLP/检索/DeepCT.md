# DeepCT算法

从BM25算法可知，常用的文档表示方法一般都是为IDF，但是IDF不能考虑到每个词的上下文语义，[DeepCT](https://github.com/AdeDZY/DeepCT)改善了这个问题。

DeepCT全称Deep Contexualized Term Weighting framework，深层语境化术语权重框架

## Introduction

搜索引擎一般都分为第一阶段粗排和第二阶段精排，第一阶段有三种方式：bool模型、概率模型和向量空间模型，然后从一个倒置的索引中获取信息。

第一阶段排序算法的一个关键点是如何量化每个查询或者文档关键词的贡献，大多数检索算法都是基于频率（如：tf，qtf）来确定一个词在当前文档下的重要性，以及逆文档概率（如：idf）来确定在所有文档中的重要性。

![](DeepCT/%E6%88%AA%E5%B1%8F2021-09-16%20%E4%B8%8B%E5%8D%8810.02.23.png)

词频并不一定能够表明某个词语是否重要或者说更加贴近文本的含义。如果搜索“stomach”，基于词频的检索模型的话认为是相似的，因为两次查询都提到了关键词“stomach”，但是实际上第二段话是偏离主题的。

要确定哪些词是中心词，需要更深入的理解，考虑一个词的含义、整个文本的含义已经改词在整个文本中的作用。

Bert可以捕捉一个词的语义和语法特征，不仅如此，还可以使相同的词在不同语境中具有的变化。

论文中提出DeepCT，通过Bert模型表征不同上下文词语提升第一阶段检索模型结果。由于一个词语的表征取决于它的具体语境，因此对同一词语的估计重要性也会随着语境的不用而变化、

DeepCt的一个用途是识别重要的段落术语，以便于段落的索引。段落通常具有平坦的术语权重分布，使得基于术语频率的检索效率较低，DeepCT-index可以离线对长篇文章中的术语进行加权和索引，经过训练的模型将应用于集合中的每个段落。这个建立索引的过程在离线过程中完成。基于上下文的段落关键词权重被缩放为类似于tf的整数，并被存储在一个普通的第一阶段的倒排索引中。

**另一个用途是识别长query中的关键词，对于涉及许多术语和概念的长query，重要的是确定哪些是最核心的** 。通过相关的query-document对来训练DeepCT，通过被相关文档提及的可能性来对query的关键词进行加权。预测结果被用来生成加权query，可用于广泛使用的检索模型，如BM25算法。

## Related wrok

对于查询术语加权，一个研究方向是基于特征的方法。需要针对一个文档集合运行query以生成特征。 与基于概率的查询术语加权相比，这些方法提高了搜索准确性，但是使用假相关的反馈会导致额外的计算成本。为了从文本内容中预测query关键词的权重，Zheng和Callan提出了一种基于单词嵌入的方法，称为DeepTR。DeepTR为每个查询词构建一个特征向量。使用关键词的word2vec嵌入和平均query embedding之间的差异为每个查询词构建一个特征向量。然后学习一个回归模型，将该特征向量映射关键词的真实权重上。预估的权重被用来生成可在第一阶段检索的词袋查询。

在早期的第一阶段基于神经网络的算法中，大多都是使用连续的表示方式，是query在某种程度上与每个文档匹配。但这肯定不切实际。最近的两种方式解决了这一效率问题，都是使用潜在表征。

一种是学习query和文档的底维密集嵌入，支持使用嵌入空间中的近邻搜索进行快速检索，但是存在一个效率与准确性的权衡。第二种方式是学习高维但是稀疏的潜在表征，其中query和文档由一组‘latent words’ 表示。稀疏的‘latent words’ 允许以倒置索引的方式进行查询，这种方法效率比较高，而且还引入了所有受控词汇表中发现的特异性与穷举权衡。

最近，Nogueira等人[23]提出了Doc2Query，它使用了神经模型来修改基于单词的离散文档表示。它使用神经机器翻译从文档中生成潜在的查询，并将这些查询作为文档索引扩展术语。我们不知道其他使用基于离散词的文本表征和大型词汇表的第一阶段神经模型词汇表，而这些词汇表是现代搜索引擎的基础。

## DeepCT Framework

本节介绍了DeepCT，以及它如何用于权衡query关键词（DeepCT - Query）和索引文档（DeepCT - Index）。

DeepCT包含两个主要部分：通过Bert生成上下文关联的词嵌入；通过线性回归预测关键词权重

### Contextualized word embedding generation

为了估计一个词在特定文本中的重要性，最关键的问题是生成描述一个词与文本上下文关系的特征，DeepCT利用Bert来提取一个词的上下文特征

#### 3.1 Map to target weights

语境化word embedding是一个特征向量，用于描述该词在特定语境中的句法和语义作用。DeepCT将这些特征线性地组合成词的重要性得分。

$$
\hat{y}_{t,c}=\vec{w}T_{t,c}+b \tag{1}
$$


这里的$T_{t,c}$指token t在文本c中的上下文embedding，w和b是线性组合权重和偏差。

DeepCT以每个字符的回归任务训练。给定文本c中每个词的基础真实术语权重，表示为${y_1,c , . . . ,y_N,c }$，DeepCT的目标是最小化预测权重$ \hat{y} $与目标权重$y$之间的均方误差

$$
loss_{MSE}=\sum_c\sum_t(y_t,c-\hat{t},c)^2\tag2
$$


预测词权重$y^t,c$可能的范围为$(-\infty, \infty)$，但是实际上大多就在$[0,1]$范围内，如3.3节所示，真实权重为$[0,1]$，query/document 加权方法接受任何非负权重；负权重的关键词被丢弃。

Bert对于未见过的词会生成subword，例如，"DeepCT "被标记为 "deep "和 "##ct"）。使用第一个子词的权重作为整个单词的权重。在计算MSE损失时，其他子词被屏蔽掉了。

DeepCT模型从Bert到回归层都是端到端的优化。Bert组件用预训练的Bert模型进行初始化，以减少过拟合。对Bert进行微调，以使得语境化的word embedding与关键词预测任务一致，最后一个回归层是从头开始学习的。

DeepCT是一个通用的框架，可以学习与语境有关的关键词权重，DeepCT能够学习到不同关键词的重要性，取决于真实关键词如何被定义。根据任务的不同，预测的术语权重也可以使用不同的方法。下面介绍使用DeepCT框架改进第一阶段检索的两种方法。

#### 3.2 Index Passage with DeepCT

DeepCT的一个新用途是识别对一段话或一篇文章的关键词，已实现高效和有效的检索段落和短文本。

DeepCT-Index使用DeepCT获取段落关键词的权重并将其存储在一个典型的倒置索引中。

Target Term Weights for Training DeepCT适当的目标关键词权重应该反映出一个关键词对于文章是否重要，将查询关键词的召回率作为真实文章中关键词是否重要的估计。

$$
QTR(t,d)=\frac{Q_{d,t}}{Q_d}\tag{3}
 
$$


$Q_d$是与passage=d有相关性的query的集合。$Q_{d,t}$是Q_d包含关键词t的子集，$QTR(t,d)$是t在q中的query关键词召回权重。QTR范围是$[0,1]$。query关键词召回基于这样一个假设：搜索queries可以反映文档的关键思想。出现在相关查询中的单词比文档中的其他单词更重要。

训练需要相关联的query-passage pairs。模型采集一段文字的内容进行预测，并使用相关query生成的目标权重计算损失。在推理过程中，该模型只需要该段落。

**Index with predicted term weights** .一旦DeepCT学习到模型参数，它就可以对任何passage进行估计，而且无需query。这就使得在能够离线计算关键词的权重并存储。索引能够被线上的设备高效地搜索。

将训练好的DeepCT模型应用于所有的passage的集合。预测的权重从整数缩放到**[0,1]** ，可以被现存的检索模型调用，这种权重称为TF_{DeepCT}，用以表现关键词t在passage d中的重要性的另外一种方式。

$$
TF_{DeepCT}(t,d)=round(\hat{y}_{t,d}*N)\tag{4}
$$


这里的$\hat{y}_{t,d}$是passage d中预测关键词t的权重。N将预测权重缩放为整数范围。论文中使用N=100。$TF_{DeepCT}$被用来替换原始倒排索引中的TF。关键词t的计算方式从$[docid(d), TF(t,d)]$变为$[docid(d), TF_{DeepCT}(t,d)]$。$TF_{DeepCT}$可以通过主流的词包检索模型，如BM25或者 query likelihood model (QL)进行搜索。基于上下文的关键词权重$TF_{DeepCT}$将会使检索模型偏向于检索passage的中心词。以防止偏离主题的passage的被检索出来。

**Efficiency** 

DeepCT-Index和传统的倒排的区别是关键词的权重从TF替换为$TF_{DeepCT}$，因此查询的延迟并不会变长。**但是公式4有一个副作用，一些关键词的** **TF_{DeepCT}** **变成0，这可以被视为一种索引修剪的形式。** 

#### 3.3 Query Term Weighting with DeepCT

DeepCT在IR任务中的另一个直接的用途是在长query对查询关键词进行加权。对于提及很多关键词和概念的长query，确定哪些是很重要的。“Find locations of volcanic activity which occurred within the present day boundaries of the U.S and its territories”中理想的情况下“volcanic activity”是关键概念，并且“boundaries of the U.S”可能就不是那么重要。Zheng和Callan提出了一个基于word2vec的的查询关键词重新加权框架，称为DeepTR，它能有效地对bag-of-words查询进行重新加权。论文中使用DeepCT取代基于Word2Vec的模型，称之为DeepCT-Query。

Target TermWeights for Training DeepCT

受到Zheng and Callan的启发，DeepCT-Query使用关键词召回：

$$
TR(t,q)=\frac{D_{q,t}}{D_q}\tag{5}
$$


D_q是与query相关的documents的集合。D_{q,t}包含关键词t的documents的子集，TR(t,q)是关键词t在query q中的召回权重。关键词召回率是在[0,1]范围之间。关键词召回是基于假设：一个query关键词如果被更多的文档提及便更重要。

训练需要相关的query-document pairs。 模型获取query的文本内容，进行预测，并使用从相关文档生成的target权重计算损失。在推理过程中，模型只需要query。

**Re-weight queries with predicted term weights.** 

当一个query被接受（online），经过训练的模型预测每个关键词的重要性。根据DeepTR，使用预估的query关键词权重来生成bag-of-words queries(BOW)和 sequential dependency model queries(SDM)。例如：在原始BOW query“apple pie”被重新表述 #wight (0.8 apple 0.7 pie)。Sequential dependency model增加了在一个窗口内bigrams和 词共现（word co-occurrences）到query。论文中使用了重新加权（re-weighted）的BOW query来取代SDM query中的bags-of-words部分。非正的权重将会被抛弃，就效率而言，为了一个新的query预测关键词权重只是简单的通过DeepCT的前向传播（feed-forward）。使用Bow-DeepCt-Query 和SDM-DeepCt-Query来表示重新加权的bag-of-words和sequ dependency queries。

## Experimential Methodology For DeepC-Index

本节介绍第二项任务的实验方法—passage term(关键词)权重和索引。

**Datasets** 

两个主要由段落组成的数据集 MS MARCO和TREC-CAR。

MS MARCO是一个question-to-passage的检索数据集，其中包括8.8M的段落。平均段落长度约为55字。训练集包含了大约0.5万对查询和相关段落。训练集包含大约50w对query和相关段落。平均每个query有一个相关段落。开发（dev）集包含6980个查询和它们的相关标签。测试集包含6,900个查询，但相关标签被微软隐藏了

TREC-CAR由2970万个英语维基百科段落组成，平均长度为61个单词。query和相关段落是综合生成的。一个query是一个维基百科文章的标题和其中一个章节的标题的串联。论文中使用了自动相关性判断，将章节内的段落视为query相关的段落。训练集和验证集分别有330万个query-passage pairs和80万个query-passage paris。

**Baselines** 

传统的BM25算法

将TextRank的关键词权重范围(0,1)按照公式4扩展到整数，以便索引。

Doc2Query是一个有监督的神经网络的baseline。它训练了一个sequence-to-sequence模型，以便从段落中产生潜在的query。将查询索引为文档扩展项。Doc2Query隐式地重新加权关键词，因为重要的段落关键词可能会出现在生成的查询中。

三种实验索引方法包括所提出的DeepCT-Index和使用不同embedding的两个变体。

DeepCT_W-Index将DeepCT中的Bert组件替换为语境无关的embedding。为了给每个词提供上下文，使用average word embeddings对文章进行建模，并从每个单词的embedding中减去段落嵌入量，其灵感来自Zheng和Callan。embedding由Word2Vec初始化，并在训练期间进行微调。

DeepCT_E-Index将DeepCT中的Bert组件替换为Elmo。

**Indexing, Retrieval, and Evaluation** 

第一阶段排名由两种主流检索模型进行。BM25和query likelihood with Jelinek-Mercer smoothing (QL)。使用Anserini工具实现。微调了BM25的参数k_1和b以及通过对训练集中的500个query进行参数扫描，得到QL平滑因子λ。Re-ranking有两个：Conv-KNRM和BERT Re-ranker。

ranking/Re-ranking的结果是通过10个段落的平均相互排名(Mean Reciprocal Rank)进行评估的。这是MS MARCO的官方评价指标。 对于TREC-CAR，按照以前工作中使用的评价方法，计算了深度为1000的MAP。

**DeepCT Setting** 

DeepCT-index的Bert部分使用预训练参数初始化。对于MS MARCO，使用了官方预训练的BERT。TREC-CAR不能使用官方模型，因为它的测试文档与BERT的预训练文档重叠了。使用了Nogueira和Cho的BERT模型，其中重叠的文档被从预训练数据中删除。DeepCT在数据集的训练分割上训练了3个小时，使用了学习率为2e-5和最大输入文本长度为128个符号。

## DeepCT-Index Results

接下来的两个子部分描述了使用DeepCT索引索引第一阶段搜索精度的实验，以及为什么DeepCT索引关键词权重有效。

### Retrieval Accuracy of DeepCT-Index

本节研究了DeepCT-Index是否比baseline关键词加权方法提高了第一阶段的检索准确率。然后与其他方法进行比较，最后，研究了使用DeepCT-Index的第一阶段对多阶段检索系统的端到端准确性的影响。

**DeepCT-Index Retrieval Performance** 

![](DeepCT/%E6%88%AA%E5%B1%8F2021-09-18%20%E4%B8%8B%E5%8D%886.57.26.png)

使用了6种方法对BM25和QL进行第一阶段检索的准确率。

DeepCT_W索引和DeepCT_E索引的结果证明了上下文的重要性。非上下文word2vec嵌入产生的术语权重不如tf有效。ELMo产生了更有效的术语权重，但BERT对上下文的更强使用产生了最有效的权重。这些结果也显示了DeepCT框架的通用性。

**First-stage search with DeepCT-Index vs re-ranking** 

![](DeepCT/%E6%88%AA%E5%B1%8F2021-09-22%20%E4%B8%8A%E5%8D%8811.13.54.png)

第一阶段：DeepCT-Index BM25的表现超过了官方标准BM25和Doc2Query BM25 。Re-Ranker是Re-ranking最好的模型。

DeepCT-Index BM25比其他几个Re-ranking方法要好，比基于特征的学习排名方法更准确。

DeepCT-Index BM25没有Bert Re-ranking和Conv-KNRM这两个Re-ranking算法要差。

**DeepCT-Index as the first-stage of re-ranking systems** 

![](DeepCT/%E6%88%AA%E5%B1%8F2021-09-22%20%E4%B8%8A%E5%8D%8811.14.12.png)

下一个实验检验了由DeepCT-Index BM25产生的第一阶段排名是否能改善后期的Re-ranking。Bert Re-Ranking有最高的准确率。测试了各种Re-Ranking的深度。在较浅的深度重新排序效率较高，但可能会遗漏更多相关段落。

召回率显示了相关段落在重排段落集中的百分比。DeepCT-Index在所有深度都有较高的召回率。

基于深度神经的Re-Ranking的高计算成本是在在线服务中采用它们的最大担忧之一。Nogueira等人的论文中指出，增加一个BERT Re-Ranker，其重排深度为1000，即使使用GPU或TPU，也会给BM25第一阶段的排名带来10倍的延迟。DeepCT-Index将重新排名的深度降低了5倍到10倍，使基于深度神经的Re-Ranker在延迟/资源敏感的系统中变得实用。

**Summary** 

之前有很多关于passage关键词 加权的研究，但不清楚如何在特定的passage中有效地模拟一个词的语法和语义。我们的研究结果表明，一个深度的、上下文的神经语言模型能够捕捉到一些所需的属性，并且可以用来为段落索引生成有效的术语权重。在DeepCT-Index上进行的BM25检索可以比经典的基于tf的索引准确25%，并且比一些广泛使用的多阶段检索系统更准确。第一阶段排名的改进进一步有利于下游重新排名的效果和效率。

### Understanding Sources of Effectiveness

本节旨在通过几个分析来了解DeepCT-Index的有效性来源。

每个case都有一个查询，一个相关的段落，以及一个提到查询概念但实际上是离题的非相关段落。颜色深度可视化了DeepCT-Index中的关键词权重。权重由段落中所有关键词的权重之和归一，以反映段落中的相对术语重要性。

**Emphasize central terms and suppress non-central terms** 

![](DeepCT/%E6%88%AA%E5%B1%8F2021-09-22%20%E4%B8%8A%E5%8D%8811.28.01.png)

DeepCT能够识别对文本主题具有核心意义的关键词。在第一个查询中，两个段落都提到了 "susan boyle"。在相关的段落中，DeepCT-Index认识到主题是 "susan boyle"，并把几乎所有的权重放在这两个词上。偏离主题的段落是关于 "troll "的定义，而 "susan boyle "被用于一个例子中。DeepCT-Index成功地识别了中心概念 "troll"，并抑制了其他非主题关键词；"susan boyle "所占的权重不到10%。

在新的权重下，查询和非主题段落之间的BM25得分大大降低。

DeepCT-Index和tf指数的术语权重分布。它绘制了每个段落的最高权重词的平均权重，第二高权重词的平均权重，以此类推。原始的tf分布是平坦的。DeepCT-Index将高权重分配给几个中心词，导致了倾斜的词权分布。这种倾斜的分布证实了我们在案例研究中的观察，即DeepCT-Index积极地强调少数中心词，而压制其他的词。

![](DeepCT/%E6%88%AA%E5%B1%8F2021-09-22%20%E4%B8%8A%E5%8D%8811.33.30.png)

DeepCT对中心词的强烈偏爱解释了它的有效性：促进主题词，压制非主题词。这也是一个错误的来源。在许多失败的案例中，DeepCT-Index正确地识别了段落的中心词，但查询的答案却在段落的非中心部分提到。DeepCT-Index降低了这些部分的权重，甚至忽略了这些部分，导致相关段落的排名降低。值得探讨的是如何减少丢失有用但非中心信息的风险。

**Context-based weights vs. frequency-based weights** 

DeepCT-Index产生的关键词权重是基于上下文的意义而不是频率。一个关键词即使经常出现，也可能得到较低的权重（例如，在最后一个 "Genomics"passage中，"DNA "被认为是不重要的，尽管它被提到了3次）。即使tf相同，同一个词在不同段落中得到的权重也大不相同。这种独立于频率信号的程度在以前的术语加权方法中是不常见的；即使是语义文本表示法，如Word2Vec和Glove，也被报道与关键词频率有很高的相关性

## EXPERIMENTAL METHODOLOGY AND RESULTS FOR DeepCT-Query

**Datasets** 

使用了Robust04和Gov2 TREC集合。Robust04是一个新闻语料库，有0.5万个文档和249个测试主题。Gov2是一个有2500万个网页和150个测试主题的网络集合。每个测试主题都有3种类型的查询：短标题查询、长句子查询描述和长句子查询叙述。

**Baselines** 

用6个基线做了实验，这些基线使用两种形式的查询结构（BOW, SDM）和三种类型的术语权重（tf, DeepTR, Oracle）。BOW和SDM代表bag-of-word queries和 sequential dependency queries。tf是经典的query 关键词 频率加权。DeepTR是之前最先进的query加权方法。它使用单词自身的嵌入和查询的平均嵌入之间的差异来提取单词特征。这些特征被线性组合以产生术语权重。DeepTR根据术语召回率进行监督训练（公式3）。Oracle通过真实关键词召回权重对查询术语进行加权；它反映了DeepTR和DeepCT-Query在做出完美预测的情况下能达到多少，估计出一个上限

**Indexing, Retrieval and Evaluation** 

使用Indri搜索引擎并进行标准的词干和停顿词过滤，用5倍的交叉验证来训练和评估DeepCT-Query和DeepTR， query likelihood（QL）模型的性能比BM25略好，所以使用QL来搜索索引，检索结果用标准的TREC指标进行评估：NDCG@20和MAP@1000。

**DeepCT Settings** 

DeepCT的BERT部分是用官方预训练的BERT。DeepCT，包括BERT层和最后的回归层，都进行了端到端的微调。该模型被训练了10个 epochs。使用了2e -5的学习率。查询标题（ query titles）、描述（descriptions）和叙述（narratives）的最大输入文本长度被设定为30、50和100。

**Results** 

短的标题查询并没有从术语加权的方法中获益。标题查询通常由几个关键词组成，这些关键词都是必不可少的，所以重新加权就不那么重要了。此外，DeepCT也没有太多的上下文可以利用来估计术语的重要性。关于查询的外部信息，如伪相关反馈pseudo-relevance feedback ，可能是理解短查询所必需的。

描述性和叙述性query提到了许多术语和概念；在检索过程中，确定哪些是核心内容是很重要的。加权的查询比未加权的查询更有效。DeepCT-Query在大多数情况下比DeepTR更准确。DeepCT-Query与DeepTR的不同之处在于它们如何在上下文方面代表一个术语。结果表明，DeepCT-Query能更好地反映一个词在查询中的作用。与描述性查询相比，在叙述性查询上观察到更大的改进。结果表明，对于短句子，简单的上下文建模可能是有效的。但对于更复杂的查询，像BERT这样的深度语言建模组件可以导致搜索结果的改善。

## Conclusion

DeepCT的一个用途是DeepCT-Index，它给passage 关键词 加权。DeepCT产生的整数关键词权重可以存储在一个典型的倒置索引中，并与流行的第一阶段检索模型（如BM25和QL）兼容。DeepCT的另一个用途是DeepCT-Query，它对查询术语进行加权。实验结果表明，DeepCT-Query极大地提高了较长查询的准确性，这是因为它能够在复杂的背景下识别中心查询词。

分析显示了DeepCT相对于经典关键词加权方法的主要优势。DeepCT可以找到文本中最核心的词汇，即使它们只被提及一次。非中心词，即使在文本中经常被提及，也会被压制。这种行为在以前的术语加权方法中是不常见的。DeepCT是一个从 "frequencies "到 "meanings "的步骤。



