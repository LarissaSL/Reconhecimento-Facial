  function carregarHorarios() {
            const listaHorarios = document.getElementById('listaHorarios');
            const horarios = [
                "13:10", "14:00", "14:50", "15:40", "16:40", "17:30"
            ];

            // Obtém a hora atual
            const dataAtual = new Date();
            const horaAtual = dataAtual.getHours();
            const minutoAtual = dataAtual.getMinutes();
            const minutoAtualTotal = horaAtual * 60 + minutoAtual; // Hora atual em minutos

            // Tolerância de 10 minutos (em minutos)
            const tolerancia = 10;
            const limiteTolerancia = minutoAtualTotal + tolerancia;

            console.log("Hora atual:", `${horaAtual}:${minutoAtual < 10 ? "0" + minutoAtual : minutoAtual}`);  // Mostra a hora atual no console

            listaHorarios.innerHTML = '';

            // Preenche a lista de horários com checkboxes
            horarios.forEach(horario => {
                const [hora, minuto] = horario.split(":").map(Number);
                const minutoHorarioTotal = hora * 60 + minuto;

                const li = document.createElement('li');
                const checkbox = document.createElement('input');
                checkbox.type = 'checkbox';
                checkbox.disabled = true;


                if (minutoHorarioTotal <= minutoAtualTotal + tolerancia && minutoHorarioTotal >= minutoAtualTotal) {
                    checkbox.checked = true;
                }

                const label = document.createElement('label');
                label.textContent = horario;

                li.appendChild(checkbox);
                li.appendChild(label);
                listaHorarios.appendChild(li);

                // Log para verificar se o checkbox está marcado ou não
                console.log(`Horário: ${horario}, Status: ${checkbox.checked ? 'Ativado (Presença Marcada)' : 'Desativado'}`);
            });
        }

        // Chama a função para carregar os horários
        carregarHorarios();