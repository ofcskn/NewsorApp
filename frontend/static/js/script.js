document.addEventListener("DOMContentLoaded", () => {
  const chatForm = document.getElementById("chat-form");
  const messageList = document.getElementById("message-list");

  chatForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    const formData = new FormData(chatForm);
    const userMessage = formData.get("message");

    // Display user's message
    addMessage("user", userMessage);

    // Clear the textarea
    chatForm.reset();

    try {
      const response = await fetch("/api/send_message", {
        method: "POST",
        body: formData,
      });
      const data = await response.json();

      if (response.ok) {
        // Display AI's response
        addMessage("ai", data.response);
      } else {
        addMessage("error", data.error || "Something went wrong.");
      }
    } catch (err) {
      addMessage("error", "Failed to connect to the server.");
    }
  });

  function addMessage(sender, message) {
    const messageDiv = document.createElement("div");
    messageDiv.classList.add(sender);
    messageDiv.textContent = message;
    messageList.appendChild(messageDiv);
    messageList.scrollTop = messageList.scrollHeight; // Auto-scroll to the bottom
  }
});
