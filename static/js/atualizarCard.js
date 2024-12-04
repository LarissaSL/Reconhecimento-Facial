// Atualiza o card com as informações do localStorage
function atualizarCard() {
    const ultimaInformacao = localStorage.getItem('ultimaInformacao');
    const userName = document.getElementById('userName');
    const userInfo = document.getElementById('userInfo');
    const userPhoto = document.getElementById('userPhoto'); 
    console.log("Dados recuperados de localStorage:", ultimaInformacao);

    try {
        const match = ultimaInformacao.match(/Nome: (.*?), Confiança: ([\d.]+)/);

        if (match) {
            const nome = match[1];
            const confianca = match[2];

            userName.textContent = nome || "Usuário Desconhecido";
        

            // Atualiza a foto do usuário com base no nome
            if (nome === "Larissa") {
                userPhoto.src = "/static/img/Larissa.jpg";
                userInfo.textContent = `RA:1371392222020`; 
            } else if (nome === "Wesley") {
                userPhoto.src = "/static/img/wesley.jpg";  
                userInfo.textContent = `RA:1371392222024`; 
            } else {
                userPhoto.src = "/static/img/user-placeholder.png";  
            }
        } else {
            throw new Error("Dados não correspondem ao formato esperado.");
        }

    } catch (error) {
        console.warn("Erro ao interpretar os dados:", error);

        userName.textContent = "Usuário Desconhecido";
        userInfo.textContent = "Confiança: Indisponível"; 
        userPhoto.src = "/static/img/user-placeholder.png"; 
    }
}

atualizarCard(); // Chama a função para atualizar o card
