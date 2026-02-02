// Auto-close alerts after 5 seconds
document.addEventListener('DOMContentLoaded', function() {
    // Handle alert close buttons
    const closeButtons = document.querySelectorAll('.close-alert');
    closeButtons.forEach(button => {
        button.addEventListener('click', function() {
            this.parentElement.style.animation = 'slideUp 0.3s ease';
            setTimeout(() => {
                this.parentElement.remove();
            }, 300);
        });
    });

    // Auto-close alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.animation = 'slideUp 0.3s ease';
            setTimeout(() => {
                alert.remove();
            }, 300);
        }, 5000);
    });

    // Form validation
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const nameInputs = form.querySelectorAll('input[name="name"], input[name="course"]');
            nameInputs.forEach(input => {
                const value = input.value.trim();
                if (value && !/^[A-Za-z ]+$/.test(value)) {
                    e.preventDefault();
                    alert(input.name.charAt(0).toUpperCase() + input.name.slice(1) + ' should only contain letters and spaces');
                    input.focus();
                }
            });
        });
    });

    // Add animation to cards
    const cards = document.querySelectorAll('.dashboard-card');
    cards.forEach((card, index) => {
        card.style.animation = `fadeIn 0.5s ease ${index * 0.1}s both`;
    });

    // Table row hover effect
    const tableRows = document.querySelectorAll('.students-table tbody tr');
    tableRows.forEach(row => {
        row.style.cursor = 'pointer';
    });
});

// Smooth scroll behavior
document.documentElement.style.scrollBehavior = 'smooth';

// Confirm delete actions
function confirmDelete(studentName) {
    return confirm(`Are you sure you want to delete ${studentName}? This action cannot be undone.`);
}