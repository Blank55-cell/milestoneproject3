# BookVault

BookVault is a small project I'm building to keep track of books. Instead of scattered notes or trying to remember which chapter had the moment you liked, this site lets me store everything in one place. I can save books, mark the chapters I'm obsessed with, and keep personal notes. There’s also a search feature so I can look up books, see what they’re about, and decide if they match what I’m looking for.

---

# Wireframes

I used Whimsical to plan the layout and user flow for BookVault. This helped me map out how the authentication flow connects to the main library and search features before I started coding.

- [Interactive Whimsical Board](https://whimsical.com/project-314/project3-SvbFMeGhZ2RBvFT4ScK62Z)

---

# Quick Links

- [Wireframes](#wireframes)
- [What This Site Is For](#what-this-site-is-for)  
- [User Stories](#user-stories)  
- [Tools (Work in Progress)](#tools-work-in-progress)  
- [Who This Is For](#who-this-is-for)  
- [Pages Used in This Project](#pages-used-in-this-project)  
- [Features](#features)  
- [Website Testing](#website-testing)  
- [JSLint Testing](#jslint-testing)  
- [Google Lighthouse Testing](#google-lighthouse-testing)  
- [Python Linter Testing](#python-linter-testing)  
- [Deployment](#deployment)  
- [HTML Bugs](#html-bugs)  
- [CSS Bugs](#css-bugs)  
- [JS Bug Report](#js-bug-report)  
- [SQLite / Database Bugs](#sqlite--database-bugs-i-ran-into)  
- [Python / Django Bugs](#python--django-bugs-i-ran-into)  
- [Manual Testing](#manual-testing)
- [External Code Attribution](#external-code-attribution)  
- [Disclaimer](#disclaimer)  

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

---

# Tools (Work in Progress)

- Chapter tracker  
- Quote and notes storage  
- Reading status section  
- Book search (summary + basic info)  

---

# Who This Is For

Readers who want to keep track of their current reading progress while maintaining a clean work area, ensuring a more organised and clearer enjoyment for the books they love.

---

# Pages Used in This Project

- **home.html** – The main dashboard and entry point.  
- **account.html** – User profile and settings.  
- **add_book.html** – Form to add a new book to the database.  
- **library.html** – Displaying all saved books.  
- **search.html** – Searching for new books and checking summaries.  
- **books_details.html** – Viewing specific saved notes and chapter progress.  

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

# Website Testing

### Validation Results
| Feature | Tool | Image |
| --- | --- | --- |
| HTML | [Nu HTML Checker](https://validator.w3.org/) | ![HTML Validation](testing/htmlvalidation/htmlvalidation.png) |
| JavaScript | [JSHint](https://jshint.com/) | ![JS Validation](testing/jslint/javascriptlint.png) |
| Performance | [Lighthouse](https://developers.google.com/web/tools/lighthouse) | ![Lighthouse Score](testing/lighthouse/signinlighthouse.png) |
| Python | [CI Python Linter](https://pep8ci.herokuapp.com/) | ![Python Linter](testing/pythonlint/bookviewstest.png) |
| CSS | [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) | ![CSS Validation](testing/cssvalidation/cssvalidator.png) |

---

# JSLint Testing

I used JSHint to check my JavaScript for any syntax errors or missing parts.

![JS Validation Results](testing/jslint/javascriptlint.png)

- **What I found:** The linter caught a few missing semicolons and some variables that weren't properly defined.
- **What I fixed:** I went through and added the missing semicolons and made sure all variables were declared correctly so the code runs more reliably.

---

# Google Lighthouse Testing

I ran Lighthouse in Chrome DevTools to see how the site performs and if it's easy for everyone to use.

![Lighthouse Results](testing/lighthouse/signinlighthouse.png)

**What I focused on:**
- **Performance:** Making sure book covers don't slow down the page load.
- **Accessibility:** Checking that text is easy to read against the background and adding alt text to images.
- **Best Practices:** Making sure all links are secure.

---

# Python Linter Testing

I ran my Django files through the PEP8 linter to make sure the code is clean and follows standard Python formatting.

![Python Linter Results](testing/pythonlint/bookviewstest.png)

- **Results:** No errors found in the final version of the code.
- **What I fixed:** I had to shorten some long lines in `views.py` and clear out extra spaces in `models.py` to get it to pass perfectly.

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

# Deployment

The project is hosted on Railway. It’s set up to automatically deploy whenever I push my code changes to GitHub.

---

# Manual Testing

I tested the site manually on different screens to make sure the layout looks right everywhere. I also checked that the database connects properly whether I’m working locally on my MSI Crosshair or checking the live site.

---

# External Code Attribution

- Google Books API for pulling in book details and covers.
- Django Documentation for help with the database and views.

---

# Disclaimer

This is a personal student project and isn't affiliated with any book publishers or the APIs used.