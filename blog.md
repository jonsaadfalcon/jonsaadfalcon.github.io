---
layout: page
title: Blog
subtitle: Blog posts from Scaling Intelligence Lab and Hazy Research.
---

<ul class="pub-list">
  {% for post in site.data.blog-posts %}
  <li class="pub-item">
    <div class="pub-title"><a href="{{ post.url }}" target="_blank" style="color: inherit; border-bottom: none;">{{ post.title }}</a></div>
    <div class="pub-authors">
      {% for author in post.authors %}{% if author == "Jon Saad-Falcon" %}<span class="me">{{ author }}</span>{% else %}{{ author }}{% endif %}{% unless forloop.last %}, {% endunless %}{% endfor %}
    </div>
    <div class="pub-venue">{{ post.lab }} &middot; {{ post.date }}</div>
    <div class="pub-links">
      <a class="pub-link" href="{{ post.url }}" target="_blank">read</a>
    </div>
  </li>
  {% endfor %}
</ul>
