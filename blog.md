---
layout: page
title: Blog
subtitle: Thoughts on research, AI, and building things.
---

{% assign posts = site.posts | where_exp: "post", "post.categories contains 'blog'" %}

{% if posts.size > 0 %}
<ul class="pub-list">
  {% for post in posts %}
  <li class="pub-item">
    <div class="pub-title"><a href="{{ post.url }}" style="color: inherit; border-bottom: none;">{{ post.title }}</a></div>
    <div class="pub-venue" style="font-style: normal;">{{ post.date | date: "%B %d, %Y" }}</div>
    {% if post.excerpt %}<div class="pub-authors">{{ post.excerpt | strip_html | truncate: 200 }}</div>{% endif %}
  </li>
  {% endfor %}
</ul>
{% else %}
<div style="padding: 40px 0; text-align: center; color: #888; font-size: 0.92rem;">
  <i class="fa-solid fa-pencil" style="font-size: 1.5rem; margin-bottom: 12px; display: block; color: rgba(46, 125, 111, 0.3);"></i>
  Posts coming soon.
</div>
{% endif %}
