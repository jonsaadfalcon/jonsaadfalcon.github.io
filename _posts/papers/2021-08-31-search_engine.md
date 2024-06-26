---
layout: paper
categories: papers
permalink: papers/search_engine
id: search_engine
title: "A Search Engine for Discovery of Scientific Challenges and Directions"
authors: 
  - Dan Lahav
  - Jon Saad-Falcon
  - Bailey Kuehl
  - Sophie Johnson
  - Sravanthi Parasa
  - Noam Shomron
  - Duen Horng Chau
  - Diyi Yang
  - Eric Horvitz
  - Daniel S. Weld
  - Tom Hope
venue: AAAI Conference on Artificial Intelligence
venue-shorthand: AAAI
year: 2022
highlight: Oral Presentation
url: /papers/search_engine
pdf: https://arxiv.org/abs/2108.13751
code: https://github.com/Dan-La/scientific-challenges-and-directions
demo: https://challenges.apps.allenai.org
type: conference
image: /images/papers/search_engine.png
figure: /images/featured/search_engine.png
feature-title: "COVID-19 Literature Exploration"
feature-description: "A Search Engine for Discovery of Scientific Challenges and Directions"
featured: false
selected: false
bibtex: |-

  @misc{lahav2021search,
      title={A Search Engine for Discovery of Scientific Challenges and Directions}, 
      author={Dan Lahav and Jon Saad Falcon and Bailey Kuehl and Sophie Johnson and Sravanthi Parasa and Noam Shomron and Duen Horng Chau and Diyi Yang and Eric Horvitz and Daniel S. Weld and Tom Hope},
      year={2021},
      eprint={2108.13751},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
  }
  
---

Keeping track of scientific challenges, advances and emerging directions is a fundamental part of research. However, researchers face a flood of papers that hinders discovery of important knowledge. In biomedicine, this directly impacts human lives. To address this problem, we present a novel task of extraction and search of scientific challenges and directions, to facilitate rapid knowledge discovery. We construct and release an expert-annotated corpus of texts sampled from full-length papers, labeled with novel semantic categories that generalize across many types of challenges and directions. We focus on a large corpus of interdisciplinary work relating to the COVID-19 pandemic, ranging from biomedicine to areas such as AI and economics. We apply a model trained on our data to identify challenges and directions across the corpus and build a dedicated search engine. In experiments with 19 researchers and clinicians using our system, we outperform a popular scientific search engine in assisting knowledge discovery. Finally, we show that models trained on our resource generalize to the wider biomedical domain and to AI papers, highlighting its broad utility. We make our data, model and search engine publicly available.
