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
            //var apiUrl = "http://localhost:8000/RAG/invoke";
            var apiUrl = "http://127.0.0.1:8000/RAG/invoke";

            // Maak een HTTP-client aan
            using (var client = new HttpClient())
            {
                // Stel de gegevens in die je wilt versturen
                var data = new
                {
                    input = "Wat doet yannick lansink"
                    //input = new
                    //{
                    //    question = "Hello, how are you?",
                    //}
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
                    var responseContent = await response.Content.ReadAsStringAsync();
                    var parsedResponse = JsonConvert.DeserializeObject<dynamic>(responseContent);

                    // Print only the value of "output"
                    Console.WriteLine(parsedResponse.output.ToString());
                }
                else
                {
                    Console.WriteLine("Error: " + response.StatusCode);
                    var errorContent = await response.Content.ReadAsStringAsync();
                    Console.WriteLine("Error details: " + errorContent);
                }
            }
        }

    }
}