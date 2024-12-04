function carregarAulasDoDia() {
    const listaAulas = document.getElementById('listaAulas');
    const dataAtual = new Date();

    // Corrigir o formato do dia da semana
    const diaSemana = dataAtual.toLocaleDateString('pt-BR', { weekday: 'long' }).normalize('NFD').replace(/[\u0300-\u036f]/g, "").toLowerCase();

    console.log(diaSemana);
    const aulas = {
        "segunda-feira": [
            { nome: "Inglês III", horario: "13:10 - 14:50" },
            { nome: "Programação para Dispositivos Móveis II", horario: "14:50 - 18:20" }
        ],
        "terca-feira": [
            { nome: "Aprendizagem de Máquina", horario: "14:50 - 18:20" },
        ],
        "quarta-feira": [
            { nome: "Computação em Nuvem I ", horario: "13:10 - 16:20" },
            { nome: "Fundamentos da Redação Técnica", horario: "16:20 - 18:20" }
        ],
        "quinta-feira": [
            { nome: "Laboratório de Desenvolvimento para Dispositivos Móveis", horario: "13:10 - 16:20" },
        ],
        "sexta-feira": [
            { nome: "Segurança no Desenvolvimento de Aplicações", horario: "13:10 - 16:20" },
        ]
    };

    // Recupera as aulas do dia
    const aulasHoje = aulas[diaSemana] || [];

    if (aulasHoje.length > 0) {
        listaAulas.innerHTML = '';
        aulasHoje.forEach(aula => {
            const divAula = document.createElement('div');
            divAula.className = 'aula';

            const tituloAula = document.createElement('h4');
            tituloAula.textContent = aula.nome;

            const horarioAula = document.createElement('p');
            horarioAula.textContent = `Horário: ${aula.horario}`;

            divAula.appendChild(tituloAula);
            divAula.appendChild(horarioAula);

            listaAulas.appendChild(divAula);
        });
    } else {
        listaAulas.textContent = "Nenhuma aula programada para hoje.";
    }
}



carregarAulasDoDia();
