# BookVault

BookVault is a small project I'm building to keep track of books. Instead of scattered notes or trying to remember which chapter had the moment you liked, this site lets me store everything in one place. I can save books, mark the chapters I'm obsessed with, and keep personal notes. There’s also a search feature so I can look up books, see what they’re about, and decide if they match what I’m looking for.

---

# Quick Links

- [What This Site Is For](#what-this-site-is-for)  
- [User Stories](#user-stories)  
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
- [JSLint Testing](#jslint-testing)  
- [Google Lighthouse Testing](#google-lighthouse-testing)  
- [Python Linter Testing](#python-linter-testing)  
- [Deployment](#deployment)  
- [UX](#ux)  
- [HTML Bugs](#html-bugs)  
- [CSS Bugs](#css-bugs)  
- [JS Bug Report](#js-bug-report)  
- [SQLite / Database Bugs](#sqlite--database-bugs-i-ran-into)  
- [Python / Django Bugs](#python--django-bugs-i-ran-into)  
- [Expectations vs Actual Outcomes](#expectations-vs-actual-outcomes)  
- [Project Purpose](#project-purpose)  
- [Automated Testing](#automated-testing)  
- [External Code Attribution](#external-code-attribution)  
- [Disclaimer](#disclaimer)  
- [CSS Validation](#css-validation)  
- [Manual Testing](#manual-testing)

---

# What This Site Is For

The goal is to keep everything simple. Each page focuses on one aspect of the site such as one page being focused on the page I bookmarked in my book. Further additions to the site will include the usage of a login and sign‑up page.

---

# User Stories

These are written in a natural tone to reflect how I actually use the site.

- As someone who reads a lot, I want a place to save the books I’m working through so I don’t forget the chapters or notes that matter to me.  
- I want to quickly check the books I’ve saved so I can pick up where I left off.  
- I want to search for books online so I can see summaries before deciding to add them.  
- I want to store my favourite chapters so I can revisit the parts I enjoyed.  
- I want to write notes about each book so I don’t lose track of important details.  
- I want to delete books I no longer need so my library stays tidy.  
- I want a simple details page so I can see everything I’ve saved about a book in one place.  
- I want book covers to appear in my library so it feels more visual and easier to browse.  

---

# Tools (Work in Progress)

- Chapter tracker  
- Quote and notes storage  
- Reading status section  
- Book search (summary + basic info)  

---

# Books Covered

The project starts with general book tracking and search results. More features may be added later if they make sense for the way people use the site.

---

# Who This Is For

Readers who want to keep track of their current reading progress while maintaining a clean work area, ensuring a more organised and clearer enjoyment for the books they love.

---

# Pages Used in This Project

- **index.html** – Homepage  
- **add.html** – Add a new book  
- **library.html** – View all saved books  
- **search.html** – Look up books and check summaries  

---

# Features

### Current Features

- Clean, minimal UI  
- Responsive layout  
- Navigation across all pages  
- Add and store books  
- Save favourite chapters and notes  
- Basic search functionality using an external API  
- Simple card layout for book entries  
- Book covers pulled from Google Books  
- Details page for each book  
- Delete functionality  

---

# Current Content

The main focus right now is getting the core features working: storing books, displaying them cleanly, and making the search page functional.

---

# Visual Style

The design is intentionally simple. Clear typography, readable spacing, and a layout that doesn’t get in the way.

---

# Planned Page Layouts

- Cleaner book details page  
- More structured search results  
- Optional dark mode  
- Improved navigation layout  

---

# Roadmap

- User accounts  
- Better search filters  
- Reading progress tracker  
- Recommendations  
- Import/export book lists  

---

# Website Testing

This section is where I keep track of all the testing I’ve done across the site, including layout checks, form behaviour, and how the site responds on different devices and browsers.

---

# JSLint Testing

This is where I record the results from running my JavaScript through JSLint.  
I’ll add the actual output here once I finish testing.

Things I plan to note:

- Any warnings or errors JSLint picked up  
- What I fixed afterwards  
- Anything I intentionally ignored and why  

---

# Google Lighthouse Testing

This section is for my Lighthouse results from Chrome DevTools.  
I’ll paste the scores and screenshots here once I run the tests.

I’ll be tracking:

- Performance  
- Accessibility  
- Best Practices  
- SEO  
- Any improvements I made based on Lighthouse suggestions  

---

# Python Linter Testing

This is where I’ll store the results from running a Python linter (flake8 or pylint) on my Django code.

I’ll be noting:

- Error count  
- Warnings  
- Style issues  
- What I fixed  
- Anything I left as‑is and the reason  

---

# Deployment

Deployment will happen once the core features are stable.

---

# UX

The UX goal is to keep everything obvious: clear buttons, simple forms, and pages that explain themselves.

---

# HTML Bugs

| Bug | Root Cause | Fix |
|-----|------------|------|
| CSS not loading on Add Book page | Wrong path | Updated `<link>` path |
| Navigation list not rendering | `<li>` without `<ul>` | Wrapped in `<ul>` |
| Panels not switching | Missing `hidden` class | Added class |
| Search layout breaking | Missing closing `<div>` | Closed tag |
| Library not showing cards | JS targeted wrong ID | Updated JS |
| Textarea not styled | Missing class | Added `.notes-box` |

---

# CSS Bugs

| Bug | Root Cause | Fix |
|-----|------------|------|
| Blossom background missing | Missing `sakura-bg` class | Added class |
| Button inconsistency | Raw `<button>` used | Replaced with `.btn-sakura` |
| Nav spacing uneven | Default `<ul>` padding | Reset padding |
| Shadow too strong | Old test value | Reduced blur |
| Grid collapsing | `minmax()` too large | Adjusted value |
| Textarea overflow | No width rule | Added `width: 100%` |

---

# JS Bug Report

| Bug | Root Issue | Fix |
|-----|------------|----------------|
| Forgot Password link broken | Wrong ID | Matched IDs |
| Login/Register null errors | HTML IDs didn’t match JS | Updated IDs |
| Reset panel not opening | Missing element | Optional chaining |
| Back buttons not responding | Missing IDs | Added IDs |
| Panels flashing | Missing `hidden` class | Added class |
| Errors on pages without auth UI | JS ran globally | Optional chaining |
| Register button wrong panel | Wrong ID | Updated HTML |
| Hidden class overridden | CSS conflict | Ensured global `.hidden` |

---

# SQLite / Database Bugs I Ran Into

| Bug ID | What Happened | Why | Fix |
|--------|----------------|------|------|
| S001 | Tables missing | Forgot migrations | Ran migrations |
| S002 | FK error | Missing user | Added `user=request.user` |
| S003 | Categories not saving | No logic | Added logic |
| S004 | Old fields remained | SQLite doesn’t auto‑update | Deleted DB + migrations |
| S005 | Duplicate categories | No unique constraint | Added `unique=True` |
| S006 | Slow search | No index | Added index |
| S007 | DBML mismatch | Wrong types | Updated DBML |
| S008 | Duplicate BookCategory | No constraint | Added `unique_together` |

---

# Python / Django Bugs I Ran Into

| Bug ID | What Happened | Why It Happened | Fix |
|--------|----------------|------------------|------|
| P001 | “NOT NULL constraint failed: books.user_id” | Didn’t pass user | Added `user=request.user` |
| P002 | Login page crashed | Referenced missing view | Added login_view |
| P003 | Library showed all books | Used `.all()` | Filtered by user |
| P004 | Search returned other users’ books | Forgot filter | Added filter |
| P005 | 18 unapplied migrations | Forgot to migrate | Ran migrations |
| P006 | settings.py removed | Git removed file | Restored via checkout |
| P007 | Template missing | Forgot file | Added template |
| P008 | “Reverse for 'library' not found” | Wrong URL name | Fixed URL |
| P009 | 405 Method Not Allowed | Form submitted without proper POST handling | Ensured POST + CSRF |
| P010 | Books not appearing after POST | Template had no loop | Added `{% for book in books %}` |
| P011 | Silent failure saving books | Old migrations created NOT NULL field | Deleted migrations + recreated |
| P012 | NoReverseMatch: 'book_details' not found | URL/view/template missing | Added URL + view + template |
| P013 | Details button did nothing | It was a `<button>` with no link | Replaced with `<a href>` |
| P014 | Delete didn’t work | No delete view/URL | Added delete_book |

---

# Expectations vs Actual Outcomes

This section is where I compare what I originally planned with what actually ended up working or changing during development.

---

# Project Purpose

A small, personal tool to track books in a clean, simple way.

---

# Automated Testing

Will be added later once the main logic is stable.

---

# External Code Attribution

Any external libraries or snippets will be listed here.

---

# Disclaimer

This is a personal project and not affiliated with any book publishers or APIs used.

---

# CSS Validation

Notes from W3C validation checks.

---

# Manual Testing

Manual checks across devices and browsers.
