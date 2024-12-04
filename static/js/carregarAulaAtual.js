function carregarAulaAtual() {
    const aulaAtualElement = document.getElementById('aulaAtual');
    const descricaoAulaElement = document.getElementById('descricaoAula');  
    const aulas = {
        "segunda-feira": [
            { nome: "Inglês III", 
            horario: "13:10 - 14:50", 
            descricao: "Nesta aula, vamos focar em práticas de conversação e vocabulário avançado." },
            { nome: "Programação para Dispositivos Móveis II", 
            horario: "14:50 - 18:20", 
            descricao: "A aula abordará a implementação de interfaces interativas para aplicativos móveis." }
        ],
        "terca-feira": [
            { nome: "Aprendizagem de Máquina", horario: "14:50 - 18:20", descricao: "A aula discutirá técnicas de aprendizado supervisionado e não supervisionado." },
        ],
        "quarta-feira": [
            { nome: "Computação em Nuvem I", horario: "13:10 - 16:20", descricao: "Vamos aprender sobre a arquitetura de computação em nuvem e seus benefícios." },
            { nome: "Fundamentos da Redação Técnica", horario: "16:20 - 18:20", descricao: "A aula será focada na criação de textos técnicos claros e objetivos." }
        ],
        "quinta-feira": [
            { nome: "Laboratório de Desenvolvimento para Dispositivos Móveis", horario: "13:10 - 16:20", descricao: "Prática de desenvolvimento de aplicativos móveis com foco em soluções reais." },
        ],
        "sexta-feira": [
            { nome: "Segurança no Desenvolvimento de Aplicações", horario: "13:10 - 16:20", descricao: "Abordaremos as melhores práticas de segurança no desenvolvimento de software." },
        ]
    };

    const dataAtual = new Date();
    const diaSemana = dataAtual.toLocaleDateString('pt-BR', { weekday: 'long' }).normalize('NFD').replace(/[\u0300-\u036f]/g, "").toLowerCase();

    const aulasHoje = aulas[diaSemana] || [];
    if (aulasHoje.length > 0) {
        // Exibe a aula atual com base no horário
        const horaAtual = dataAtual.getHours();
        const minutoAtual = dataAtual.getMinutes();
        let aulaAtual = aulasHoje[0]; 

        for (let i = 0; i < aulasHoje.length; i++) {
            const [horaInicio, minutoInicio] = aulasHoje[i].horario.split(" - ")[0].split(":").map(Number);
            const [horaFim, minutoFim] = aulasHoje[i].horario.split(" - ")[1].split(":").map(Number);
            const inicio = horaInicio * 60 + minutoInicio;
            const fim = horaFim * 60 + minutoFim;
            const atual = horaAtual * 60 + minutoAtual;

            if (atual >= inicio && atual <= fim) {
                aulaAtual = aulasHoje[i]; 
                break;
            }
        }

        aulaAtualElement.textContent = `${aulaAtual.nome} (${aulaAtual.horario})`;
        descricaoAulaElement.textContent = aulaAtual.descricao; 
    } else {
        aulaAtualElement.textContent = "Nenhuma aula programada para hoje.";
        descricaoAulaElement.textContent = "";
    }
}
// Chama a função para carregar a aula atual
carregarAulaAtual();