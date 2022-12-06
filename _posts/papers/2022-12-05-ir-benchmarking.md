---
layout: paper
categories: papers
permalink: papers/ir-benchmarking
id: ir-benchmarking
title: "Moving Beyond Downstream Task Accuracy for Information Retrieval Benchmarking"
authors: 
  - Keshav Santhanam*
  - Jon Saad-Falcon*
  - Martin Franz
  - Omar Khattab
  - Avirup Sil
  - Radu Florian
  - Md Arafat Sulton
  - Salim Roukos
  - Matei Zaharia
  - Christopher Potts
venue: Preprint, under review
year: 2022
url: /papers/ir-benchmarking
pdf: https://arxiv.org/abs/2212.01340
code: https://github.com/primeqa/primeqa
type: conference
figure: /images/papers/ir-benchmark.png
image: /images/papers/ir-benchmark.png
featured: false
feature-title: "Moving Beyond Accuracy"
feature-description: "Information Retrieval Benchmarking"
feature-order: 5
selected: false
bibtex: |-

  @misc{saadfalcon2020peoplemap,
    title={Mapping Researchers with PeopleMap},
    author={Jon Saad-Falcon and Omar Shaikh and Zijie J. Wang and Austin P. Wright and Sasha Richardson and Duen Horng Chau},
    booktitle={IEEE Visualization Conference (VIS)},
    publisher={IEEE},
    year={2020},
    url={https://poloclub.github.io/people-map/}
  }
---

Neural information retrieval (IR) systems have progressed rapidly in recent years, in large part 
due to the release of publicly available benchmarking tasks. Unfortunately, some dimensions of this progress are illusory: 
the majority of the popular IR benchmarks today focus exclusively on downstream task accuracy and thus conceal the costs 
incurred by systems that trade away efficiency for quality. Latency, hardware cost, and other efficiency considerations are 
paramount to the deployment of IR systems in user-facing settings. We propose that IR benchmarks structure their evaluation 
methodology to include not only metrics of accuracy, but also efficiency considerations such as a query latency and the corresponding 
cost budget for a reproducible hardware setting. For the popular IR benchmarks MS MARCO and XOR-TyDi, we show how the best choice 
of IR system varies according to how these efficiency considerations are chosen and weighed. We hope that future benchmarks will 
adopt these guidelines toward more holistic IR evaluation.