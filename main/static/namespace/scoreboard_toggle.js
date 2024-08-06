document.addEventListener('DOMContentLoaded', function() {
    const toggleButton = document.getElementById('toggleButton');
    const recreationElements = document.querySelectorAll('.recreation');
    const wholeElements = document.querySelectorAll('.whole');
    
    function getCookie(name) {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) return parts.pop().split(';').shift();
    }

    // 쿠키에 토글 상태 저장
    function setCookie(name, value, days) {
        const d = new Date();
        d.setTime(d.getTime() + (days * 24 * 60 * 60 * 1000));
        const expires = "expires="+ d.toUTCString();
        document.cookie = `${name}=${value}; ${expires}; path=/`;
    }

    // 초기 상태 결정
    let showRecreation = getCookie('showRecreation') === 'true';

    function updateDisplay() {
        if (showRecreation) {
            // 'recreation' 요소들을 표시하고 'whole' 요소들을 숨기기
            recreationElements.forEach(element => {
                element.style.display = 'block';
            });
            wholeElements.forEach(element => {
                element.style.display = 'none';
            });

            toggleButton.textContent = '전체 점수';

        } else {
            // 'whole' 요소들을 표시하고 'recreation' 요소들을 숨기기
            recreationElements.forEach(element => {
                element.style.display = 'none';
            });
            wholeElements.forEach(element => {
                element.style.display = 'block';
            });

            toggleButton.textContent = '레크레이션 점수';

        }
    }

    // 버튼 클릭 이벤트 핸들러
    toggleButton.addEventListener('click', function() {
        showRecreation = !showRecreation;
        updateDisplay();
        setCookie('showRecreation', showRecreation, 7); // 쿠키에 상태 저장, 7일 유효
    });

    // 페이지 로드 시 초기 상태 적용
    updateDisplay();
});