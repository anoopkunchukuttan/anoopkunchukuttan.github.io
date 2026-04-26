## Pre-training corpora 

I have been recently poring over literature and documentation on pre-training corpora and understanding the landscape. The scenario for pre-training corpora is now very rich - a far cry from the early days when collections like [CCNet](https://arxiv.org/abs/1911.00359), [C4](https://huggingface.co/datasets/allenai/c4) and [OpenWebText](https://skylion007.github.io/OpenWebTextCorpus/) were released. This article is not an exhaustive survey of pre-training corpora, but highlights the major developments in pre-training corpora development and points to some representative corpora - with a bias towards the latest corpora. I will also discuss the corpora available in the public domain. 

**Large-scale, curated corpora**
The first and foremost feature is the colossal scale of the corpora - with corpora of the order of trillions of tokens. [FineWeb2](https://arxiv.org/abs/2506.20920) (3 trillion words) and [Essential Web](https://huggingface.co/datasets/EssentialAI/essential-web-v1.0) (24 trillion tokens) are the amongst the most prominent. EssentialWeb also provides detailed categories covering topic, web page type, content complexity, and quality. FineWeb2 is multilingual corpora covering 1000 languages. A lot of effort goes into ensuring high quality, diversity and safety of the corpora (see FineWeb2 paper) - all essential ingredients to build high-quality modern LLMs.  

Wikipedia is of course a great source of high quality content. and not pre-training dataset is complete with incorporating Wikipedia. [FineWiki](https://huggingface.co/datasets/HuggingFaceFW/finewiki) is a recent effort to create pre-training datasets from Wikipedia which works on HTML dumps and thus preserves formatting and structured content. 

**High Quality PDF Documents**
A lot of knowledge is locked up in PDFs and these are generally high-quality educational material from academic sources. [FinePDF](https://huggingface.co/datasets/HuggingFaceFW/finepdfs) and [Olmo3's PDF collection](https://huggingface.co/datasets/allenai/dolma3_pdf_mix-1025) are efforts to make PDF knowledge easily accessible.  The Olmo3 PDF corpus is more focussed on academic papers, while FinePDF is a more broad-based corpus extracted from CommonCrawl.

**Domain-specific corpora**
While training LLMs, there is more emphasis on some domain as opposed to others. Typically, coding and STEM are given more importance clearly since many downstream evaluations are targeting these domains. Hence, Math and coding datasets are also commonly included in pre-training corpora. For coding, [StackEDU](https://huggingface.co/datasets/HuggingFaceTB/stack-edu) - a filtered code dataset focussing on educational and well-documented code is a good source of pre-training code. For math content, [FineMath](https://huggingface.co/datasets/HuggingFaceTB/finemath) is a high quality corpus, with subsets defined by quality scores also publicly available. 

High-quality, information, easy to learn content is useful for pre-training. An example of such a dataset is [FineWebEDU](https://arxiv.org/abs/2406.17557), a subset of FineWeb that has been filtered for high-quality educational material (textbooks, tutorials, etc) and has been shown to be very effective for pre-training. 

**Pre-training data mix**
It is not just the dataset that is important, but the data mix as well. The proportion in which various topics are represented, the quality of the pages, etc. matters. Hence, a lot of effort goes into empirically determining the right mix of the above mentioned sources. [DCLM-pool](https://arxiv.org/abs/2406.11794) is a standardized pre-training dataset that be used for experiments to determine the right data mix. [DCLM-baseline](https://huggingface.co/datasets/mlfoundations/dclm-baseline-1.0) is one such mix provided as part of the DCLM dataset and can be used for pre-training. Similarly, the [Dolma3mix](https://huggingface.co/datasets/allenai/dolma3_mix-6T-1025) is the pre-training mix used in training the OlMo3 model. These pre-training datasets can be large, and if you are interested in small-scale experiments - then the [Codelion](https://huggingface.co/blog/codelion/optimal-dataset-mixing) collection of datasets which are subsets of DCML-baseline, FinePDF and FineWebEDU sampled via reservoir sampling.

**Mid-training corpora**
Mid-training is now a distinct stage in modern LLM training recipes. This stage follows pre-training and prepares the model for the finetuning stage by adapting the model on high quality data, focussing on certain data domains and styles that are important for downstream usecases. 

Synthetic content is useful in this stage to cover information rich, learning-friendly data. [Cosmopediav2](https://huggingface.co/blog/smollm#from-cosmopedia-v1-to-v2) is an example of such a synthetic dataset that has content that resembles textbooks, tutorials and structured content. 

High-quality content is also incorporated in mid-training - [FineWebEDU](https://arxiv.org/abs/2406.17557) and [FineWeb2-HQ](https://huggingface.co/datasets/HuggingFaceFW/fineweb-2) are examples of such datasets. While the former focusses on educational content, the latter focusses of high quality data from the general web. 

Mid-training also sets the stage for instruction tuning by incorporating datasets in pre-training that resemble QA, instruction-following and reasoning formats. Typically, these datasets are sourced from publicly available human curated and synthetic datasets for these tasks. Synthetic datasets are give the scale required during mid-training to make meaningful impact. 

**Mid-training Data Mix**
Again, the mix of datasets during mid-training matters. The [Dolma3-Dolmino-Mix](https://huggingface.co/datasets/allenai/dolma3_dolmino_mix-100B-1025) dataset provides a mixture for mid-training that was used for OlMO3. You can also look up the [SmolLM3](https://huggingface.co/blog/smollm3) and [Nemotron3](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Nano-Technical-Report.pdf) papers for descriptions of the mid-training mix. 

**Long training mix**
The final stage of pre-training is typically long-context extension. For this stage, long high-quality documents are used. Olmo3 uses academic PDFs along with synthetic data and a subset of the mid-training mix. This is available as part of the [LongMino Mix](https://huggingface.co/datasets/allenai/dolma3_longmino_mix-50B-1025). Other models like SmolLM3 and Nemotron 3 have their own selection of long-context documents. Typically, the documents are a mix of long context documents and the ones used in the previous stage.

_To summarize_:

- **General Corpora**: Essential Web, FineWeb2, FineWiki, FinePDF, DCLM-Pool
- **Domain-specific/Mid-training Corpora**: FineWebEDU, FineMath, Olmo3 PDF Collection, StackEDU
- **Pre-training (Mixture)**: DCLM-baseline, Dolma3mix, Codelion
- **Mid-training (Mixture)**: Dolma3-Dolmino-Mix, LongMino Mix

So, that is a short tour of pre-training corpora - mostly focussing on English. More on pre-training corpora for Indian languages soon...

|Stage|Corpus|
|--|--|
|General|Essential Web, FineWeb2, FineWiki, FinePDF, DCLM-Pool|
|Domain-specific/Mid-training|FineWebEDU, FineMath, Olmo3 PDF Collection, StackEDU|
|Pre-training (Mixture)|DCLM-baseline, Dolma3mix, Codelion|
|Mid-training (Mixture)|Dolma3-Dolmino-Mix, LongMino Mix|
