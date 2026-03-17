// Simple panel switching for sign-in
const loginPanel = document.getElementById("login-panel");
const registerPanel = document.getElementById("registerPanel");
const forgotPanel = document.getElementById("forgotPanel");
const resetPanel = document.getElementById("resetPanel");


// Show the selected panel
function show(panel) {
  const panels = [loginPanel, registerPanel, forgotPanel, resetPanel];
  panels.forEach(p => p.classList.add("hidden"));
  panel.classList.remove("hidden");
}

//Nav Link 
document.getElementById("navLogin").onclick = () => show(loginPanel);
document.getElementById("navRegister").onclick = () => show(registerPanel);


// Forgot password 
document.getElementById()