using Microsoft.AspNetCore.StaticFiles;
using System.Net.Http;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;

public class MyRAGService
{
    private readonly HttpClient _httpClient;

    public MyRAGService(IHttpClientFactory httpClientFactory)
    {
        _httpClient = httpClientFactory.CreateClient("RAGClient");
    }

    public async Task StreamRAGAsync(string input, Func<string, Task> onChunkReceived)
    {
        var requestData = new { input = input };
        var json = JsonSerializer.Serialize(requestData);
        var content = new StringContent(json, Encoding.UTF8, "application/json");

        var request = new HttpRequestMessage(HttpMethod.Post, "/RAG/stream")
        {
            Content = content
        };

        var response = await _httpClient.SendAsync(request, HttpCompletionOption.ResponseHeadersRead);

        if (response.IsSuccessStatusCode)
        {
            var stream = await response.Content.ReadAsStreamAsync();
            using (var reader = new StreamReader(stream))
            {
                while (!reader.EndOfStream)
                {
                    var chunk = await reader.ReadLineAsync();
                    if (!string.IsNullOrEmpty(chunk) && chunk.StartsWith("data: "))
                    {
                        var chunkData = chunk.Substring(6);
                        await onChunkReceived(chunkData);
                    }
                }
            }
        }
        else
        {
            var errorContent = await response.Content.ReadAsStringAsync();
            throw new ApplicationException($"Error: {response.StatusCode}, Details: {errorContent}");
        }
    }
}
