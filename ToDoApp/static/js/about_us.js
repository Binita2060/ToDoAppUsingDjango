document.addEventListener('DOMContentLoaded', function () {
    const toggleButtons = {
        mission: document.getElementById('toggle-mission-button'),
        vision: document.getElementById('toggle-vision-button'),
        story: document.getElementById('toggle-story-button')
    };

    const texts = {
        mission: {
            more: document.getElementById('more-mission-text'),
            short: document.getElementById('mission-content').querySelector('p.card-text')
        },
        vision: {
            more: document.getElementById('more-vision-text'),
            short: document.getElementById('vision-content').querySelector('p.card-text')
        },
        story: {
            more: document.getElementById('more-story-text'),
            short: document.getElementById('story-text')
        }
    };

    function toggleContent(buttonId, contentIds) {
        const button = toggleButtons[buttonId];
        const moreText = texts[buttonId].more;
        const shortText = texts[buttonId].short;

        button.addEventListener('click', function () {
            if (moreText.classList.contains('d-none')) {
                moreText.classList.remove('d-none');
                button.textContent = 'Read Less';
            } else {
                moreText.classList.add('d-none');
                button.textContent = 'Read More';
            }
        });
    }

    // Initialize the toggle functionality
    toggleContent('mission', ['more-mission-text']);
    toggleContent('vision', ['more-vision-text']);
    toggleContent('story', ['more-story-text']);
});
