# BookVault

BookVault is a small project I'm building to keep track of books. Instead of scattered notes or trying to remember which chapter had the moment you liked, this site lets me store everything in one place. I can save books, mark the chapters I'm obsessed with, and keep personal notes. There’s also a search feature so I can look up books, see what they’re about, and decide if they match what I’m looking for.

---

# Wireframes

I used Whimsical to plan the layout and user flow for BookVault. This helped me map out how the authentication flow connects to the main library and search features before I started coding.

- [Interactive Whimsical Board](https://whimsical.com/project-314/project3-SvbFMeGhZ2RBvFT4ScK62Z)

---


# Quick Links

- [Live Website](#live-website-link)
- [Wireframes](#wireframes)
- [What This Site Is For](#what-this-site-is-for)  
- [User Stories](#user-stories)  
- [Tools (Work in Progress)](#tools-work-in-progress)  
- [Who This Is For](#who-this-is-for)  
- [Pages Used in This Project](#pages-used-in-this-project)  
- [Features](#features)  
- [Website Testing](#website-testing)  
- [HTML Testing](#html-testing)
- [JSLint Testing](#jslint-testing)  
- [Google Lighthouse Testing](#google-lighthouse-testing)  
- [Python Linter Testing](#python-linter-testing)  
- [Deployment](#deployment)  
- [HTML Bugs](#html-bugs)  
- [Database ERD](#database-schema-erd)
- [CSS Bugs](#css-bugs)  
- [JS Bug Report](#js-bug-report)  
- [SQLite / Database Bugs](#sqlite--database-bugs-i-ran-into)  
- [Python / Django Bugs](#python--django-bugs-i-ran-into)  
- [Manual Testing](#manual-testing)
- [External Code Attribution](#external-code-attribution)  
- [Disclaimer](#disclaimer)  
- [Responsive Design Testing](#responsive-design-testing)

---

# What This Site Is For

The goal is to keep everything simple. Each page focuses on one aspect of the site such as one page being focused on the page I bookmarked in my book. Further additions to the site will include the usage of a login and sign‑up page.

---

# Database Schema (ERD)

To keep the structure of BookVault clear, I created an ERD that shows how the main tables connect — Books, Categories, Reviews, and Users. This helped me visualise how everything fits together before building the database models.

**ERD Diagram:**  
https://dbdiagram.io/d/dbforbooks-69e236a0a5db712fe57b2e96

The diagram shows the relationships between users, their saved books, the categories linked to those books, and any reviews added. It also reflects the many‑to‑many setup between books and categories.




---

# Deployment 

Follow these steps to clone the project and run it locally.

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR-USERNAME/milestoneproject3.git
```

### 2. Navigate Into the Project Folder
```bash
cd milestoneproject3
```

### 3. Create a Virtual Environment
```bash
python -m venv venv
```

### 4. Activate the Virtual Environment
**Windows:**
```bash
venv\Scripts\activate
```

**macOS / Linux:**
```bash
source venv/bin/activate
```

### 5. Install All Required Packages
```bash
pip install -r requirements.txt
```

### 6. Apply Migrations
```bash
python manage.py migrate
```

### 7. Run the Development Server
```bash
python manage.py runserver
```

### 8. Open the Website 
Visit:

http://127.0.0.1:8000



## Cloud Deployment Procedure (Railway)

This project is fully configured to deploy straight to the cloud using Railway. Use this procedure to take your application live:

### 1. Prepare Configuration Variables
Ensure your Django project variables are protected in production. Your live configuration must pull sensitive data from environment values rather than hardcoded strings (e.g., `SECRET_KEY`, `DEBUG = False`, and database connection strings).

### 2. Connect the Project to Railway
1. Log into your **Railway.app** account dashboard via GitHub authorization.
2. Click **New Project** in the upper-right corner of the interface.
3. Choose **Deploy from GitHub repo** and select your project repository from the listing.

### 3. Configure Production Environment Variables
Once the repository link completes initialization, open the service dashboard, navigate to the **Variables** tab, and populate your required keys:
* `SECRET_KEY` = *Your secure application production key*
* `DEBUG` = `False`
* `DATABASE_URL` = *Automatically configured by Railway if a Database service is attached*

### 4. Trigger Deployment Syncs
Railway listens for updates automatically on your linked branch. When you want to push updates to your live site, simply execute your standard Git tracking terminal commands:
```bash
git add .
git commit -m "chore: deployment updates and configuration fixes"
git push




```

---



# Responsive Design Testing

To ensure the user interface provides an optimal viewing and interactive experience, the application was rigorously tested across multiple devices and viewport screens using native mobile layouts and browser developer emulation tools.

### Desktop Viewports
* **Target Layouts:** Standard 1080p Monitors, Laptops (13" to 15")
* **Observations:** The navigation links align horizontally with comfortable spacing, and the layout features a structured multi-column layout for books and detailed summaries.

---

### Tablet Viewports
* **Target Layouts:** iPad Air, iPad Mini, Generic 10" Tablets
* **Observations:** Structural layout components dynamically rescale widths gracefully. Elements wrap into streamlined vertical structures where space is restricted, preventing any overflow clipping.


---

### Mobile Viewports
* **Target Layouts:** iPhone 13/14/15, Samsung Galaxy S22/S23, Small Viewports (up to 320px)
* **Observations:** Form fields, interactive action buttons, and text input sections dynamically resize to occupy full container fluid widths for easy thumb interaction. The navigation bar switches seamlessly into an easy-to-read vertical structure.










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

## HTML Testing

All HTML files in BookVault were validated using the **Nu HTML Checker**.  
Each page was tested after adding semantic headings and accessibility improvements.  
Below are the validation results for each template.

### Home Page  
![Home Page HTML Test](testing/htmlvalidation/htmlvalidation.png)

### Add Book Page  
![Add Book HTML Test](testing/htmlvalidation/addbook.png)

### Edit Book Page  
![Edit Book HTML Test](testing/htmlvalidation/editbook.png)

### Register Page  
![Register HTML Test](testing/htmlvalidation/register.png)

### Sign In Page  
![Sign In HTML Test](testing/htmlvalidation/signin.png)

### Library Page  
![Library HTML Test](testing/htmlvalidation/library.png)

### Search Page  
![Search HTML Test](testing/htmlvalidation/search.png)





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
![Lighthouse Results](testing/lighthouse/searchpagelighthouse.png)
![Lighthouse Results](testing/lighthouse/registerpage.png)
![Lighthouse Results](testing/lighthouse/lighthousehomepage.png)
![Lighthouse Results](testing/lighthouse/librarylighthouse.png)
![Lighthouse Results](testing/lighthouse/addbooklighthouse.png) 


**What I focused on:**
- **Performance:** Making sure book covers don't slow down the page load.
- **Accessibility:** Checking that text is easy to read against the background and adding alt text to images.
- **Best Practices:** Making sure all links are secure.

---

# Python Linter Testing

I ran my Django files through the PEP8 linter to make sure the code is clean and follows standard Python formatting.

### views.py
![Python Linter Results](testing/pythonlint/bookviewstest.png)

### urls.py
![Python Linter Results](testing/pythonlint/bookurls.png)

### models.py
![Python Linter Results](testing/pythonlint/bookmodels.png)

### apps.py
![Python Linter Results](testing/pythonlint/bookapps.png)

### admin.py
![Python Linter Results](testing/pythonlint/bookadmin.png)

### accounts/views.py
![Python Linter Results](testing/pythonlint/accountsviews.png)

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
| Edit form inputs loading blank | Forgot to pass existing book data into the form template | Added `value="{{ book.title }}"` to the inputs |
| Nav menu breaking on edit page | Left the menu links floating without a proper wrapper | Wrapped the links inside a standard `<ul>` list |
| Heading structure warning | Skipped straight from an `<h1>` to an `<h3>` on the details page | Changed the subheadings to `<h2>` to keep it sequential |
| Form labels not working | Forgot the `for` attribute on the labels | Aligned all label `for` attributes with input `id` tags |
| Broken image links | Hardcoded relative paths broke when navigating to nested pages | Swapped to dynamic paths using `{% static %}` tags |

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
| Style layout broke entirely | Missed a closing curly brace `}` on a dropdown style rule | Found the missing brace and added it back in |
| Typo in background property | Accidentally typed `backgroud-color` with a missing 'n' | Fixed the spelling typo |
| Flex layout buttons overlapping | Forgot to give the flex container a layout gap | Added `display: flex; gap: 1rem;` |
| Invalid center alignment value | Tried using `justify-content: middle;` which isn't valid | Changed the value to `center` |
| Text spilling out of card boxes | Used a fixed height rule that clipped text on small screens | Swapped out `height` for `min-height` so it stretches |
| Buttons missing pointer hand | Forgot to add the hand icon cursor to custom styled links | Added `cursor: pointer;` to the button classes |

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
| S009 | Saving edit form crashed | Form select dropdown name didn't match backend lookup | Made sure `request.POST.get()` used the correct input name |

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
| P015 | Code check spacing warning | Only put one blank line between the new view functions | Added a second blank line to keep PEP8 happy |
| P016 | Indentation error on save | Used a mix of tabs and spaces when writing form data logic | Cleaned up lines to use exactly 4 spaces |
| P017 | Trailing whitespace warnings | Left accidental spaces at the very end of code lines | Deleted the empty spaces at the ends of lines |
| P018 | 403 Forbidden error on update | Form didn't have security verification tokens | Added `{% csrf_token %}` inside the HTML form tag |
| P019 | Edit redirect crashed | Forgot to pass the book ID back into the redirect path | Fixed redirect to use `book_id=book.id` |

---

# Live Website Link

The project is hosted on Railway. It’s set up to automatically deploy whenever I push my code changes to GitHub.


### **[Live Railway Website](ca://s?q=Open_my_Railway_website)**  
https://milestoneproject3-production.up.railway.app




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
