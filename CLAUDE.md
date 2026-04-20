# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Personal academic portfolio website for Jon Saad-Falcon, built with Jekyll and hosted on GitHub Pages at jonsaadfalcon.com.

## Build & Serve Commands

```bash
bundle install          # Install Ruby dependencies
bundle exec jekyll serve --livereload   # Serve locally with live reload (also: npm start)
bundle exec jekyll build                # Build site to _site/
```

## Architecture

**Static site generator:** Jekyll (latest from GitHub), using Kramdown with GFM for markdown and Rouge for syntax highlighting.

**Content is data-driven.** Most CV and site content lives in `_data/` as YAML files (awards, education, experiences, papers, people, press, skills, social links, etc.). Templates in `_includes/cv/` render these data files into the CV page. Editing content usually means editing YAML, not HTML.

**Publications** are Jekyll posts in `_posts/papers/`. Each paper has extensive front matter (title, authors, venue, links, featured flag, paper-order). Papers with `featured: true` appear on the homepage. The `paper.html` layout renders individual paper pages with author info, material links, and BibTeX.

**Layout hierarchy:** `default.html` is the base layout (header + footer). `home.html` is a special layout without the header. `page.html`, `post.html`, `paper.html`, and `cv.html` extend default.

**Styling:** Custom SCSS in `_sass/` (no CSS framework). Key variables in `_variables.scss`. Responsive breakpoint at 768px (`$mobile`). Uses Google Fonts "Gaegu" and Font Awesome 5.5.0 via CDN. Output is compressed CSS.

**Minimal JavaScript.** Only `_includes/js/scripts.js`, conditionally loaded on the CV page via the `jsarr` front-matter variable.
