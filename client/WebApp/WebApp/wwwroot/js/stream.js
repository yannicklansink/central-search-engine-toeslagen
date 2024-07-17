window.updateOutput = (chunk) => {
    const outputElement = document.getElementById('output');
    if (outputElement) {
        outputElement.innerText += chunk;
        outputElement.scrollTop = outputElement.scrollHeight;
    }
};

// een functie window.updateOutput die gebruikt wordt om de inhoud van een HTML-element met het id output bij te werken.


