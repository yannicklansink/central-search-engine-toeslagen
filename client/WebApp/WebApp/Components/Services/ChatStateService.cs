using Microsoft.JSInterop;
using System.Collections.Generic;
using System.Text.Json;
using System.Threading.Tasks;

namespace WebApp.Components.Services
{
    public class ChatStateService
    {
        private readonly IJSRuntime _jsRuntime;
        private List<string> _chatHistory = new List<string>();

        public ChatStateService(IJSRuntime jsRuntime)
        {
            _jsRuntime = jsRuntime;
        }

        public IReadOnlyList<string> ChatHistory => _chatHistory.AsReadOnly();

        public async Task AddMessageAsync(string message)
        {
            _chatHistory.Add(message);
            await SaveChatHistoryAsync();
        }

        public void ClearHistory()
        {
            _chatHistory.Clear();
        }

        public async Task LoadChatHistoryAsync()
        {
            var json = await _jsRuntime.InvokeAsync<string>("localStorage.getItem", "chatHistory");
            if (!string.IsNullOrEmpty(json))
            {
                _chatHistory = JsonSerializer.Deserialize<List<string>>(json);
            }
        }

        private async Task SaveChatHistoryAsync()
        {
            var json = JsonSerializer.Serialize(_chatHistory);
            await _jsRuntime.InvokeVoidAsync("localStorage.setItem", "chatHistory", json);
        }
    }
}
