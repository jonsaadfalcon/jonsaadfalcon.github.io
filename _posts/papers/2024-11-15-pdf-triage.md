---
layout: paper
categories: papers
permalink: papers/pdftriage
id: pdftriage
title: "PDFTriage: Question Answering over Long, Structured Documents"
authors: 
  - Jon Saad-Falcon
  - Joe Barrow
  - Alexa Siu
  - Ani Nenkova
  - Seunghyun Yoon
  - Ryan A. Rossi
  - Franck Dernoncourt
venue: EMNLP Industry
year: 2024
url: /papers/pdftriage
pdf: https://aclanthology.org/2024.emnlp-industry.13.pdf
code: https://github.com/adobe-research/pdftriage
type: conference
figure: /images/papers/pdftriage_figure.png
image: /images/papers/pdftriage_image.png
featured: false
feature-order: 1
feature-title: "PDFTriage"
feature-description: "Document QA with Structure"
selected: true
bibtex: |-

  @inproceedings{saad-falcon-etal-2024-pdftriage,
      title = "{PDFT}riage: Question Answering over Long, Structured Documents",
      author = "Saad-Falcon, Jon  and
        Barrow, Joe  and
        Siu, Alexa  and
        Nenkova, Ani  and
        Yoon, Seunghyun  and
        Rossi, Ryan A.  and
        Dernoncourt, Franck",
      booktitle = "Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing: Industry Track",
      month = nov,
      year = "2024",
      address = "Miami, Florida, US",
      publisher = "Association for Computational Linguistics",
      url = "https://aclanthology.org/2024.emnlp-industry.13/",
      doi = "10.18653/v1/2024.emnlp-industry.13",
      pages = "153--169"
  }
  
---
Large Language Models (LLMs) have issues with document question answering (QA) in situations where the document is unable to fit in the small context length of an LLM. To overcome this issue, most existing works focus on retrieving the relevant context from the document, representing them as plain text. However, documents such as PDFs, web pages, and presentations are naturally structured with different pages, tables, sections, and so on. Representing such structured documents as plain text is incongruous with the user's mental model of these documents with rich structure. When a system has to query the document for context, this incongruity is brought to the fore, and seemingly trivial questions can trip up the QA system. To bridge this fundamental gap in handling structured documents, we propose an approach called PDFTriage that enables models to retrieve the context based on either structure or content. Our experiments demonstrate the effectiveness of the proposed PDFTriage-augmented models across several classes of questions where existing retrieval-augmented LLMs fail. To facilitate further research on this fundamental problem, we release our benchmark dataset consisting of 900+ human-generated questions over 80 structured documents from 10 different categories of question types for document QA.
