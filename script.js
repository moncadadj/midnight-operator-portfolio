// ── CURSOR ────────────────────────────────────────────────────────
const cursor = document.getElementById('cursor');
const ring = document.getElementById('cursorRing');
let mx = 0, my = 0, rx = 0, ry = 0;

document.addEventListener('mousemove', e => {
  mx = e.clientX; my = e.clientY;
  cursor.style.left = mx + 'px';
  cursor.style.top = my + 'px';
});

function animateRing() {
  rx += (mx - rx) * 0.12;
  ry += (my - ry) * 0.12;
  ring.style.left = rx + 'px';
  ring.style.top = ry + 'px';
  requestAnimationFrame(animateRing);
}
animateRing();

document.querySelectorAll('a, button, .pillar, .exp-card, .phase, .tool-card, .principle').forEach(el => {
  el.addEventListener('mouseenter', () => {
    cursor.style.width = '18px';
    cursor.style.height = '18px';
    ring.style.width = '52px';
    ring.style.height = '52px';
    ring.style.borderColor = 'var(--gold)';
    ring.style.opacity = '0.8';
  });
  el.addEventListener('mouseleave', () => {
    cursor.style.width = '10px';
    cursor.style.height = '10px';
    ring.style.width = '36px';
    ring.style.height = '36px';
    ring.style.borderColor = 'var(--gold)';
    ring.style.opacity = '0.5';
  });
});

// ── SCROLL PROGRESS ───────────────────────────────────────────────
const progress = document.getElementById('progress');
const nav = document.getElementById('nav');

window.addEventListener('scroll', () => {
  const scrolled = window.scrollY;
  const total = document.documentElement.scrollHeight - window.innerHeight;
  progress.style.width = (scrolled / total * 100) + '%';

  if (scrolled > 60) nav.classList.add('scrolled');
  else nav.classList.remove('scrolled');
});

// ── SCROLL REVEAL ─────────────────────────────────────────────────
const reveals = document.querySelectorAll('.reveal');
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

reveals.forEach(el => observer.observe(el));

// ── PRINCIPLE NUMBER PARALLAX ─────────────────────────────────────
document.querySelectorAll('.principle-num').forEach(num => {
  const principle = num.parentElement;
  principle.addEventListener('mouseenter', () => {
    num.style.color = 'var(--gold)';
    num.style.opacity = '0.15';
  });
  principle.addEventListener('mouseleave', () => {
    num.style.color = 'var(--border)';
    num.style.opacity = '1';
  });
});

// ── TRANSLATION LOGIC ─────────────────────────────────────────────
const langToggle = document.getElementById('langToggle');
let currentLang = localStorage.getItem('lang') || 'en';

function applyTranslations(lang) {
  const elements = document.querySelectorAll('[data-i18n]');
  elements.forEach(el => {
    const key = el.getAttribute('data-i18n');
    if (translations[lang] && translations[lang][key]) {
      el.innerHTML = translations[lang][key];
    }
  });
  langToggle.textContent = lang === 'en' ? 'ES / EN' : 'EN / ES';
  document.documentElement.lang = lang;
}

// Apply initial translations
applyTranslations(currentLang);

langToggle.addEventListener('click', () => {
  currentLang = currentLang === 'en' ? 'es' : 'en';
  localStorage.setItem('lang', currentLang);
  applyTranslations(currentLang);
});
