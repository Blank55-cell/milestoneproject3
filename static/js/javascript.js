// Panels
const loginPanel = document.getElementById("loginPanel");
const registerPanel = document.getElementById("registerPanel");
const forgotPanel = document.getElementById("forgotPanel");
const resetPanel = document.getElementById("resetPanel");

// Show a specific panel
function show(panel) {
  const panels = [loginPanel, registerPanel, forgotPanel, resetPanel];
  panels.forEach(p => p.classList.add("hidden"));
  panel.classList.remove("hidden");
}

// Navigation links
document.getElementById("navLogin").onclick = () => show(loginPanel);
document.getElementById("navRegister").onclick = () => show(registerPanel);

// Forgot password link
document.getElementById("linkForgot").onclick = () => show(forgotPanel);

// Back to login (from forgot panel)
document.getElementById("backToLogin").onclick = () => show(loginPanel);

// Reset password link (from email)
document.getElementById("resetLink")?.addEventListener("click", () => {
  show(resetPanel);
});

// Back to login (from reset panel)
document.getElementById("resetBack")?.addEventListener("click", () => show(loginPanel));
