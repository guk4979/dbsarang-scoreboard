document.addEventListener('DOMContentLoaded', function() {
    const dynamicFontElements = document.querySelectorAll('.responsive-text');

    function adjustFontSize(element) {
        const textLength = element.textContent.length;
        const screenWidth = window.innerWidth;

        let fontSize;

        if (textLength <= 5 ) {
            fontSize = screenWidth <= 651 ? '28px' : '36px';
        } else if (textLength <= 8) {
            fontSize = screenWidth <= 651 ? '16px' : '24px';
        } else if (textLength <= 20) {
            fontSize = screenWidth <= 651 ? '15px' : '24px';
        } else {
            fontSize = screenWidth <= 651 ? '12px' : '16px';
        }

        element.style.fontSize = fontSize;
    }

    dynamicFontElements.forEach(adjustFontSize);

    window.addEventListener('resize', function() {
        dynamicFontElements.forEach(adjustFontSize);
    });
});