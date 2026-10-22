// Run before the stylesheet so a saved preference is applied before first paint.
(() => {
  const root = document.documentElement;
  const systemTheme = window.matchMedia("(prefers-color-scheme: dark)");
  const storageKey = "portfolio-theme";
  let preference = null;
  let button;

  try {
    const saved = localStorage.getItem(storageKey);
    if (saved === "light" || saved === "dark") preference = saved;
  } catch {
    // Storage can be unavailable in private or restricted browser contexts.
  }

  function applyTheme() {
    const theme = preference || (systemTheme.matches ? "dark" : "light");
    root.dataset.theme = theme;
    document
      .querySelector('meta[name="theme-color"]')
      ?.setAttribute("content", theme === "dark" ? "#111318" : "#ffffff");
    button?.setAttribute("aria-pressed", String(theme === "dark"));
  }

  applyTheme();
  systemTheme.addEventListener("change", () => {
    if (preference === null) applyTheme();
  });

  document.addEventListener("DOMContentLoaded", () => {
    button = document.querySelector(".theme-toggle");
    if (!button) return;
    button.hidden = false;
    applyTheme();
    button.addEventListener("click", () => {
      preference = root.dataset.theme === "dark" ? "light" : "dark";
      try {
        localStorage.setItem(storageKey, preference);
      } catch {
        // The selected theme still works for this visit if persistence fails.
      }
      applyTheme();
    });
  });
})();
