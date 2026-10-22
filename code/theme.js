// Follow the system theme until the reader chooses a mode explicitly.
(() => {
  const storageKey = 'blog-color-theme';
  const root = document.documentElement;
  const system = window.matchMedia('(prefers-color-scheme: dark)');
  let preference = null;
  try {
    const saved = localStorage.getItem(storageKey);
    if (saved === 'light' || saved === 'dark') preference = saved;
  } catch (_) {
    // Private browsing may disable storage; switching still works for this page.
  }

  const button = document.getElementById('theme-toggle');
  const update = () => {
    if (preference) root.dataset.theme = preference;
    else delete root.dataset.theme;
    const theme = preference || (system.matches ? 'dark' : 'light');
    button.setAttribute('aria-checked', String(theme === 'dark'));
    button.title = `Dark mode ${theme === 'dark' ? 'on' : 'off'}`;
  };
  button.addEventListener('click', () => {
    preference = (preference || (system.matches ? 'dark' : 'light')) === 'dark' ? 'light' : 'dark';
    try { localStorage.setItem(storageKey, preference); } catch (_) { /* non-persistent fallback */ }
    update();
  });
  system.addEventListener('change', update);
  update();
})();
