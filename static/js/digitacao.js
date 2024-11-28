document.addEventListener("DOMContentLoaded", () => {
    const textoDestacado = "com o GIGA!"; // Texto que será destacado e digitado
    const elemento = document.getElementById("typewriter");
    let index = 0;
    let isDeleting = false; // Flag para saber se estamos apagando o texto
    let speed = 100; // Velocidade de digitação (100ms)
    let deleteSpeed = 60; // Velocidade de apagar o texto

    function digitar() {
        if (!isDeleting && index < textoDestacado.length) {
            // Digitar a parte do textoDestacado
            const destacado = textoDestacado.charAt(index);
            const span = document.createElement('span');
            span.classList.add('highlight');
            span.textContent = destacado;
            elemento.appendChild(span);
            index++;
            setTimeout(digitar, speed);
        } else if (isDeleting && index > 0) {
            // Apagar a letra do texto digitado
            elemento.textContent = textoDestacado.substring(0, index - 1);
            index--;
            setTimeout(digitar, deleteSpeed);
        } else if (!isDeleting && index === textoDestacado.length) {
            // Pausa antes de começar a apagar
            setTimeout(() => {
                isDeleting = true;
                digitar();
            }, 8000); // Pausa de 8 segundos
        } else if (isDeleting && index === 0) {
            // Reiniciar o processo de digitação
            setTimeout(() => {
                isDeleting = false;
                digitar();
            }, 1000); // Pausa antes de começar novamente
        }
    }

    digitar(); // Iniciar o efeito
});
