document.addEventListener('DOMContentLoaded', function() {
    const contactTrigger = document.querySelector('.contact-trigger');
    const contactWrapper = document.querySelector('.floating-contact-wrapper');

    if (contactTrigger && contactWrapper) {
        contactTrigger.addEventListener('click', function() {
            contactWrapper.classList.toggle('active');
        });

        // Close when clicking outside
        document.addEventListener('click', function(event) {
            if (!contactWrapper.contains(event.target)) {
                contactWrapper.classList.remove('active');
            }
        });
    }
});
