# BookVault

BookVault is a small project I'm building to keep track of books. Instead of scattered notes or trying to remember which chapter had the moment you liked, i'm gonna try to make sure my site lets you store everything in one place. You can save books, mark the chapters you're obsessed with, and keep personal notes. There's also a search feature so you can look up books, see what they're about, and decide if they match what you're looking for.

---

## Quick Links

- [What This Site Is For](#what-this-site-is-for)  
- [Tools (Work in Progress)](#tools-work-in-progress)  
- [Books Covered](#books-covered)  
- [Who This Is For](#who-this-is-for)  
- [Pages Used in This Project](#pages-used-in-this-project)  
- [Features](#features)  
- [Current Content](#current-content)  
- [Visual Style](#visual-style)  
- [Planned Page Layouts](#planned-page-layouts)  
- [Roadmap](#roadmap)  
- [Website Testing](#website-testing)  
- [Deployment](#deployment)  
- [UX](#ux)  
- [HTML Bug Report](#html-bug-report)  
- [CSS Bug Report](#css-bug-report)  
- [JS Bug Report](#js-bug-report)  
- [Expectations vs Actual Outcomes](#expectations-vs-actual-outcomes)  
- [Project Purpose](#project-purpose)  
- [Automated Testing](#automated-testing)  
- [External Code Attribution](#external-code-attribution)  
- [Disclaimer](#disclaimer)  
- [CSS Validation](#css-validation)  
- [Manual Testing](#manual-testing)
  

---

## What This Site Is For

The goal is to keep everything simple. Each page focuses on one aspect of the site such as one page being focused on the page you bookmarked in your book, further additions to the site will include the usage of a login anjd sign up page.

---

## Tools (Work in Progress)

- Chapter tracker  
- Quote and notes storage  
- Reading status section  
- Book search (summary + basic info)  

Might be reworked and tested on later.

---

## Books Covered

The project starts with general book tracking and for search results. More features may be added later if they make sense for the way people use the site.

---

## Who This Is For

Readers who want to keep track of their current reading progress, while maintaing a clean work area, ensuring a more organised and clearer enjoyment for the books people love .

---

## Pages Used in This Project

The site is built using four main HTML pages:

- **index.html** – Homepage with a short intro and links to the rest of the site  
- **add.html** – Add a new book with notes, quotes, and chapter info  
- **library.html** – View all saved books  
- **search.html** – Look up books and check summaries, genres, and basic details  

Each page is kept simple and focused. The goal is to make it easy for readers to find what they need without clutter or distractions.

---

## Features

### Current Features

- Clean, minimal UI  
- Responsive layout  
- Navigation across all pages  
- Add and store books locally  
- Save favourite chapters and notes  
- Basic search functionality using an external API  
- Simple card layout for book entries  

---

## Current Content

The main focus right now is getting the core features working: storing books, displaying them cleanly, and making the search page functional. More detailed layouts and styling will be added once the main logic is stable.

---

## Visual Style

The design is intentionally simple. Clear typography, readable spacing, and a layout that doesn’t get in the way. The goal is to make the content — your notes and your books — the main focus.

---

## Planned Page Layouts

- Cleaner book details page with space for chapter notes  
- More structured search results page  
- Optional dark mode  
- Improved navigation layout  

---

## Roadmap

- User accounts  
- Better search filters  
- Reading progress tracker  
- Recommendations based on saved books  
- Import/export book lists  

---

## Website Testing

Testing will cover layout consistency, form validation, search accuracy, and general responsiveness across devices.

---

## Deployment

Deployment will happen once the core features are stable and the UI is consistent across pages.

---

## UX

The UX goal is to keep everything obvious: clear buttons, simple forms, and pages that explain themselves without extra text.

---
### HTML Bugs

| Bug | Root Cause | Fix |
|-----|------------|------|
| CSS not loading on Add Book page | Linked to `assets/style.css` instead of `assets/css/style.css` | Updated `<link>` path to correct folder |
| Navigation list not rendering correctly | Used `<li>` elements without wrapping them in a `<ul>` | Replaced loose `<li>` tags with a proper `<ul>` structure |
| Panels not switching on auth page | Missing `hidden` class on some panels | Added `class="hidden"` to inactive panels |
| Search page layout breaking | Forgot to close a `<div>` around the search container | Closed the missing tag and re‑indented the section |
| Library page not showing book cards | Template ID was correct but JS was targeting the wrong container ID | Updated JS to use `bookList` (matching HTML) |
| Textarea not styled | Forgot to add class name to `<textarea>` | Added `class="notes-box"` to match CSS |



---

### CSS Bugs

| Bug | Root Cause | Fix |
|-----|------------|------|
| Blossom background not applying | Body was missing `class="sakura-bg"` on some pages | Added the class to all HTML pages |
| Buttons looked inconsistent | Some pages used raw `<button>` styles instead of `.btn-sakura` | Replaced default buttons with `.btn-sakura` |
| Navigation bar spacing uneven | Forgot to reset default `<ul>` padding on search page | Added `ul { padding: 0; margin: 0; list-style: none; }` |
| Soft card shadow too strong | Shadow value was copied from an earlier test | Reduced blur and opacity for a calmer look |
| Grid layout collapsing on mobile | `minmax()` value too large for small screens | Adjusted to `minmax(180px, 1fr)` |
| Textarea overflowing container | No width rule applied to `.notes-box` | Added `width: 100%` and matching padding |


---

## JS Bug Report

Search errors, form handling bugs, or data not saving/displaying correctly.

| Bug | Root Issue | How I Fixed It |
|-----|------------|----------------|



---

## Expectations vs Actual Outcomes

This section will document what features were planned, what changed during development, and what ended up working better than expected.

---

## Project Purpose

The purpose is to build a small, personal tool that solves a real problem: keeping track of books in a way that feels natural and not bloated.

---

## Automated Testing

Will be added later once the main logic is stable.

---

## External Code Attribution

Any external libraries, snippets, or API usage will be listed here.

---

## Disclaimer

This is a personal project and not affiliated with any book publishers or APIs used.

---

## CSS Validation

Notes from W3C validation checks.

---

## Manual Testing

Manual checks across different devices, browsers, and screen sizes.
