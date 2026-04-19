# Website Redesign — Design Spec

## Overview

Complete redesign of jonsaadfalcon.com (Jekyll, GitHub Pages) from the current Gaegu-font academic site to a polished, Georgia-serif site with Forest Mint accent. Targeting dual audience: faculty hiring committees and investors/industry.

## Design Decisions

### Typography
- **Font:** Georgia (system serif, no web font loading)
- **Headings:** Georgia, 700 weight, -0.01em tracking
- **Body:** Georgia, 0.92rem, line-height 1.75
- **Fluid sizing:** `clamp()` for responsive headings (e.g., `clamp(1.5rem, 2.5vw + 0.8rem, 1.9rem)`)

### Color Palette
- **Accent:** Forest Mint `#2E7D6F`
- **Accent hover:** `#246858`
- **Highlight background:** `#E8F5F0`
- **Accent border (links):** `rgba(46, 125, 111, 0.3)`
- **Body text:** `#222`
- **Secondary text:** `#555`
- **Muted text:** `#888`
- **Background:** `#ffffff`
- **Borders:** `#e8e8e8` (standard), `#f0f0f0` (light)

### Link Style
- Color: `--accent` with 1px bottom border at `--accent-border` opacity
- Hover: darker accent + solid border
- Pub/code links use sans-serif font-family at 0.78rem for contrast

## Site Structure

### Navigation
- **Sticky nav bar** with frosted glass effect (`backdrop-filter: blur(8px)`)
- Left: "Jon Saad-Falcon" (links to home)
- Right: **Home | Publications | CV | Blog**
- CV links directly to PDF (opens in new tab with external-link icon)
- Active tab highlighted in accent color + 600 weight

### Pages

#### 1. Home (`index.md`, layout: `home`)
Sections in order:

1. **Hero** — two-column grid (`clamp(160px, 22vw, 210px)` left / `1fr` right)
   - **Left column (stacked, centered):**
     - Profile photo (14px border-radius, shadow)
     - "Computer Science Ph.D. & MBA Candidate / Stanford University" (0.74rem)
     - 2x3 social icon grid (38x38px, 9px border-radius): Scholar (Academicons `ai-google-scholar`), LinkedIn, Twitter/X, GitHub, Email, CV
     - Advisors section (bold label, comma-separated linked names)
     - Current Mentees (same format, names linked where available)
     - Past Mentees (same format, with parenthetical destinations)
   - **Right column:**
     - Name as h1
     - Bio paragraph 1: Position, advisors (linked), Google SR, research focus (LMs x ML systems, intelligence efficiency, commoditizing intelligence), IPW project link
     - Bio paragraph 2: Doctoral fellowships (Stanford Graduate, JP Morgan AI/ML, EDGE, GEM), post-grad scholarships (Fulbright, Gates-Cambridge), background (AI2, Georgia Tech, Stamps)
     - Supporters line: "My research is generously supported by Stanford HAI, Laude Institute, Lambda Labs, Ollama, and IBM Research."

2. **Announcement Bubble** — commented out, CSS commented out. Mint background, 3px left accent border. Ready to uncomment for job market / recruiting announcements.

3. **News Timeline** — commented out, CSS commented out. Grid layout with 90px date column. Ready to uncomment.

4. **Selected Publications** — 5 featured papers. Each shows: title (600 weight), authors (your name bolded), venue (italic, muted), paper/code links. "View all publications →" link to Publications page.

5. **Invited Talks** — Audrey-style. Talk title in quotes, bulleted venue list underneath with location and date. Grouped by talk topic.

6. **Fellowships & Awards** — Two-column grid: name+org on left, year on right. Reverse chronological: PhD fellowships (Stanford Graduate, EDGE, JP Morgan, GEM PhD, Knight-Hennessy Finalist), post-grad (Gates-Cambridge, Fulbright), undergrad (Harvard SVMP, U.N. Millennium, D.E. Shaw, Stamps). Donald V. Jackson commented out.

7. **Footer** — centered social icons (muted, hover to accent) + copyright.

#### 2. Publications (`publications.md`, layout: `page`)
- Page title + subtitle
- All papers grouped by year (2025, 2024, 2023, 2022, 2021, 2020)
- Year headings in accent color with accent-light bottom border
- Full author lists, venue with award highlights (Oral, Best Poster in gold `#b8860b`)
- Paper/code/demo/video links per paper

#### 3. CV
- Nav link opens `/cv.pdf` in new tab
- No separate HTML page
- PDF to be redesigned separately (Shreya Shankar's clean format + Audrey Cheng's comprehensive sections)
- Target sections for CV PDF: Education, Research Experience, Publications, Awards & Honors, Invited Talks, Teaching, Mentorship (Graduate/Undergraduate), Academic Service, Leadership & Community Engagement

#### 4. Blog (`blog.md`, layout: `page`)
- Simple reverse-chronological post list
- Each post: title (linked), date, excerpt
- Will be populated with paper blog posts
- Empty state: pencil icon + "Posts coming soon"

### Responsive Behavior
- Breakpoint at 640px
- Hero collapses to single column, photo centered at 200px width
- Nav links reduce gap to 16px
- Award items stack vertically

## Technical Approach

### Stack
- **Jekyll** (existing setup, GitHub Pages native)
- **SCSS** for styling (existing `_sass/` architecture)
- **Font Awesome 6.5** (CDN) + **Academicons** (CDN) for icons
- No JS frameworks; minimal vanilla JS (nav active state, potential hamburger menu)

### Implementation Strategy
1. Create new SCSS variables file with the color/font system
2. Rebuild layouts: `default.html`, `home.html`, `page.html`
3. Rebuild includes: `head.html`, `header.html`, `footer.html`, new `social-icons.html`
4. Add new data files as needed (talks, mentees)
5. Update `index.md` with new bio content
6. Create `publications.md` page
7. Create `blog.md` page
8. Update `_config.yml` if needed
9. Test locally with `bundle exec jekyll serve --livereload`

### Data Files Needed
- `_data/talks.yaml` — invited talks (title, venues with location/date)
- `_data/mentees.yaml` — current mentees: Hangoo Kang, Hannah Gao, Harsh Singh, Matthew Hart, Orhun Akengin, Tanvir Bhathal, Tarun Suresh. Past mentees: Adrian Lafuente Gamarra (Salesforce), Brendan McLaughlin (Reflection AI), Herumb Shandilya (Mixed Bread), Robby Manihani (Pace), Wes Griffin (Stanford)
- Existing files to keep: `awards.yaml`, `social-links.yaml`, `education.yaml`, `experiences.yaml`, `people.yaml`

### Files to Create/Modify
- **Create:** `_sass/_variables-new.scss`, `_sass/_nav.scss`, `_sass/_hero.scss`, `_sass/_publications.scss`, `_sass/_talks.scss`, `_sass/_awards.scss`
- **Modify:** `_layouts/default.html`, `_layouts/home.html`, `_includes/head.html`, `_includes/header.html`, `_includes/footer.html`, `index.md`, `styles.scss`, `_config.yml`
- **Create:** `publications.md`, `blog.md`
- **Remove from nav:** `cv.md` HTML page (keep PDF), Code page

## Reference Mockup
The approved mockup is at `.superpowers/brainstorm/28052-1776614274/content/all-pages-mockup-v2.html`

## Design Inspirations
- **Primary:** Shreya Shankar (sh-reya.com) — section structure, mentee display, clean hierarchy
- **Secondary:** Nicholas Carlini (nicholas.carlini.com) — typographic identity, serif font, accent color
- **Tertiary:** Audrey Cheng (audreyccheng.com) — fluid typography, news timeline, awards section, talks format
- **Tertiary:** Sewon Min (sewonmin.com) — collapsible info boxes, clean navigation

## Style Notes
- No em-dashes anywhere; use commas, periods, semicolons, colons, or parentheses instead
- "commoditizing intelligence" is bolded in the bio
- "language models and ML systems" is plain text (not bold, not italic)
- Supporters line is slightly smaller (0.85rem) and secondary-colored

## Out of Scope (separate tasks)
- CV PDF redesign (Shreya format + Audrey sections)
- Blog post content creation
- Actual talk data verification
