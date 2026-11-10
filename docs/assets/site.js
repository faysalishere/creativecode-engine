(() => {
  'use strict';
  const tabs = Array.from(document.querySelectorAll('[role="tab"][data-concept]'));
  const scenes = Array.from(document.querySelectorAll('.stage-scene[role="tabpanel"]'));
  const stageCode = document.getElementById('stage-code');
  const stageSummary = document.getElementById('stage-summary');
  const concepts = {
    editorial: { index: 'A / 03', summary: 'An editorial opening organizes identity, philosophy and projects as a story.' },
    dossier: { index: 'B / 03', summary: 'A navigable index puts evidence, case studies and individual projects first.' },
    chapters: { index: 'C / 03', summary: 'A chapter structure reveals identity and work as a sequence instead of a grid.' }
  };
  function selectConcept(name, focus = false) {
    if (!Object.prototype.hasOwnProperty.call(concepts, name)) return;
    for (const tab of tabs) {
      const active = tab.dataset.concept === name;
      tab.setAttribute('aria-selected', String(active));
      tab.tabIndex = active ? 0 : -1;
      if (active && focus) tab.focus();
    }
    for (const scene of scenes) scene.hidden = scene.id !== `panel-${name}`;
    stageCode.textContent = concepts[name].index;
    stageSummary.textContent = concepts[name].summary;
  }
  tabs.forEach((tab, i) => {
    tab.addEventListener('click', () => selectConcept(tab.dataset.concept));
    tab.addEventListener('keydown', e => {
      if (['ArrowLeft', 'ArrowRight', 'Home', 'End'].includes(e.key)) {
        e.preventDefault();
        const index = e.key === 'Home' ? 0 : e.key === 'End' ? tabs.length - 1 : (i + (e.key === 'ArrowRight' ? 1 : -1) + tabs.length) % tabs.length;
        selectConcept(tabs[index].dataset.concept, true);
      }
    });
  });
  const menuButton = document.getElementById('menu-toggle');
  const nav = document.getElementById('site-nav');
  function closeMenu() { menuButton.setAttribute('aria-expanded', 'false'); menuButton.setAttribute('aria-label', 'Open navigation'); nav.classList.remove('is-open'); }
  menuButton.addEventListener('click', () => { const open = menuButton.getAttribute('aria-expanded') !== 'true'; menuButton.setAttribute('aria-expanded', String(open)); menuButton.setAttribute('aria-label', open ? 'Close navigation' : 'Open navigation'); nav.classList.toggle('is-open', open); });
  nav.querySelectorAll('a').forEach(link => link.addEventListener('click', closeMenu));
  document.addEventListener('keydown', e => { if (e.key === 'Escape') closeMenu(); });
  const copyButton = document.getElementById('copy-command');
  const installText = [
    'git clone https://github.com/faysalishere/creativecode-engine.git',
    'cd creativecode-engine',
    'python3 -m creativecode concepts --brief examples/portfolio_brief.json --out /tmp/creativecode-concepts.json'
  ].join('\n');
  copyButton.addEventListener('click', async () => {
    try {
      await navigator.clipboard.writeText(installText);
      copyButton.textContent = 'COPIED';
      copyButton.setAttribute('aria-label', 'Commands copied');
    } catch {
      copyButton.textContent = 'SELECT CODE';
      copyButton.setAttribute('aria-label', 'Select the commands in the terminal panel to copy');
      const range = document.createRange();
      range.selectNodeContents(document.getElementById('install-command'));
      window.getSelection().removeAllRanges();
      window.getSelection().addRange(range);
    }
  });
  selectConcept('editorial');
})();
