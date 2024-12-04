// Atualiza a card com as informações do localStorage
function atualizarCard() {
    const ultimaInformacao = localStorage.getItem('ultimaInformacao');
    const userName = document.getElementById('userName');
    const userInfo = document.getElementById('userInfo');

    console.log("Dados recuperados de localStorage:", ultimaInformacao);

    try {
        const dados = JSON.parse(ultimaInformacao);
        console.log("Dados após parse:", dados);

        userName.textContent = dados.nome || "Usuário Desconhecido";
        userInfo.textContent = `Confiança: ${dados.confianca?.toFixed(2) || "Indisponível"}`;
    } catch (error) {
        console.warn("Erro ao interpretar os dados como JSON:", error);

        // Faz parsing manual caso seja uma string formatada
        const match = ultimaInformacao.match(/Nome: (.*?), Confiança: ([\d.]+)/);
        if (match) {
            const nome = match[1];
            const confianca = parseFloat(match[2]);

            userName.textContent = nome || "Usuário Desconhecido";
            userInfo.textContent = `Confiança: ${confianca.toFixed(2)}%` || "Indisponível";
        } else {
            // Fallback no caso de dados inválidos
            userName.textContent = "Usuário Desconhecido";
            userInfo.textContent = "Confiança: Indisponível";
        }
    }
}
atualizarCard();
