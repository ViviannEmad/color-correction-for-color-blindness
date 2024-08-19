document.addEventListener('DOMContentLoaded', function () {
    const nextButton = document.getElementById('next-button');
    const plate1 = document.getElementById('plate1');
    const plate2 = document.getElementById('plate2');

    nextButton.addEventListener('click', function () {
        if (plate1.style.display === 'none') {
            plate1.style.display = 'block';
            plate2.style.display = 'none';
        } else {
            plate1.style.display = 'none';
            plate2.style.display = 'block';
        }
    });
});
