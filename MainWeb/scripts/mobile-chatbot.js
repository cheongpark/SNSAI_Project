const element = document.querySelector('.chatElement');
window.watsonAssistantChatOptions = {
    integrationID: "864e4bad-f3d6-45d2-a5db-3ffda0c96cf3",
    region: "us-south",
    serviceInstanceID: "adf0314c-0da1-42f0-92ce-9fd1b6a1d5d1",

    element: element,
    hideCloseButton: true,
    showLauncher: false,
    openChatByDefault: true,

    onLoad: function(instance) {
        instance.render();
    }
};

setTimeout(function() {
    const t = document.createElement('script');
    t.src = "https://web-chat.global.assistant.watson.appdomain.cloud/versions/" + (window.watsonAssistantChatOptions.clientVersion || 'latest') + "/WatsonAssistantChatEntry.js"
    document.head.appendChild(t);
});