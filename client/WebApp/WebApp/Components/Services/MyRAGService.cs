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

    public async Task<string> InvokeRAGAsync(string input)
    {
        var data = new { input = input };
        var json = JsonSerializer.Serialize(data);
        var content = new StringContent(json, Encoding.UTF8, "application/json");

        var response = await _httpClient.PostAsync("/RAG/invoke", content);

        if (response.IsSuccessStatusCode)
        {
            var responseContent = await response.Content.ReadAsStringAsync();
            var parsedResponse = JsonSerializer.Deserialize<JsonElement>(responseContent);
            return parsedResponse.GetProperty("output").GetString();
        }
        else
        {
            var errorContent = await response.Content.ReadAsStringAsync();
            throw new ApplicationException($"Error: {response.StatusCode}, Details: {errorContent}");
        }
    }
}
