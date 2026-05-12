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


