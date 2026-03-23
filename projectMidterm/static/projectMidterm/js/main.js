/* ============================================================
   TYRON LEE PAIRA — Portfolio Main JS
   ============================================================ */

document.addEventListener('DOMContentLoaded', function () {

    /* ── Nav scroll effect ─────────────────────────────────── */
    const nav = document.getElementById('siteNav');

    function updateNav() {
        if (nav) {
            nav.classList.toggle('scrolled', window.scrollY > 50);
        }
    }

    window.addEventListener('scroll', updateNav, { passive: true });
    updateNav();

    /* ── Mobile hamburger ──────────────────────────────────── */
    const hamburger = document.getElementById('navHamburger');
    const navLinks = document.getElementById('navLinks');

    if (hamburger && navLinks) {
        hamburger.addEventListener('click', function () {
            const isOpen = navLinks.classList.toggle('open');
            hamburger.classList.toggle('open', isOpen);
            hamburger.setAttribute('aria-expanded', isOpen);
            // Prevent body scroll when menu is open
            document.body.style.overflow = isOpen ? 'hidden' : '';
        });

        // Close on link click
        navLinks.querySelectorAll('a').forEach(function (link) {
            link.addEventListener('click', function () {
                navLinks.classList.remove('open');
                hamburger.classList.remove('open');
                hamburger.setAttribute('aria-expanded', 'false');
                document.body.style.overflow = '';
            });
        });

        // Close on Escape key
        document.addEventListener('keydown', function (e) {
            if (e.key === 'Escape' && navLinks.classList.contains('open')) {
                navLinks.classList.remove('open');
                hamburger.classList.remove('open');
                hamburger.setAttribute('aria-expanded', 'false');
                document.body.style.overflow = '';
            }
        });
    }

    /* ── Scroll reveal ─────────────────────────────────────── */
    const revealEls = document.querySelectorAll('.reveal');

    if (revealEls.length > 0) {
        const revealObserver = new IntersectionObserver(
            function (entries) {
                entries.forEach(function (entry) {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('visible');
                        revealObserver.unobserve(entry.target);
                    }
                });
            },
            { threshold: 0.1, rootMargin: '0px 0px -40px 0px' }
        );

        revealEls.forEach(function (el) {
            revealObserver.observe(el);
        });
    }

    /* ── Skill bar animation ───────────────────────────────── */
    const barCols = document.querySelectorAll('.skills-col');

    if (barCols.length > 0) {
        const barObserver = new IntersectionObserver(
            function (entries) {
                entries.forEach(function (entry) {
                    if (entry.isIntersecting) {
                        entry.target.querySelectorAll('.bar-fill').forEach(function (bar) {
                            bar.classList.add('animate');
                        });
                        barObserver.unobserve(entry.target);
                    }
                });
            },
            { threshold: 0.2 }
        );

        barCols.forEach(function (col) {
            barObserver.observe(col);
        });
    }

    /* ── Flash message auto-dismiss ────────────────────────── */
    document.querySelectorAll('.flash-close').forEach(function (btn) {
        btn.addEventListener('click', function () {
            const item = btn.closest('.flash-item');
            if (item) {
                item.style.opacity = '0';
                item.style.transform = 'translateX(20px)';
                item.style.transition = 'opacity 0.3s, transform 0.3s';
                setTimeout(function () { item.remove(); }, 300);
            }
        });
    });

    // Auto-dismiss after 5 seconds
    document.querySelectorAll('.flash-item').forEach(function (item) {
        setTimeout(function () {
            if (item.parentElement) {
                item.style.opacity = '0';
                item.style.transform = 'translateX(20px)';
                item.style.transition = 'opacity 0.3s, transform 0.3s';
                setTimeout(function () { item.remove(); }, 300);
            }
        }, 5000);
    });

    /* ── Stagger reveal-delay for grid children ────────────── */
    // Auto-add stagger delays to grid/list children that have reveal class
    document.querySelectorAll('.stagger-children').forEach(function (parent) {
        parent.querySelectorAll(':scope > .reveal').forEach(function (child, i) {
            child.style.transitionDelay = (i * 0.08) + 's';
        });
    });

});