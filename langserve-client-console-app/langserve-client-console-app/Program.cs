using Newtonsoft.Json;
using System.Text;

namespace langserve_client_console_app
{
    public class Program
    {
        static async Task Main(string[] args)
        {
            Console.WriteLine("Hello, World!");
            // De URL van je langchain langserve API
            var apiUrl = "http://localhost:8000/chain/invoke";

            // Maak een HTTP-client aan
            using (var client = new HttpClient())
            {
                // Stel de gegevens in die je wilt versturen
                var data = new
                {
                    input = new
                    {
                        language = "ffrench",
                        text = "hi"
                    }
                };

                // Converteer de gegevens naar een JSON-string
                var json = JsonConvert.SerializeObject(data);

                // Maak een HTTP-content object van de JSON-string
                var content = new StringContent(json, Encoding.UTF8, "application/json");

                // Verstuur een POST-verzoek naar de API
                var response = await client.PostAsync(apiUrl, content);

                // Zorg dat je de response controleert
                if (response.IsSuccessStatusCode)
                {
                    // Lees de inhoud van de response
                    var responseContent = await response.Content.ReadAsStringAsync();
                    Console.WriteLine("Response: " + responseContent);
                }
                else
                {
                    Console.WriteLine("Error: " + response.StatusCode);
                }
            }
        }

    }
}