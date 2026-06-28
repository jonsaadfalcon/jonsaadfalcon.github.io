---
layout: paper
categories: papers
permalink: papers/openjarvis
id: openjarvis
title: "OpenJarvis: Personal AI, On Personal Devices"
authors:
  - Jon Saad-Falcon
  - Avanika Narayan
  - Hakki Orhun Akengin
  - Herumb Shandilya
  - Robby Manihani
  - Gabriel Bo
  - John Hennessy
  - Azalia Mirhoseini
  - Christopher Ré
venue: Preprint
year: 2026
url: /papers/openjarvis
pdf: https://arxiv.org/abs/2605.17172
blog: https://scalingintelligence.stanford.edu/blogs/openjarvis/
code: https://github.com/open-jarvis/OpenJarvis
image: /images/papers/openjarvis_image.png
type: preprint
featured: true
feature-order: 0
feature-title: "OpenJarvis"
feature-description: "Personal AI, On Personal Devices"
selected: true
---
OpenJarvis is an open-source framework for personal AI agents that runs entirely on-device. The system provides composable primitives for building on-device agents while treating efficiency metrics like energy and cost as primary evaluation targets alongside accuracy.

<h2 class="section-title" style="margin-top: 36px;">Coverage &amp; Adoption</h2>

<p style="font-size: 0.92rem; color: #555; line-height: 1.7;">Selected industry and community references to <em>OpenJarvis</em>.</p>

<h3 style="font-family: Georgia, serif; font-size: 1rem; font-weight: 700; color: #2E7D6F; margin-top: 24px; margin-bottom: 8px;">Industry &amp; Analyst</h3>
<ul class="pub-list">
{% for item in site.data.openjarvis-coverage %}
  {% if item.category == "industry" %}
  <li class="pub-item">
    <div class="pub-title">{{ item.title }}</div>
    <div class="pub-venue" style="font-style: normal;">{{ item.publisher }} &middot; {{ item.date }}</div>
    <div class="pub-links"><a class="pub-link" href="{{ item.url }}" target="_blank">read</a></div>
  </li>
  {% endif %}
{% endfor %}
</ul>
