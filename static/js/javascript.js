
(function () {
    "use strict";

    // Panels
    var loginPanel = document.getElementById("loginPanel");
    var registerPanel = document.getElementById("registerPanel");
    var forgotPanel = document.getElementById("forgotPanel");
    var resetPanel = document.getElementById("resetPanel");

    // Navigation links
    var navLogin = document.getElementById("navLogin");
    var navRegister = document.getElementById("navRegister");
    var linkForgot = document.getElementById("linkForgot");
    var backToLogin = document.getElementById("backToLogin");

    /**
     * Show a specific panel and hide others.
     * @param {HTMLElement} panel - The panel to display.
     */
    function show(panel) {
        // Just hiding all the panels first, then showing the one I need
        var panels = [loginPanel, registerPanel, forgotPanel, resetPanel];

        panels.forEach(function (p) {
            if (p) {
                p.classList.add("hidden");
            }
        });

        if (panel) {
            panel.classList.remove("hidden");
        }
    }

    // Event Handlers
    if (navLogin) {
        navLogin.onclick = function () {
            show(loginPanel);
        };
    }

    if (navRegister) {
        navRegister.onclick = function () {
            show(registerPanel);
        };
    }

    // These only run if the forgot/reset stuff exists in the HTML
    if (linkForgot) {
        linkForgot.onclick = function () {
            show(forgotPanel);
        };
    }

    if (backToLogin) {
        backToLogin.onclick = function () {
            show(loginPanel);
        };
    }
}());
