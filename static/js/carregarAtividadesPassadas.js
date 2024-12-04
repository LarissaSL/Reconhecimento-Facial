function carregarAtividadesPassadas() {
    const containerAtividades = document.querySelector('.atividade-container');
    const btnAnterior = document.getElementById('btnAnterior');
    const btnProximo = document.getElementById('btnProximo');

    const dataAtual = new Date();
    const diaSemana = dataAtual.toLocaleDateString('pt-BR', { weekday: 'long' })
        .normalize('NFD').replace(/[\u0300-\u036f]/g, "").toLowerCase();

    const atividadesPorDia = {
        "segunda-feira": [
            {
                materia: "Teste 1",
                atividade: "Atividade 1",
                dataEntrega: "📆 22/11/2024",
                pontuacao: "9/10 Pts",
                criterios: [
                    { descricao: "Critério 1", atendido: true },
                    { descricao: "Critério 2", atendido: true },
                    { descricao: "Critério 3", atendido: true }
                ]
            },
        ],
        "terça-feira": [
            {
                materia: "Teste 1",
                atividade: "Atividade 1",
                dataEntrega: "📆 22/11/2024",
                pontuacao: "9/10 Pts",
                criterios: [
                    { descricao: "Critério 1", atendido: true },
                    { descricao: "Critério 2", atendido: true },
                    { descricao: "Critério 3", atendido: true }
                ]
            },
        ],
        "quarta-feira": [
            {
                materia: "Teste 1",
                atividade: "Atividade 1",
                dataEntrega: "📆 22/11/2024",
                pontuacao: "9/10 Pts",
                criterios: [
                    { descricao: "Critério 1", atendido: true },
                    { descricao: "Critério 2", atendido: true },
                    { descricao: "Critério 3", atendido: true }
                ]
            },
            {
                materia: "Teste 2",
                atividade: "Atividade 2",
                dataEntrega: "📆 22/11/2024",
                pontuacao: "8/10 Pts",
                criterios: [
                    { descricao: "Critério 1", atendido: true },
                    { descricao: "Critério 2", atendido: false },
                    { descricao: "Critério 3", atendido: true }
                ]
            }
        ],
        "quinta-feira": [
            {
                materia: "Teste 1",
                atividade: "Atividade 1",
                dataEntrega: "📆 22/11/2024",
                pontuacao: "9/10 Pts",
                criterios: [
                    { descricao: "Critério 1", atendido: true },
                    { descricao: "Critério 2", atendido: true },
                    { descricao: "Critério 3", atendido: true }
                ]
            },
        ],
        "sexta-feira": [
            {
                materia: "Teste 1",
                atividade: "Atividade 1",
                dataEntrega: "📆 22/11/2024",
                pontuacao: "9/10 Pts",
                criterios: [
                    { descricao: "Critério 1", atendido: true },
                    { descricao: "Critério 2", atendido: true },
                    { descricao: "Critério 3", atendido: true }
                ]
            },
        ],
    };

    const atividadesHoje = atividadesPorDia[diaSemana] || [];
    let indiceAtual = 0; // Controle da atividade ativa

    if (atividadesHoje.length > 0) {
        containerAtividades.innerHTML = '';

        // Cria as atividades
        atividadesHoje.forEach((atividade, index) => {
            const divAtividade = document.createElement('div');
            divAtividade.className = 'atividade';
            if (index === 0) divAtividade.classList.add('active');

            const tituloMateria = document.createElement('h3');
            tituloMateria.textContent = atividade.materia;

            const detalhes = document.createElement('p');
            detalhes.innerHTML = `${atividade.atividade}<br>${atividade.dataEntrega}<br><strong>Pontuação:</strong> ${atividade.pontuacao}`;

            const ulCriterios = document.createElement('ul');
            ulCriterios.className = 'criterios';

            atividade.criterios.forEach(criterio => {
                const li = document.createElement('li');
                const checkbox = document.createElement('input');
                checkbox.type = 'checkbox';
                checkbox.checked = criterio.atendido;
                checkbox.disabled = true;

                const label = document.createElement('label');
                label.textContent = criterio.descricao;

                li.appendChild(checkbox);
                li.appendChild(label);
                ulCriterios.appendChild(li);
            });

            divAtividade.appendChild(tituloMateria);
            divAtividade.appendChild(detalhes);
            divAtividade.appendChild(ulCriterios);

            containerAtividades.appendChild(divAtividade);
        });

        // Função para atualizar a atividade exibida
        function atualizarAtividade() {
            const atividades = document.querySelectorAll('.atividade');
            atividades.forEach((atividade, index) => {
                atividade.classList.toggle('active', index === indiceAtual);
            });
        }

        // Eventos dos botões
        btnAnterior.addEventListener('click', () => {
            if (indiceAtual > 0) {
                indiceAtual--;
                atualizarAtividade();
            }
        });

        btnProximo.addEventListener('click', () => {
            if (indiceAtual < atividadesHoje.length - 1) {
                indiceAtual++;
                atualizarAtividade();
            }
        });
    } else {
        containerAtividades.innerHTML = "<p>Nenhuma atividade registrada para este dia.</p>";
    }
}

carregarAtividadesPassadas();