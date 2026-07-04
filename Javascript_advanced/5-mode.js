function changeMode(size, weight, transform, background, color) {
    return function() {
        document.body.style.fontSize = size + 'px';
        document.body.style.fontWeight = weight;
        document.body.style.textTransform = transform;
        document.body.style.backgroundColor = background;
        document.body.style.color = color;
    };
}

function main() {
    // Mövzular üçün closure funksiyalarının yaradılması
    let spooky = changeMode(9, 'bold', 'uppercase', 'pink', 'green');
    let darkMode = changeMode(12, 'bold', 'capitalize', 'black', 'white');
    let screamMode = changeMode(12, 'normal', 'lowercase', 'white', 'black');

    // Paraqraf elementinin yaradılması və bədənə (body) əlavə edilməsi
    let paragraph = document.createElement('p');
    paragraph.textContent = 'welcome Holberton!';
    document.body.appendChild(paragraph);

    // Spooky düyməsinin yaradılması
    let btnSpooky = document.createElement('button');
    btnSpooky.textContent = 'Spooky';
    btnSpooky.addEventListener('click', spooky);
    document.body.appendChild(btnSpooky);

    // Dark mode düyməsinin yaradılması
    let btnDark = document.createElement('button');
    btnDark.textContent = 'Dark mode';
    btnDark.addEventListener('click', darkMode);
    document.body.appendChild(btnDark);

    // Scream mode düyməsinin yaradılması
    let btnScream = document.createElement('button');
    btnScream.textContent = 'Scream mode';
    btnScream.addEventListener('click', screamMode);
    document.body.appendChild(btnScream);
}

// main funksiyasının çağırılması
main();
