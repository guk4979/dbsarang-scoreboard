document.addEventListener('DOMContentLoaded', function() {
    const toggleButton = document.getElementById('toggleButton');
    const recreationElements = document.querySelectorAll('.recreation');
    const wholeElements = document.querySelectorAll('.whole');

    let showRecreation = true;

    toggleButton.addEventListener('click', function() {
        if (showRecreation) {
            // 'recreation' 요소들을 표시하고 'whole' 요소들을 숨기기
            recreationElements.forEach(element => {
                element.style.display = '';
            });
            wholeElements.forEach(element => {
                element.style.display = 'none';
            });
        } else {
            // 'whole' 요소들을 표시하고 'recreation' 요소들을 숨기기
            recreationElements.forEach(element => {
                element.style.display = 'none';
            });
            wholeElements.forEach(element => {
                element.style.display = '';
            });
        }
        showRecreation = !showRecreation; // 다음 클릭 시 반대 상태로 전환
    });

    // 초기 상태 설정
    recreationElements.forEach(element => {
        element.style.display = '';
    });
    wholeElements.forEach(element => {
        element.style.display = 'none';
    });
});