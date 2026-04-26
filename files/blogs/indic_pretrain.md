
#  The Evolving Landscape of Indic Language Pre-training Corpora

While there is a large amount of high-quality and diverse pre-training corpora for English, the situation is much more challenging for Indian languages. This post summarizes the current state of Indic corpora in the public domain and highlights the gaps we must bridge to improve Indic LLMs.

---

## From Sentences to Documents
In the pre-LLM era, data efforts like **IndicCorp v1 & v2** focused on sentence-level collections curated for efficiently training small models like IndicBert and IndicBart. However, training effective decoder LLM models requires long-range context.

* **Early Explorations:** **Vaarta** was an early pioneer in document-level Indic data, though it remained relatively unused.
* **The Modern Standard:** Current efforts prioritize document integrity, which is essential for learning reasoning, coherence, and complex syntax across long sequences.

## Major Indic Web Corpora

The web is a major source of corpora for Indic languages, and accounts for a major portion of pre-training corpora available for Indian languages. I will mention a few notable attempts at curation of Indian languages corpora. 

### Sangraha (AI4Bharat)
The **Sangraha** corpus represents one of the most comprehensive open-source efforts for 22 Indian languages to date. There are two major subsets:

* **Sangraha-Verified (64B Tokens):** High-fidelity data from curated sources including the web, Wikipedia, Internet Archive (OCR), and YouTube transcripts. Notably, its English subset focuses on **Indian English**, capturing regional nuances and local topics.
* **Sangraha-Unverified (24B Tokens):** A broader, more diverse collection derived from filtered versions of **CulturaX**.

### MILA (Multilingual Indic Language Archive)
The **MILA** project is a significant new effort for Indic data. By processing CommonCrawl specifically for Indic languages, it has generated a massive **410B token corpus**. 
* **Quality Filtering:** MILA represents one of the first major attempts to apply sophisticated quality filtering and deduplication at this scale for Indian languages.
* **Public Access:** While currently under review, the project has committed to releasing these datasets into the public domain.

### Multilingual Global Collections
Researchers also extract Indic subsets from massive global crawls. Some of the most prominent recent collections include:
* **FineWeb-2:** Hugging Face’s latest high-quality web crawl.
* **CulturaX & HPLT 3.0:** Massive-scale, deduplicated, and cleaned multilingual repositories. Notably, HPLT 3.0 also processes Internet Archive.

Each of these corpora is the result of rigorous, multi-stage processing pipelines—incorporating deduplication, toxicity filtering, and heuristic-based cleaning—to ensure they are "pre-training ready." However, a significant gap remains: most existing datasets lack granular domain classification and quality labels, metadata that is increasingly critical for targeted mid-training and curriculum learning. The MILA project represents an important step forward in this regard, introducing a more systematic approach to quality scoring and filtering for Indic languages.

## English data in Indian context

Beyond its native languages, English is also heavily used in India. Indian English is not merely a subset of global English; it possesses distinct structural nuances and a vast volume of locally generated content. While  Indian language datasets often lack topical coverage on the web, English-language content from India provides a wealth of regional context.

To bridge this gap, modern efforts like Sangraha-Verified and Vaarta specifically crawl English sources within India to capture these linguistic peculiarities. Similarly, the MILA project curates content from Wikimedia properties focused on Indian topics, where English serves as a primary vehicle for regional knowledge. By upsampling this Indian English data, model trainers can ensure that pre-training corpora are not only linguistically accurate but also culturally grounded.

## Wikimedia 

Wikimedia projects remain a major source for open, high-quality multilingual Indic language data. While Wikipedia represents a very small volume compared to web crawls, its density of factual information and quality make it an important source. FineWiki provides a processed version of Wikipedia by preserving document formatting in clean Markdown—a format increasingly preferred for maintaining structural integrity during training. The MILA project has expanded the scope beyond just Wikipedia, aggregating content from the broader ecosystem of Wikimedia properties to further diversify its Indic language archive.

## Unlocking "Locked" Data
Significant portions of Indian linguistic heritage are "locked" in PDF documents rather than native HTML. 

* **OCR Pipelines:** While projects like **FinePDF** extract text without OCR, **Sangraha** and **MILA** have utilized advanced OCR to digitize literary and official content from the **Internet Archive**.
* **Government & Legal:** The **Pralekha** corpus curates documents from the **Press Information Bureau (PIB)**. This provides high-quality official information and document-level parallel corpora, which are vital for cross-lingual transfer.
* **Education:** While English has **FineWeb-Edu**, Indic languages lack a direct HTML equivalent. However, **MILA** has curated data from the **National Digital Library of India (NDLI)** and various school boards, unlocking rich, textbook-quality material.

## Synthetic Data
When raw native data is limited, synthetic pipelines provide a bridge to high-quality knowledge.

### Translated Data

* **Wikipedia:** **Sangraha** translated the entirety of English Wikipedia into 14 languages using **IndicTrans2**, providing 90B tokens of information-rich content.
* **Cosmopedia:** The **BhashaKritika** project translated the **Cosmopedia** corpus (30M synthetic documents) using Sarvam Translate. This provides a source of high-quality, textbook-style data that can be useful for building instruction-following Indic LLMs.
* **FineWeb-Edu:** The MILA project has also translated **FineWeb-Edu** using a sophisticated pipeline involving **IndicTrans2** followed by LLM-based post-processing to ensure naturalness and fluency.

### Generated Data

As modern LLMs hit the "data wall," synthetic data has become essential for generating high-quality, diverse content that addresses niche edge cases missing from organic web crawls. This is particularly critical in the Indian context, where organic digital data is often sparse, linguistically limited, and lacks representative diversity.

Two primary methodologies have emerged to solve the Indic data scarcity:

**Document-Grounded Synthesis**: BhashaKritika focuses on creating original, high-fidelity content grounded in authentic Indian source documents. This system generates information-heavy text across various styles—including academic papers and blog posts—tailored to the Indian context. This is further bolstered by retrieving related web documents and synthesizing new, contextually relevant content based on those retrievals.

**Persona-Driven Generation**: Leveraging the "Persona" framework has proven highly effective for diversifying synthetic datasets. While BhashaKritika utilizes PersonaHub to generate Indian-centric documents, they have also created 50,000 native Indic personas derived directly from local language web data. MILA has developed IndicPersonaHub, an expansive project capturing 300 million personas that reflect a vast spectrum of roles and tasks relevant to India.

**Scale and Composition**:

These persona-driven frameworks enable the generation of massive instruction and pre-training datasets:

- BhashaKritika: ~500 billion tokens.
- MILA: ~2.5 trillion tokens.

While these datasets represent significant advances, the quality and factuality of generated documents need to be further studied. Given that the underlying LLMs used to generate this data often have inherent limitations in Indic languages, the risk of "hallucinated" content or cultural inaccuracies persists. The evolution of these datasets will be a defining factor in whether synthetic pipelines can truly elevate the performance of next-generation Indic LLMs.

## A Quick Peek at Hindi pre-training datasets

I compiled and computed some quick stats on Hindi pre-training datasets that are available in the public domain. See the table below for stats: 

| Dataset | Documents (millions) | Words (billions) | Tokens [phi4-mini] (billions) | Tokens [gemma3] (billions) | Words per Document |
|---------|---------------------|------------------|------------------------------|---------------------------|-------------------:|
| Sangraha (verified) | 17.42 | 7.45 | 12.82 | 11.03 | 427.86 |
| Sangraha (unverified) | 16.89 | 8.59 | 14.78 | 12.71 | 508.45 |
| Fineweb-2 | 22.10 | 10.22 | 17.58 | 15.12 | 462.48 |
| Fineweb-2 (removed) | 17.17 | 6.63 | 11.40 | 9.81 | 386.22 |
| HPLT 3.0 | 36.33 |	19.40	| 33.36 	| 28.71 |	534.01 |
| Vaarta | 14.42 | 4.86 | 8.36 | 7.19 | 337.08 |
| Finepdfs | 0.85 | 3.00 | 5.16 | 4.44 | 3,530.51 |
| Finepdfs-edu | 0.08 | 0.68 | 1.17 | 1.01 | 8,147.23 |
| Finewiki | 0.17 | 0.06 | 0.10 | 0.08 | 335.14 |
| Pralekha (train) | 0.20 | 0.12 | 0.21 | 0.18 | 618.77 |
| Pralekha (unalignable) | 0.10 | 0.05 | 0.09 | 0.08 | 507.5 |
| Sangraha (translated) | 5.78 | 3.35 | 5.75 | 4.95 | 579.27 |
| **Total** | **125.72** | **61.06** | **105.02** | **90.37** | **485.68** |

I think this is a fair estimate of the web corpora that exists for Hindi. There will be duplication across these sources as well since overlapping CommonCrawl snapshots is ingested by all these corpora. While this is good for some language modeling, it is surely not sufficient for capturing all the knowledge that LLMs should possess. The organic high-quality resources and long-context documents like finepdfs and Pralekha are also limited. The Hindi data is an upper-bound on what would be available for Indic languages. 

At this point, MILA has not released its corpus and BhashaKritika has put out only a small fraction of its synthetic corpus. It would be interesting to see the increase in organic data from MILA's data collection as well as the quantum of synthetic data. 

Here are the stats for English from Indian sources, which looks like a sizable corpus.

| Dataset | Documents (millions) | Words (billions) | Tokens [phi4-mini] (billions) | Tokens [gemma3] (billions) | Words per Document |
|---------|---------------------|------------------|------------------------------|---------------------------|-------------------:|
| Sangraha (verified,eng) | 17.48 | 7.91 | 9.34 | 10.60 | 452.63 |
| Vaarta (eng) | 7.25 | 2.88 | 3.40 | 3.87 | 397.83 |

If you want diverse English corpora during pre-training, you can take a look at the Dolma3 (for pre-training from scratch) or Dolmino3 (for CPT) mixes. You can read [my previous article](https://airesearchindia.substack.com/p/a-quick-tour-of-pre-training-corpora) for more about English pre-training data sources. 


## Final Comments

While we have made significant strides in building robust pre-training corpora, several  opportunities remain to further refine the quality and depth of Indic data:

* **Beyond Web-Scraping:** There is a critical need to diversify into varied genres, including classical literary archives, nuanced conversational data, and high-fidelity transcripts of spontaneous speech. Building these specialized, large-scale resources requires a sustained, collective effort that moves beyond simple web crawls toward intentional data curation.
* **Linguistic Realism:** 
    * **Code-Mixing:** Since mixing languages (e.g., Hinglish) is a daily reality in India, corpora must reflect this hybrid usage to be truly representative.
    * **Romanized Script Support:** Romanized Indic content is ubiquitous in social media and private messaging. While not a substitute for native scripts, supporting this transliterated data is essential for modern communication models.
* **Expanding the Long Tail:** Current public web resources are heavily skewed toward the top 10–12 Indian languages. We must scale efforts to encompass all 22 scheduled languages and beyond. This requires unlocking data from fieldwork, university research, and specialized bodies like Tribal Research Institutes.
* **Iterative Quality & Metadata:** We must move toward "smarter" data by annotating corpora with rich metadata. Most current datasets lack granular topic classification and "educational value" scores—metadata that is indispensable for effective **mid-training**.
* **English Data Selection:** Given the limited Indian language data, what subset of English data is useful for maximum knowledge transfer and cross-lingual alignment.
* **Optimized Data Mixes:** The community needs established recipes and collections for data-mixing across different stages: initial pre-training, mid-training, and "cooldown" phases. Specifically, small-scale, high-quality mixes would significantly lower the barrier for research and ablation studies.



---
## References

### Indic Language Models & Corpora

1. **IndicNLPSuite (IndicCorp v1, IndicBERT)** - Kakwani et al. (2020). *IndicNLPSuite: Monolingual Corpora, Evaluation Benchmarks and Pre-trained Multilingual Language Models for Indian Languages*. Findings of EMNLP 2020. [arXiv](https://arxiv.org/abs/2005.00085)

2. **IndicCorp v2** - Doddapaneni et al. (2023). *Towards Leaving No Indic Language Behind: Building Monolingual Corpora, Benchmark and Models for Indic Languages*. ACL 2023. [arXiv](https://arxiv.org/abs/2212.05409)

3. **IndicBART** - Dabre et al. (2022). *IndicBART: A Pre-trained Model for Indic Natural Language Generation*. ACL 2022 Findings. [arXiv](https://arxiv.org/abs/2109.02903)

4. **Vaarta** - Aralikatte et al. (2023). *Vārta: A Large-Scale Headline-Generation Dataset for Indic Languages*. ACL 2023 Findings. [arXiv](https://arxiv.org/abs/2305.05858)

5. **Sangraha** - Khan et al. (2024). *IndicLLMSuite: A Blueprint for Creating Pre-training and Fine-Tuning Datasets for Indian Languages*. [arXiv](https://arxiv.org/abs/2403.06350)

6. **Pralekha** - Suryanarayanan et al. (2025). *PRALEKHA: Cross-Lingual Document Alignment for Indic Languages*. IJCNLP-AACL 2025. [arXiv](https://arxiv.org/abs/2411.19096)

7. **IndicTrans2** - Gala et al. (2023). *IndicTrans2: Towards High-Quality and Accessible Machine Translation Models for all 22 Scheduled Indian Languages*. TMLR 2023. [arXiv](https://arxiv.org/abs/2305.16307)

8. **MILA** - Anonymous. (2025). *MILA (MULTILINGUAL INDIC LANGUAGE ARCHIVE): A DATASET FOR EQUITABLE MULTILINGUAL LLMS*. (under review). [OpenReview](https://openreview.net/pdf?id=WPw6ERKUZL)

9. **BhashaKritika** - Manoj et al. (2026). *BhashaKritika: Building Synthetic Pretraining Data at Scale for Indic Languages*. [arXiv](https://arxiv.org/abs/2511.10338)

### Multilingual Web Corpora

10. **CulturaX** - Nguyen et al. (2024). *CulturaX: A Cleaned, Enormous, and Multilingual Dataset for Large Language Models in 167 Languages*. LREC 2024. [arXiv](https://arxiv.org/abs/2309.09400)

11. **FineWeb** - Penedo et al. (2024). *The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale*. [arXiv](https://arxiv.org/abs/2406.17557)

12. **FineWeb-2** - Penedo et al. (2025). *FineWeb2: One Pipeline to Scale Them All -- Adapting Pre-Training Data Processing to Every Language*. [arXiv](https://arxiv.org/abs/2506.20920)

13. **FineWiki** - HuggingFace. *FineWiki: The finest knowledge from the Free Encyclopedia*. [HuggingFace](https://huggingface.co/datasets/HuggingFaceFW/finewiki)

14. **FinePDFs** - HuggingFace. *FinePDFs: Liberating 3T of the finest tokens from PDFs*. [HuggingFace](https://huggingface.co/datasets/HuggingFaceFW/finepdfs)

15. **FineWeb-Edu** - Penedo et al. (2024). *FineWeb-Edu: The finesh collection of educational content the web has to offer*. [HuggingFace](https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu)

16. **HPLT** - de Gibert et al. (2024). *A New Massive Multilingual Dataset for High-Performance Language Technologies*. LREC-COLING 2024. [arXiv](https://arxiv.org/abs/2403.14009)

### Synthetic Data

17. **Cosmopedia** - Ben Allal et al. (2024). *Cosmopedia: How to Create Large-Scale Synthetic Data for Pre-training*. [HuggingFace](https://huggingface.co/blog/cosmopedia)

18. **PersonaHub** - Ge et al. (2024). *Scaling Synthetic Data Creation with 1,000,000,000 Personas*. [arXiv](https://arxiv.org/abs/2406.20094)

---
