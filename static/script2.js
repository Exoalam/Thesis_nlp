document.getElementById('user-input').addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        e.preventDefault();

        let userMessageText = this.value.trim();
        if (userMessageText) {

            const userMessage = document.createElement('div');
            userMessage.classList.add('message', 'user-message');

            const messageText = document.createElement('div');

            const youTextStrong = document.createElement('strong');
            var youTextNode = document.createTextNode('Input');
            youTextStrong.appendChild(youTextNode);
            messageText.appendChild(youTextStrong);

            var lineBreak = document.createElement('br');
            messageText.appendChild(lineBreak);

            var userMessageTextNode = document.createTextNode(userMessageText);
            messageText.appendChild(userMessageTextNode);

            userMessage.appendChild(messageText);

            const userIcon = document.createElement('div');
            userIcon.classList.add('icon', 'user-icon');

            userMessage.insertBefore(userIcon, messageText);
            this.value = '';
            const chatBox = document.getElementById('chat-box');
            chatBox.appendChild(userMessage);
            chatBox.scrollTop = chatBox.scrollHeight;


            fetch('/asktoken', {
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
                    const messageContent = document.createElement('div');

                    const botPrefixStrong = document.createElement('strong');
                    var botPrefixTextNode = document.createTextNode('Tokens');
                    botPrefixStrong.appendChild(botPrefixTextNode); 

                    messageContent.appendChild(botPrefixStrong);

                    var lineBreak = document.createElement('br');
                    messageContent.appendChild(lineBreak);

                    var botMessageTextNode = document.createTextNode(data.message);
                    messageContent.appendChild(botMessageTextNode);

                    botMessage.appendChild(messageContent);
                    const botIcon = document.createElement('div');
                    botIcon.classList.add('icon', 'bot-icon');
                    //botMessage.appendChild(botIcon);
                    botMessage.insertBefore(botIcon, messageContent);
                    const chatBox = document.getElementById('chat-box');
                    chatBox.appendChild(botMessage);
                    chatBox.scrollTop = chatBox.scrollHeight;

                })
                .catch(error => console.error('Error:', error));
        }
    }
});
