---
layout: home
title: Home
---

<div class="hero">
  <div class="hero-left">
    <img class="hero-photo" src="/images/jon.png" alt="Jon Saad-Falcon">
    <div class="hero-role">
      Computer Science Ph.D.<br>& MBA Candidate<br>Stanford University
    </div>
    <div class="social-icons">
      <a class="social-icon" href="https://scholar.google.com/citations?user=zCVmjboAAAAJ&hl=en" title="Google Scholar"><i class="ai ai-google-scholar"></i></a>
      <a class="social-icon" href="https://www.linkedin.com/in/jonsaadfalcon" title="LinkedIn"><i class="fa-brands fa-linkedin-in"></i></a>
      <a class="social-icon" href="https://twitter.com/JonSaadFalcon" title="Twitter / X"><i class="fa-brands fa-x-twitter"></i></a>
      <a class="social-icon" href="https://github.com/jonsaadfalcon" title="GitHub"><i class="fa-brands fa-github"></i></a>
      <a class="social-icon" href="mailto:jonsaadfalcon@stanford.edu" title="Email"><i class="fa-solid fa-envelope"></i></a>
      <a class="social-icon" href="/cv.pdf" title="CV"><i class="fa-solid fa-file-lines"></i></a>
    </div>
    <div class="hero-people">
      <div class="hero-people-label">Advisors</div>
      <div class="hero-people-text"><a href="https://www.azaliamirhoseini.com/">Azalia Mirhoseini</a>, <a href="https://cs.stanford.edu/~chrismre/">Christopher R&eacute;</a></div>
      <div class="hero-people-label">Current Mentees</div>
      <div class="hero-people-text">{% for m in site.data.mentees.current %}{{ m.name }}{% unless forloop.last %}, {% endunless %}{% endfor %}</div>
      <div class="hero-people-label">Past Mentees</div>
      <div class="hero-people-text">{% for m in site.data.mentees.past %}{{ m.name }} <span class="dest">({{ m.destination }})</span>{% unless forloop.last %}, {% endunless %}{% endfor %}</div>
    </div>
  </div>

  <div class="hero-text">
    <!-- <h1>Jon Saad-Falcon</h1> -->

    <div class="hero-bio">
      <strong>About Me:</strong> I am a joint Computer Science Ph.D. and MBA student at Stanford University, advised by <a href="https://www.azaliamirhoseini.com/">Azalia Mirhoseini</a> (<a href="https://scalingintelligence.stanford.edu/">Scaling Intelligence Lab</a>) and <a href="https://cs.stanford.edu/~chrismre/">Christopher R&eacute;</a> (<a href="https://hazyresearch.stanford.edu/">Hazy Research</a>). I am also a Google Student Researcher on the TPU and Gemini teams.
    </div>

    <div class="hero-bio">
      My research lies at the intersection of language models and ML systems. Most recently, I've studied the <strong>intelligence efficiency</strong> of LM systems, with the goal of <strong>commoditizing intelligence</strong> through increasingly efficient open-source LMs and hardware accelerators. By reducing the energy, compute, and capital required for deploying LMs at scale, we hope to make LM systems more broadly utilized around the world. Our agenda spans foundation models, ML systems, electrical engineering, and economics, and is anchored by the <a href="https://www.intelligence-per-watt.ai/">Intelligence per Watt</a> project.
    </div>

    <div class="hero-bio">
      I've been fortunate to collaborate with <a href="https://profiles.stanford.edu/john-hennessy">John Hennessy</a> (Stanford), <a href="https://www.achowdhery.com/">Aakanksha Chowdhery</a> (Stanford / Reflection AI), and <a href="https://www.linkedin.com/in/jspisak/">Joe Spisak</a> (Meta), among others.
    </div>

    <div class="hero-bio">
      My doctoral studies are supported by the <a href="https://vpge.stanford.edu/fellowships-funding/sgf">Stanford Graduate Fellowship</a>, <a href="https://www.jpmorganchase.com/about/technology/research/ai">JP Morgan AI/ML Fellowship</a>, <a href="https://vpge.stanford.edu/fellowships-funding/EDGE">Stanford EDGE Fellowship</a>, and <a href="https://www.gemfellowship.org/gem-fellowship-program/">GEM Fellowship</a>. I am a recipient of the <a href="https://us.fulbrightonline.org/">Fulbright Scholarship</a> (Research Award, Germany) and <a href="https://www.gatescambridge.org/">Gates-Cambridge Scholarship</a> for post-graduate studies. Previously, I was a Predoctoral Young Investigator at the <a href="https://allenai.org/">Allen Institute for AI</a> and completed the joint B.S./M.S. in Computer Science at <a href="https://www.scs.gatech.edu/">Georgia Tech</a> as a <a href="https://stampsps.gatech.edu/">Stamps President's Scholar</a>.
    </div>

    <div class="hero-supporters">
      My research is generously supported by Stanford HAI, Laude Institute, Lambda Labs, Ollama, and IBM Research.
    </div>
  </div>
</div>

<!-- Announcement bubble (uncomment when needed)
<div class="announcement-bubble">
  Your announcement here.
</div>
-->

<!-- News timeline (uncomment when needed)
<div class="section">
  <h2 class="section-title">News</h2>
</div>
-->

<div class="section">
  <h2 class="section-title">Selected Publications</h2>
  <ul class="pub-list">
    {% assign sortedPubs = site.categories.papers | where: 'featured', true | sort: 'date' | reverse %}
    {% for pub in sortedPubs %}
      <li class="pub-item">
        <div class="pub-title">{{ pub.title }}</div>
        <div class="pub-authors">
          {% for author in pub.authors %}{% if author == "Jon Saad-Falcon" %}<span class="me">{{ author }}</span>{% else %}{{ author }}{% endif %}{% unless forloop.last %}, {% endunless %}{% endfor %}
        </div>
        <div class="pub-venue">{{ pub.venue }} {{ pub.year }}{% if pub.highlight %} <span class="highlight">{{ pub.highlight }}</span>{% endif %}</div>
        <div class="pub-links">
          {% if pub.pdf %}<a class="pub-link" href="{{ pub.pdf }}">paper</a>{% endif %}
          {% if pub.code %}<a class="pub-link" href="{{ pub.code }}">code</a>{% endif %}
          {% if pub.blog %}<a class="pub-link" href="{{ pub.blog }}">blog</a>{% endif %}
          {% if pub.demo %}<a class="pub-link" href="{{ pub.demo }}">demo</a>{% endif %}
          {% if pub.video %}<a class="pub-link" href="{{ pub.video }}">video</a>{% endif %}
        </div>
      </li>
    {% endfor %}
  </ul>
  <div style="margin-top: 14px;"><a href="/publications" style="font-size: 0.88rem;">View all publications &rarr;</a></div>
</div>

<div class="section">
  <h2 class="section-title">In the News</h2>
  <ul class="pub-list">
    {% for item in site.data.ipw-coverage %}
      {% if item.featured %}
      <li class="pub-item">
        <div class="pub-title">{{ item.title }}</div>
        <div class="pub-venue" style="font-style: normal;">{{ item.publisher }} &middot; {{ item.date }}</div>
        <div class="pub-links">
          <a class="pub-link" href="{{ item.url }}" target="_blank">read</a>
        </div>
      </li>
      {% endif %}
    {% endfor %}
  </ul>
  <div style="margin-top: 14px;"><a href="/papers/ipw" style="font-size: 0.88rem;">View full coverage list &rarr;</a></div>
</div>

<div class="section">
  <h2 class="section-title">Invited Talks</h2>
  <ul class="talk-list">
    {% for talk in site.data.talks %}
    <li class="talk-item">
      <div class="talk-title">&ldquo;{{ talk.title }}&rdquo;</div>
      <ul class="talk-venues">
        {% for venue in talk.venues %}
        <li class="talk-venue">{{ venue.name }}: <span class="talk-date">{{ venue.date }}.</span></li>
        {% endfor %}
      </ul>
    </li>
    {% endfor %}
  </ul>
</div>

<div class="section">
  <h2 class="section-title">Fellowships &amp; Awards</h2>
  <ul class="award-list">
    {% for award in site.data.awards %}
    <li class="award-item">
      <span class="award-name"><span class="award-org">{{ award.name }}</span>{% if award.org %} <em style="font-weight: normal; color: #555;">&mdash; {{ award.org }}</em>{% endif %}</span>
      <span class="award-year">{{ award.year }}</span>
    </li>
    {% endfor %}
  </ul>
</div>
