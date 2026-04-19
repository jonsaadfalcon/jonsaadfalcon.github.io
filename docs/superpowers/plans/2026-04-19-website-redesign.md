# Website Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rebuild jonsaadfalcon.com from the current Gaegu-font site to a polished Georgia + Forest Mint (#2E7D6F) design with 4-tab navigation (Home/Publications/CV/Blog).

**Architecture:** Jekyll static site with SCSS. Replace existing variables/layouts/includes wholesale. Data-driven content via YAML files for mentees, talks, and awards. Homepage uses a custom `home` layout; Publications and Blog use a `page` layout. CV links directly to a PDF.

**Tech Stack:** Jekyll, SCSS, Font Awesome 6.5 (CDN), Academicons (CDN), GitHub Pages.

**Reference mockup:** `.superpowers/brainstorm/32440-1776616151/content/all-pages-mockup-v3.html`

---

### Task 1: SCSS Foundation

Replace the variables file and create the new base styles.

**Files:**
- Modify: `_sass/_variables.scss`
- Modify: `_sass/_base.scss`

- [ ] **Step 1: Replace `_sass/_variables.scss` with new design tokens**

Replace the entire file contents with:

```scss
// Breakpoints
$mobile: 640px;

// Design tokens
$accent: #2E7D6F;
$accent-hover: #246858;
$accent-light: #E8F5F0;
$accent-border: rgba(46, 125, 111, 0.3);

$text: #222;
$text-secondary: #555;
$text-muted: #888;

$bg: #ffffff;
$border: #e8e8e8;
$border-light: #f0f0f0;

$font-serif: Georgia, 'Times New Roman', serif;
$font-sans: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;

$max-width: 740px;

$award-highlight: #b8860b;
```

- [ ] **Step 2: Replace `_sass/_base.scss` with new base styles**

Replace the entire file contents with:

```scss
*, *::before, *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  scroll-behavior: smooth;
}

body {
  font-family: $font-serif;
  color: $text;
  background: $bg;
  line-height: 1.7;
  font-size: 16px;
  -webkit-font-smoothing: antialiased;
}

a {
  color: $accent;
  text-decoration: none;
  border-bottom: 1px solid $accent-border;
  padding-bottom: 0.5px;
  transition: border-color 0.2s, color 0.2s;

  &:hover {
    color: $accent-hover;
    border-bottom-color: $accent;
  }
}

img {
  max-width: 100%;
  height: auto;
}

.container {
  max-width: $max-width;
  margin: 0 auto;
  padding: 0 24px;
}

// Section shared styles
.section {
  margin-bottom: 40px;
}

.section-title {
  font-family: $font-serif;
  font-size: 1.15rem;
  font-weight: 700;
  color: $text;
  margin-bottom: 18px;
  padding-bottom: 10px;
  border-bottom: 2px solid $accent-light;
  letter-spacing: -0.01em;
}

// Page header (for subpages)
.page-header {
  padding: 40px 0 24px;

  h1 {
    font-family: $font-serif;
    font-size: 1.6rem;
    font-weight: 700;
    color: $text;
    letter-spacing: -0.01em;
  }

  p {
    font-size: 0.9rem;
    color: $text-secondary;
    margin-top: 6px;
  }
}
```

- [ ] **Step 3: Verify build compiles**

Run: `cd /Users/jonsaadfalcon/Documents/PersonalWebsite/jonsaadfalcon.github.io && bundle exec jekyll build 2>&1 | tail -5`

Expected: Build succeeds (may have visual issues since layouts aren't updated yet, but no SCSS compile errors).

- [ ] **Step 4: Commit**

```bash
git add _sass/_variables.scss _sass/_base.scss
git commit -m "feat: replace SCSS foundation with Georgia + Forest Mint design tokens"
```

---

### Task 2: Head, Nav, and Footer Includes

Replace the `<head>`, header (navigation), and footer partials.

**Files:**
- Modify: `_includes/head.html`
- Modify: `_includes/header.html`
- Modify: `_includes/footer.html`

- [ ] **Step 1: Replace `_includes/head.html`**

Replace the entire file contents with:

```html
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <!-- Share card -->
  <meta name="twitter:card" content="summary" />
  <meta name="twitter:site" content="@jonsaadfalcon" />
  <meta name="twitter:creator" content="@jonsaadfalcon" />
  <meta property="og:url" content="https://jonsaadfalcon.com/" />
  <meta property="og:title" content="Jon Saad-Falcon" />

  <title>
    {% if page.title == "Home" %}
      {{ site.title }}
    {% else %}
      {{ page.title }} — {{ site.title }}
    {% endif %}
  </title>

  <!-- CSS -->
  <link rel="stylesheet" href="{{ site.baseurl }}/styles.css">

  <!-- Icons: Font Awesome 6.5 + Academicons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/jpswalsh/academicons@1/css/academicons.min.css">

  <!-- Favicons -->
  <link rel="apple-touch-icon" sizes="180x180" href="/icons/apple-touch-icon.png?v=xQdLjRyXLj">
  <link rel="icon" type="image/png" sizes="32x32" href="/icons/favicon-32x32.png?v=xQdLjRyXLj">
  <link rel="icon" type="image/png" sizes="16x16" href="/icons/favicon-16x16.png?v=xQdLjRyXLj">
  <link rel="manifest" href="/icons/site.webmanifest?v=xQdLjRyXLj">
  <link rel="shortcut icon" href="/icons/favicon.ico?v=xQdLjRyXLj">
  <meta name="theme-color" content="#ffffff">

  <!-- Feed -->
  {% feed_meta %}
</head>
```

- [ ] **Step 2: Replace `_includes/header.html`**

Replace the entire file contents with:

```html
<nav class="site-nav">
  <div class="nav-inner">
    <a class="nav-name" href="{{ site.baseurl }}/">{{ site.title }}</a>
    <ul class="nav-links">
      <li><a href="{{ site.baseurl }}/" {% if page.title == "Home" %}class="active"{% endif %}>Home</a></li>
      <li><a href="{{ site.baseurl }}/publications" {% if page.title == "Publications" %}class="active"{% endif %}>Publications</a></li>
      <li><a href="{{ site.baseurl }}/cv.pdf" class="cv-pdf-link" target="_blank">CV <i class="fa-solid fa-arrow-up-right-from-square"></i></a></li>
      <li><a href="{{ site.baseurl }}/blog" {% if page.title == "Blog" %}class="active"{% endif %}>Blog</a></li>
    </ul>
  </div>
</nav>
```

- [ ] **Step 3: Replace `_includes/footer.html`**

Replace the entire file contents with:

```html
<footer class="site-footer">
  <div class="container">
    <div class="footer-icons">
      <a class="footer-icon" href="https://scholar.google.com/citations?user=zCVmjboAAAAJ&hl=en" title="Google Scholar"><i class="ai ai-google-scholar"></i></a>
      <a class="footer-icon" href="https://www.linkedin.com/in/jonsaadfalcon" title="LinkedIn"><i class="fa-brands fa-linkedin-in"></i></a>
      <a class="footer-icon" href="https://github.com/jonsaadfalcon" title="GitHub"><i class="fa-brands fa-github"></i></a>
      <a class="footer-icon" href="https://twitter.com/JonSaadFalcon" title="Twitter / X"><i class="fa-brands fa-x-twitter"></i></a>
      <a class="footer-icon" href="mailto:jonsaadfalcon@stanford.edu" title="Email"><i class="fa-solid fa-envelope"></i></a>
      <a class="footer-icon" href="{{ site.baseurl }}/cv.pdf" title="CV"><i class="fa-solid fa-file-lines"></i></a>
    </div>
    <div class="footer-text">&copy; {{ site.time | date: '%Y' }} Jon Saad-Falcon</div>
  </div>
</footer>
```

- [ ] **Step 4: Commit**

```bash
git add _includes/head.html _includes/header.html _includes/footer.html
git commit -m "feat: replace head/header/footer with new nav and icon libraries"
```

---

### Task 3: SCSS Component Styles

Create the SCSS partials for nav, hero, publications, talks, awards, footer, and update imports.

**Files:**
- Create: `_sass/_nav.scss`
- Create: `_sass/_hero.scss`
- Create: `_sass/_publications.scss`
- Create: `_sass/_talks.scss`
- Create: `_sass/_awards.scss`
- Modify: `_sass/_footer.scss`
- Modify: `styles.scss`

- [ ] **Step 1: Create `_sass/_nav.scss`**

```scss
.site-nav {
  position: sticky;
  top: 0;
  z-index: 100;
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  border-bottom: 1px solid $border;
}

.nav-inner {
  max-width: $max-width;
  margin: 0 auto;
  padding: 14px 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.nav-name {
  font-family: $font-serif;
  font-size: 1.05rem;
  font-weight: 700;
  color: $text;
  border: none;

  &:hover {
    color: $accent;
    border: none;
  }
}

.nav-links {
  display: flex;
  gap: 28px;
  list-style: none;

  a {
    font-family: $font-serif;
    font-size: 0.88rem;
    color: $text-secondary;
    border: none;
    transition: color 0.2s;

    &:hover {
      color: $accent;
      border: none;
    }

    &.active {
      color: $accent;
      font-weight: 600;
    }

    &.cv-pdf-link {
      display: inline-flex;
      align-items: center;
      gap: 4px;

      i {
        font-size: 0.72rem;
        opacity: 0.6;
      }
    }
  }

  @media (max-width: $mobile) {
    gap: 16px;

    a {
      font-size: 0.82rem;
    }
  }
}
```

- [ ] **Step 2: Create `_sass/_hero.scss`**

```scss
.hero {
  padding: 48px 0 36px;
  display: grid;
  grid-template-columns: clamp(160px, 22vw, 210px) 1fr;
  gap: clamp(24px, 3.5vw, 36px);
  align-items: start;

  @media (max-width: $mobile) {
    grid-template-columns: 1fr;
    text-align: center;
    gap: 20px;
  }
}

.hero-left {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;

  @media (max-width: $mobile) {
    width: 200px;
    margin: 0 auto;
  }
}

.hero-photo {
  width: 100%;
  aspect-ratio: 1;
  border-radius: 14px;
  object-fit: cover;
  box-shadow: 0 6px 16px rgba(0, 0, 0, 0.08);
}

.hero-role {
  font-size: 0.74rem;
  color: $text-secondary;
  text-align: center;
  line-height: 1.35;
}

// Social icon grid (2x3)
.social-icons {
  display: grid;
  grid-template-columns: repeat(3, 38px);
  gap: 10px;
  justify-content: center;
}

.social-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 38px;
  height: 38px;
  border-radius: 9px;
  background: $accent-light;
  color: $accent;
  font-size: 1.05rem;
  border: none;
  transition: background 0.2s, color 0.2s, transform 0.15s;

  &:hover {
    background: $accent;
    color: #fff;
    border: none;
    transform: translateY(-1px);
  }
}

// Advisor/mentee section under photo
.hero-people {
  width: 100%;
  margin-top: 6px;
  text-align: left;

  @media (max-width: $mobile) {
    text-align: center;
  }
}

.hero-people-label {
  font-size: 0.78rem;
  font-weight: 700;
  color: $text;
  margin-bottom: 2px;
  margin-top: 10px;

  &:first-child {
    margin-top: 0;
  }
}

.hero-people-text {
  font-size: 0.76rem;
  color: $text-secondary;
  line-height: 1.5;

  a {
    color: $accent;
    border-bottom: none;
    font-size: 0.76rem;

    &:hover {
      border-bottom: 1px solid $accent-border;
    }
  }

  .dest {
    color: $text-muted;
    font-size: 0.72rem;
  }
}

// Right column
.hero-text {
  h1 {
    font-size: clamp(1.5rem, 2.5vw + 0.8rem, 1.9rem);
    font-weight: 700;
    line-height: 1.15;
    margin-bottom: 12px;
    letter-spacing: -0.01em;
  }
}

.hero-bio {
  font-size: 0.92rem;
  line-height: 1.75;
  margin-bottom: 16px;

  strong {
    font-weight: 600;
  }
}

.hero-supporters {
  font-size: 0.85rem;
  color: $text-secondary;
  margin-bottom: 16px;
}
```

- [ ] **Step 3: Create `_sass/_publications.scss`**

```scss
.pub-list {
  list-style: none;
}

.pub-item {
  padding: 16px 0;
  border-bottom: 1px solid $border-light;

  &:last-child {
    border-bottom: none;
  }
}

.pub-title {
  font-size: 0.92rem;
  font-weight: 600;
  color: $text;
  margin-bottom: 4px;
  line-height: 1.4;
}

.pub-authors {
  font-size: 0.82rem;
  color: $text-secondary;
  margin-bottom: 3px;
  line-height: 1.45;

  .me {
    font-weight: 700;
    color: $text;
  }
}

.pub-venue {
  font-size: 0.8rem;
  color: $text-muted;
  font-style: italic;
  margin-bottom: 6px;

  .highlight {
    font-style: normal;
    color: $award-highlight;
    font-weight: 600;
  }
}

.pub-links {
  display: flex;
  gap: 14px;
}

.pub-link {
  font-size: 0.78rem;
  font-family: $font-sans;
  color: $accent;
  border-bottom: 1px solid $accent-border;
  font-weight: 500;
  letter-spacing: 0.01em;

  &:hover {
    border-bottom-color: $accent;
  }
}

.year-heading {
  font-family: $font-serif;
  font-size: 1.05rem;
  font-weight: 700;
  color: $accent;
  margin-top: 32px;
  margin-bottom: 4px;
  padding-bottom: 6px;
  border-bottom: 1px solid $accent-light;

  &:first-of-type {
    margin-top: 0;
  }
}
```

- [ ] **Step 4: Create `_sass/_talks.scss`**

```scss
.talk-list {
  list-style: none;
}

.talk-item {
  padding: 14px 0;
  border-bottom: 1px solid $border-light;

  &:last-child {
    border-bottom: none;
  }
}

.talk-title {
  font-size: 0.92rem;
  font-weight: 600;
  color: $text;
  margin-bottom: 8px;
  line-height: 1.4;
}

.talk-venues {
  list-style: disc;
  padding-left: 20px;
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.talk-venue {
  font-size: 0.82rem;
  color: $text-secondary;
  line-height: 1.45;

  .talk-date {
    color: $text-muted;
    font-size: 0.78rem;
  }
}
```

- [ ] **Step 5: Create `_sass/_awards.scss`**

```scss
.award-list {
  list-style: none;
}

.award-item {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 16px;
  padding: 10px 0;
  border-bottom: 1px solid $border-light;
  align-items: baseline;

  &:last-child {
    border-bottom: none;
  }

  @media (max-width: $mobile) {
    grid-template-columns: 1fr;
    gap: 2px;
  }
}

.award-name {
  font-size: 0.88rem;
  color: $text;
  line-height: 1.45;
}

.award-org {
  font-weight: 600;
}

.award-year {
  font-size: 0.8rem;
  color: $text-muted;
  white-space: nowrap;
  font-variant-numeric: tabular-nums;
}
```

- [ ] **Step 6: Replace `_sass/_footer.scss`**

Replace the entire file contents with:

```scss
.site-footer {
  margin-top: 48px;
  padding: 28px 0;
  border-top: 1px solid $border;
  text-align: center;
}

.footer-icons {
  display: flex;
  justify-content: center;
  gap: 16px;
  margin-bottom: 12px;
}

.footer-icon {
  color: $text-muted;
  font-size: 1rem;
  border: none;
  transition: color 0.2s;

  &:hover {
    color: $accent;
    border: none;
  }
}

.footer-text {
  font-size: 0.75rem;
  color: $text-muted;
  font-family: $font-sans;
}
```

- [ ] **Step 7: Update `styles.scss` imports**

Replace the entire file contents with:

```scss
---
# Main SCSS file
---

@import "variables";
@import "base";

@import "nav";
@import "hero";
@import "publications";
@import "talks";
@import "awards";
@import "footer";

@import "code";
@import "syntax";
@import "print";
```

- [ ] **Step 8: Verify build compiles**

Run: `cd /Users/jonsaadfalcon/Documents/PersonalWebsite/jonsaadfalcon.github.io && bundle exec jekyll build 2>&1 | tail -5`

Expected: Build succeeds with no SCSS errors.

- [ ] **Step 9: Commit**

```bash
git add _sass/_nav.scss _sass/_hero.scss _sass/_publications.scss _sass/_talks.scss _sass/_awards.scss _sass/_footer.scss styles.scss
git commit -m "feat: add all SCSS component styles for new design"
```

---

### Task 4: Layouts

Update the default and home layouts, and the page layout.

**Files:**
- Modify: `_layouts/default.html`
- Modify: `_layouts/home.html`
- Modify: `_layouts/page.html`

- [ ] **Step 1: Replace `_layouts/default.html`**

Replace the entire file contents with:

```html
<!DOCTYPE html>
<html lang="{{ site.lang | default: "en-US" }}">
  {% include head.html %}
  <body>
    {% include header.html %}
    <main class="container">
      {{ content }}
    </main>
    {% include footer.html %}
  </body>
</html>
```

- [ ] **Step 2: Replace `_layouts/home.html`**

Replace the entire file contents with:

```html
<!DOCTYPE html>
<html lang="{{ site.lang | default: "en-US" }}">
  {% include head.html %}
  <body>
    {% include header.html %}
    <main class="container">
      {{ content }}
    </main>
    {% include footer.html %}
  </body>
</html>
```

- [ ] **Step 3: Replace `_layouts/page.html`**

Replace the entire file contents with:

```html
---
layout: default
---

<div class="page-header">
  <h1>{{ page.title }}</h1>
  {% if page.subtitle %}
  <p>{{ page.subtitle }}</p>
  {% endif %}
</div>
{{ content }}
```

- [ ] **Step 4: Commit**

```bash
git add _layouts/default.html _layouts/home.html _layouts/page.html
git commit -m "feat: update layouts for new design system"
```

---

### Task 5: Data Files

Create YAML data files for mentees and talks.

**Files:**
- Create: `_data/mentees.yaml`
- Create: `_data/talks.yaml`

- [ ] **Step 1: Create `_data/mentees.yaml`**

```yaml
current:
  - name: Hangoo Kang
  - name: Hannah Gao
  - name: Harsh Singh
  - name: Matthew Hart
  - name: Orhun Akengin
  - name: Tanvir Bhathal
  - name: Tarun Suresh

past:
  - name: Adrian Lafuente Gamarra
    destination: Salesforce
  - name: Brendan McLaughlin
    destination: Reflection AI
  - name: Herumb Shandilya
    destination: Mixed Bread
  - name: Robby Manihani
    destination: Pace
  - name: Wes Griffin
    destination: Stanford
```

- [ ] **Step 2: Create `_data/talks.yaml`**

```yaml
- title: "Intelligence Efficiency: Measuring and Optimizing AI Performance per Watt"
  venues:
    - name: MBZUAI Speech and NLP Symposium
      date: "Jan. 2026"
    - name: Measuring Intelligence Summit at PyTorch Conference
      date: "Oct. 2025"

- title: "Archon and Inference-Time Techniques"
  venues:
    - name: Together AI
      date: "Jul. 2025"
    - name: LLMs Meet Data Processing Workshop, UC Berkeley
      date: "May 2025"

- title: "Automated Evaluation for Retrieval-Augmented Generation"
  venues:
    - name: Contextual AI
      date: "Oct. 2024"
    - name: Databricks
      date: "Feb. 2024"
```

- [ ] **Step 3: Commit**

```bash
git add _data/mentees.yaml _data/talks.yaml
git commit -m "feat: add mentees and talks data files"
```

---

### Task 6: Homepage Content

Rewrite `index.md` with the full homepage: hero, selected publications, invited talks, fellowships & awards.

**Files:**
- Modify: `index.md`

- [ ] **Step 1: Replace `index.md`**

Replace the entire file contents with:

```markdown
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
    <h1>Jon Saad-Falcon</h1>

    <div class="hero-bio">
      I am a joint Computer Science Ph.D. and MBA student at Stanford University, advised by <a href="https://www.azaliamirhoseini.com/">Azalia Mirhoseini</a> (<a href="https://scalingintelligence.stanford.edu/">Scaling Intelligence Lab</a>) and <a href="https://cs.stanford.edu/~chrismre/">Christopher R&eacute;</a> (<a href="https://hazyresearch.stanford.edu/">Hazy Research</a>). I am also a Google Student Researcher on the TPU and Gemini teams. My research lies at the intersection of language models and ML systems, with a focus on <strong>intelligence efficiency</strong> for LM training and inference. I work on <strong>commoditizing intelligence</strong>: making AI capabilities dramatically cheaper and more accessible through efficient use of hardware, power, and open-source models, so that language models can be deployed more broadly across society. This agenda spans LMs, ML systems, electrical engineering, and economics, and is anchored by the <a href="https://www.intelligence-per-watt.ai/">Intelligence per Watt</a> project.
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
  <ul class="news-list">
    <li class="news-item">
      <span class="news-date">Jun 2025</span>
      <span class="news-text">Paper accepted.</span>
    </li>
  </ul>
</div>
-->

<div class="section">
  <h2 class="section-title">Selected Publications</h2>
  <ul class="pub-list">
    {% assign sortedPubs = site.categories.papers | sort: 'feature-order' %}
    {% for pub in sortedPubs %}
      {% if pub.featured == true %}
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
      {% endif %}
    {% endfor %}
  </ul>
  <div style="margin-top: 14px;"><a href="/publications" style="font-size: 0.88rem;">View all publications &rarr;</a></div>
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
      <span class="award-name"><span class="award-org">{{ award.name }}</span></span>
      <span class="award-year">{{ award.year }}</span>
    </li>
    {% endfor %}
  </ul>
</div>
```

- [ ] **Step 2: Update `_data/awards.yaml`**

Replace the entire file contents with the new reverse-chronological ordering:

```yaml
- name: Stanford Graduate Fellowship
  year: 2023

- name: Stanford EDGE Fellowship
  year: 2023

- name: "JP Morgan AI/ML Fellowship"
  year: 2023

- name: "GEM PhD Fellowship, National GEM Consortium"
  year: 2023

- name: "Knight-Hennessy Scholarship, Finalist, Stanford University"
  year: 2023

- name: "Gates-Cambridge Scholarship, Bill & Melinda Gates Foundation"
  year: 2023

- name: "Fulbright Scholarship, Research Award, Germany"
  year: 2022

- name: "Summer Venture in Management Program, Harvard Business School"
  year: 2022

- name: "U.N. Millennium Fellowship, United Nations"
  year: 2021

- name: "D.E. Shaw Nexus Fellowship"
  year: 2020

- name: "Stamps President's Scholarship, Georgia Tech"
  year: "2018 - 2022"
```

- [ ] **Step 3: Build and verify homepage**

Run: `cd /Users/jonsaadfalcon/Documents/PersonalWebsite/jonsaadfalcon.github.io && bundle exec jekyll serve --livereload`

Open http://localhost:4000 in a browser. Verify:
- Sticky nav with Home/Publications/CV/Blog
- Hero with photo, role, 2x3 social icons, advisors, mentees
- Bio text with correct formatting
- Selected publications pulled from paper posts
- Invited talks rendered from talks.yaml
- Fellowships & Awards in correct order
- Footer with social icons

- [ ] **Step 4: Commit**

```bash
git add index.md _data/awards.yaml
git commit -m "feat: rebuild homepage with hero, publications, talks, and awards"
```

---

### Task 7: Publications and Blog Pages

Create the Publications and Blog subpages.

**Files:**
- Create: `publications.md`
- Create: `blog.md`

- [ ] **Step 1: Create `publications.md`**

```markdown
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
```

- [ ] **Step 2: Create `blog.md`**

```markdown
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
```

- [ ] **Step 3: Build and verify subpages**

Run: `cd /Users/jonsaadfalcon/Documents/PersonalWebsite/jonsaadfalcon.github.io && bundle exec jekyll serve --livereload`

Open http://localhost:4000/publications in browser. Verify papers are grouped by year.
Open http://localhost:4000/blog in browser. Verify empty state shows.
Click CV in nav. Verify it opens the PDF in a new tab.

- [ ] **Step 4: Commit**

```bash
git add publications.md blog.md
git commit -m "feat: add publications and blog pages"
```

---

### Task 8: Cleanup and Final Verification

Remove unused SCSS files and old includes, verify responsive behavior.

**Files:**
- Delete unused SCSS imports (they are no longer imported in `styles.scss` so they are inert, but clean them up)

- [ ] **Step 1: Verify the full site works**

Run: `cd /Users/jonsaadfalcon/Documents/PersonalWebsite/jonsaadfalcon.github.io && bundle exec jekyll serve --livereload`

Check all pages at http://localhost:4000:
- Home: hero, publications, talks, awards, footer all render correctly
- Publications: papers grouped by year with correct links
- CV: opens PDF in new tab
- Blog: shows empty state
- Responsive: resize browser to < 640px, verify hero stacks vertically, nav compresses, awards stack

- [ ] **Step 2: Add `.superpowers/` to `.gitignore`**

Append to `.gitignore` (create if it doesn't exist):

```
.superpowers/
```

- [ ] **Step 3: Final commit**

```bash
git add -A
git commit -m "chore: cleanup and add .gitignore for superpowers directory"
```
