

// Panels
const loginPanel = document.getElementById("loginPanel");
const registerPanel = document.getElementById("registerPanel");
const forgotPanel = document.getElementById("forgotPanel");
const resetPanel = document.getElementById("resetPanel");

/**
 * Show a specific panel and hide others.
 * @param {HTMLElement} panel - The panel to display.
 */
function show(panel) {
    const panels = [loginPanel, registerPanel, forgotPanel, resetPanel];

    panels.forEach(function (p) {
        if (p) {
            p.classList.add("hidden");
        }
    });

    if (panel) {
        panel.classList.remove("hidden");
    }
}

// Navigation links - Using 'if' checks to prevent errors on pages like Home
const navLogin = document.getElementById("navLogin");
if (navLogin) {
    navLogin.onclick = function () {
        show(loginPanel);
    };
}

const navRegister = document.getElementById("navRegister");
if (navRegister) {
    navRegister.onclick = function () {
        show(registerPanel);
    };
}

// Forgot password link
const linkForgot = document.getElementById("linkForgot");
if (linkForgot) {
    linkForgot.onclick = function () {
        show(forgotPanel);
    };
}

// Back to login (from forgot panel)
const backToLogin = document.getElementById("backToLogin");
if (backToLogin) {
    backToLogin.onclick = function () {
        show(loginPanel);
    };
}

