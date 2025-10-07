document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const href = this.getAttribute('href');
        if (!href || href === '#') return;
        const target = document.querySelector(href);
        if (target) {
            e.preventDefault();
            target.scrollIntoView({ behavior: 'smooth', block: 'start' });

            const navbarToggler = document.querySelector('.navbar-collapse.show');
            if (navbarToggler) {
                const bsCollapse = bootstrap.Collapse.getInstance(navbarToggler);
                if (bsCollapse) bsCollapse.hide();
            }
        }
    });
});
