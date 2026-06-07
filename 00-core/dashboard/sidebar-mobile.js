/* Sidebar único · fuente de verdad central
 * - Reescribe el contenido del <aside class="sidebar"> con el menú canónico
 * - Marca como .active el item correspondiente a la URL actual
 * - Inyecta hamburger mobile + collapse desktop
 *
 * Para agregar/quitar/reordenar items: editá NAV_ITEMS y COMING_SOON acá.
 * El cambio se ve en TODAS las páginas al recargar.
 *
 * Uso: <script src="/sidebar-mobile.js" defer></script> en cualquier página con <aside class="sidebar"></aside>
 */
(function () {
  const COLLAPSED_KEY = 'miramar_sidebar_collapsed';

  // === ÚNICA FUENTE DE VERDAD del sidebar ===
  const NAV_ITEMS = [
    { href: '/',                icon: '🏠', label: 'Resumen' },
    { href: '/tareas.html',     icon: '✅', label: 'Tareas' },
    { href: '/ideas.html',      icon: '💡', label: 'Ideas' },
    { href: '/documentos.html', icon: '📄', label: 'Documentos' },
    { href: '/legal.html',      icon: '⚖️', label: 'Legal' },
    { href: '/arrancar.html',   icon: '🚀', label: 'Arrancar' },
    { href: '/tecnologia.html', icon: '🛜', label: 'Tecnología' },
  ];
  const COMING_SOON = [
    { icon: '⏳', label: 'Aprobaciones' },
    { icon: '📅', label: 'Cronograma' },
    { icon: '💰', label: 'Cotizaciones' },
  ];

  function rebuildSidebar() {
    const sidebar = document.querySelector('.sidebar');
    if (!sidebar) return;
    const currentPath = window.location.pathname;
    const isActive = (href) => {
      if (href === '/') return currentPath === '/' || currentPath === '' || currentPath === '/index.html';
      return currentPath === href;
    };
    let html = '<div class="sidebar-brand">Mira<span>mar</span></div>';
    html += '<div class="sidebar-section-title">Navegación</div>';
    NAV_ITEMS.forEach(item => {
      const cls = isActive(item.href) ? 'nav-item active' : 'nav-item';
      html += `<a href="${item.href}" class="${cls}"><span class="nav-icon">${item.icon}</span><span class="nav-label">${item.label}</span></a>`;
    });
    html += '<div class="sidebar-section-title">Pronto</div>';
    COMING_SOON.forEach(item => {
      html += `<span class="nav-item coming-soon"><span class="nav-icon">${item.icon}</span><span class="nav-label">${item.label}</span><span class="nav-badge">pronto</span></span>`;
    });
    sidebar.innerHTML = html;
  }

  function injectStyles() {
    if (document.getElementById('sidebar-mobile-styles')) return;
    const css = `
      /* === Hamburger button === */
      .mm-hamburger {
        position: fixed;
        top: 10px;
        left: 10px;
        z-index: 999;
        width: 44px;
        height: 44px;
        border-radius: 10px;
        background: #fff;
        border: 1px solid #DBDBDB;
        box-shadow: 0 2px 8px rgba(15,15,15,.10);
        display: none;
        align-items: center;
        justify-content: center;
        font-size: 20px;
        cursor: pointer;
        font-family: inherit;
        line-height: 1;
        color: #2A2A2A;
      }
      .mm-hamburger:active { background: #F4F6F8; }

      /* === Backdrop === */
      .mm-backdrop {
        position: fixed;
        inset: 0;
        background: rgba(15,15,15,.4);
        z-index: 990;
        opacity: 0;
        pointer-events: none;
        transition: opacity .2s ease;
      }
      .mm-backdrop.open {
        opacity: 1;
        pointer-events: auto;
      }

      /* === Desktop: collapse toggle === */
      @media (min-width: 769px) {
        body.mm-collapsed .app-shell { grid-template-columns: 64px 1fr !important; }
        body.mm-collapsed .sidebar { padding: 16px 8px !important; }
        body.mm-collapsed .sidebar-brand,
        body.mm-collapsed .sidebar-section-title,
        body.mm-collapsed .nav-item .nav-label,
        body.mm-collapsed .nav-item .nav-badge { display: none !important; }
        body.mm-collapsed .nav-item { justify-content: center; padding: 12px 8px; }
        .mm-collapse-btn {
          background: transparent;
          border: 1px solid #DBDBDB;
          padding: 8px;
          border-radius: 8px;
          cursor: pointer;
          font-family: inherit;
          font-size: 14px;
          color: #555;
          margin-top: auto;
          margin-bottom: 8px;
        }
        body.mm-collapsed .mm-collapse-btn-label { display: none; }
      }
      @media (max-width: 768px) {
        .mm-collapse-btn { display: none; }
      }

      /* === Mobile: hide sidebar by default, show as drawer === */
      @media (max-width: 768px) {
        body { padding-top: 56px; }
        .mm-hamburger { display: inline-flex; }

        .sidebar {
          position: fixed !important;
          top: 0 !important;
          left: 0 !important;
          height: 100vh !important;
          width: 270px !important;
          max-width: 80vw;
          flex-direction: column !important;
          padding: 60px 16px 24px !important;
          gap: 4px !important;
          overflow-y: auto !important;
          overflow-x: hidden !important;
          z-index: 995;
          transform: translateX(-100%);
          transition: transform .25s ease;
          box-shadow: 4px 0 20px rgba(0,0,0,.15);
          border-right: 1px solid #DBDBDB;
          border-bottom: none !important;
        }
        body.mm-open .sidebar { transform: translateX(0); }

        .sidebar-brand { display: block !important; font-size: 22px; padding: 8px 12px 16px !important; }
        .sidebar-section-title { display: block !important; padding: 8px 12px !important; }
        .nav-item {
          flex-shrink: 0 !important;
          width: 100% !important;
          min-width: 0 !important;
          padding: 12px 14px !important;
          font-size: 15px !important;
          min-height: 48px !important;
        }
        .nav-item .nav-label { display: inline !important; }

        /* App shell se vuelve 1 columna */
        .app-shell { grid-template-columns: 1fr !important; }

        /* Page brand bar arriba */
        .mm-topbar {
          position: fixed;
          top: 0;
          left: 0;
          right: 0;
          height: 56px;
          background: #fff;
          border-bottom: 1px solid #DBDBDB;
          display: flex;
          align-items: center;
          gap: 12px;
          padding: 0 60px 0 64px;
          z-index: 800;
          font-weight: 800;
          font-size: 16px;
          color: #0F0F0F;
        }
      }
      @media (min-width: 769px) {
        .mm-topbar { display: none; }
      }
    `;
    const style = document.createElement('style');
    style.id = 'sidebar-mobile-styles';
    style.textContent = css;
    document.head.appendChild(style);
  }

  function injectHamburger() {
    const btn = document.createElement('button');
    btn.className = 'mm-hamburger';
    btn.setAttribute('aria-label', 'Abrir menú');
    btn.textContent = '☰';
    document.body.appendChild(btn);

    const backdrop = document.createElement('div');
    backdrop.className = 'mm-backdrop';
    document.body.appendChild(backdrop);

    // Top bar with brand (mobile only)
    const topbar = document.createElement('div');
    topbar.className = 'mm-topbar';
    topbar.innerHTML = '<span>Mira<span style="color:#029ECB">mar</span></span>';
    document.body.appendChild(topbar);

    function open() {
      document.body.classList.add('mm-open');
      backdrop.classList.add('open');
      btn.textContent = '✕';
    }
    function close() {
      document.body.classList.remove('mm-open');
      backdrop.classList.remove('open');
      btn.textContent = '☰';
    }
    btn.addEventListener('click', () => {
      if (document.body.classList.contains('mm-open')) close(); else open();
    });
    backdrop.addEventListener('click', close);

    // Close on nav item click
    document.querySelectorAll('.sidebar .nav-item').forEach(item => {
      item.addEventListener('click', () => {
        if (window.innerWidth <= 768) close();
      });
    });
  }

  function injectCollapseBtn() {
    const sidebar = document.querySelector('.sidebar');
    if (!sidebar) return;
    const btn = document.createElement('button');
    btn.className = 'mm-collapse-btn';
    btn.innerHTML = '◀ <span class="mm-collapse-btn-label">Minimizar</span>';
    btn.setAttribute('aria-label', 'Minimizar menú');
    sidebar.appendChild(btn);

    // Estado inicial desde localStorage
    if (localStorage.getItem(COLLAPSED_KEY) === '1') {
      document.body.classList.add('mm-collapsed');
      btn.innerHTML = '▶';
    }

    btn.addEventListener('click', () => {
      const isCollapsed = document.body.classList.toggle('mm-collapsed');
      localStorage.setItem(COLLAPSED_KEY, isCollapsed ? '1' : '0');
      btn.innerHTML = isCollapsed ? '▶' : '◀ <span class="mm-collapse-btn-label">Minimizar</span>';
    });
  }

  function init() {
    if (!document.querySelector('.sidebar')) return;
    rebuildSidebar();   // ← reescribe el menú con la fuente única de verdad
    injectStyles();
    injectHamburger();
    injectCollapseBtn();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
