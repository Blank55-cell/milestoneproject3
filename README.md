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
| Forgot Password Link Not Working | The JS looked for `linkForgot` but the HTML used a different ID, so `getElementById()` returned null | Matched the JS ID to the HTML so the event listener attached correctly |
| Login/Register Buttons Throwing Null Errors | VS Code showed “Cannot read properties of null (reading 'onclick')” because the HTML IDs didn’t match the JS (`loginPanel`, `registerPanel`) | Updated the HTML IDs to match the JS naming |
| Reset Panel Never Opening | `resetLink` didn’t exist on most pages, so the event listener silently failed | Wrapped the listener in optional chaining (`?.addEventListener`) so it only runs when the element exists |
| Back Buttons Not Responding | The HTML was missing the IDs `backToLogin` and `resetBack`, so the JS references pointed to null | Added the correct IDs to the HTML buttons |
| Panels Flashing on Page Load | Panels didn’t start with the `hidden` class, so they were visible before JS ran | Added `class="hidden"` to all non‑default panels |
| Console Errors on Pages Without Auth UI | JS ran globally, but some pages didn’t contain the panel elements | Wrapped all event listeners in optional chaining to avoid null reference errors |
| Register Button Opening Wrong Panel | The Register button had the wrong ID in the HTML (`registerBtn` instead of `navRegister`) | Updated the HTML to use the correct ID |
| Hidden Class Not Working | Another stylesheet overrode `.hidden`, so `display: none` didn’t apply | Ensured `.hidden { display: none; }` was defined globally and not overridden |



---



## SQLite / Database Bugs I Ran Into

| Bug ID | What Happened | Why It Happened | Fix |
|--------|----------------|------------------|------|
| S001 | Tables didn’t exist when running the server | I forgot to run migrations after creating models | Ran `makemigrations` + `migrate` |
| S002 | Foreign key error when saving a book | Book model requires user_id but I wasn’t passing a user | Added `user=request.user` in add_book view |
| S003 | Category relationships didn’t save | I created the BookCategory model but never added logic to save categories | Added logic to create BookCategory entries |
| S004 | Database kept old fields after I changed models | SQLite doesn’t auto‑update schema | Deleted db.sqlite3 and migrations, then recreated them |
| S005 | Duplicate categories appeared | I didn’t enforce unique names in Category | Added `unique=True` to Category.name |
| S006 | Search queries were slow | I used `icontains` on a large table without indexing | Added an index on title field |
| S007 | Wrong data types in DBML vs Django | I used varchar in DBML but Django uses CharField | Updated DBML to match Django’s field types |
| S008 | BookCategory table didn’t enforce uniqueness | I forgot to add a unique constraint on (book, category) | Added `unique_together = ('book', 'category')` |

---

## Python / Django Bugs I Ran Into

| Bug ID | What Happened | Why It Happened | Fix |
|--------|----------------|------------------|------|
| P001 | Adding a book crashed with “NOT NULL constraint failed: books.user_id” | My Book model requires a user FK, but my add_book view didn’t pass request.user | Added `user=request.user` when creating the Book |
| P002 | Login page broke with “AttributeError: module 'accounts.views' has no attribute 'login_view'” | I referenced login_view in urls.py but never actually created the function | Added a proper login_view function in accounts/views.py |
| P003 | Library page showed everyone’s books | I used `Book.objects.all()` instead of filtering by the logged‑in user | Changed it to `Book.objects.filter(user=request.user)` |
| P004 | Search returned books from other users | Same issue — I forgot to filter by user in the search view | Updated search to filter by both user and title |
| P005 | Django complained about 18 unapplied migrations | I added new models but never ran makemigrations/migrate | Ran `python manage.py makemigrations` and `python manage.py migrate` |
| P006 | Server crashed after removing settings.py from Git | Git removed the file from disk, not just from tracking | Restored it using `git checkout -- bookvault/settings.py` |
| P007 | “TemplateDoesNotExist” error on /add/ | I forgot to create add_book.html in templates | Added the missing template file |
| P008 | “Reverse for 'library' not found” | My redirect used a URL name that didn’t exist | Added the correct name in urls.py |


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
