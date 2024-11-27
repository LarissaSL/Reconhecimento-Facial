document.addEventListener("DOMContentLoaded", function() {
    const burguer = document.getElementById("burguer");
    const navLista = document.querySelector(".nav-lista");

    // Verifica se a tela é móvel (menor que 1440px)
    function isMobile() {
        return window.innerWidth < 1440;
    }

    if (isMobile()) {
        burguer.addEventListener("click", function() {
            navLista.style.display = navLista.style.display === "flex" ? "none" : "flex";
        });
    } else {
        navLista.style.display = "flex";
    }

    // Fecha o menu quando clicar fora dele
    window.addEventListener("click", function(event) {
        if (!navLista.contains(event.target) && event.target !== burguer && isMobile()) {
            navLista.style.display = "none";
        }
    });

    // Ajuste do menu ao redimensionar a tela
    window.addEventListener("resize", function() {
        if (isMobile()) {
            navLista.style.display = "none";
        } else {
            navLista.style.display = "flex";
        }
    });
});
