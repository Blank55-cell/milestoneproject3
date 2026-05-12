// Panels
const loginPanel = document.getElementById("loginPanel");
const registerPanel = document.getElementById("registerPanel");
const forgotPanel = document.getElementById("forgotPanel");
const resetPanel = document.getElementById("resetPanel");

// Show a specific panel
function show(panel) {
    const panels = [loginPanel, registerPanel, forgotPanel, resetPanel];
    panels.forEach(p => {
        if (p) p.classList.add("hidden");
    });
    if (panel) panel.classList.remove("hidden");
}

// Navigation links - Using 'if' checks to prevent errors on pages like Home
const navLogin = document.getElementById("navLogin");
if (navLogin) {
    navLogin.onclick = () => show(loginPanel);
}

const navRegister = document.getElementById("navRegister");
if (navRegister) {
    navRegister.onclick = () => show(registerPanel);
}

// Forgot password link
const linkForgot = document.getElementById("linkForgot");
if (linkForgot) {
    linkForgot.onclick = () => show(forgotPanel);
}

// Back to login (from forgot panel)
const backToLogin = document.getElementById("backToLogin");
if (backToLogin) {
    backToLogin.onclick = () => show(loginPanel);
}

/* 
  COMMENTED OUT TO PREVENT CONFLICT WITH DJANGO HTML FORMS
  
//  Handle login (CSRF FIXED)
document.getElementById("loginForm")?.addEventListener("submit", async (e) => {
  e.preventDefault();

  const email = document.getElementById("loginEmail").value;
  const password = document.getElementById("loginPassword").value;

  // Pull CSRF from THIS form
  const csrf = e.target.querySelector("[name=csrfmiddlewaretoken]").value;

  const response = await fetch("/accounts/login/", {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
      "X-CSRFToken": csrf
    },
    body: new URLSearchParams({
      email: email,
      password: password
    })
  });

  const data = await response.json();

  if (data.success) {
    window.location.href = "/library/";
  } else {
    alert(data.error || "Incorrect email or password");
  }
});


//  Handle registration (CSRF FIXED)
document.getElementById("registerForm")?.addEventListener("submit", async (e) => {
  e.preventDefault();

  const username = document.getElementById("regUsername").value;
  const email = document.getElementById("regEmail").value;
  const password = document.getElementById("regPassword").value;

  // Pull CSRF from THIS form
  const csrf = e.target.querySelector("[name=csrfmiddlewaretoken]").value;

  const response = await fetch("/accounts/register/", {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
      "X-CSRFToken": csrf
    },
    body: new URLSearchParams({
      username: username,
      email: email,
      password: password
    })
  });

  const data = await response.json();

  if (data.success) {
    show(loginPanel); // move back to login after creating account
  } else {
    alert(data.error || "Could not create account");
  }
});
*/
