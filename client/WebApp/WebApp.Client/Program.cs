using Microsoft.AspNetCore.Components.WebAssembly.Hosting;

var builder = WebAssemblyHostBuilder.CreateDefault(args);

await builder.Build().RunAsync();

// Alle componenten die de Interactive WebAssembly render modes gebruiken,
// moeten worden gebouwd vanuit dit client project, zodat ze worden opgenomen
// in de gedownloade app-bundel.
