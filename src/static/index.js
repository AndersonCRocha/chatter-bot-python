(() => {
  const form = document.querySelector('[data-js="message-form"]')
  const messagesBox = document.querySelector('.messages-box')

  async function sendMessage(message) {
    if (!message) return

    const myMessage = createMessageBallon({ message, isBot: false })
    messagesBox.appendChild(myMessage)
    scrollToElementBottom(messagesBox)

    const response = await fetch(`http://localhost:5000/answer/${message}`)
    const responseText = await response.text()

    const botMessage = createMessageBallon({ message: responseText, isBot: true })
    messagesBox.appendChild(botMessage)
    scrollToElementBottom(messagesBox)
  }

  function createMessageBallon({ message, isBot }) {
    const balloon = document.createElement('p')
    balloon.className = `message ${isBot ? 'bot-message' : 'my-message'}`
    balloon.innerText = message

    return balloon
  }

  function scrollToElementBottom(element) {
    element.scrollTop = element.scrollHeight - element.clientHeight;
  }

  form.addEventListener('submit', function (event) {
    event.preventDefault()
    sendMessage(this.message.value)
    this.message.value = ''
  })
})();