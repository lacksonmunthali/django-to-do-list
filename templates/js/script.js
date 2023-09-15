// JavaScript for handling login and tasks
function login() {
    const username = document.getElementById('username').value;
    if (username.trim() !== '') {
        document.getElementById('login-section').style.display = 'none';
        document.getElementById('todo-section').style.display = 'block';
    }
}

function addTask() {
    const taskText = document.getElementById('task').value;
    if (taskText.trim() !== '') {
        const taskList = document.getElementById('task-list');
        const li = document.createElement('li');
        li.innerHTML = `
            <span>${taskText}</span>
            <div class="task-actions">
                <button onclick="completeTask(this)">Complete</button>
                <button onclick="deleteTask(this)">Delete</button>
            </div>
        `;
        taskList.appendChild(li);
        document.getElementById('task').value = '';
    }
}

function completeTask(button) {
    const taskItem = button.parentElement.parentElement;
    taskItem.style.textDecoration = 'line-through';
    button.style.display = 'none';
}

function deleteTask(button) {
    const taskItem = button.parentElement.parentElement;
    taskItem.remove();
}


// JavaScript for handling login, signup, and tasks
function login() {
    const username = document.getElementById('login-username').value;
    const password = document.getElementById('login-password').value;
    
    // Implement your login logic here (e.g., check credentials)
    
    if (username.trim() !== '' && password.trim() !== '') {
        document.getElementById('login-section').style.display = 'none';
        document.getElementById('signup-section').style.display = 'none';
        document.getElementById('todo-section').style.display = 'block';
    }
}

function signup() {
    const username = document.getElementById('signup-username').value;
    const password = document.getElementById('signup-password').value;
    const email = document.getElementById('signup-email').value;
    
    // Implement your signup logic here (e.g., create a new user)
    
    if (username.trim() !== '' && password.trim() !== '' && email.trim() !== '') {
        document.getElementById('signup-section').style.display = 'none';
        document.getElementById('login-section').style.display = 'none';
        document.getElementById('todo-section').style.display = 'block';
    }
}

function addTask() {
    const taskText = document.getElementById('task').value;
    if (taskText.trim() !== '') {
        const taskList = document.getElementById('task-list');
        const li = document.createElement('li');
        li.innerHTML = `
            <span>${taskText}</span>
            <div class="task-actions">
                <button onclick="completeTask(this)">Complete</button>
                <button onclick="deleteTask(this)">Delete</button>
            </div>
        `;
        taskList.appendChild(li);
        document.getElementById('task').value = '';
    }
}

function completeTask(button) {
    const taskItem = button.parentElement.parentElement;
    taskItem.style.textDecoration = 'line-through';
    button.style.display = 'none';
}

function deleteTask(button) {
    const taskItem = button.parentElement.parentElement;
    taskItem.remove();
}

