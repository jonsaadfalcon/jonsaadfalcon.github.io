---
layout: page
title: Publications
subtitle: Full list of research publications, ordered by year.
---

{% assign pubs_by_year = site.categories.papers | group_by_exp: "pub", "pub.year" | sort: "name" | reverse %}

{% for year_group in pubs_by_year %}
<h3 class="year-heading">{{ year_group.name }}</h3>
<ul class="pub-list">
  {% assign sorted_pubs = year_group.items | sort: 'date' | reverse %}
  {% for pub in sorted_pubs %}
  <li class="pub-item">
    <div class="pub-title">{{ pub.title }}</div>
    <div class="pub-authors">
      {% for author in pub.authors %}{% if author == "Jon Saad-Falcon" %}<span class="me">{{ author }}</span>{% else %}{{ author }}{% endif %}{% unless forloop.last %}, {% endunless %}{% endfor %}
    </div>
    <div class="pub-venue">{{ pub.venue }} {{ pub.year }}{% if pub.highlight %} <span class="highlight">{{ pub.highlight }}</span>{% endif %}</div>
    <div class="pub-links">
      {% if pub.pdf %}<a class="pub-link" href="{{ pub.pdf }}">paper</a>{% endif %}
      {% if pub.code %}<a class="pub-link" href="{{ pub.code }}">code</a>{% endif %}
      {% if pub.demo %}<a class="pub-link" href="{{ pub.demo }}">demo</a>{% endif %}
      {% if pub.video %}<a class="pub-link" href="{{ pub.video }}">video</a>{% endif %}
    </div>
  </li>
  {% endfor %}
</ul>
{% endfor %}
