document.getElementById('user-input').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        e.preventDefault();

        let userMessageText = this.value.trim();
        if (userMessageText) {
            const userMessage = document.createElement('div');
            userMessage.classList.add('message', 'user-message');
            userMessage.textContent = userMessageText;

            const userIcon = document.createElement('div');
            userIcon.classList.add('icon', 'user-icon');
            userMessage.insertBefore(userIcon, userMessage.firstChild);

            this.value = '';
            const chatBox = document.getElementById('chat-box');
            chatBox.appendChild(userMessage);
            chatBox.scrollTop = chatBox.scrollHeight;

            fetch('/ask', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: userMessageText }),
            })
            .then(response => response.json())
            .then(data => {
                const botMessage = document.createElement('div');
                botMessage.classList.add('message', 'bot-message');
                botMessage.textContent = data.message;

                const botIcon = document.createElement('div');
                botIcon.classList.add('icon', 'bot-icon');
                botMessage.appendChild(botIcon);

                chatBox.appendChild(botMessage);
                chatBox.scrollTop = chatBox.scrollHeight;
            })
            .catch(error => console.error('Error:', error));
        }
    }
});
