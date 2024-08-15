document.addEventListener('DOMContentLoaded', function() {
    const menuIcon = document.getElementById('menu-icon');
    const dropdownMenu = document.getElementById('dropdown-menu');

    menuIcon.addEventListener('click', function() {
        if (dropdownMenu.style.display === 'flex') {
            dropdownMenu.style.display = 'none';
        } else {
            dropdownMenu.style.display = 'flex';
        }
    });

    document.querySelectorAll('.open-html-button').forEach(button => {
        button.addEventListener('click', function() {
            const targetPage = this.getAttribute('data-target');
            window.location.href = targetPage;
        });
    });
});

