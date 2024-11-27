document.addEventListener('DOMContentLoaded', () => {
    const tasks = [];
    const addTaskButton = document.getElementById('add-task');
    const showTasksButton = document.getElementById('show-tasks');
    const taskList = document.getElementById('task-list');

    // Adiciona uma nova tarefa ao array
    addTaskButton.addEventListener('click', () => {
        const taskText = document.getElementById('task-text').value;
        const taskDate = document.getElementById('task-date').value;
        const taskPriority = document.getElementById('task-priority').value;

        if (taskText.trim() === '') {
            alert('Por favor, insira uma descrição para a tarefa.');
            return;
        }

        tasks.push({ text: taskText, date: taskDate, priority: taskPriority });
        alert('Tarefa adicionada com sucesso!');

        // Limpa os campos de entrada
        document.getElementById('task-text').value = '';
        document.getElementById('task-date').value = '';
        document.getElementById('task-priority').value = 'low';
    });

    // Mostra ou esconde a lista de tarefas
    showTasksButton.addEventListener('click', () => {
        taskList.innerHTML = ''; // Limpa a lista antes de recriá-la

        if (tasks.length === 0) {
            taskList.style.display = 'none';
            alert('Nenhuma tarefa adicionada ainda.');
            return;
        }

        tasks.forEach((task, index) => {
            const taskItem = document.createElement('li');
            taskItem.className = 'task-item';
            taskItem.innerHTML = `
                <strong>${index + 1}. ${task.text}</strong> - 
                ${task.date ? `Data: ${task.date}` : 'Sem data'} - 
                Prioridade: ${task.priority.charAt(0).toUpperCase() + task.priority.slice(1)}
                <button class="edit-btn" data-index="${index}">Editar</button>
                <button class="delete-btn" data-index="${index}">Excluir</button>
            `;
            taskList.appendChild(taskItem);
        });

        taskList.style.display = taskList.style.display === 'none' ? 'block' : 'none';
    });

    // Edita ou exclui uma tarefa
    taskList.addEventListener('click', (event) => {
        const index = event.target.dataset.index;

        if (event.target.classList.contains('edit-btn')) {
            const newText = prompt('Edite a tarefa:', tasks[index].text);
            if (newText !== null && newText.trim() !== '') {
                tasks[index].text = newText;
                alert('Tarefa editada com sucesso!');
                showTasksButton.click(); // Atualiza a lista
            }
        }

        if (event.target.classList.contains('delete-btn')) {
            if (confirm('Tem certeza que deseja excluir esta tarefa?')) {
                tasks.splice(index, 1);
                alert('Tarefa excluída com sucesso!');
                showTasksButton.click(); // Atualiza a lista
            }
        }
    });
});
